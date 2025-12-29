#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import shutil
import sys

# 定义要删除的文件列表
def get_files_to_remove():
    # 剩余的不必要文件
    remaining_files = [
        'java_auth_debugger.py',
        'fix_class_selector.js',
        'check_db_structure.py',
        'generate_class_data.py',
        'init_databases.py',
        'migrate.py',
    ]
    
    return remaining_files

# 定义要删除的目录列表
def get_dirs_to_remove():
    return [
        '__pycache__',
        'logs',
        'official_demos',
        'templates/.idea',
        'apps/__pycache__',
        # 其他可能不需要的临时目录
    ]

# 定义要保留但可能需要清理的文件（例如日志文件）
def get_files_to_clean():
    return [
        # 这里可以添加需要保留但内容可以清空的文件
    ]

# 确认删除函数
def confirm_removal(items, item_type):
    print(f"即将删除以下{item_type}:")
    for item in items:
        print(f"  - {item}")
    
    confirm = input(f"\n确认要删除以上{item_type}吗？(y/n): ").lower()
    return confirm == 'y' or confirm == 'yes'

# 清理主函数
def clean_project():
    print("===== 开始清理智能教辅项目 =====")
    
    # 获取项目根目录
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # 删除文件
    files_to_remove = get_files_to_remove()
    existing_files = [f for f in files_to_remove if os.path.exists(f)]
    
    if existing_files and confirm_removal(existing_files, "文件"):
        for file_path in existing_files:
            try:
                os.remove(file_path)
                print(f"已删除文件: {file_path}")
            except Exception as e:
                print(f"删除文件 {file_path} 失败: {e}")
    
    # 删除目录
    dirs_to_remove = get_dirs_to_remove()
    existing_dirs = [d for d in dirs_to_remove if os.path.exists(d)]
    
    if existing_dirs and confirm_removal(existing_dirs, "目录"):
        for dir_path in existing_dirs:
            try:
                shutil.rmtree(dir_path)
                print(f"已删除目录: {dir_path}")
            except Exception as e:
                print(f"删除目录 {dir_path} 失败: {e}")
    
    # 清理文件内容
    files_to_clean = get_files_to_clean()
    existing_clean_files = [f for f in files_to_clean if os.path.exists(f)]
    
    if existing_clean_files and confirm_removal(existing_clean_files, "需要清理内容的文件"):
        for file_path in existing_clean_files:
            try:
                open(file_path, 'w').close()
                print(f"已清空文件内容: {file_path}")
            except Exception as e:
                print(f"清空文件 {file_path} 失败: {e}")
    
    print("\n===== 项目清理完成 =====")
    print("建议后续操作:")
    print("1. 检查是否有遗漏的不需要文件")
    print("2. 备份重要数据文件")
    print("3. 运行项目确保功能正常")

if __name__ == "__main__":
    # 以管理员权限运行的提示（可选）
    if os.name == 'nt':  # Windows系统
        try:
            # 检查是否以管理员权限运行
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if not is_admin:
                print("警告: 可能需要管理员权限才能删除某些文件")
        except:
            pass
    
    # 开始清理
    clean_project()
    
    # 暂停以便查看结果
    if os.name == 'nt':
        input("按Enter键退出...")