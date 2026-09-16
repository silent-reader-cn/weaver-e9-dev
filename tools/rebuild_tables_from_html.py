#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从泛微「数据字典」HTML 重建表结构文档
====================================
上游的 HTML 数据字典比此前落库的 Markdown **信息量大得多**，此前提取时丢失了：

  表级：中文名称、主键、说明            —— 全部 1687 张表都丢了
  列级：是否为外键、是否自增长、外键信息、默认值 —— 全部 18,002 列都丢了
  列本身：整列缺失                        —— 1,182 列 / 92 张表
  「允许为空」取值                        —— 584 处（旧格式 B 缺该列，只能填 `-`）
  4 张 kq_flow_split_* 存根表             —— 被整个丢弃

本脚本以 HTML 为准重建全部表文档，并把解析结果落成 JSON 存档（体积远小于 HTML 原件）。

用法:
    python tools/rebuild_tables_from_html.py <源目录> [--dry-run]
"""
import os
import re
import sys
import json
import glob

import collections

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)
from parse_dict_html import parse_file  # noqa: E402

DB_DIR = os.path.join(ROOT, "references", "01_database")
TABLES_DIR = os.path.join(DB_DIR, "tables")
SOURCE_DIR = os.path.join(DB_DIR, "_source")
JSON_NAME = "db_dictionary.json"


def esc(v):
    """转义 Markdown 表格单元格：竖线转义，换行转 <br>。"""
    if v is None:
        return ""
    s = str(v).replace("|", "\\|")
    s = re.sub(r"\s*\n\s*", "<br>", s.strip())
    return s


def cell(v, dash_if_empty=True):
    s = esc(v)
    return s if s else ("-" if dash_if_empty else "")


def render_md(info):
    """把解析结果渲染成表结构 Markdown。"""
    table = info.get("table") or ""
    cn = info.get("cn") or ""
    module = info.get("module") or ""
    pk = info.get("pk") or ""
    memo = (info.get("memo") or "").strip()
    cols = info.get("columns") or []

    L = ["# 泛微OA 数据表: `%s`" % table, ""]
    if cn:
        L.append("- **中文名称**: %s" % cn)
    L.append("- **所属模块**: `%s`" % module)
    L.append("- **数据库表名**: `%s`" % table)
    if pk:
        L.append("- **主键**: `%s`" % pk)
    L.append("- **字段数**: `%d`" % len(cols))
    L.append("")

    if memo and memo != cn:
        L.append("> 说明：%s" % memo.replace("\n", " "))
        L.append("")

    L.append("## 表结构定义 (Schema)")
    L.append("")

    if not cols:
        # 存根表：说明里写着「表结构和 X 一致」，本身没有列定义
        m = re.search(r"表结构和\s*([A-Za-z_][A-Za-z0-9_]*)\s*一致", memo)
        L.append("> [!NOTE]")
        L.append("> 本表在数据字典导出中**没有单独的列定义**。")
        if m:
            tgt = m.group(1)
            L.append("> 原始说明：「%s」" % memo)
            L.append(">")
            L.append("> 请参考 [`%s`](./%s.md)。" % (tgt, tgt))
        else:
            L.append("> 原始说明：「%s」" % memo if memo else "> （无说明）")
        L.append("")
        return "\n".join(L).rstrip() + "\n"

    L.append("| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 "
             "| 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |")
    L.append("| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: "
             "| :--- | :--- | :--- |")
    for c in cols:
        L.append("| %s | `%s` | %s | `%s` | %s | %s | %s | %s | %s | %s | %s |" % (
            cell(c.get("seq")), esc(c.get("name")), cell(c.get("cn")),
            esc(c.get("type")) or "-", cell(c.get("len")),
            cell(c.get("nullable")), cell(c.get("fk")), cell(c.get("auto")),
            cell(c.get("fk_info")), cell(c.get("default")), cell(c.get("memo"))))
    L.append("")
    return "\n".join(L).rstrip() + "\n"


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    src = argv[0]
    dry = "--dry-run" in argv
    if not os.path.isdir(src):
        print("!! 源目录不存在: %s" % src)
        return 1

    modules = sorted(d for d in os.listdir(src) if os.path.isdir(os.path.join(src, d)))
    print("源目录: %s" % src)
    print("模块数: %d" % len(modules))

    records = []      # [(模块, 表名, info)]
    skipped = []
    for mod in modules:
        for fp in sorted(glob.glob(os.path.join(src, mod, "**", "*.html"), recursive=True)):
            base = os.path.basename(fp)
            if base.lower() == "index.html":
                continue
            info = parse_file(fp)
            if not info.get("table"):
                skipped.append(fp)
                continue
            info["module_dir"] = mod
            if not info.get("module"):
                info["module"] = mod
            records.append((mod, info["table"], info))

    n_cols = sum(len(r[2]["columns"]) for r in records)
    n_stub = sum(1 for r in records if not r[2]["columns"])
    print("表页面: %d（其中无列定义的存根 %d）" % (len(records), n_stub))
    print("列总数: %d" % n_cols)
    if skipped:
        print("跳过 %d 个无法识别的文件" % len(skipped))

    if dry:
        print("\n[dry-run] 未写入任何文件。样例：")
        print(render_md(records[0][2])[:600])
        return 0

    # 1) 落 JSON 存档
    os.makedirs(SOURCE_DIR, exist_ok=True)
    payload = {
        "source": "泛微 OA 数据字典 HTML 导出（OA数据库结构）",
        "modules": modules,
        "table_count": len(records),
        "column_count": n_cols,
        "tables": [
            {
                "module": m, "table": t,
                "cn": i.get("cn", ""), "pk": i.get("pk", ""),
                "memo": i.get("memo", ""),
                "columns": i["columns"],
            } for m, t, i in records
        ],
    }
    jp = os.path.join(SOURCE_DIR, JSON_NAME)
    json.dump(payload, open(jp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("已写入 %s (%.1f MB)" % (os.path.relpath(jp, ROOT).replace("\\", "/"),
                                   os.path.getsize(jp) / 1048576))

    # 2) 重建 Markdown —— 原地覆盖，不做删除
    #    现有 1699 个表文件都是源 1703 张表的子集，多出的 4 个是存根表，直接新增即可。
    #    （用 rmtree 清空目录会被安全策略拦截，也没有必要。）
    per_mod = collections.Counter()
    written = set()
    for mod, table, info in records:
        d = os.path.join(TABLES_DIR, mod)
        os.makedirs(d, exist_ok=True)
        dst = os.path.join(d, "%s.md" % table)
        open(dst, "w", encoding="utf-8").write(render_md(info))
        written.add(os.path.normcase(os.path.abspath(dst)))
        per_mod[mod] += 1

    # 3) 报告「旧目录里有、但源数据里没有」的残留文件（不删除，仅提示）
    stale = []
    for fp in glob.glob(os.path.join(TABLES_DIR, "**", "*.md"), recursive=True):
        if os.path.normcase(os.path.abspath(fp)) not in written:
            stale.append(os.path.relpath(fp, TABLES_DIR).replace("\\", "/"))

    print("\n已重建 %d 个表文档，分布：" % sum(per_mod.values()))
    for m in modules:
        print("   %-24s %4d" % (m, per_mod[m]))
    if stale:
        print("\n!! 有 %d 个文件在源数据中不存在（未删除，请人工确认）：" % len(stale))
        for s in stale[:20]:
            print("   ", s)
    else:
        print("\n无残留文件，目录与源数据一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
