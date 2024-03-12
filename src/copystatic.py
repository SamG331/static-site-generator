import os
import shutil

def copy_files_recursively(src_path: str, dst_path: str):
    if not os.path.exists(src_path):
        raise ValueError("src path doesn't exist")
    if not os.path.exists(dst_path):
        raise ValueError("dst path doesn't exist")
    src_list = []
    for item in os.listdir(path=src_path):
        extended_src = os.path.join(src_path, item)
        extended_dst = os.path.join(dst_path, item)
        print(f" * {extended_src} -> {extended_dst}")
        if os.path.isfile(extended_src):
            shutil.copy(extended_src, extended_dst)
            src_list.append(extended_src)
        else:
            os.mkdir(extended_dst)
            copy_files_recursively(extended_src, extended_dst)