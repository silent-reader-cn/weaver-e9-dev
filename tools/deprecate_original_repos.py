#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给两个原仓库的 README 顶部插入「已归档，请改用新仓库」提示。

以**远程当前 README** 为基础（而非本地旧克隆），避免覆盖远程的新改动。

用法:
    python tools/deprecate_original_repos.py --dry-run
    python tools/deprecate_original_repos.py
"""
import os
import re
import sys
import json
import base64
import subprocess

OWNER = "silent-reader-cn"
NEW_REPO = "https://github.com/silent-reader-cn/weaver-e9-dev"

BANNERS = {
    "weaver-oa-dev": """## ⚠️ 本仓库已归档，请改用新仓库

本仓库内容已**全部合并**至 👉 **[weaver-e9-dev](%(new)s)**

合并后做的改进：

- **统一文档范式**：538 个后端接口 + 1,699 张表 + 138 个前端方法，现在**可被同一个检索脚本搜索**
- **修复残缺目录**：本仓库 `skills/weaver-oa-dev/` 下**缺失整个 `scripts/`**（没有检索工具与字典），表文件也只有 920/1699；`docs/` 与 `.agents/` 两份才是完整的
- **去掉三份重复副本**（`docs/` + `skills/` + `.agents/`），仓库体积 **38MB → 12MB**
- **统一两套混用的表结构列格式**，并修复了「结果被 `--limit` 截断时谎报总数」的检索脚本问题

**新仓库地址 → %(new)s**

本仓库已停止维护，保留仅供历史查阅。""",
    "weaver-e9-backend": """## ⚠️ 本仓库已归档，请改用新仓库

本仓库的文档范式、认证深度参考与检索机制已**全部并入** 👉 **[weaver-e9-dev](%(new)s)**

合并后做的改进：

- **接口扩充**：本仓库 538 个接口中唯一路径为 494 个，全部被 `weaver-oa-dev` 覆盖；合并后取并集，**多出 43 个接口**
- **检索升级**：`search_apis.py` 升级为统一的 `search.py`，支持 `--scope api|db|js|int|auth`，可跨「数据库 / 后端接口 / 前端 JSAPI / 集成扩展」四大块检索
- **新增内容**：1,699 张表结构、前端 WfForm/ModeForm API、WebService (SOAP)、Java 二次开发、消息推送、第三方 SSO
- **修复**：原脚本在结果被 `--limit` 截断时会谎报总数（命中 137 条却只报 20 条），新脚本会显式告知真实总数

**新仓库地址 → %(new)s**

本仓库已停止维护，保留仅供历史查阅。""",
}

COMMIT_MSG = """docs: 标注本仓库已归档，内容合并至 weaver-e9-dev

本仓库的内容已全部合并到 https://github.com/silent-reader-cn/weaver-e9-dev
并在合并中修复了若干问题（详见 README 顶部提示）。
本仓库不再维护，保留仅供历史查阅。"""


def gh(args, input_data=None, retries=5):
    """调用 gh CLI。GitHub API 偶发 502/503，做指数退避重试。"""
    import time
    env = dict(os.environ)
    env.setdefault("GH_CONFIG_DIR", r"C:\Users\Admin\AppData\Roaming\GitHub CLI")
    last = ""
    for attempt in range(retries):
        r = subprocess.run(["gh"] + args, capture_output=True, text=True,
                           input=input_data, encoding="utf-8", env=env)
        if r.returncode == 0:
            return r.stdout
        last = r.stderr.strip()
        if attempt < retries - 1 and re.search(r"Bad Gateway|502|503|timeout|EOF", last, re.I):
            wait = 2 ** attempt
            print("      API 暂时不可用，%d 秒后重试 (%d/%d)..." % (wait, attempt + 1, retries))
            time.sleep(wait)
            continue
        break
    raise RuntimeError("gh %s 失败:\n%s" % (" ".join(args), last))


def get_remote_readme(repo):
    out = gh(["api", "repos/%s/%s/contents/README.md" % (OWNER, repo)])
    data = json.loads(out)
    return base64.b64decode(data["content"]).decode("utf-8"), data["sha"]


def insert_banner(text, banner):
    """在首个 H1 标题之后插入提示块。若已存在则跳过。"""
    if "本仓库已归档" in text:
        return text, False
    lines = text.split("\n")
    idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if idx is None:
        return banner + "\n\n" + text, True
    out = lines[:idx + 1] + ["", "> [!IMPORTANT]"] + \
        [("> " + l) if l.strip() else ">" for l in banner.split("\n")] + \
        [""] + lines[idx + 1:]
    return "\n".join(out), True


def main(argv):
    dry = "--dry-run" in argv
    for repo, banner_tpl in BANNERS.items():
        print("=" * 70)
        print("仓库: %s/%s" % (OWNER, repo))
        text, sha = get_remote_readme(repo)
        print("  远程 README: %d 字符, sha=%s" % (len(text), sha[:10]))
        banner = banner_tpl % {"new": NEW_REPO}
        new_text, changed = insert_banner(text, banner)
        if not changed:
            print("  已含归档提示，跳过。")
            continue
        print("  插入提示后: %d 字符 (+%d)" % (len(new_text), len(new_text) - len(text)))
        if dry:
            print("  [dry-run] 前 20 行预览:")
            for l in new_text.split("\n")[:20]:
                print("     " + l)
            continue
        payload = json.dumps({
            "message": COMMIT_MSG,
            "content": base64.b64encode(new_text.encode("utf-8")).decode("ascii"),
            "sha": sha,
            "branch": "main",
        })
        out = gh(["api", "-X", "PUT",
                  "repos/%s/%s/contents/README.md" % (OWNER, repo),
                  "--input", "-"], input_data=payload)
        res = json.loads(out)
        print("  ✓ 已提交: %s" % res["commit"]["html_url"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
