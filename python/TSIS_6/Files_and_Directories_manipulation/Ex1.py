def show_directories(path : str) -> str :
    from os import listdir
    print(listdir(path))

show_directories("C:\\")


show_directories("C:\\Study\\")