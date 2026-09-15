#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weaver-e9-dev 统一检索工具
=========================
跨四大内容块按关键词检索，返回命中条目的**完整正文**，无需再打开 .md 文件。

  块一 数据库      references/01_database/tables/**/*.md   （1,699 张表）
  块二 后端接口    references/02_backend_api/*.md          （538 个 REST 接口）
  块三 前端 JSAPI  references/03_frontend_jsapi/*.md       （WfForm + ModeForm）
  块四 集成与扩展  references/04_integration/*.md
  横切 认证        references/auth/*.md

设计要点
--------
- **Markdown 是唯一真相源**：本脚本直接读 Markdown，不依赖任何预生成的字典，
  因此不存在「改了文档忘了重建索引导致搜不到」的漂移问题。
- 实测直接读取全部 1,699 个表文件仅约 0.23 秒，无需 JSON 加速层。
- 块二沿用 weaver-e9-backend 的检索机制（`^## ` 切块 + 正则抓 `### 请求方式` /
  `### 请求地址`），保证与原有使用习惯完全一致。

用法
----
  python scripts/search.py <关键词...> [选项]

示例
----
  python scripts/search.py 待办                              # 全块检索
  python scripts/search.py 待办 --scope api                  # 只搜后端接口
  python scripts/search.py getToDoWorkflowRequestList --full
  python scripts/search.py workflow_currentoperator --scope db
  python scripts/search.py 待办 --scope db -d                # 表结构详情
  python scripts/search.py convertFieldNameToId --scope js   # 前端 JS API
  python scripts/search.py 钉钉 --scope int                  # 集成文档
  python scripts/search.py 分部 --scope api --brief
  python scripts/search.py 请假 流程 --all
  python scripts/search.py 人员 --scope api --method GET --limit 10

选项
----
  --scope S     检索范围，可逗号组合：api | db | js | int | auth | all（默认 all）
  --brief       精简输出：仅一行 范围 | 标题 | 定位
  --full        输出命中条目的完整正文（不截断）
  --all         多个关键词需全部命中（默认任一命中即可）
  --method M    仅块二有效，按请求方式过滤 (GET/POST/PUT/DELETE)
  --limit N     最多返回结果数（默认 20）
  --max N       非 --full 时每条正文最多展示字符数（默认 1600）
  -d, --detail  同 --full（表结构检索时更顺手）

说明
----
- 关键词大小写不敏感；中文按子串匹配。
- 结果按命中次数降序排列。
- 脚本通过 __file__ 自动定位 references 目录，任意 cwd 下均可运行。
"""
import os
import re
import sys
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
REFS = os.path.join(ROOT, "references")

SCOPES = ["api", "db", "js", "int", "auth"]
SCOPE_LABEL = {
    "api": "后端接口",
    "db": "数据库",
    "js": "前端JSAPI",
    "int": "集成扩展",
    "auth": "认证",
}


# --------------------------------------------------------------------------
# 各块的解析器：统一产出 {scope, file, title, meta, body}
# --------------------------------------------------------------------------

def _split_blocks(text, pattern):
    """按 pattern 切块，返回 [(标题, 正文)]。pattern 需含一个标题捕获组。"""
    parts = re.split(pattern, text)
    out = []
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        out.append((title, body))
    return out


def _extract(body, header):
    """从正文中抽取某个 ### 小节的首行值（如 请求方式 / 请求地址）。"""
    m = re.search(r"###\s*%s\s*\n+(.*?)(?:\n###|\Z)" % re.escape(header), body, re.S)
    if not m:
        return ""
    return m.group(1).strip().split("\n")[0].strip()


def iter_api():
    """块二：每个 `## 标题` 为一个接口，跳过接口索引块。"""
    for fp in sorted(glob.glob(os.path.join(REFS, "02_backend_api", "*.md"))):
        name = os.path.basename(fp)
        if name.upper() == "_INDEX.MD":
            continue
        text = open(fp, encoding="utf-8").read()
        for title, body in _split_blocks(text, r"(?m)^##\s+(.*)$"):
            if "索引" in title:
                continue
            method = _extract(body, "请求方式")
            addr = _extract(body, "请求地址")
            meta = "方式: %s   地址: %s" % (method or "-", addr or "-")
            yield {"scope": "api", "file": name, "title": title,
                   "meta": meta, "method": method, "addr": addr, "body": body}


def iter_db():
    """块一：每个表定义文件为一条记录，表名/模块/字段全部纳入检索。"""
    pattern = os.path.join(REFS, "01_database", "tables", "**", "*.md")
    for fp in sorted(glob.glob(pattern, recursive=True)):
        rel = os.path.relpath(fp, os.path.join(REFS, "01_database"))
        text = open(fp, encoding="utf-8").read()
        m = re.search(r"数据库表名\*\*\s*[:：]\s*`([^`]+)`", text)
        if not m:
            m = re.search(r"(?m)^#\s*泛微OA 数据表\s*[:：]\s*`([^`]+)`", text)
        table = m.group(1) if m else os.path.splitext(os.path.basename(fp))[0]
        mm = re.search(r"所属模块\*\*\s*[:：]\s*`([^`]+)`", text)
        module = mm.group(1) if mm else os.path.basename(os.path.dirname(fp))
        mc = re.search(r"字段总数\*\*\s*[:：]\s*`?(\d+)`?", text)
        ncol = mc.group(1) if mc else ""
        meta = "模块: %s   字段数: %s" % (module, ncol or "-")
        yield {"scope": "db", "file": rel.replace("\\", "/"), "title": table,
               "meta": meta, "module": module, "body": text}


def iter_js():
    """块三：按 `### N.M` / `#### N.M` 编号小节切出每个前端方法。"""
    for fp in sorted(glob.glob(os.path.join(REFS, "03_frontend_jsapi", "*.md"))):
        name = os.path.basename(fp)
        if name.upper() == "_INDEX.MD":
            continue
        text = open(fp, encoding="utf-8").read()
        blocks = _split_blocks(text, r"(?m)^#{3,4}\s+(\d+\.\d+[^\n]*)$")
        if not blocks:
            blocks = [(_first_heading(text) or name, text)]
        for title, body in blocks:
            yield {"scope": "js", "file": name, "title": title,
                   "meta": "来源: %s" % name, "body": body}


def iter_md_scope(scope, subdir):
    """块四 / 认证：按 `## 标题` 切块；无 ## 时整篇作为一条。"""
    for fp in sorted(glob.glob(os.path.join(REFS, subdir, "*.md"))):
        name = os.path.basename(fp)
        if name.upper() == "_INDEX.MD":
            continue
        text = open(fp, encoding="utf-8").read()
        blocks = _split_blocks(text, r"(?m)^##\s+(.*)$")
        if not blocks:
            blocks = [(_first_heading(text) or name, text)]
        for title, body in blocks:
            yield {"scope": scope, "file": name, "title": title,
                   "meta": "来源: %s" % name, "body": body}


def _first_heading(text):
    m = re.search(r"(?m)^#\s+(.*)$", text)
    return m.group(1).strip() if m else ""


ITERATORS = {
    "api": iter_api,
    "db": iter_db,
    "js": iter_js,
    "int": lambda: iter_md_scope("int", "04_integration"),
    "auth": lambda: iter_md_scope("auth", "auth"),
}


# --------------------------------------------------------------------------
# 渲染
# --------------------------------------------------------------------------

def render(rec, full, max_chars):
    out = []
    out.append("▪ %s" % rec["title"])
    out.append("  [%s] %s" % (SCOPE_LABEL[rec["scope"]], rec["file"]))
    if rec.get("meta"):
        out.append("  %s" % rec["meta"])
    body = rec["body"].strip("\n")
    if body.strip():
        if not full and len(body) > max_chars:
            view = body[:max_chars].rstrip() + \
                "\n  …(已截断，完整正文请加 --full 或打开 %s)" % rec["file"]
        else:
            view = body
        out.append("\n".join(("  " + l) if l.strip() else "" for l in view.split("\n")))
    out.append("")
    return "\n".join(out)


def main(argv):
    args = list(argv)
    terms, scopes = [], ["all"]
    brief = full = all_match = False
    method = None
    limit, max_chars = 20, 1600

    i = 0
    while i < len(args):
        a = args[i]
        if a == "--brief":
            brief = True
        elif a == "--full":
            full = True
        elif a in ("-d", "--detail"):
            full = True
        elif a == "--all":
            all_match = True
        elif a == "--scope":
            i += 1
            scopes = [s.strip() for s in args[i].split(",")] if i < len(args) else ["all"]
        elif a == "--method":
            i += 1
            method = args[i].upper() if i < len(args) else None
        elif a == "--limit":
            i += 1
            limit = int(args[i]) if i < len(args) else 20
        elif a == "--max":
            i += 1
            max_chars = int(args[i]) if i < len(args) else 1600
        elif a.startswith("-"):
            pass
        else:
            terms.append(a)
        i += 1

    if not terms:
        print(__doc__)
        return 1

    if "all" in scopes:
        scopes = list(SCOPES)
    bad = [s for s in scopes if s not in ITERATORS]
    if bad:
        print("未知范围: %s（可选: %s, all）" % (", ".join(bad), " | ".join(SCOPES)))
        return 1

    results = []
    for scope in scopes:
        for rec in ITERATORS[scope]():
            if method and scope == "api" and rec.get("method", "").upper() != method:
                continue
            hay = (rec["title"] + "\n" + rec.get("meta", "") + "\n" + rec["body"]).lower()
            matched = [(t, hay.count(t.lower())) for t in terms if t.lower() in hay]
            if not matched:
                continue
            if all_match and len(matched) < len(terms):
                continue
            rec["score"] = sum(c for _, c in matched)
            results.append(rec)

    results.sort(key=lambda r: -r["score"])
    total = len(results)
    results = results[:limit]

    scope_txt = ",".join(scopes)
    if not results:
        print("未找到匹配「%s」的内容（范围: %s）。" % (" ".join(terms), scope_txt))
        return 0

    # 必须区分「总命中数」与「本次显示数」，否则用户会误以为只有这么多条
    if total > len(results):
        print("共找到 %d 条匹配（关键词: %s ；范围: %s），"
              "本次显示前 %d 条，可用 --limit N 调整：\n"
              % (total, " ".join(terms), scope_txt, len(results)))
    else:
        print("找到 %d 条匹配（关键词: %s ；范围: %s）：\n"
              % (total, " ".join(terms), scope_txt))
    for r in results:
        if brief:
            print("[%s] %s | %s" % (SCOPE_LABEL[r["scope"]], r["title"], r["file"]))
        else:
            print(render(r, full, max_chars))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
