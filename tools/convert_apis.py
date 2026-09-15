#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 weaver-oa-dev 的 538 个后端 REST 接口文档，重排为 weaver-e9-backend 的文档范式。

源范式（oa-dev，每个接口）:
    ### 1. 流程实例：删除流程（对外）
    > **补充说明**：流程删除
    - **接口路径 (Endpoint)**: `/api/workflow/paService/deleteRequest`
    - **请求方式 (HTTP Method)**: `POST`
    - **版本要求**: 系统版本 ≥ 9.00
    - **模块归属**: `工作流程 > 流程实例：删除流程（对外）`
    #### 请求参数 (Request Parameters)
    | 参数名 | 类型 | 必填 | 说明 | 示例值 |
    #### 响应字段 (Response Fields)
    | 字段名 | 类型 | 说明 |
    #### 响应示例 (Response Example)
    ```json ... ```

目标范式（e9-backend，每个接口）:
    ## 流程实例：删除流程（对外）

    ### 概述
    **补充说明**：流程删除

    ### 请求方式
    POST

    ### 请求地址
    /api/workflow/paService/deleteRequest

    ### 版本信息
    | Ecology版本 | 生效 KB 版本 |
    | --- | --- |
    | 9.00 |  |

    ### 请求参数说明
    ...
    ### 返回值类型
    JSON
    ### 返回示例
    ...
    ### 返回参数说明
    ...

为什么要转: references/02_backend_api/ 下的文档由 scripts/search.py 按
「^## 切块 + 正则抓 ### 请求方式 / ### 请求地址」检索，只有目标范式才能被搜到。
因此 `### 请求方式` / `### 请求地址` 的值必须是裸文本（不能带反引号或列表符号）。

用法:
    python tools/convert_apis.py <oa_dev_references_dir> <out_dir>
