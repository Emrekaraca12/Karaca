def how_much_lines_in_text(path : str) -> int:
    line_count = 0

    file = open(path, "r")
    for line in file:
        line_count += 1

    file.close()

    return line_count

print(f"There is {how_much_lines_in_text('file_1.txt')} lines in text")
print(f"There is {how_much_lines_in_text('file_2.txt')} lines in text")