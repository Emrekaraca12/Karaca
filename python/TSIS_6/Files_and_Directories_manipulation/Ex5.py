def write_a_list_in_file(path : str, some_list : list) -> None:
    file = open(path, "a")
    try:
        file.write("".join([x for x in some_list]) + '\n')
        print("List has been written")
    except Exception as e:
        print(f"Error: {e}")

    file.close()

    return None

write_a_list_in_file("file_to_write.txt", "[1 2 3 4 5 6]")