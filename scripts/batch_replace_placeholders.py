#!/usr/bin/env python3
"""
批量替换 Markdown 文件中的占位符格式
将 [占位符] 替换为 <占位符>
"""

import re
import os
from pathlib import Path

def replace_placeholders(file_path):
    """替换文件中的占位符格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换模式：**[内容]** → **<内容>**
    # 匹配 **[xxx]**: [yyy] 格式
    patterns = [
        # 匹配表格中的 [内容]
        (r'\| (\[.*?\])', r'| <\1>'),
        # 匹配列表项 - **[xxx]**: [yyy]
        (r'- \*\*(.+?)\*\*: \[(.+?)\]', r'- **\1**: <\2>'),
        # 匹配普通 [内容]
        (r'(?<!\[)\[([^\[\]]+?)\](?!\])', r'<\1>'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 已处理：{file_path}")

def main():
    modes_dir = Path('/Users/chenzhiqiang/Desktop/T/novel_writer_skill/novel-writer-skill/modes')
    
    # 处理所有 markdown 文件
    md_files = list(modes_dir.rglob('*.md'))
    
    print(f"找到 {len(md_files)} 个 Markdown 文件")
    
    for md_file in md_files:
        try:
            replace_placeholders(md_file)
        except Exception as e:
            print(f"❌ 处理失败 {md_file}: {e}")
    
    print("\n✨ 批量替换完成！")

if __name__ == '__main__':
    main()
