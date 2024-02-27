def copy_to_another(first_file_path : str, second_file_path : str) -> None:
    file_1 = open(first_file_path, "r")
    file_2 = open(second_file_path, "a")
    try:
        text_to_write = file_1.read()
        file_2.write(text_to_write + ' ')
        print("File has been written")
    except Exception as e:
        print(f"Error: {e}")


    file_1.close(), file_2.close()

    return None

copy_to_another("Copy_file.txt", "Write_file.txt")