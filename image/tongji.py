import os
#这个脚本用于收集当前目录下的所有jpg文件并格式化输出以方便存入Config.ini
def collect_jpg_files():
    """
    收集当前目录下的所有jpg文件并格式化输出
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    jpg_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.jpg')]
    print(f"当前目录: {current_dir}")
    print(f"找到 {len(jpg_files)} 个JPG文件: {jpg_files}")
    
    # 按文件名排序
    jpg_files.sort()
    
    # 格式化输出
    # 直接输出实际文件名
    print(", ".join(jpg_files))

if __name__ == "__main__":
    collect_jpg_files()