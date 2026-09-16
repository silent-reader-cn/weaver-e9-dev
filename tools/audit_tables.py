#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
表结构文档可信度审计
====================
背景
----
`references/01_database/tables/` 下的表结构文档**不是完整表结构**，
而是**部分收录**——很多表只记录了升级补丁新增的列，缺少 CREATE TABLE 的基础列。

实例（铁证）：
  - `workflow_requestlog` 文档只收录 1 列（`issubmitdirect`），
    但本仓库 `core_tables.md` 明确写了它有 `requestid/nodeid/operator/remark/logtype`；
  - `workflow_requestbase` 文档缺 `requestid`，
    但本仓库 `sql_cookbook.md` 的 SQL 里写着 `JOIN workflow_requestbase r ON c.requestid = r.requestid`。

若 agent 直接信任这些文档去写 SQL，会写出错误语句。本脚本把「不可信」这一点
**显式标注**出来，让消费方（agent / 人）第一时间看到。

本脚本做三件事
--------------
  1. 把误导性的标签 `字段总数` 改名为 `文档收录字段数`（1699 个文件）
  2. 用两个**仓库内权威来源**交叉验证，找出**可确证不完整**的表，
     在其文档顶部插入警告块（幂等）
  3. 生成 `references/01_database/_QUALITY.md` 数据质量报告

交叉验证来源
------------
  A. `core_tables.md` —— 手写的核心表关键字段清单
  B. `sql_cookbook.md` —— 生产级 SQL 模板（解析 FROM/JOIN 别名与 `别名.列名` 引用）

用法:
    python tools/audit_tables.py --check     # 只报告，不修改
    python tools/audit_tables.py             # 执行
