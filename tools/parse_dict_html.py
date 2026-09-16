#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
解析泛微「数据字典」导出的 HTML
================================
原始数据是每个表一个 HTML（`<表名>(<中文名>).html`），内容是一张表格。

表级字段：数据库表名 / 中文名称 / 所属模块 / 主键 / 说明
列级字段：序号 / 数据库列名 / 中文名称 / 数据类型 / 长度 /
          是否允许空值 / 是否为外键 / 是否自增长 / 外键信息 / 默认值 / 说明

用法（作为库）:
    from parse_dict_html import parse_file
    info = parse_file(path)
"""
import os
import re
import html
from html.parser import HTMLParser


class TableParser(HTMLParser):
    """把 HTML 里的所有 <table> 解析成 [[cell,...],...]，自动处理 colspan/rowspan。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self._tstack = []
        self._row = None
        self._cell = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table":
            self._tstack.append([])
        elif tag == "tr" and self._tstack:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = {"text": [], "colspan": int(a.get("colspan", 1) or 1),
                          "rowspan": int(a.get("rowspan", 1) or 1)}
        elif tag == "br" and self._cell is not None:
            self._cell["text"].append("\n")

    def handle_data(self, data):
        if self._cell is not None:
            self._cell["text"].append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self._cell is not None and self._row is not None:
            txt = "".join(self._cell["text"])
            txt = re.sub(r"[ \t\u00a0]+", " ", txt).strip()
            self._row.append({"text": txt, "colspan": self._cell["colspan"]})
            self._cell = None
        elif tag == "tr" and self._row is not None and self._tstack:
            if self._row:
                self._tstack[-1].append(self._row)
            self._row = None
        elif tag == "table" and self._tstack:
            self.tables.append(self._tstack.pop())

    def error(self, message):
        pass


def _flat_rows(rows):
    """把带 colspan 的行展开成对齐的文本列表。"""
    out = []
    for r in rows:
        cells = []
        for c in r:
            cells.append(c["text"])
            for _ in range(c["colspan"] - 1):
                cells.append("")
        out.append(cells)
    return out


def parse_html(text):
    """解析列定义。

    注意：少数文件的列头行与表级信息分处**不同的 <table>**，
    所以先把所有 table 的行按文档顺序拼起来，再定位「数据库列名」列头行。
    """
    p = TableParser()
    p.feed(text)
    all_rows = []
    for tbl in p.tables:
        all_rows.extend(_flat_rows(tbl))
    for i, r in enumerate(all_rows):
        if any("数据库列名" in c for c in r):
            return _extract(all_rows, i)
    return None


def _extract(rows, header_idx):
    """从列头行往后提取字段定义。"""
    header = rows[header_idx]
    # 定位各列在行中的下标（列头可能跨列，取第一个非空匹配）
    def find(*keys):
        for j, c in enumerate(header):
            for k in keys:
                if k in c:
                    return j
        return None

    idx = {
        "seq": find("序号"),
        "name": find("数据库列名"),
        "cn": find("中文名称"),
        "type": find("数据类型"),
        "len": find("长度"),
        "nullable": find("是否允许空值", "允许空值"),
        "fk": find("是否为外键"),
        "auto": find("是否自增长"),
        "fk_info": find("外键信息"),
        "default": find("默认值"),
        "memo": find("说明"),
    }
    cols = []
    for r in rows[header_idx + 1:]:
        if len(r) < 3:
            continue
        seq = r[idx["seq"]] if idx["seq"] is not None and idx["seq"] < len(r) else ""
        if not re.fullmatch(r"\d+", (seq or "").strip()):
            continue
        def g(k):
            j = idx[k]
            return r[j].strip() if j is not None and j < len(r) else ""
        name = g("name")
        if not name:
            continue
        cols.append({
            "seq": seq.strip(), "name": name, "cn": g("cn"), "type": g("type"),
            "len": g("len"), "nullable": g("nullable"), "fk": g("fk"),
            "auto": g("auto"), "fk_info": g("fk_info"), "default": g("default"),
            "memo": g("memo"),
        })
    return cols


def parse_meta(text):
    """提取表级字段（数据库表名 / 中文名称 / 所属模块 / 主键 / 说明）。

    注意：表级信息都在「数据库列名」列头行**之前**。列头行里也有「中文名称」，
    必须排除，否则会把「数据类型」误当成中文表名。
    """
    p = TableParser()
    p.feed(text)
    vals = []
    for tbl in p.tables:
        rows = _flat_rows(tbl)
        cut = None
        for i, r in enumerate(rows):
            if any("数据库列名" in c for c in r):
                cut = i
                break
        for r in (rows[:cut] if cut is not None else rows):
            vals.extend([c for c in r if c])
    meta = {}
    labels = {"数据库表名": "table", "中文名称": "cn", "所属模块": "module",
              "主键": "pk", "说明": "memo"}
    for i, v in enumerate(vals):
        if v in labels and i + 1 < len(vals):
            key = labels[v]
            nxt = vals[i + 1]
            if key not in meta or not meta[key]:
                meta[key] = nxt
    return meta


def parse_file(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    cols = parse_html(text) or []
    meta = parse_meta(text)
    base = os.path.basename(path)
    m = re.match(r"^(.*?)\((.+)\)\.html?$", base)
    if m:
        # 文件名里的表名与中文名最可靠，优先采用
        meta["table"] = m.group(1)
        meta["cn"] = m.group(2)
    meta["columns"] = cols
    meta["file"] = path
    return meta


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    info = parse_file(sys.argv[1])
    print("表名:", info.get("table"))
    print("中文名:", info.get("cn"))
    print("所属模块:", info.get("module"))
    print("主键:", info.get("pk"))
    print("列数:", len(info["columns"]))
    for c in info["columns"][:8]:
        print("  ", c)
