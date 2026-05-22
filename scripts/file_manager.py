#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一文件管理模块
功能：提供统一的文件保存接口，支持大纲、细纲、章节、包装方案等多种文件类型
"""

import os
import sys
import datetime
import traceback

# 添加脚本目录到路径，支持从任意目录运行
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 非法字符映射表（用于文件名规范化）
ILLEGAL_CHARS_MAP = {
    '/': '-', ':': '-', '?': '-', '*': '-', 
    '"': '-', '<': '-', '>': '-', '|': '-',
    '\\': '-', '\0': ''
}

# 错误处理类
class SaveError(Exception):
    """保存错误基类"""
    pass

class PermissionError(SaveError):
    """权限错误"""
    pass

class DiskSpaceError(SaveError):
    """磁盘空间不足"""
    pass

class PathError(SaveError):
    """路径错误"""
    pass

class FileConflictError(SaveError):
    """文件冲突"""
    pass

class FileSaver:
    """保存器基类"""
    
    def __init__(self, file_manager):
        self.fm = file_manager
    
    def save(self, content, **kwargs):
        """保存文件（子类实现）"""
        raise NotImplementedError
    
    def get_directory(self, **kwargs):
        """获取目录路径（子类实现）"""
        raise NotImplementedError
    
    def get_filename(self, **kwargs):
        """获取文件名（子类实现）"""
        raise NotImplementedError

class OutlineSaver(FileSaver):
    """大纲保存器"""
    
    def get_directory(self, **kwargs):
        book_name = kwargs.get('book_name', '')
        return os.path.join(self.fm.base_dir, "大纲")
    
    def get_filename(self, **kwargs):
        book_name = kwargs.get('book_name', '')
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = self.fm.sanitize_filename(book_name)
        return f"{safe_name}_核心大纲_{timestamp}.md"
    
    def save(self, content, **kwargs):
        return self.fm._save_file(
            content=content,
            directory=self.get_directory(**kwargs),
            filename=self.get_filename(**kwargs)
        )

class DetailedOutlineSaver(FileSaver):
    """细纲保存器"""
    
    def get_directory(self, **kwargs):
        volume_name = kwargs.get('volume_name', '')
        return os.path.join(self.fm.base_dir, "细纲", volume_name)
    
    def get_filename(self, **kwargs):
        volume_name = kwargs.get('volume_name', '')
        safe_name = self.fm.sanitize_filename(volume_name)
        return f"{safe_name}_细纲.md"
    
    def save(self, content, **kwargs):
        return self.fm._save_file(
            content=content,
            directory=self.get_directory(**kwargs),
            filename=self.get_filename(**kwargs)
        )

class ChapterSaver(FileSaver):
    """章节保存器"""
    
    def get_directory(self, **kwargs):
        volume_name = kwargs.get('volume_name', '')
        return os.path.join(self.fm.base_dir, "正文", volume_name)
    
    def get_filename(self, **kwargs):
        chapter_num = kwargs.get('chapter_num', 1)
        chapter_title = kwargs.get('chapter_title', '')
        safe_title = self.fm.sanitize_filename(chapter_title)
        return f"第{chapter_num:03d}章_{safe_title}.md"
    
    def save(self, content, **kwargs):
        return self.fm._save_file(
            content=content,
            directory=self.get_directory(**kwargs),
            filename=self.get_filename(**kwargs)
        )

class PackagingSaver(FileSaver):
    """包装方案保存器"""
    
    def get_directory(self, **kwargs):
        return os.path.join(self.fm.base_dir, "包装")
    
    def get_filename(self, **kwargs):
        book_name = kwargs.get('book_name', '')
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = self.fm.sanitize_filename(book_name)
        return f"{safe_name}_包装方案_{timestamp}.md"
    
    def save(self, content, **kwargs):
        return self.fm._save_file(
            content=content,
            directory=self.get_directory(**kwargs),
            filename=self.get_filename(**kwargs)
        )

class MemorySaver(FileSaver):
    """记忆库保存器"""
    
    def get_directory(self, **kwargs):
        return self.fm.base_dir
    
    def get_filename(self, **kwargs):
        return "记忆库.md"
    
    def save(self, content, **kwargs):
        return self.fm._save_file(
            content=content,
            directory=self.get_directory(**kwargs),
            filename=self.get_filename(**kwargs)
        )

class FileManager:
    """统一文件管理器"""
    
    FILE_TYPES = {
        'outline': OutlineSaver,
        'detailed_outline': DetailedOutlineSaver,
        'chapter': ChapterSaver,
        'packaging': PackagingSaver,
        'memory': MemorySaver,
    }
    
    def __init__(self, base_dir=None):
        """
        初始化文件管理器
        
        Args:
            base_dir: 基础目录，默认为当前工作目录
        """
        self.base_dir = base_dir or os.getcwd()
        self.savers = {}
    
    def get_saver(self, file_type):
        """获取对应类型的保存器"""
        if file_type not in self.savers:
            saver_class = self.FILE_TYPES.get(file_type)
            if not saver_class:
                return False, f"不支持的文件类型: {file_type}", None
            self.savers[file_type] = saver_class(self)
        return True, "", self.savers[file_type]
    
    def sanitize_filename(self, filename):
        """
        清理文件名中的非法字符
        
        Args:
            filename: 原始文件名
        
        Returns:
            安全的文件名
        """
        if not isinstance(filename, str):
            filename = str(filename)
        
        safe_name = filename
        for char, replacement in ILLEGAL_CHARS_MAP.items():
            safe_name = safe_name.replace(char, replacement)
        
        # 去除首尾空白
        safe_name = safe_name.strip()
        
        # 如果文件名为空，使用默认名称
        if not safe_name:
            safe_name = "未命名"
        
        return safe_name
    
    def ensure_directory(self, dir_path):
        """
        确保目录存在，不存在则创建
        
        Args:
            dir_path: 目录路径
        
        Returns:
            (是否成功, 消息, 实际使用的路径)
        """
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                return True, f"目录创建成功: {dir_path}", dir_path
            return True, f"目录已存在: {dir_path}", dir_path
        except PermissionError:
            # 尝试使用用户home目录作为备选
            home_dir = os.path.expanduser("~")
            project_name = os.path.basename(os.path.dirname(dir_path)) if os.path.dirname(dir_path) else "novel_data"
            alt_dir = os.path.join(home_dir, "novel_data", project_name, os.path.basename(dir_path))
            print(f"警告: 当前目录权限不足，将文件保存到备选位置: {alt_dir}")
            os.makedirs(alt_dir, exist_ok=True)
            return True, f"当前目录权限不足，已使用备选路径: {alt_dir}", alt_dir
        except OSError as e:
            # 处理其他OS错误，包括权限问题
            if e.errno == 1:  # EPERM - Operation not permitted
                home_dir = os.path.expanduser("~")
                project_name = os.path.basename(os.path.dirname(dir_path)) if os.path.dirname(dir_path) else "novel_data"
                alt_dir = os.path.join(home_dir, "novel_data", project_name, os.path.basename(dir_path))
                print(f"警告: 当前目录权限不足 (errno={e.errno})，将文件保存到备选位置: {alt_dir}")
                os.makedirs(alt_dir, exist_ok=True)
                return True, f"当前目录权限不足，已使用备选路径: {alt_dir}", alt_dir
            return False, f"创建目录时发生错误: {str(e)}", None
        except Exception as e:
            return False, f"创建目录时发生错误: {str(e)} (类型: {type(e).__name__})", None
    
    def _save_file(self, content, directory, filename):
        """
        核心保存逻辑
        
        Args:
            content: 文件内容
            directory: 目录路径
            filename: 文件名
        
        Returns:
            (是否成功, 消息, 文件路径)
        """
        try:
            # 1. 确保目录存在（返回值已更新为三元组）
            success, msg, actual_dir = self.ensure_directory(directory)
            if not success:
                return False, msg, None
            
            # 2. 构建完整路径（使用实际目录路径）
            file_path = os.path.join(actual_dir, filename)
            
            # 3. 检查文件是否已存在（避免覆盖）
            counter = 1
            original_file_path = file_path
            while os.path.exists(file_path):
                name, ext = os.path.splitext(filename)
                file_path = os.path.join(actual_dir, f"{name}_{counter}{ext}")
                counter += 1
                if counter > 100:
                    return False, "文件数量过多，无法创建新文件", None
            
            # 4. 写入文件
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
            except PermissionError:
                return False, f"权限不足，无法写入文件: {file_path}", None
            except Exception as e:
                return False, f"写入文件时发生错误: {str(e)}", None
            
            # 5. 验证文件是否保存成功
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                return True, f"文件保存成功！\n路径: {file_path}\n大小: {file_size} 字节", file_path
            else:
                return False, "文件保存后验证失败，文件不存在", None
        
        except Exception as e:
            error_trace = traceback.format_exc()
            return False, f"保存文件时发生未预期错误:\n{error_trace}", None
    
    def save(self, content, file_type, **kwargs):
        """
        统一保存接口
        
        Args:
            content: 文件内容
            file_type: 文件类型 ('outline', 'detailed_outline', 'chapter', 'packaging', 'memory')
            **kwargs: 类型特定参数
                - book_name: 书名（大纲/包装）
                - volume_name: 卷名（细纲/章节）
                - chapter_num: 章节号（章节）
                - chapter_title: 章节标题（章节）
        
        Returns:
            (是否成功, 消息, 文件路径)
        """
        # 获取保存器
        success, msg, saver = self.get_saver(file_type)
        if not success:
            return False, msg, None
        
        # 使用保存器保存
        return saver.save(content, **kwargs)
    
    def save_with_backup(self, content, file_type, **kwargs):
        """
        保存文件（带备份机制）
        
        Args:
            content: 文件内容
            file_type: 文件类型
            **kwargs: 类型特定参数
        
        Returns:
            (是否成功, 消息, 文件路径)
        """
        # 尝试保存到主目录
        success, msg, file_path = self.save(content, file_type, **kwargs)
        
        if success:
            return success, msg, file_path
        
        # 如果失败，尝试保存到用户目录作为备选
        original_base_dir = self.base_dir
        try:
            self.base_dir = os.path.expanduser("~/Documents/小说创作")
            success, msg, file_path = self.save(content, file_type, **kwargs)
            
            if success:
                msg = f"主目录保存失败，已保存到备用目录。\n{msg}"
                return success, msg, file_path
        finally:
            self.base_dir = original_base_dir
        
        # 如果仍失败，尝试保存到临时目录
        try:
            self.base_dir = os.path.join(os.getcwd(), "temp_novel")
            success, msg, file_path = self.save(content, file_type, **kwargs)
            
            if success:
                msg = f"主目录和用户目录均保存失败，已保存到临时目录。\n{msg}"
                return success, msg, file_path
        finally:
            self.base_dir = original_base_dir
        
        return False, msg, None
    
    def get_save_path(self, file_type, **kwargs):
        """
        获取保存路径（不实际保存）
        
        Args:
            file_type: 文件类型
            **kwargs: 类型特定参数
        
        Returns:
            (是否成功, 消息, 文件路径)
        """
        success, msg, saver = self.get_saver(file_type)
        if not success:
            return False, msg, None
        
        directory = saver.get_directory(**kwargs)
        filename = saver.get_filename(**kwargs)
        file_path = os.path.join(directory, filename)
        
        return True, "路径计算成功", file_path
    
    def list_files(self, file_type, **kwargs):
        """
        列出指定类型的所有文件
        
        Args:
            file_type: 文件类型
            **kwargs: 类型特定参数
        
        Returns:
            文件列表
        """
        success, msg, saver = self.get_saver(file_type)
        if not success:
            return []
        
        directory = saver.get_directory(**kwargs)
        if not os.path.exists(directory):
            return []
        
        try:
            files = [f for f in os.listdir(directory) if f.endswith('.md')]
            files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
            return files
        except PermissionError:
            return []
        except Exception:
            return []

def main():
    """命令行测试入口"""
    import argparse
    
    parser = argparse.ArgumentParser(description='统一文件管理器 - novel-writer skill')
    parser.add_argument('--test', action='store_true', help='运行测试')
    parser.add_argument('--file-type', choices=['outline', 'detailed_outline', 'chapter', 'packaging', 'memory'],
                        help='文件类型')
    parser.add_argument('--book-name', help='书名')
    parser.add_argument('--volume-name', help='卷名')
    parser.add_argument('--chapter-num', type=int, default=1, help='章节号')
    parser.add_argument('--chapter-title', help='章节标题')
    parser.add_argument('--content', help='文件内容')
    
    args = parser.parse_args()
    
    if args.test:
        # 运行测试
        print("=" * 60)
        print("📚 统一文件管理器测试")
        print("=" * 60)
        
        fm = FileManager()
        
        # 测试1: 大纲保存
        print("\n--- 测试1: 大纲保存 ---")
        content = "## 《测试小说》核心大纲\n\n测试内容"
        success, msg, path = fm.save(content, 'outline', book_name='测试小说')
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试2: 细纲保存
        print("\n--- 测试2: 细纲保存 ---")
        content = "## 《测试小说》第一卷细纲\n\n章节规划..."
        success, msg, path = fm.save(content, 'detailed_outline', volume_name='第一卷_初入江湖')
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试3: 章节保存
        print("\n--- 测试3: 章节保存 ---")
        content = "## 第1章 觉醒\n\n正文内容..."
        success, msg, path = fm.save(content, 'chapter', volume_name='第一卷_初入江湖', 
                                     chapter_num=1, chapter_title='觉醒')
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试4: 包装方案保存
        print("\n--- 测试4: 包装方案保存 ---")
        content = "## 《测试小说》包装方案\n\n书名建议..."
        success, msg, path = fm.save(content, 'packaging', book_name='测试小说')
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试5: 记忆库保存
        print("\n--- 测试5: 记忆库保存 ---")
        content = "## 记忆库\n\n人物设定..."
        success, msg, path = fm.save(content, 'memory')
        print(f"结果: {'成功' if success else '失败'}")
        print(f"消息: {msg}")
        
        # 测试6: 文件列出
        print("\n--- 测试6: 列出大纲文件 ---")
        files = fm.list_files('outline')
        print(f"大纲目录文件数: {len(files)}")
        if files:
            print("最近的文件:")
            for f in files[:3]:
                print(f"  - {f}")
        
        print("\n" + "=" * 60)
        print("🎉 所有测试完成！")
        
    elif args.file_type and args.content:
        # 执行保存
        fm = FileManager()
        kwargs = {}
        if args.book_name:
            kwargs['book_name'] = args.book_name
        if args.volume_name:
            kwargs['volume_name'] = args.volume_name
        if args.chapter_num:
            kwargs['chapter_num'] = args.chapter_num
        if args.chapter_title:
            kwargs['chapter_title'] = args.chapter_title
        
        success, msg, path = fm.save(args.content, args.file_type, **kwargs)
        print(msg)
        sys.exit(0 if success else 1)
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()