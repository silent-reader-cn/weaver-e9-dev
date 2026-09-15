#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一数据库表结构文档的列格式
============================
weaver-oa-dev 源仓库里存在**两套表结构导出格式**。表头完全相同，但数据行不同：

  格式 A（1636 张，主流）
      | 1 | `id` | 主键ID | `integer` | - | 否 | - |
      序号 | 列名 | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注

  格式 B（62 张，另有 1 张同构）
      | 1 | - | id | `主键ID` | integer | - | - |
      序号 |  ─  | 列名 | 中文说明 | 数据类型 | 长度 | 字段备注
      ^ 整行自第 2 列起右移一格，多出一个 `-` 占位列，且缺少「允许为空」

本脚本把格式 B 归一化为格式 A：

  1 | - | id | `主键ID` | integer | - | -
    ↓
  1 | `id` | 主键ID | `integer` | - | - | -

说明：
- 「允许为空」在格式 B 中不存在，填 `-` 表示未知，不臆造 `否`。
- 中文说明在格式 B 里带反引号、格式 A 里不带，转换时剥掉。
- 脚本幂等：已是格式 A 的行不会被二次修改。

用法:
    python tools/normalize_tables.py --check     # 只报告，不修改
    python tools/normalize_tables.py             # 执行归一化
    python tools/normalize_tables.py <tables_dir>
"""
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
DEFAULT_DIR = os.path.join(ROOT, "references", "01_database", "tables")

ROW_RE = re.compile(r"^\|\s*\d+\s*\|")


def is_format_b(cells):
    """格式 B 的特征：第 2 列（列名位）是占位符 `-`。"""
    return len(cells) >= 4 and cells[1] in ("-", "")


def convert_row(line):
    """把一行格式 B 数据行转成格式 A。非格式 B 行原样返回。"""
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 7 or not is_format_b(cells):
        return line
    seq, _, col, cn, typ, length, memo = cells
    col = col.strip("`").strip()
    cn = cn.strip("`").strip()
    typ = typ.strip("`").strip()
    if not col:
        return line
    return "| %s | `%s` | %s | `%s` | %s | - | %s |" % (
        seq, col, cn or "-", typ or "-", length or "-", memo or "-")


def convert_text(text):
    """转换整篇文档，返回 (新文本, 改动行数)。"""
    out, changed = [], 0
    for line in text.split("\n"):
        if ROW_RE.match(line):
            new = convert_row(line)
            if new != line:
                changed += 1
                out.append(new)
                continue
        out.append(line)
    return "\n".join(out), changed


def normalize_tree(root, check_only=False):
    files = []
    for dirpath, _, names in os.walk(root):
        for n in names:
            if n.endswith(".md"):
                files.append(os.path.join(dirpath, n))
    files.sort()

    touched, total_rows = [], 0
    for fp in files:
        text = open(fp, encoding="utf-8").read()
        new, changed = convert_text(text)
        if changed:
            total_rows += changed
            touched.append((os.path.relpath(fp, root), changed))
            if not check_only:
                open(fp, "w", encoding="utf-8").write(new)

    print("扫描文件: %d 个" % len(files))
    if touched:
        print("%s: %d 个文件 / %d 行" % (
            "待归一化" if check_only else "已归一化", len(touched), total_rows))
        for rel, n in touched[:10]:
            print("   %-52s %d 行" % (rel, n))
        if len(touched) > 10:
            print("   ... 另有 %d 个文件" % (len(touched) - 10))
    else:
        print("全部已是格式 A，无需处理。")
    return len(touched), total_rows


def main(argv):
    check_only = "--check" in argv
    args = [a for a in argv if not a.startswith("-")]
    root = args[0] if args else DEFAULT_DIR
    if not os.path.isdir(root):
        print("!! 目录不存在: %s" % root)
        return 1
    print("目标目录: %s" % root)
    normalize_tree(root, check_only=check_only)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
