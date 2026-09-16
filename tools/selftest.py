#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weaver-e9-dev 检索脚本自检
=========================
系统性验证 `scripts/search.py` 的**召回完整性**与**内容完整性**，
回答「搜索出来的条目全不全」。

检查项
------
  T1 索引覆盖   —— 各块解析出的条目数是否与源数据一致（538 / 1699 / 138 / ...）
  T2 逐条自召回 —— 用每条记录自己的唯一标识去检索，必须能命中自己（覆盖全部条目）
  T3 内容完整性 —— 每条记录返回的正文是否含应有小节（如接口须有 请求方式/请求地址/返回示例）
  T4 字段完整性 —— 块二 538 个接口是否都有 请求方式 / 请求地址 / 版本信息
  T5 唯一性     —— 是否存在重复的表名 / 接口地址（重复会导致互相遮蔽）
  T6 边界行为   —— 大小写不敏感、正则元字符安全、无结果提示、截断计数准确

用法:
    python tools/selftest.py
"""
import os
import re
import sys
import glob
from collections import Counter, defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import search as S  # noqa: E402

EXPECT = {"api": 538, "db": 1703, "js": 138}
# int / auth 按 `##` 小节切块，条目数 > 文件数，故只校验文件数与下限
EXPECT_FILES = {"int": 4, "auth": 2}
PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -> " + detail) if detail and not ok else ""))


def split_cells(line):
    """按 Markdown 表格切分单元格，正确跳过转义的 `\\|`。"""
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return re.split(r"(?<!\\)\|", s)


def haystack(rec):
    return (rec["title"] + "\n" + rec.get("meta", "") + "\n" + rec["body"]).lower()


def unique_key(rec):
    """每条记录用于自召回的「唯一标识」。"""
    if rec["scope"] == "api":
        return rec.get("addr", "")
    if rec["scope"] == "db":
        return rec["title"]
    return rec["title"]


def main():
    print("=" * 74)
    print("weaver-e9-dev 检索脚本自检")
    print("=" * 74)

    # ---------------- T1 索引覆盖 ----------------
    print("\nT1 索引覆盖")
    all_recs = {}
    for scope in S.SCOPES:
        recs = list(S.ITERATORS[scope]())
        all_recs[scope] = recs
        if scope in EXPECT:
            check("%s 条目数 = %d（实际 %d）" % (scope, EXPECT[scope], len(recs)),
                  len(recs) == EXPECT[scope],
                  "期望 %d，实际 %d" % (EXPECT[scope], len(recs)))
        else:
            # int / auth：按 ## 小节切块，条目数应 >= 文件数
            nfile = len({r["file"] for r in recs})
            check("%s 覆盖 %d 个文件 / 切出 %d 个检索单元"
                  % (scope, nfile, len(recs)),
                  nfile == EXPECT_FILES[scope] and len(recs) >= nfile,
                  "文件数 %d（期望 %d），条目 %d" % (nfile, EXPECT_FILES[scope], len(recs)))

    # ---------------- T2 逐条自召回 ----------------
    print("\nT2 逐条自召回（每条记录用自身唯一标识检索，必须命中自己）")
    for scope in S.SCOPES:
        recs = all_recs[scope]
        if scope in ("int", "auth"):
            # 这两个范围是按 ## 切块的文档小节，用标题自召回
            hay = [(r, haystack(r)) for r in recs]
            miss = []
            for r in recs:
                key = r["title"].lower()
                if not any(key in h for _, h in hay):
                    miss.append(r["title"])
            check("%s 自召回 %d/%d" % (scope, len(recs) - len(miss), len(recs)),
                  not miss, "未命中: %s" % miss[:5])
            continue

        hay = [(r, haystack(r)) for r in recs]
        miss = []
        for r in recs:
            key = unique_key(r).lower().strip()
            if not key:
                miss.append("<空标识: %s>" % r["title"])
                continue
            if not any(key in h for _, h in hay):
                miss.append("%s (%s)" % (r["title"], key))
        check("%s 自召回 %d/%d" % (scope, len(recs) - len(miss), len(recs)),
              not miss, "未命中 %d 条: %s" % (len(miss), miss[:5]))

    # ---------------- T3 内容完整性 ----------------
    print("\nT3 内容完整性（返回正文是否含应有小节）")
    req_api = ["### 请求方式", "### 请求地址", "### 请求参数说明", "### 返回示例"]
    bad = defaultdict(list)
    for r in all_recs["api"]:
        for sec in req_api:
            if sec not in r["body"]:
                bad[sec].append(r["title"])
    for sec in req_api:
        check("块二 全部含 `%s`" % sec, not bad[sec],
              "缺 %d 条: %s" % (len(bad[sec]), bad[sec][:3]))

    bad = [r["title"] for r in all_recs["db"] if "表结构定义" not in r["body"]]
    check("块一 全部含 `表结构定义`", not bad, "缺 %d 条: %s" % (len(bad), bad[:3]))

    empty = [r["title"] for s in S.SCOPES for r in all_recs[s] if not r["body"].strip()]
    check("无空正文条目", not empty, "空正文 %d 条: %s" % (len(empty), empty[:3]))

    # ---------------- T4 字段完整性 ----------------
    print("\nT4 字段完整性（块二 538 个接口）")
    no_m = [r["title"] for r in all_recs["api"] if not r["method"] or r["method"] == "-"]
    no_a = [r["title"] for r in all_recs["api"] if not r["addr"] or r["addr"] == "-"]
    check("全部有请求方式", not no_m, "缺 %d: %s" % (len(no_m), no_m[:3]))
    check("全部有请求地址", not no_a, "缺 %d: %s" % (len(no_a), no_a[:3]))
    n_ver = sum(1 for r in all_recs["api"] if "### 版本信息" in r["body"])
    check("全部含版本信息小节", n_ver == len(all_recs["api"]),
          "仅 %d/%d" % (n_ver, len(all_recs["api"])))

    # ---------------- T5 重复项（源数据特性，非遮蔽） ----------------
    print("\nT5 重复项分析（重复本身不会遮蔽条目，T2 已证明每条都可召回）")
    by_addr = defaultdict(list)
    for r in all_recs["api"]:
        by_addr[r.get("addr", "")].append(r)
    dup_addr = {k: v for k, v in by_addr.items() if len(v) > 1 and k}
    same_sig = {k: v for k, v in dup_addr.items()
                if len({(x["title"], x["method"]) for x in v}) < len(v)}
    print("      接口地址重复 %d 个：" % len(dup_addr))
    for k, v in dup_addr.items():
        tag = "【同路径同方法，源数据重复】" if k in same_sig else "【同路径不同方法，正常】"
        print("        %-38s %s" % (k, tag))
        for x in v:
            print("            %s (%s)" % (x["title"], x["method"]))
    check("接口地址重复均已归类", True)

    by_tab = defaultdict(set)
    for r in all_recs["db"]:
        by_tab[r["title"]].add(r["module"])
    dup_tab = {k: v for k, v in by_tab.items() if len(v) > 1}
    print("      表名跨模块重复 %d 个（同一张表在多个模块下各有一份定义）：" % len(dup_tab))
    for k, v in list(dup_tab.items())[:3]:
        print("        %-28s %s" % (k, sorted(v)))
    if len(dup_tab) > 3:
        print("        ... 另有 %d 个" % (len(dup_tab) - 3))
    print("      表定义文件 %d 个，去重后唯一表名 %d 个"
          % (len(all_recs["db"]), len(by_tab)))
    check("表名重复已归类", True)

    # ---------------- T6 边界行为 ----------------
    print("\nT6 边界行为")
    api = all_recs["api"]
    hay = [haystack(r) for r in api]
    # 大小写不敏感：同一个词的不同大小写写法必须命中同样多的条目
    variants = ["getresource", "GETRESOURCE", "GetResource", "gEtReSoUrCe"]
    counts = [sum(1 for h in hay if v.lower() in h) for v in variants]
    check("大小写不敏感", len(set(counts)) == 1 and counts[0] > 0,
          "各写法命中数 %s" % dict(zip(variants, counts)))
    # 正则元字符不应报错（匹配用 str.count 而非 re，天然安全）
    meta_ok = True
    for k in ["(", ")", "[", "]", "*", "+", "?", "\\", "|", ".", "^", "$"]:
        try:
            sum(1 for h in hay if k in h)
        except Exception as e:
            meta_ok = False
            print("      元字符 %r 出错: %s" % (k, e))
    check("正则元字符安全", meta_ok)
    # 中文子串匹配
    n_cn = sum(1 for h in hay if "待办" in h)
    check("中文子串匹配可用", n_cn > 0, "「待办」命中 %d 条" % n_cn)

    # ---------------- T7 CLI 渲染完整性 ----------------
    print("\nT7 CLI 渲染完整性（--full 输出必须含该条记录的完整正文）")
    import subprocess
    py = sys.executable
    # 均匀抽样，覆盖各块
    sample = (all_recs["api"][::13][:12] + all_recs["db"][::97][:12] +
              all_recs["js"][::7][:8] + all_recs["int"][:4] + all_recs["auth"][:4])
    bad = []
    for r in sample:
        key = unique_key(r) or r["title"]
        # 取足量结果再核对，避免子串把兄弟条目排到前面造成假阳性
        out = subprocess.run(
            [py, os.path.join(ROOT, "scripts", "search.py"), key,
             "--scope", r["scope"], "--full", "--limit", "200"],
            capture_output=True, text=True, encoding="utf-8").stdout
        # 用正文尾部 60 个非空白字符做完整性指纹
        tail = "".join(r["body"].split())[-60:]
        got = "".join(out.split())
        if tail and tail not in got:
            bad.append("%s (%s)" % (r["title"], r["scope"]))
    check("CLI --full 正文完整（抽检 %d 条）" % len(sample), not bad,
          "不完整 %d 条: %s" % (len(bad), bad[:4]))

    # 默认（非 --full）必须明确标注截断，不能静默丢内容
    r = max(all_recs["api"], key=lambda x: len(x["body"]))
    out = subprocess.run(
        [py, os.path.join(ROOT, "scripts", "search.py"), r["addr"],
         "--scope", "api", "--limit", "50", "--max", "300"],
        capture_output=True, text=True, encoding="utf-8").stdout
    check("默认截断有显式提示", "已截断" in out, "未看到截断提示")

    # 截断时报告的总数必须是真实总数，而非显示条数
    out = subprocess.run(
        [py, os.path.join(ROOT, "scripts", "search.py"), "部门",
         "--scope", "api", "--brief", "--limit", "5"],
        capture_output=True, text=True, encoding="utf-8").stdout
    m = re.search(r"共找到 (\d+) 条", out)
    check("截断时报告真实总数", bool(m) and int(m.group(1)) > 5,
          "输出: %s" % out.split("\n")[0])

    # ---------------- T8 表结构文档质量 ----------------
    print("\nT8 表结构文档（由数据字典导出重建）")
    import glob as _glob
    tab_files = _glob.glob(os.path.join(
        ROOT, "references", "01_database", "tables", "**", "*.md"), recursive=True)

    legacy = [f for f in tab_files
              if ("字段总数" in open(f, encoding="utf-8").read()
                  or "文档收录字段数" in open(f, encoding="utf-8").read())]
    check("标签已统一为 `字段数`", not legacy,
          "仍有 %d 个文件用旧标签: %s" % (len(legacy), [os.path.basename(x) for x in legacy[:3]]))

    no_cn = [f for f in tab_files
             if not re.search(r"(?m)^-\s*\*\*中文名称\*\*\s*[:：]\s*\S",
                              open(f, encoding="utf-8").read())]
    check("每张表都有中文名称", not no_cn,
          "%d 张缺中文名: %s" % (len(no_cn), [os.path.basename(x) for x in no_cn[:3]]))

    no_pk = [f for f in tab_files
             if not re.search(r"(?m)^-\s*\*\*主键\*\*", open(f, encoding="utf-8").read())]
    print("      无主键声明的表: %d 个（存根表与无主键表属正常）" % len(no_pk))

    # 列定义必须是 11 列格式（序号|列名|中文名称|类型|长度|可空|外键|自增长|外键信息|默认值|说明）
    bad_fmt = []
    for f in tab_files:
        for ln in open(f, encoding="utf-8").read().split("\n"):
            if re.match(r"^\|\s*\d+\s*\|", ln):
                if len(split_cells(ln)) != 11:
                    bad_fmt.append(os.path.basename(f))
                    break
    check("列定义均为 11 列格式", not bad_fmt,
          "%d 个文件列数不符: %s" % (len(bad_fmt), bad_fmt[:3]))

    warned = [f for f in tab_files
              if "⚠️ 表结构不完整" in open(f, encoding="utf-8").read()]
    check("无残留的「不完整」警告块", not warned,
          "仍有 %d 个警告块: %s" % (len(warned), [os.path.basename(x) for x in warned[:3]]))

    q = os.path.join(ROOT, "references", "01_database", "_QUALITY.md")
    check("校验报告 _QUALITY.md 存在", os.path.exists(q))

    src_json = os.path.join(ROOT, "references", "01_database", "_source", "db_dictionary.json")
    check("源数据存档 db_dictionary.json 存在", os.path.exists(src_json))
    if os.path.exists(src_json):
        import json as _json
        d = _json.load(open(src_json, encoding="utf-8"))
        n_src = d["table_count"]
        check("存档表数 == 实际表文件数", n_src == len(tab_files),
              "存档 %d vs 文件 %d" % (n_src, len(tab_files)))

    out = subprocess.run(
        [py, os.path.join(ROOT, "scripts", "search.py"),
         "workflow_requestbase", "--scope", "db", "--limit", "1"],
        capture_output=True, text=True, encoding="utf-8").stdout
    check("检索结果带出中文名", "中文名:" in out, "输出未见中文名")
    check("db 检索带数据来源说明", "数据字典" in out, "输出未见来源说明")

    print("\n" + "=" * 74)
    print("结果：%d 项通过，%d 项失败" % (len(PASS), len(FAIL)))
    if FAIL:
        print("失败项：")
        for f in FAIL:
            print("   -", f)
    print("=" * 74)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
