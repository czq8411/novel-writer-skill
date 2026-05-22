#!/usr/bin/env python3
"""
测试验证脚本 - v21.2 版本验证
"""

import os
import re
from pathlib import Path

def check_file_exists(file_path):
    """检查文件是否存在"""
    if file_path.exists():
        print(f"✅ {file_path}")
        return True
    else:
        print(f"❌ {file_path} - 不存在")
        return False

def check_version(file_path, expected_version="v21.2"):
    """检查文件版本号"""
    if not file_path.exists():
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配版本号
    match = re.search(r'(?:\*\*版本\*\*：|v)(\d+\.\d+)', content)
    if match:
        version = f"v{match.group(1)}"
        if version == expected_version:
            print(f"✅ {file_path.name}: 版本 {version}")
            return True
        else:
            print(f"⚠️ {file_path.name}: 版本 {version} (预期 {expected_version})")
            return False
    else:
        print(f"❌ {file_path.name}: 未找到版本号")
        return False

def check_placeholders(file_path):
    """检查文件中是否存在旧格式占位符"""
    if not file_path.exists():
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否还有方括号占位符（排除代码块中的）
    # 匹配 [xxx] 但不匹配 **[xxx]**（这是已处理的）
    pattern = r'(?<!\*)\[([^\[\]]+)\](?!\*)'
    matches = re.findall(pattern, content)
    
    if matches:
        print(f"⚠️ {file_path.name}: 存在 {len(matches)} 个旧格式占位符")
        return False
    else:
        print(f"✅ {file_path.name}: 占位符格式正确")
        return True

def check_feature_modules():
    """检查新增功能模块"""
    print("\n--- 检查新增功能模块 ---")
    
    features = [
        ("灵感碰撞模块", "modes/mode-e/inspiration-collision.md"),
        ("格式规范文档", "shared/format-spec.md"),
        ("大纲生成模板", "modes/mode-b-outline.md"),
        ("细纲模板", "modes/mode-b2-detailed-outline.md"),
        ("正文检测", "modes/mode-c-writing.md"),
    ]
    
    all_passed = True
    for feature_name, rel_path in features:
        file_path = Path(rel_path)
        if file_path.exists():
            print(f"✅ {feature_name}: {rel_path}")
        else:
            print(f"❌ {feature_name}: {rel_path} - 不存在")
            all_passed = False
    
    return all_passed

def main():
    print("="*60)
    print("🔍 v21.2 版本测试验证")
    print("="*60)
    
    base_dir = Path('/Users/chenzhiqiang/Desktop/T/novel_writer_skill/novel-writer-skill')
    
    # 1. 检查主要模式文件
    print("\n--- 检查主要模式文件 ---")
    main_files = [
        base_dir / 'modes/mode-a-inspiration.md',
        base_dir / 'modes/mode-b-outline.md',
        base_dir / 'modes/mode-b2-detailed-outline.md',
        base_dir / 'modes/mode-c-writing.md',
        base_dir / 'modes/mode-d-packaging.md',
        base_dir / 'modes/mode-e-diagnostics.md',
        base_dir / 'modes/mode-f-auto-pipeline.md',
        base_dir / 'modes/mode-card-drawing.md',
    ]
    
    for file_path in main_files:
        check_file_exists(file_path)
    
    # 2. 检查版本号
    print("\n--- 检查版本号 ---")
    for file_path in main_files:
        check_version(file_path)
    
    # 3. 检查占位符格式
    print("\n--- 检查占位符格式 ---")
    for file_path in main_files[:5]:  # 检查前5个核心文件
        check_placeholders(file_path)
    
    # 4. 检查新增功能模块
    check_feature_modules()
    
    # 5. 检查脚本文件
    print("\n--- 检查新增脚本 ---")
    scripts = [
        base_dir / 'scripts/batch_replace_placeholders.py',
        base_dir / 'scripts/batch_update_version.py',
    ]
    
    for script_path in scripts:
        if script_path.exists():
            print(f"✅ {script_path.name}")
        else:
            print(f"❌ {script_path.name} - 不存在")
    
    # 6. 检查灵感碰撞模块内容
    print("\n--- 检查灵感碰撞模块内容 ---")
    inspiration_file = base_dir / 'modes/mode-e/inspiration-collision.md'
    if inspiration_file.exists():
        with open(inspiration_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查关键内容
        checks = [
            ("自动触发机制", "自动触发机制"),
            ("五维度评估", "五维度评估"),
            ("文学性", "文学性"),
            ("故事架构", "故事架构"),
            ("人物塑造", "人物塑造"),
            ("情节逻辑", "情节逻辑"),
            ("市场潜力", "市场潜力"),
            ("评级系统", "评级系统"),
        ]
        
        print(f"✅ 灵感碰撞模块存在")
        for check_name, keyword in checks:
            if keyword in content:
                print(f"   ✅ {check_name}")
            else:
                print(f"   ❌ {check_name}")
    
    print("\n" + "="*60)
    print("🎉 测试验证完成！")
    print("="*60)

if __name__ == '__main__':
    main()
