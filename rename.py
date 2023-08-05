import os


def rename_files(folder_path, prefix):
    """フォルダ内のファイルを走査して名前を変更する"""
    file_list = os.listdir(folder_path)
    for i, filename in enumerate(file_list):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{i}{ext}"
        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_name))
