def does_file_exist(file_path : str) -> str:
    from os import path
    
    if path.exists(file_path):
        filename = path.basename(file_path)
        directory = path.dirname(file_path)
        print(f"Filename: {filename}\nDirectory: {directory}")
    else:
        print(f"Given path ({file_path}) does not exist")

does_file_exist("C:\\Study\\repos")
does_file_exist("C:\\Study\\c++")