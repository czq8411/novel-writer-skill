#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：验证细纲文件自动保存功能
"""

import os
import sys
import json

def test_detailed_outline_save():
    """测试细纲文件保存功能"""
    # 获取当前工作目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")
    
    # 模拟数据
    book_name = "苍穹之上"
    volume_name = "第一卷_初入江湖"
    chapter_count = 10
    
    # 构建细纲内容
    outline_content = f"""## 《{book_name}》{volume_name}细纲

### 卷主题
{volume_name}

### 章节规划
"""
    
    for i in range(1, chapter_count + 1):
        chapter_title = f"第{i}章_章节标题{i}"
        outline_content += f"""

#### {chapter_title}
- **核心事件**：第{i}章核心事件描述
- **场景**：场景{i}
- **爽点设计**：
  - 类型：打脸/升级
  - 强度：{min(i * 2, 10)}/10
- **章末钩子**：第{i}章悬念钩子
"""
    
    # 创建目录结构
    outline_dir = os.path.join(current_dir, "细纲", volume_name)
    os.makedirs(outline_dir, exist_ok=True)
    print(f"创建目录: {outline_dir}")
    
    # 保存细纲文件
    file_path = os.path.join(outline_dir, f"{volume_name}_细纲.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(outline_content)
    print(f"细纲文件已保存: {file_path}")
    
    # 验证文件是否存在
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        print(f"✅ 文件保存成功！大小: {file_size} 字节")
        return True
    else:
        print("❌ 文件保存失败！")
        return False

def test_outline_save():
    """测试大纲文件保存功能"""
    current_dir = os.getcwd()
    book_name = "苍穹之上"
    
    outline_content = f"""## 《{book_name}》核心大纲

### 核心定位
- **一句话简介**：少年觉醒神秘力量，踏上修仙之路
- **核心爽点**：逆袭打脸、升级成长
- **市场对标**：《斗破苍穹》

### 主角设定
- **姓名**：林辰
- **身份**：废柴少主→一代仙尊
- **性格**：坚毅、机智、重情重义

### 金手指设定
- **名称**：神秘玉佩
- **功能**：加速修炼、推演功法
- **限制**：消耗精神力

### 故事脉络
| 卷 | 目标 | 高潮 |
|---|------|------|
| 一 | 初入江湖 | 宗门大比夺冠 |
| 二 | 闯荡大陆 | 秘境探险 |
| 三 | 称霸天下 | 最终对决 |
"""
    
    # 创建目录
    outline_dir = os.path.join(current_dir, "大纲")
    os.makedirs(outline_dir, exist_ok=True)
    print(f"创建目录: {outline_dir}")
    
    # 保存文件
    file_path = os.path.join(outline_dir, f"{book_name}_大纲.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(outline_content)
    print(f"大纲文件已保存: {file_path}")
    
    if os.path.exists(file_path):
        print("✅ 大纲文件保存成功！")
        return True
    else:
        print("❌ 大纲文件保存失败！")
        return False

def test_chapter_save():
    """测试正文章节保存功能"""
    current_dir = os.getcwd()
    book_name = "苍穹之上"
    volume_name = "第一卷_初入江湖"
    chapter_num = 1
    chapter_title = "觉醒"
    
    chapter_content = f"""## 第{chapter_num}章 {chapter_title}

夕阳的余晖洒落在青阳城的上空，给这座古老的城池镀上了一层金色。

林辰独自站在家族演武场的角落，望着远处那些正在修炼的族人，眼神中充满了不甘。

"废物就是废物，就算再努力也没用。"

一道嘲讽的声音传来，林辰转头看去，只见族兄林虎带着几个跟班走了过来，脸上带着戏谑的笑容。

林辰握紧了拳头，指甲深深嵌入掌心。他知道，在这个以实力为尊的世界，弱者只能被欺负。

就在这时，他胸口处的玉佩突然微微发热，一股神秘的力量涌入体内......
"""
    
    # 创建目录
    chapter_dir = os.path.join(current_dir, "正文", volume_name)
    os.makedirs(chapter_dir, exist_ok=True)
    print(f"创建目录: {chapter_dir}")
    
    # 保存文件
    file_name = f"第{chapter_num:03d}章_{chapter_title}.md"
    file_path = os.path.join(chapter_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(chapter_content)
    print(f"章节文件已保存: {file_path}")
    
    if os.path.exists(file_path):
        print("✅ 章节文件保存成功！")
        return True
    else:
        print("❌ 章节文件保存失败！")
        return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("📚 小说创作文件保存功能测试")
    print("=" * 60)
    
    # 使用当前工作目录（pwd）作为根目录，符合SKILL.md规范
    # 所有文件（大纲、细纲、正文、记忆库）均在当前工作目录下创建和管理
    print(f"\n📁 当前工作目录: {os.getcwd()}")
    
    # 执行测试
    results = []
    
    print("\n--- 测试1: 大纲文件保存 ---")
    results.append(test_outline_save())
    
    print("\n--- 测试2: 细纲文件保存 ---")
    results.append(test_detailed_outline_save())
    
    print("\n--- 测试3: 正文章节保存 ---")
    results.append(test_chapter_save())
    
    # 输出测试结果
    print("\n" + "=" * 60)
    if all(results):
        print("🎉 所有测试通过！")
        print("\n📂 生成的目录结构:")
        for root, dirs, files in os.walk(os.getcwd()):
            level = root.replace(os.getcwd(), '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
    else:
        print("❌ 部分测试失败！")
        sys.exit(1)

if __name__ == "__main__":
    main()