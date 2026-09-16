#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weaver-e9-dev 索引构建工具
=========================
从 Markdown 反向生成四块的 `_INDEX.md` 人类可读索引。

设计原则：**Markdown 是唯一真相源**。索引只由本脚本从 Markdown 派生，
不手工维护，因此永远不会与正文脱节。修改任何文档后重跑本脚本即可。

生成的索引：
  references/01_database/_INDEX.md        1,699 张表（模块统计 + 分模块清单）
  references/02_backend_api/_INDEX.md     538 个接口（模块 → 接口/方法/地址/文件）
  references/03_frontend_jsapi/_INDEX.md  前端 JS API 方法清单
  references/04_integration/_INDEX.md     集成与扩展文档清单

用法:
    python scripts/build_index.py
"""
import os
import re
import sys
import glob
from collections import OrderedDict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
REFS = os.path.join(ROOT, "references")


def split_blocks(text, pattern):
    parts = re.split(pattern, text)
    out = []
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        out.append((title, body))
    return out


def extract(body, header):
    m = re.search(r"###\s*%s\s*\n+(.*?)(?:\n###|\Z)" % re.escape(header), body, re.S)
    return m.group(1).strip().split("\n")[0].strip() if m else ""


def write(path, lines):
    open(path, "w", encoding="utf-8").write("\n".join(lines).rstrip() + "\n")
    print("  已生成 %s" % os.path.relpath(path, ROOT).replace("\\", "/"))


# ---------------------------------------------------------------- 块一 数据库

def build_db_index():
    base = os.path.join(REFS, "01_database")
    pattern = os.path.join(base, "tables", "**", "*.md")
    modules = OrderedDict()
    for fp in sorted(glob.glob(pattern, recursive=True)):
        text = open(fp, encoding="utf-8").read()
        m = re.search(r"数据库表名\*\*\s*[:：]\s*`([^`]+)`", text)
        table = m.group(1) if m else os.path.splitext(os.path.basename(fp))[0]
        mm = re.search(r"所属模块\*\*\s*[:：]\s*`([^`]+)`", text)
        module = mm.group(1) if mm else os.path.basename(os.path.dirname(fp))
        mc = re.search(r"文档收录字段数\*\*\s*[:：]\s*`?(\d+)`?", text) or \
            re.search(r"字段总数\*\*\s*[:：]\s*`?(\d+)`?", text)
        ncol = int(mc.group(1)) if mc else 0
        # tools/audit_tables.py 写入的完整性警告
        incomplete = "⚠️ 表结构不完整" in text

        cols = []
        for ln in text.split("\n"):
            if not re.match(r"^\|\s*\d+\s*\|", ln):
                continue
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) < 4:
                continue
            # 源仓库里存在两种导出格式，表头相同但数据行不同：
            #   A: | 1 | `id` | 主键ID | `integer` | - | 否 | - |      列名在第 2 列
            #   B: | 1 | - | id | `主键ID` | integer | - | - |         整行右移一列（多一个占位列）
            if cells[1] in ("-", ""):
                name, cn = cells[2], cells[3]
            else:
                name, cn = cells[1], cells[2]
            name = name.strip("`").strip()
            cn = cn.strip("`").strip()
            if name:
                cols.append((name, "" if cn == "-" else cn))

        rel = os.path.relpath(fp, base).replace("\\", "/")
        modules.setdefault(module, []).append((table, ncol, cols, rel, incomplete))

    total = sum(len(v) for v in modules.values())
    L = ["# 数据库表总索引", "",
         "> 共收录 **%d** 张表（表定义文件数；去重后唯一表名见下），覆盖 %d 个业务模块。"
         "索引由 `scripts/build_index.py` 从 `tables/` 下的 Markdown 自动生成，请勿手工编辑。"
         % (total, len(modules)),
         "",
         "> [!WARNING]",
         "> **这些表结构文档是「部分收录」，不是完整表结构。** 很多表只记录了升级补丁",
         "> 新增的列，缺少 `CREATE TABLE` 的基础列。表中「文档收录字段数」是**本文件记录了几行**，",
         "> 不等于表的真实列数。",
         ">",
         "> 写 SQL 前请用真实库核对：",
         "> ```sql",
         "> SELECT column_name, data_type, data_length, nullable",
         "> FROM user_tab_columns WHERE table_name = 'WORKFLOW_REQUESTBASE'",
         "> ORDER BY column_id;",
         "> ```",
         ">",
         "> 带 ⚠️ 的表已**确证不完整**（本仓库其他文档引用了它没收录的列），",
         "> 完整清单与判定依据见 [`_QUALITY.md`](./_QUALITY.md)。",
         "",
         "> 检索表结构请用统一检索脚本（比翻本文件更快）：",
         "> ```bash",
         "> python scripts/search.py workflow_currentoperator --scope db -d",
         "> python scripts/search.py 待办 --scope db",
         "> ```",
         "",
         "## 模块统计概览", "",
         "| 序号 | 业务模块 | 表数量 | 说明 |",
         "| :---: | :--- | :---: | :--- |"]
    for i, (mod, items) in enumerate(sorted(modules.items(), key=lambda kv: -len(kv[1])), 1):
        L.append("| %d | [%s](#%s) | **%d** | 涵盖 %s 模块核心业务与系统配置表 |"
                 % (i, mod, mod.lower(), len(items), mod))
    L.append("| **合计** | **全部模块** | **%d** | - |" % total)
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 分模块全量表清单")
    L.append("")
    for mod, items in sorted(modules.items(), key=lambda kv: -len(kv[1])):
        L.append("### %s" % mod)
        L.append("")
        L.append("> 本模块共收录 `%d` 张数据表。" % len(items))
        L.append("")
        L.append("| 序号 | 数据库表名 | 文档收录字段数 | 关键字段预览 | 详细定义文件 |")
        L.append("| :---: | :--- | :---: | :--- | :--- |")
        for i, (table, ncol, cols, rel, incomplete) in enumerate(sorted(items), 1):
            if cols:
                head = "、".join("`%s`(%s)" % (c, cn or "-") for c, cn in cols[:4])
                preview = head + (" 等共 %d 个字段" % ncol if ncol > 4 else "")
            else:
                preview = "-"
            flag = " ⚠️" if incomplete else ""
            L.append("| %d | `%s`%s | %d | %s | [%s](./%s) |"
                     % (i, table, flag, ncol, preview, os.path.basename(rel), rel))
        L.append("")
    write(os.path.join(base, "_INDEX.md"), L)
    return total, len(modules)


# ------------------------------------------------------------ 块二 后端接口

MODULE_ORDER = ["协作管理", "邮件模块", "表单建模", "人力资源",
                "工作流程", "知识管理", "考勤", "门户管理"]


def build_api_index():
    base = os.path.join(REFS, "02_backend_api")
    rows = OrderedDict()
    for fp in sorted(glob.glob(os.path.join(base, "*.md"))):
        name = os.path.basename(fp)
        if name.upper() == "_INDEX.MD":
            continue
        # 去掉 .md 后再剥掉切块编号后缀（人力资源_01 -> 人力资源）
        module = re.sub(r"_\d+$", "", name[:-3])
        text = open(fp, encoding="utf-8").read()
        for title, body in split_blocks(text, r"(?m)^##\s+(.*)$"):
            if "索引" in title:
                continue
            rows.setdefault(module, []).append(
                (title, extract(body, "请求方式"), extract(body, "请求地址"), name))

    total = sum(len(v) for v in rows.values())
    L = ["# 泛微 E9 后端接口总索引", "",
         "> 共 **%d** 个接口，按官网 8 大模块分类。大模块已切分为多个小文件，"
         "下表「文件」列指向具体文件。" % total, "",
         "> 索引由 `scripts/build_index.py` 自动生成，请勿手工编辑。",
         "> 检索接口请用统一检索脚本：",
         "> ```bash",
         "> python scripts/search.py getToDoWorkflowRequestList",
         "> python scripts/search.py 分部 --scope api --brief",
         "> ```",
         ""]
    for module in MODULE_ORDER:
        items = rows.get(module)
        if not items:
            continue
        L.append("## %s" % module)
        L.append("")
        L.append("| 接口 | 方法 | 地址 | 文件 |")
        L.append("|---|---|---|---|")
        for title, method, addr, fname in items:
            L.append("| %s | %s | `%s` | [%s](%s) |" % (title, method, addr, fname, fname))
        L.append("")
    write(os.path.join(base, "_INDEX.md"), L)
    return total, len(rows)


# ------------------------------------------------------------ 块三 前端 JSAPI

def build_js_index():
    base = os.path.join(REFS, "03_frontend_jsapi")
    rows = []
    for fp in sorted(glob.glob(os.path.join(base, "*.md"))):
        name = os.path.basename(fp)
        if name.upper() == "_INDEX.MD":
            continue
        text = open(fp, encoding="utf-8").read()
        h1 = ""
        m = re.search(r"(?m)^#\s+(.*)$", text)
        if m:
            h1 = m.group(1).strip()
        methods = []
        for title, body in split_blocks(text, r"(?m)^#{3,4}\s+(\d+\.\d+[^\n]*)$"):
            sig = ""
            sm = re.search(r"(?m)^>\s*([A-Za-z_][\w.]*)\s*:\s*function", body)
            if sm:
                sig = sm.group(1)
            methods.append((title, sig))
        rows.append((name, h1, methods))

    total = sum(len(m) for _, _, m in rows)
    L = ["# 前端 JS API 总索引", "",
         "> 共 **%d** 个前端接口方法，覆盖流程表单 `WfForm` 与表单建模 `ModeForm`。" % total, "",
         "> 索引由 `scripts/build_index.py` 自动生成，请勿手工编辑。",
         "> 检索请用统一检索脚本：",
         "> ```bash",
         "> python scripts/search.py convertFieldNameToId --scope js",
         "> python scripts/search.py 明细表 --scope js",
         "> ```",
         ""]
    for name, h1, methods in rows:
        L.append("## %s" % (h1 or name))
        L.append("")
        L.append("> 文件：[`%s`](./%s)　共 `%d` 个方法。" % (name, name, len(methods)))
        L.append("")
        L.append("| 序号 | 方法说明 | 接口名 | 文件 |")
        L.append("| :---: | :--- | :--- | :--- |")
        for i, (title, sig) in enumerate(methods, 1):
            L.append("| %d | %s | %s | [%s](./%s) |"
                     % (i, title, ("`%s`" % sig) if sig else "-", name, name))
        L.append("")
    write(os.path.join(base, "_INDEX.md"), L)
    return total, len(rows)


# ------------------------------------------------------------ 块四 集成扩展

def build_int_index():
    base = os.path.join(REFS, "04_integration")
    rows = []
    for fp in sorted(glob.glob(os.path.join(base, "*.md"))):
        name = os.path.basename(fp)
        if name.upper() == "_INDEX.MD":
            continue
        text = open(fp, encoding="utf-8").read()
        m = re.search(r"(?m)^#\s+(.*)$", text)
        h1 = m.group(1).strip() if m else name
        secs = [t for t, _ in split_blocks(text, r"(?m)^##\s+(.*)$")]
        rows.append((name, h1, secs))

    L = ["# 集成与扩展总索引", "",
         "> 覆盖 WebService (SOAP)、Java 后端二次开发、消息中心推送、"
         "第三方单点登录与组织架构同步。", "",
         "> 索引由 `scripts/build_index.py` 自动生成，请勿手工编辑。",
         "> 检索请用统一检索脚本：",
         "> ```bash",
         "> python scripts/search.py 钉钉 --scope int",
         "> python scripts/search.py BaseCronJob --scope int",
         "> ```",
         ""]
    for name, h1, secs in rows:
        L.append("## %s" % h1)
        L.append("")
        L.append("> 文件：[`%s`](./%s)" % (name, name))
        L.append("")
        if secs:
            for s in secs:
                L.append("- %s" % s)
            L.append("")
    write(os.path.join(base, "_INDEX.md"), L)
    return len(rows), 0


def main():
    if not os.path.isdir(REFS):
        print("!! 找不到 references 目录: %s" % REFS)
        return 1
    print("开始生成索引（源: Markdown）...")
    n_tab, n_mod = build_db_index()
    print("     块一 数据库: %d 张表 / %d 个模块" % (n_tab, n_mod))
    n_api, n_am = build_api_index()
    print("     块二 后端接口: %d 个接口 / %d 个模块" % (n_api, n_am))
    n_js, n_jf = build_js_index()
    print("     块三 前端 JSAPI: %d 个方法 / %d 个文件" % (n_js, n_jf))
    n_int, _ = build_int_index()
    print("     块四 集成扩展: %d 篇文档" % n_int)
    print("完成。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
