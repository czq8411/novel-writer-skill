#!/usr/bin/env python3
"""章节字数检查脚本

用法:
    python scripts/check_chapter_wordcount.py <章节文件路径>
    python scripts/check_chapter_wordcount.py <章节文件路径> --target 4000
    python scripts/check_chapter_wordcount.py <章节文件路径> --json
    python scripts/check_chapter_wordcount.py <章节文件路径> --detail

输出:
    标准模式: 人类可读的字数报告
    --json: JSON格式输出，便于自动化流程集成
    --detail: 详细分析（对话占比、描写占比、叙述占比）
"""

import argparse
import json
import re
import sys
from pathlib import Path


def count_chinese_chars(text):
    """统计中文字符数（不含标点、英文、数字）"""
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
    return len(chinese_chars)


def count_chinese_with_punctuation(text):
    """统计中文字符数（含中文标点）"""
    chinese_and_punct = re.findall(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', text)
    return len(chinese_and_punct)


def count_total_chars(text):
    """统计总字符数（含所有字符）"""
    return len(text.replace('\n', '').replace(' ', ''))


def analyze_dialogue_ratio(text):
    """分析对话占比"""
    dialogue_lines = re.findall(r'"[^"]*"', text)
    dialogue_lines += re.findall(r'"[^"]*"', text)
    dialogue_lines += re.findall(r'「[^」]*」', text)
    dialogue_chars = sum(len(re.findall(r'[\u4e00-\u9fff]', d)) for d in dialogue_lines)
    total_chinese = count_chinese_chars(text)
    if total_chinese == 0:
        return 0, 0
    return dialogue_chars, round(dialogue_chars / total_chinese * 100, 1)


def analyze_description_ratio(text):
    """分析描写占比（环境描写、外貌描写等）"""
    description_markers = [
        r'(?:只见|望去|放眼|眼前|远处|近处|周围|四周|头顶|脚下|身后|身前)',
        r'(?:穿着|身[穿披着]|一[身件套]|打扮|模样|长相|面容|身材)',
        r'(?:弥漫|飘散|传来|响起|闻到|嗅到|感受到)',
    ]
    desc_lines = 0
    for line in text.split('\n'):
        for marker in description_markers:
            if re.search(marker, line):
                desc_lines += 1
                break
    total_lines = max(len(text.split('\n')), 1)
    return round(desc_lines / total_lines * 100, 1)


def analyze_narrative_ratio(text):
    """分析叙述占比（动作描写、情节推进）"""
    action_markers = [
        r'(?:走|跑|跳|飞|冲|退|进|出|上|下|转|回|站|坐|躺|倒|爬|跃)',
        r'(?:拔|挥|刺|砍|劈|挡|格|击|打|踢|踹|推|拉|扯|抓|握|拿|放)',
        r'(?:说|道|问|答|喊|叫|吼|骂|笑|哭|叹|哼)',
    ]
    action_lines = 0
    for line in text.split('\n'):
        for marker in action_markers:
            if re.search(marker, line):
                action_lines += 1
                break
    total_lines = max(len(text.split('\n')), 1)
    return round(action_lines / total_lines * 100, 1)


def check_wordcount(filepath, target=4000, tolerance=500, json_output=False, detail=False):
    """检查章节字数"""
    path = Path(filepath)
    if not path.exists():
        result = {
            "file": str(path),
            "exists": False,
            "error": "文件不存在"
        }
        if json_output:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"❌ 文件不存在: {filepath}")
        return result

    text = path.read_text(encoding='utf-8')
    chinese_chars = count_chinese_chars(text)
    chinese_with_punct = count_chinese_with_punctuation(text)
    total_chars = count_total_chars(text)

    min_words = target - tolerance
    max_words = target + tolerance
    passed = min_words <= chinese_chars <= max_words

    if passed:
        status = "PASS"
        status_icon = "✅"
    elif chinese_chars < min_words:
        status = "UNDER"
        status_icon = "⚠️"
    else:
        status = "OVER"
        status_icon = "⚠️"

    deviation = round((chinese_chars - target) / target * 100, 1)

    result = {
        "file": str(path),
        "exists": True,
        "chinese_chars": chinese_chars,
        "chinese_with_punctuation": chinese_with_punct,
        "total_chars": total_chars,
        "target": target,
        "tolerance": tolerance,
        "min_acceptable": min_words,
        "max_acceptable": max_words,
        "deviation_percent": deviation,
        "status": status,
        "passed": passed,
    }

    if detail:
        dialogue_chars, dialogue_ratio = analyze_dialogue_ratio(text)
        desc_ratio = analyze_description_ratio(text)
        narrative_ratio = analyze_narrative_ratio(text)
        result["detail"] = {
            "dialogue_chars": dialogue_chars,
            "dialogue_ratio": dialogue_ratio,
            "description_ratio": desc_ratio,
            "narrative_ratio": narrative_ratio,
        }

    if json_output:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"\n{'='*50}")
        print(f"  章节字数检查报告")
        print(f"{'='*50}")
        print(f"  文件: {path.name}")
        print(f"  中文字数: {chinese_chars} 字")
        print(f"  含标点字数: {chinese_with_punct} 字")
        print(f"  总字符数: {total_chars}")
        print(f"  目标字数: {target} 字 (容差 ±{tolerance})")
        print(f"  可接受范围: {min_words}-{max_words} 字")
        print(f"  偏差: {deviation:+.1f}%")
        print(f"  状态: {status_icon} {status}")
        print(f"{'='*50}")

        if detail:
            print(f"\n  详细分析:")
            print(f"  对话占比: {dialogue_ratio}% ({dialogue_chars}字)")
            print(f"  描写占比: {desc_ratio}%")
            print(f"  叙述占比: {narrative_ratio}%")
            print(f"{'='*50}")

        if not passed:
            if chinese_chars < min_words:
                shortage = min_words - chinese_chars
                print(f"\n  ⚠️ 字数不足，需补充约 {shortage} 字")
                print(f"  建议使用 content-expansion.md 中的扩充技法")
            else:
                excess = chinese_chars - max_words
                print(f"\n  ⚠️ 字数超标，建议精简约 {excess} 字")

    return result


def main():
    parser = argparse.ArgumentParser(
        description='章节字数检查脚本 - novel-writer skill',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python check_chapter_wordcount.py 第001章-开局.md
  python check_chapter_wordcount.py 第001章-开局.md --target 4000
  python check_chapter_wordcount.py 第001章-开局.md --json
  python check_chapter_wordcount.py 第001章-开局.md --detail
        """
    )
    parser.add_argument('filepath', help='章节文件路径')
    parser.add_argument('--target', type=int, default=4000, help='目标字数 (默认: 4000)')
    parser.add_argument('--tolerance', type=int, default=500, help='容差字数 (默认: 500)')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    parser.add_argument('--detail', action='store_true', help='详细分析（对话/描写/叙述占比）')
    args = parser.parse_args()

    result = check_wordcount(
        filepath=args.filepath,
        target=args.target,
        tolerance=args.tolerance,
        json_output=args.json,
        detail=args.detail,
    )

    if not result.get("passed", False) and not args.json:
        sys.exit(1)


if __name__ == '__main__':
    main()