"""
import os
import re
import sys
import glob
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
DB_DIR = os.path.join(ROOT, "references", "01_database")
TABLES_DIR = os.path.join(DB_DIR, "tables")

OLD_LABEL = "字段总数"
NEW_LABEL = "文档收录字段数"

# 警告块的机器可识别标记（search.py 依赖它）
MARK = "⚠️ 表结构不完整"
MARK_END = "<!-- audit-warning-end -->"

VERIFY_SQL = ("SELECT column_name, data_type, data_length, nullable "
              "FROM user_tab_columns WHERE table_name = '{up}' ORDER BY column_id;")


# ----------------------------------------------------------------- 读取表文档

def read_table(fp):
    """返回 (表名, 模块, 文档收录字段数, 列名集合, 全文)。"""
    t = open(fp, encoding="utf-8").read()
    m = re.search(r"数据库表名\*\*\s*[:：]\s*`([^`]+)`", t)
    name = m.group(1) if m else os.path.splitext(os.path.basename(fp))[0]
    mm = re.search(r"所属模块\*\*\s*[:：]\s*`([^`]+)`", t)
    module = mm.group(1) if mm else os.path.basename(os.path.dirname(fp))
    mc = re.search(r"(?:字段总数|文档收录字段数)\*\*\s*[:：]\s*`?(\d+)`?", t)
    ncol = int(mc.group(1)) if mc else 0
    cols = set()
    for ln in t.split("\n"):
        if not re.match(r"^\|\s*\d+\s*\|", ln):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) == 7:
            # 格式A：序号|列名|中文说明|...  格式B已归一化，此处统一按A取
            col = cells[1].strip("`").strip()
            if col:
                cols.add(col.lower())
    return name, module, ncol, cols, t


def load_all_tables():
    """返回 (全部文件列表, 按表名索引的字典)。

    注意：同一张表可能在多个模块下各有一份定义（12 个考勤表跨
    `E9新版考勤表结构` 与 `人力资源`），所以**改名要遍历文件列表**，
    不能只遍历按表名去重后的字典，否则会漏改。
    """
    all_files = []
    by_name = {}
    for fp in glob.glob(os.path.join(TABLES_DIR, "**", "*.md"), recursive=True):
        name, module, ncol, cols, text = read_table(fp)
        info = {"file": fp, "name": name, "module": module,
                "ncol": ncol, "cols": cols, "text": text}
        all_files.append(info)
        by_name.setdefault(name.lower(), info)
    return all_files, by_name


# ------------------------------------------------- 来源 A：core_tables.md

def declared_from_core():
    fp = os.path.join(DB_DIR, "core_tables.md")
    if not os.path.exists(fp):
        return {}
    out = {}
    for ln in open(fp, encoding="utf-8").read().split("\n"):
        if not ln.startswith("| `"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        tbl = cells[0].strip("`").strip().lower()
        cols = set(c.lower() for c in re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`", cells[2]))
        if tbl and cols:
            out.setdefault(tbl, set()).update(cols)
    return out


# ------------------------------------------------- 来源 B：sql_cookbook.md

def declared_from_sql():
    """解析 SQL 模板里的 FROM/JOIN 别名与 `别名.列名` 引用。"""
    fp = os.path.join(DB_DIR, "sql_cookbook.md")
    if not os.path.exists(fp):
        return {}
    text = open(fp, encoding="utf-8").read()
    refs = defaultdict(set)
    for block in re.findall(r"```sql\n(.*?)```", text, re.S):
        alias2tbl = {}
        # FROM / JOIN <table> [AS] [alias]
        for m in re.finditer(
                r"(?:FROM|JOIN)\s+([A-Za-z_][A-Za-z0-9_]*)\s*(?:AS\s+)?([a-z][A-Za-z0-9_]*)?",
                block, re.I):
            tbl, alias = m.group(1), m.group(2)
            if tbl.upper() in ("SELECT", "WHERE", "ON", "AND", "OR", "LEFT", "INNER",
                               "RIGHT", "OUTER", "JOIN", "FROM", "GROUP", "ORDER", "BY"):
                continue
            alias2tbl[(alias or tbl).lower()] = tbl.lower()
        # 别名.列名
        for m in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\.([A-Za-z_][A-Za-z0-9_]*)\b", block):
            a, col = m.group(1).lower(), m.group(2).lower()
            if a in alias2tbl:
                refs[alias2tbl[a]].add(col)
    return dict(refs)


# ----------------------------------------------------------------- 主流程

def build_findings(tables):
    core = declared_from_core()
    sql = declared_from_sql()

    findings = {}   # table_lower -> {"missing": [...], "sources": [...]}
    for src_name, decl in (("core_tables.md", core), ("sql_cookbook.md", sql)):
        for tbl, cols in decl.items():
            info = tables.get(tbl)
            if not info:
                continue
            missing = sorted(c for c in cols if c not in info["cols"])
            if missing:
                f = findings.setdefault(tbl, {"missing": set(), "sources": []})
                f["missing"].update(missing)
                f["sources"].append(src_name)
    return findings


def warning_block(tbl, info, missing, sources):
    up = tbl.upper()
    return "\n".join([
        "> %s（已确证）" % MARK,
        ">",
        "> 本文件仅收录 **%d** 个字段，缺少本表的基础列：%s" % (
            info["ncol"], "、".join("`%s`" % c for c in sorted(missing)[:8])),
        ">",
        "> 判定依据：本仓库 %s 中明确引用了上述列，但本文档未收录。"
        % " 与 ".join("`%s`" % s for s in sources),
        "> 说明本文档是**部分收录**（很可能只含升级补丁新增的列），**不是完整表结构**。",
        ">",
        "> **请勿直接依据本文档编写 SQL**。获取真实结构：",
        ">",
        "> ```sql",
        "> %s" % VERIFY_SQL.format(up=up),
        "> ```",
        MARK_END,
        "",
    ])


def apply_warning(text, block):
    """把警告块插到 H1 标题之后（幂等：已有则先移除再插入）。"""
    text = re.sub(r"> %s.*?%s\n" % (re.escape(MARK), re.escape(MARK_END)),
                  "", text, flags=re.S)
    lines = text.split("\n")
    idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if idx is None:
        return block + "\n" + text, True
    return "\n".join(lines[:idx + 1]) + "\n\n" + block + "\n".join(lines[idx + 1:]), True


def main(argv):
    check_only = "--check" in argv
    print("扫描表文档...")
    all_files, tables = load_all_tables()
    print("  表定义文件: %d 个（去重后唯一表名 %d 个）" % (len(all_files), len(tables)))

    # 1) 标签改名（遍历全部文件，含跨模块重复的表）
    renamed = 0
    for info in all_files:
        if OLD_LABEL in info["text"]:
            renamed += 1
    print("\n[1] 标签 `%s` -> `%s`：%d 个文件待改" % (OLD_LABEL, NEW_LABEL, renamed))
    if not check_only:
        for info in all_files:
            if OLD_LABEL in info["text"]:
                new = info["text"].replace(OLD_LABEL, NEW_LABEL)
                open(info["file"], "w", encoding="utf-8").write(new)
                info["text"] = new

    # 2) 交叉验证
    findings = build_findings(tables)
    print("\n[2] 交叉验证：可确证不完整的表 %d 张" % len(findings))
    for tbl, f in sorted(findings.items()):
        info = tables[tbl]
        print("   %-30s 文档仅 %3d 列，缺 %d 个被引用的列" %
              (info["name"], info["ncol"], len(f["missing"])))

    # 3) 插入警告（同样遍历全部文件，重复表两份都要标注）
    if not check_only:
        n = 0
        for info in all_files:
            tbl = info["name"].lower()
            if tbl not in findings:
                continue
            f = findings[tbl]
            block = warning_block(tbl, info, f["missing"], f["sources"])
            new, _ = apply_warning(info["text"], block)
            open(info["file"], "w", encoding="utf-8").write(new)
            info["text"] = new
            n += 1
        print("\n[3] 已为 %d 个表文件插入警告块（含跨模块重复）" % n)

    # 4) 生成质量报告
    if not check_only:
        write_quality_report(tables, findings, renamed)
    return 0


def write_quality_report(tables, findings, renamed):
    L = ["# 表结构数据质量报告", "",
         "> 本文件由 `tools/audit_tables.py` 自动生成，请勿手工编辑。", "",
         "## 结论：表结构文档是**部分收录**，不是完整表结构", "",
         "`tables/` 下的表结构文档来自上游数据源，**很多表只记录了升级补丁新增的列**，",
         "缺少 `CREATE TABLE` 的基础列。直接依据这些文档编写 SQL 会出错。", "",
         "**使用前请务必用以下 SQL 从真实库核对：**", "",
         "```sql",
         "SELECT column_name, data_type, data_length, nullable",
         "FROM user_tab_columns",
         "WHERE table_name = 'WORKFLOW_REQUESTBASE'   -- 换成你的表名（大写）",
         "ORDER BY column_id;",
         "```", "",
         "> 另外注意：文档中的 `文档收录字段数` 是**本文件记录了几行**，",
         "> 不等于表的真实列数。", "",
         "---", "",
         "## 已确证不完整的表", "",
         "判定方法：本仓库的 `core_tables.md`（手写关键字段清单）或 `sql_cookbook.md`",
         "（生产 SQL 模板）中引用了某列，但该表文档未收录 —— 说明文档必有遗漏。", ""]

    if findings:
        L += ["| 表名 | 模块 | 文档收录字段数 | 缺失的列（被本仓库其他文档引用） | 判定依据 |",
              "| :--- | :--- | :---: | :--- | :--- |"]
        for tbl, f in sorted(findings.items(), key=lambda kv: -len(kv[1]["missing"])):
            info = tables[tbl]
            miss = "、".join("`%s`" % c for c in sorted(f["missing"])[:10])
            if len(f["missing"]) > 10:
                miss += " 等 %d 个" % len(f["missing"])
            L.append("| [`%s`](./%s) | %s | %d | %s | %s |" % (
                info["name"],
                os.path.relpath(info["file"], DB_DIR).replace("\\", "/"),
                info["module"], info["ncol"], miss, " / ".join(f["sources"])))
    else:
        L.append("（无）")

    L += ["", "---", "", "## 全库字段数分布（辅助判断）", "",
          "| 文档收录字段数 | 表数量 |", "| :---: | :---: |"]
    from collections import Counter
    c = Counter()
    for info in tables.values():
        n = info["ncol"]
        key = "1" if n == 1 else "2-5" if n <= 5 else "6-10" if n <= 10 else \
              "11-20" if n <= 20 else "21-40" if n <= 40 else "41-80" if n <= 80 else "81+"
        c[key] += 1
    for k in ["1", "2-5", "6-10", "11-20", "21-40", "41-80", "81+"]:
        if c[k]:
            L.append("| %s | %d |" % (k, c[k]))
    L += ["", "> 中位数仅 **7 列**。字段数极少的表**未必**都是残缺（字典表、序列表本就很小），",
          "> 但反过来，**字段数多也不代表完整** —— 上表列出的才是已确证有遗漏的。", ""]

    fp = os.path.join(DB_DIR, "_QUALITY.md")
    open(fp, "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")
    print("  已生成 %s" % os.path.relpath(fp, ROOT).replace("\\", "/"))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
