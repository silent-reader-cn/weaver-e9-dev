#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 weaver-oa-dev 的数据库 / 前端 / 集成内容，按 weaver-e9-dev 的目录约定归位。

块一 数据库 : references/01_database/   (tables/ + core_tables.md + sql_cookbook.md)
块三 前端   : references/03_frontend_jsapi/  (wfform.md + modeform.md)
块四 集成   : references/04_integration/     (soap / java / push / sso)
横切 认证   : references/auth/          (quickstart + token 深度参考)

迁入后会自动调用 normalize_tables.normalize_tree()，把源仓库里混用的
第二套表结构列格式统一为主流格式（详见 tools/normalize_tables.py）。

用法:
    python tools/build_blocks.py <oa_dev_references_dir> <e9_backend_references_dir> <out_references_dir>
"""
import os
import re
import sys
import shutil

# 源文件 -> 目标相对路径
COPY_MAP = [
    # 块三 前端 JS API
    ("11_wfform_frontend_api.md", "03_frontend_jsapi/wfform.md"),
    ("12_modeform_frontend_api.md", "03_frontend_jsapi/modeform.md"),
    # 块四 集成与扩展
    ("14_webservice_soap_apis.md", "04_integration/webservice_soap.md"),
    ("09_custom_backend_dev.md", "04_integration/custom_backend_dev.md"),
    ("13_message_push_apis.md", "04_integration/message_push.md"),
    ("16_thirdparty_sso_and_sync.md", "04_integration/sso_and_sync.md"),
    # 横切 认证
    ("01_auth_and_security.md", "auth/auth_quickstart.md"),
]

# oa-dev 的 15 号文档要拆成「核心表全景字典」与「高频 SQL 模版」两篇
SQL_SRC = "15_high_frequency_sql_and_db_dict.md"
CORE_OUT = "01_database/core_tables.md"
SQL_OUT = "01_database/sql_cookbook.md"


def renumber(block, start=1):
    """把 `### 2.1 标题` 这类二级编号小节，重排为 `## N. 标题`。

    拆分后父级 `## 2.` 已不在同一文件里，保留 `### 2.1` 会形成孤儿编号。
    """
    counter = [start - 1]

    def repl(m):
        counter[0] += 1
        return "## %d. %s" % (counter[0], m.group(1).strip())

    return re.sub(r"(?m)^#{2,4}\s+\d+\.\d+\s+(.+)$", repl, block)


def split_sql_doc(text):
    """把 15_high_frequency_sql_and_db_dict.md 按 '## 2. 高频实用业务 SQL 模版' 拆成两篇。"""
    m = re.search(r"(?m)^##\s*2\.\s*高频", text)
    if not m:
        raise RuntimeError("未找到 SQL 模版小节，源文档结构可能已变")
    head = text[:m.start()].rstrip()
    tail = text[m.start():].rstrip()

    # 头部：去掉原标题与已不属于本文件的 SQL 引导句
    head = head.replace(
        "# 泛微OA (E-Cology) 核心数据库表结构与高频业务 SQL 字典",
        "# 核心系统表全景字典\n\n"
        "> 泛微 OA 二次开发中最常用的核心表速查：表名、中文说明、关键字段与关联关系。\n"
        "> 完整 1,699 张表见 [`tables/`](./tables/) 与 [`_INDEX.md`](./_INDEX.md)。",
        1,
    )
    head = head.replace(
        "在泛微 OA 二次开发、报表统计及数据对接中，直接查询数据库是最常见的高性能方案。"
        "本文档整理了 Ecology 核心系统表结构及最常用的高频 SQL 模版。",
        "在泛微 OA 二次开发、报表统计及数据对接中，直接查询数据库是最常见的高性能方案。",
        1,
    )
    # 去掉已成冗余的父级标题 '## 1. 核心系统表全景字典'
    head = re.sub(r"(?m)^##\s*1\.\s*核心系统表全景字典\s*$\n?", "", head)
    head = renumber(head)

    tail = tail.replace(
        "## 2. 高频实用业务 SQL 模版 (直接可用)",
        "# 高频业务 SQL 模版\n\n"
        "> 生产级 SQL 模版，直接可用。表结构定义见 [`tables/`](./tables/)。",
        1,
    )
    tail = renumber(tail)
    return head.rstrip() + "\n", tail.rstrip() + "\n"


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    oa_dir, e9_dir, out_dir = argv[0], argv[1], argv[2]

    # --- 块一：1,699 张表 ---
    src_tables = os.path.join(oa_dir, "database_tables")
    dst_tables = os.path.join(out_dir, "01_database", "tables")
    if not os.path.isdir(src_tables):
        print("!! 找不到源表目录: %s" % src_tables)
        return 1
    if os.path.isdir(dst_tables):
        shutil.rmtree(dst_tables)
    shutil.copytree(src_tables, dst_tables)
    n_tables = sum(len([f for f in fs if f.endswith(".md")])
                   for _, _, fs in os.walk(dst_tables))
    print("块一 数据库: 迁入 %d 个表定义文件 -> %s" % (n_tables, dst_tables))

    # --- 块一：核心表字典 + SQL 模版 ---
    sql_text = open(os.path.join(oa_dir, SQL_SRC), encoding="utf-8").read()
    core, cook = split_sql_doc(sql_text)
    os.makedirs(os.path.join(out_dir, "01_database"), exist_ok=True)
    open(os.path.join(out_dir, CORE_OUT), "w", encoding="utf-8").write(core)
    open(os.path.join(out_dir, SQL_OUT), "w", encoding="utf-8").write(cook)
    print("块一 数据库: 拆出 %s (%d 行) 与 %s (%d 行)"
          % (CORE_OUT, core.count("\n"), SQL_OUT, cook.count("\n")))

    # --- 块三 / 块四 / 认证 ---
    for src, dst in COPY_MAP:
        sp = os.path.join(oa_dir, src)
        dp = os.path.join(out_dir, dst)
        if not os.path.exists(sp):
            print("!! 源文件缺失: %s" % sp)
            continue
        os.makedirs(os.path.dirname(dp), exist_ok=True)
        shutil.copyfile(sp, dp)
        print("迁入 %-46s <- %s" % (dst, src))

    # --- 认证深度参考（来自 e9-backend）---
    sp = os.path.join(e9_dir, "auth_token.md")
    if os.path.exists(sp):
        dp = os.path.join(out_dir, "auth", "auth_token.md")
        os.makedirs(os.path.dirname(dp), exist_ok=True)
        shutil.copyfile(sp, dp)
        print("迁入 %-46s <- weaver-e9-backend/references/auth_token.md" % "auth/auth_token.md")
    else:
        print("!! 找不到 e9-backend 的 auth_token.md: %s" % sp)

    # --- 统一表结构列格式（源仓库混有两套导出格式）---
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from normalize_tables import normalize_tree
    print("统一表结构列格式：")
    normalize_tree(dst_tables)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
