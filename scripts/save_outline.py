#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
大纲文件保存模块（兼容层）
已迁移到 file_manager.py，此文件保持向后兼容
"""

import os
import sys
import datetime
import traceback

# 添加脚本目录到路径，支持直接运行
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入统一文件管理器
try:
    from file_manager import FileManager
except ImportError:
    from .file_manager import FileManager

def sanitize_filename(filename):
    """
    清理文件名中的非法字符（向后兼容）
    """
    fm = FileManager()
    return fm.sanitize_filename(filename)

def ensure_directory_exists(dir_path):
    """
    确保目录存在（向后兼容）
    """
    fm = FileManager()
    return fm.ensure_directory(dir_path)

def get_project_root():
    """
    获取项目根目录（向后兼容）
    """
    return os.getcwd()

def save_outline(book_name, outline_content, output_dir=None):
    """
    保存大纲文件（向后兼容接口）
    """
    fm = FileManager(output_dir) if output_dir else FileManager()
    return fm.save(outline_content, 'outline', book_name=book_name)

def save_outline_with_backup(book_name, outline_content, output_dir=None):
    """
    保存大纲文件（带备份机制，向后兼容接口）
    """
    fm = FileManager(output_dir) if output_dir else FileManager()
    return fm.save_with_backup(outline_content, 'outline', book_name=book_name)

def get_current_outline_dir():
    """
    获取当前大纲目录路径（向后兼容）
    """
    fm = FileManager()
    success, msg, path = fm.get_save_path('outline', book_name='')
    return os.path.dirname(path) if success else os.path.join(os.getcwd(), "大纲")

def list_outline_files():
    """
    列出大纲目录中的所有文件（向后兼容）
    """
    fm = FileManager()
    return fm.list_files('outline')

def generate_outline_template(book_name, mode="full"):
    """
    生成大纲模板内容
    """
    if mode == "simple":
        return f"""## 《{book_name}》核心大纲

### 一、核心设定
- 题材：
- 核心梗：
- 一句话简介：

### 二、主角设定
- 姓名：
- 身份：
- 性格：
- 目标：

### 三、故事脉络
| 卷 | 目标 | 高潮 |

### 四、关键看点
- 
"""
    else:
        return f"""## 《{book_name}》核心大纲

### 一、核心定位
- **题材**：
- **核心梗**：
- **一句话简介**：
- **市场对标**：
- **目标读者**：

### 二、世界观设定
- **时代背景**：
- **核心规则**：
- **势力格局**：
- **等级体系**：

### 三、主角设定
- **姓名**：
- **身份**：
- **性格**：
- **核心动机**：
- **成长弧线**：

### 四、金手指设定
- **名称**：
- **功能**：
- **限制/代价**：
- **来源**：

### 五、重要配角
| 角色 | 身份 | 与主角关系 | 核心动机 |

### 六、故事脉络
| 卷 | 卷名 | 核心目标 | 高潮事件 | 章数 |

### 七、黄金三章
- **第1章**：
- **第2章**：
- **第3章**：

### 八、爽点规划
| 位置 | 类型 | 设计 |

### 九、伏笔清单
| 编号 | 内容 | 埋下章节 | 回收章节 |

---

*生成时间：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

def main():
    """
    命令行测试入口（向后兼容）
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='保存小说大纲')
    parser.add_argument('--book-name', help='书名')
    parser.add_argument('--content', help='大纲内容（字符串）')
    parser.add_argument('--content-file', help='大纲内容文件路径')
    parser.add_argument('--output-dir', help='输出目录')
    parser.add_argument('--test', action='store_true', help='运行测试')
    
    args = parser.parse_args()
    
    # 非测试模式下，book-name为必需参数
    if not args.test and not args.book_name:
        parser.error("非测试模式下，必须提供 --book-name 参数")
    
    if args.test:
        # 运行测试
        print("=" * 60)
        print("📚 大纲保存功能测试（兼容层）")
        print("=" * 60)
        
        # 测试1: 基本保存功能
        print("\n--- 测试1: 基本保存功能 ---")
        content = generate_outline_template("测试小说")
        success, msg, path = save_outline("测试小说", content)
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试2: 特殊字符处理
        print("\n--- 测试2: 特殊字符文件名处理 ---")
        success, msg, path = save_outline("苍穹/之上:归来?测试*", content)
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试3: 空书名处理
        print("\n--- 测试3: 空书名处理 ---")
        success, msg, path = save_outline("", content)
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试4: 列出大纲文件
        print("\n--- 测试4: 列出大纲文件 ---")
        files = list_outline_files()
        print(f"大纲目录文件数: {len(files)}")
        if files:
            print("最近的文件:")
            for f in files[:3]:
                print(f"  - {f}")
        
        print("\n" + "=" * 60)
        print("测试完成！")
        
    else:
        # 执行保存
        if args.content:
            content = args.content
        elif args.content_file:
            try:
                with open(args.content_file, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"读取内容文件失败: {e}")
                sys.exit(1)
        else:
            print("错误：必须提供 --content 或 --content-file 参数")
            sys.exit(1)
        
        success, msg, path = save_outline_with_backup(args.book_name, content, args.output_dir)
        print(msg)
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()