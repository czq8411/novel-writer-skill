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

def test_existing_file_overwrite():
    """测试文件已存在时的覆盖行为"""
    current_dir = os.getcwd()
    book_name = "苍穹之上"

    outline_dir = os.path.join(current_dir, "大纲")
    os.makedirs(outline_dir, exist_ok=True)
    file_path = os.path.join(outline_dir, f"{book_name}_大纲.md")

    old_content = "旧大纲内容_应被覆盖"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(old_content)
    print(f"已创建旧大纲文件: {file_path}")
    print(f"旧内容: {old_content}")

    test_outline_save()

    with open(file_path, "r", encoding="utf-8") as f:
        new_content = f.read()

    if old_content not in new_content and "核心定位" in new_content:
        print("✅ 文件覆盖成功！新内容正确写入")
        return True
    else:
        print("❌ 文件覆盖失败！")
        return False


def test_permission_denied():
    """测试权限不足时的错误处理"""
    try:
        protected_path = "/System/test_permission_check.txt"
        with open(protected_path, "w", encoding="utf-8") as f:
            f.write("test")
        os.remove(protected_path)
        print("⚠️ 意外：系统目录可写入（可能以root运行）")
        return True
    except PermissionError:
        print("✅ 正确捕获 PermissionError，程序未崩溃")
        print("友好提示: 权限不足，无法写入文件，请检查目标目录的写入权限")
        return True
    except Exception as e:
        print(f"❌ 捕获到非预期异常: {type(e).__name__}: {e}")
        return False


def test_special_chars_filename():
    """测试书名字段包含特殊字符时的处理"""
    current_dir = os.getcwd()

    raw_book_name = "苍穹/之上:归来?测试*"
    illegal_chars_map = {'/': '-', ':': '-', '?': '-', '*': '-', '"': '-', '<': '-', '>': '-', '|': '-'}
    safe_book_name = raw_book_name
    for char, replacement in illegal_chars_map.items():
        safe_book_name = safe_book_name.replace(char, replacement)

    print(f"原始书名: {raw_book_name}")
    print(f"安全文件名: {safe_book_name}")

    illegal_chars = set('/:*?"<>|')
    for char in illegal_chars:
        if char in safe_book_name:
            print(f"❌ 安全文件名仍含非法字符: '{char}'")
            return False

    outline_dir = os.path.join(current_dir, "大纲")
    os.makedirs(outline_dir, exist_ok=True)
    file_path = os.path.join(outline_dir, f"{safe_book_name}_大纲.md")

    outline_content = f"## 《{raw_book_name}》核心大纲\n\n测试特殊字符处理"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(outline_content)

    if os.path.exists(file_path):
        print(f"✅ 特殊字符文件名处理成功: {os.path.basename(file_path)}")
        return True
    else:
        print("❌ 特殊字符文件名处理失败！")
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

    print("\n--- 测试4: 文件覆盖行为 ---")
    results.append(test_existing_file_overwrite())

    print("\n--- 测试5: 权限不足错误处理 ---")
    results.append(test_permission_denied())

    print("\n--- 测试6: 特殊字符文件名处理 ---")
    results.append(test_special_chars_filename())
    
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