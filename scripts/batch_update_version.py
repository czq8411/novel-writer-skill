#!/usr/bin/env python3
"""
批量更新模式文件的版本号至 v21.2
"""

import re
from pathlib import Path

def update_version(file_path):
    """更新文件中的版本号"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配版本号：**版本**：vXX.X
    pattern = r'(\*\*版本\*\*：\s*v)(\d+\.\d+(-patch\d+)?)'
    
    # 检查是否有版本号
    match = re.search(pattern, content)
    if match:
        old_version = match.group(2)
        new_content = re.sub(pattern, r'\g<1>21.2', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ {file_path.name}: v{old_version} → v21.2")
        return True
    else:
        print(f"⚠️  {file_path.name}: 未找到版本号")
        return False

def main():
    modes_dir = Path('/Users/chenzhiqiang/Desktop/T/novel_writer_skill/novel-writer-skill/modes')
    
    # 主要模式文件
    main_files = [
        modes_dir / 'mode-a-inspiration.md',
        modes_dir / 'mode-b-outline.md',
        modes_dir / 'mode-b2-detailed-outline.md',
        modes_dir / 'mode-c-writing.md',
        modes_dir / 'mode-d-packaging.md',
        modes_dir / 'mode-e-diagnostics.md',
        modes_dir / 'mode-f-auto-pipeline.md',
        modes_dir / 'mode-card-drawing.md',
    ]
    
    print("更新主要模式文件版本号...")
    updated = 0
    for md_file in main_files:
        if md_file.exists():
            if update_version(md_file):
                updated += 1
    
    print(f"\n✨ 完成！已更新 {updated} 个文件的版本号至 v21.2")

if __name__ == '__main__':
    main()
