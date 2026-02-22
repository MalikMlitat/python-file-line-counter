def count_lines(file_path):
    with open(file_path) as file:
        line_count = sum(1 for line in file if len(line.strip()) > 1)
    return line_count
