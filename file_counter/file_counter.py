def count_lines(file_path):
    """
    Counts all lines in a file, including empty lines and the last line
    even if it doesn't end with a newline character.
    """
    with open(file_path, "r") as file:
        return sum(1 for _ in file)
