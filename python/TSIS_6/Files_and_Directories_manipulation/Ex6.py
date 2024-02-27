def create_a_file() -> None:
    import string
    import os
    letters_A_to_Z = string.ascii_uppercase
    path_to_folder = "C:/Study/repos/python/TSIS_6/Files_and_Directories_manipulation/A-Z_files"

    for i in letters_A_to_Z:
        file_path = os.path.join(path_to_folder, f"{i}.txt")
        file = open(file_path, "w")

    return None

create_a_file()