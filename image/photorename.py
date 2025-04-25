import os
import re
#这个脚本便于重命名文件
def rename_photos(directory=None):
    """
    重命名目录中以'photo_'开头的jpg文件
    :param directory: 目标目录路径，默认为当前目录
    """
    target_dir = directory if directory else os.path.dirname(os.path.abspath(__file__))
    
    # 获取目标目录下所有以'photo_'开头的jpg文件
    files = [f for f in os.listdir(target_dir) 
             if f.startswith('photo_') and f.lower().endswith('.jpg')]
    print(f"在目录 {target_dir} 找到 {len(files)} 个匹配文件: {files}")
    
    # 按文件名排序
    files.sort()
    
    # 计数器
    count = 1
    
    for old_name in files:
        # 构造新文件名
        new_name = f"[巨乳{count}].jpg"
        
        # 重命名文件
        try:
            os.rename(os.path.join(target_dir, old_name), 
                     os.path.join(target_dir, new_name))
            print(f"已重命名: {old_name} -> {new_name}")
            count += 1
        except Exception as e:
            print(f"重命名失败 {old_name}: {str(e)}")

if __name__ == "__main__":
    rename_photos()