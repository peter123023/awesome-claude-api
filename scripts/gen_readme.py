#!/usr/bin/env python3
"""根据 data/traffic.json 重新生成 README.MD 中各渠道的「月访问量」标注。

JSON 为数据源（单一事实来源），README 表格的访问量单元格由本脚本渲染。
以后每月更新：只需在 traffic.json 对应渠道下补充新月份的数字，重跑本脚本即可。

用法：
    python3 scripts/gen_readme.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
README = os.path.join(REPO, "README.MD")
JSON_PATH = os.path.join(REPO, "data", "traffic.json")


def fmt(n):
    """把整数访问量格式化为 M / K 可读字符串。"""
    if n is None:
        return "—"
    if n == 0:
        return "0"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def build_sub(data, color_up, color_down):
    """生成某一行的 <sub> 访问量标注，含两月对比与环比。"""
    aug = data.get("2026-08")
    sep = data.get("2026-09")

    # 9 月数据尚未填写
    if sep is None:
        return f"月访问量: {fmt(aug)} (2026-08) · 9月待更新"

    # 8 月基数为 0 的特殊情况
    if aug == 0:
        if sep == 0:
            return "月访问量: 0 (2026-08) → 0 (2026-09) 持平"
        return f"月访问量: 0 (2026-08) → {fmt(sep)} (2026-09) 新上榜"

    pct = (sep - aug) / aug * 100
    up = sep >= aug
    arrow = "↑" if up else "↓"
    col = color_up if up else color_down
    pct_html = f'<span style="color:{col}">{arrow}{pct:+.1f}%</span>'
    return f"月访问量: {fmt(aug)} (2026-08) → {fmt(sep)} (2026-09) {pct_html}"


def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        cfg = json.load(f)
    channels = cfg["channels"]
    color_up = cfg.get("color", {}).get("up", "#c0392b")
    color_down = cfg.get("color", {}).get("down", "#27ae60")

    row_pat = re.compile(r"\|([^<]*?)<br><sub>月访问量:.*?</sub>")
    sub_pat = re.compile(r"<sub>月访问量:.*?</sub>", re.S)

    with open(README, encoding="utf-8") as f:
        lines = f.readlines()

    changed = 0
    for i, line in enumerate(lines):
        if "<sub>月访问量" not in line:
            continue
        m = row_pat.search(line)
        if not m:
            continue
        name = m.group(1).strip()
        if name not in channels:
            print(f"[skip] 未匹配到渠道: {name}", file=sys.stderr)
            continue
        new_sub = f"<sub>{build_sub(channels[name], color_up, color_down)}</sub>"
        lines[i] = sub_pat.sub(new_sub, line, count=1)
        changed += 1

    with open(README, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"已更新 {changed} 行访问量标注")


if __name__ == "__main__":
    main()