"""
import os
import re
import sys
import glob
import json
from collections import OrderedDict

# 源文件 -> 模块名。08 文件同时含协作与邮件，按接口路径再分。
MODULE_MAP = OrderedDict([
    ("02_workflow_apis.md", "工作流程"),
    ("03_hrm_apis.md", "人力资源"),
    ("04_doc_knowledge_apis.md", "知识管理"),
    ("05_attendance_apis.md", "考勤"),
    ("06_form_modeling_apis.md", "表单建模"),
    ("07_portal_apis.md", "门户管理"),
    ("08_cowork_and_email_apis.md", "协作与邮件"),
])

# 模块输出顺序（与 e9-backend 的 _INDEX.md 分组顺序一致）
MODULE_ORDER = ["协作管理", "邮件模块", "表单建模", "人力资源",
                "工作流程", "知识管理", "考勤", "门户管理"]

CHUNK_SIZE = 30  # 与 e9-backend 一致：每个切块文件最多 30 个接口

SECTION_ALIASES = {
    "params": "请求参数",
    "fields": "响应字段",
    "example": "响应示例",
}


def strip_code(s):
    """去掉包裹值的一层反引号 / 引号，得到裸文本。"""
    s = s.strip()
    s = s.strip("`").strip()
    s = s.strip('"').strip("'").strip()
    return s.strip()


def parse_descriptions(body):
    """抽取接口的描述行。

    描述行以 `> **补充说明**：` / `> **功能说明**：` 开头，但**续行不带 `>` 前缀**
    （例如 `> **功能说明**：{` 后面跟一整段 JSON 字段说明）。
    因此从描述行开始，一直吃到下一个元信息行 / 小节标题 / 另一条描述行为止。
    一个接口可能同时含两条描述，都要保留。
    """
    lines = body.split("\n")
    entries = []
    i = 0
    while i < len(lines):
        m = re.match(r"^>\s*\*\*(补充说明|功能说明)\*\*\s*[:：]\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        label = m.group(1)
        buf = [m.group(2).rstrip()]
        i += 1
        while i < len(lines):
            ln = lines[i]
            if re.match(r"^(>\s*\*\*|-\s+\*\*|####|###|---)", ln):
                break
            buf.append(ln)
            i += 1
        while buf and not buf[-1].strip():
            buf.pop()
        entries.append((label, "\n".join(buf)))
    return entries


def render_desc(entries):
    """单行描述内联；多行描述（如 JSON 字段说明）用代码块包裹。"""
    out = []
    for label, txt in entries:
        txt = txt.strip()
        if "\n" in txt:
            lang = "json" if txt.startswith("{") else "text"
            out.append("**%s**：\n\n```%s\n%s\n```" % (label, lang, txt))
        elif txt:
            out.append("**%s**：%s" % (label, txt))
        else:
            out.append("**%s**" % label)
    return "\n\n".join(out)


def parse_block(body):
    """解析单个接口块，返回 (meta, desc, sections)。"""
    # 源文档每个接口块末尾都有一条 `---` 分隔线，先剥掉，
    # 否则会被最后一个小节（响应示例）吞进去，破坏输出结构。
    body = body.rstrip()
    if body.endswith("---"):
        body = body[:-3].rstrip()

    meta = {}
    for key, pat in [("path", r"接口路径\s*\(Endpoint\)"),
                     ("method", r"请求方式\s*\(HTTP Method\)"),
                     ("version", r"版本要求"),
                     ("owner", r"模块归属")]:
        m = re.search(r"(?m)^-\s+\*\*" + pat + r"\*\*\s*[:：]\s*(.*)$", body)
        meta[key] = strip_code(m.group(1)) if m else ""

    desc = render_desc(parse_descriptions(body))

    sections = {}
    for key, pat in SECTION_ALIASES.items():
        m = re.search(r"(?m)^####\s*" + pat + r"[^\n]*\n(.*?)(?=^####\s|\Z)", body, re.S)
        sections[key] = m.group(1).strip() if m else ""
    return meta, desc, sections


def extract_version(version_text):
    """从 '系统版本 ≥ 9.00' / 'E9/KB900190601' 中抽出可放进表格的版本号。"""
    if not version_text:
        return ""
    m = re.search(r"(\d+\.\d+)", version_text)
    if m:
        return m.group(1)
    return version_text


def extract_kb(version_text):
    m = re.search(r"(KB\s*\d+)", version_text, re.I)
    return m.group(1) if m else ""


def normalize_table(seg, want_header):
    """统一表头用词，保留原有列与反引号可读性。"""
    if not seg.strip():
        return ""
    lines = seg.split("\n")
    out = []
    for i, ln in enumerate(lines):
        if i == 0 and ln.strip().startswith("|"):
            out.append(want_header)
            continue
        out.append(ln)
    # 去掉末尾空行
    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out)


PARAM_HEADER = "| 参数名 | 类型 | 必填 | 说明 | 示例值 |"
PARAM_SEP = "| --- | --- | --- | --- | --- |"
FIELD_HEADER = "| 字段名 | 类型 | 说明 |"
FIELD_SEP = "| --- | --- | --- |"


def emit_api(title, meta, desc, sections):
    """按 e9-backend 范式渲染一个接口。"""
    L = []
    L.append("## " + title)
    L.append("")

    if desc:
        L.append("### 概述")
        L.append("")
        L.append(desc)
        L.append("")

    L.append("### 请求方式")
    L.append("")
    L.append(meta["method"] or "-")          # 裸文本，供检索脚本抽取
    L.append("")

    L.append("### 请求地址")
    L.append("")
    L.append(meta["path"] or "-")            # 裸文本，供检索脚本抽取
    L.append("")

    L.append("### 版本信息")
    L.append("")
    L.append("| Ecology版本 | 生效 KB 版本 |")
    L.append("| --- | --- |")
    L.append("| %s | %s |" % (extract_version(meta["version"]) or "-", extract_kb(meta["version"])))
    L.append("")

    if meta["owner"]:
        L.append("### 模块归属")
        L.append("")
        L.append(meta["owner"])
        L.append("")

    params = sections["params"]
    L.append("### 请求参数说明")
    L.append("")
    if params.strip().startswith("|"):
        L.append(PARAM_HEADER)
        L.append(PARAM_SEP)
        rows = [l for l in params.split("\n")[2:] if l.strip()]
        L.extend(rows)
    elif params.strip():
        L.append(params.strip())
    else:
        L.append("无特定请求参数（仅需通用请求头认证）。")
    L.append("")

    L.append("### 返回值类型")
    L.append("")
    L.append("JSON")
    L.append("")

    if sections["example"].strip():
        L.append("### 返回示例")
        L.append("")
        L.append(sections["example"].strip())
        L.append("")

    fields = sections["fields"]
    if fields.strip().startswith("|"):
        L.append("### 返回参数说明")
        L.append("")
        L.append(FIELD_HEADER)
        L.append(FIELD_SEP)
        rows = [l for l in fields.split("\n")[2:] if l.strip()]
        L.extend(rows)
        L.append("")

    L.append("---")
    L.append("")
    return "\n".join(L)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    src_dir, out_dir = argv[0], argv[1]
    os.makedirs(out_dir, exist_ok=True)

    apis = []          # [(module, title, meta, desc, sections)]
    stats = {"total": 0, "no_desc": 0, "no_version": 0, "no_fields": 0}
    problems = []

    for fname, module in MODULE_MAP.items():
        fp = os.path.join(src_dir, fname)
        if not os.path.exists(fp):
            problems.append("源文件缺失: %s" % fp)
            continue
        text = open(fp, encoding="utf-8").read()
        chunks = re.split(r"(?m)^###\s+\d+\.\s*(.*)$", text)
        # chunks: [前言, 标题1, 正文1, 标题2, 正文2, ...]
        for i in range(1, len(chunks), 2):
            title = re.sub(r"\s+", " ", chunks[i].strip())
            body = chunks[i + 1]
            meta, desc, sections = parse_block(body)
            if not meta["path"]:
                problems.append("无接口路径: %s / %s" % (fname, title))
            # 08 文件按路径再分模块
            mod = module
            if module == "协作与邮件":
                if "/cowork/" in meta["path"]:
                    mod = "协作管理"
                elif "/email/" in meta["path"]:
                    mod = "邮件模块"
                else:
                    problems.append("08 文件无法归类: %s" % meta["path"])
            stats["total"] += 1
            if not desc:
                stats["no_desc"] += 1
            if not meta["version"]:
                stats["no_version"] += 1
            if not sections["fields"].strip():
                stats["no_fields"] += 1
            apis.append({"module": mod, "title": title, "meta": meta,
                         "desc": desc, "sections": sections})

    # 安全检查：正文里若出现行首 '## '，会在检索时被误切块
    for a in apis:
        blob = "\n".join(a["sections"].values())
        for ln in blob.split("\n"):
            if re.match(r"^##\s+", ln):
                problems.append("正文含行首 ## : %s" % a["title"])
                break

    # 按模块分组并切块
    grouped = OrderedDict()
    for m in MODULE_ORDER:
        grouped[m] = [a for a in apis if a["module"] == m]

    index_rows = OrderedDict()
    written = []
    for module, items in grouped.items():
        if not items:
            continue
        nchunks = (len(items) + CHUNK_SIZE - 1) // CHUNK_SIZE
        for ci in range(nchunks):
            part = items[ci * CHUNK_SIZE:(ci + 1) * CHUNK_SIZE]
            if nchunks > 1:
                fname = "%s_%02d.md" % (module, ci + 1)
                head = "# %s — E9 后端接口参考（第 %d/%d 部分）" % (module, ci + 1, nchunks)
            else:
                fname = "%s.md" % module
                head = "# %s — E9 后端接口参考" % module

            L = [head, "",
                 "> 本部分含 %d 个接口。" % len(part),
                 "> 请求地址需拼接 OA 根地址，并携带 Token 认证请求头（见《Token 认证》）。",
                 ""]
            # 本部分接口索引（标题含「索引」，检索脚本会自动跳过）
            L.append("## 本部分接口索引")
            L.append("| 接口 | 方法 | 地址 |")
            L.append("|---|---|---|")
            for a in part:
                L.append("| %s | %s | `%s` |" % (a["title"], a["meta"]["method"], a["meta"]["path"]))
            L.append("")
            L.append("")
            L.append("---")
            L.append("")
            for a in part:
                L.append(emit_api(a["title"], a["meta"], a["desc"], a["sections"]))

            open(os.path.join(out_dir, fname), "w", encoding="utf-8").write("\n".join(L))
            written.append((fname, len(part)))
            for a in part:
                index_rows.setdefault(module, []).append((a["title"], a["meta"]["method"], a["meta"]["path"], fname))

    # 生成总索引 _INDEX.md
    total = sum(len(v) for v in index_rows.values())
    IL = ["# 泛微 E9 后端接口总索引", "",
          "> 共 %d 个接口，按官网 8 大模块分类。大模块已切分为多个小文件，下表「文件」列指向具体文件。" % total,
          ""]
    for module in MODULE_ORDER:
        rows = index_rows.get(module)
        if not rows:
            continue
        IL.append("")
        IL.append("## %s" % module)
        IL.append("")
        IL.append("| 接口 | 方法 | 地址 | 文件 |")
        IL.append("|---|---|---|---|")
        for title, method, path, fname in rows:
            IL.append("| %s | %s | `%s` | [%s](%s) |" % (title, method, path, fname, fname))
    IL.append("")
    open(os.path.join(out_dir, "_INDEX.md"), "w", encoding="utf-8").write("\n".join(IL))

    # 报告
    print("=== 转换报告 ===")
    print("接口总数: %d" % stats["total"])
    print("输出文件: %d 个 + _INDEX.md" % len(written))
    print("无描述(概述): %d   无版本要求: %d   无响应字段: %d"
          % (stats["no_desc"], stats["no_version"], stats["no_fields"]))
    print("分块情况:")
    for fname, n in written:
        print("   %-22s %d" % (fname, n))
    if problems:
        print("\n!! 需要关注 %d 处:" % len(problems))
        for p in problems[:20]:
            print("   -", p)
    else:
        print("\n无结构性问题。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
