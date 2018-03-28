import os

def search_folder(folder_path, name=None, file_type=None):
    """Search a folder for files with a given name and file type
    * Convenient abstraction for csvs

    args:
    folder_path -- path to folder containing desired files
    name -- (optional) name of the desired files (checks if substring of the file)
    file_type -- (optional) extension of the desired files
    """
    name = name.lower()
    file_type = file_type.lower()
    res = []
    for f in os.listdir(folder_path):
        f_l = f.lower()
        is_filetype = f_l.endswith(file_type) if file_type else True
        has_name = name in f_l if name else True
        if is_filetype and has_name:
            res.append(f)

    return res