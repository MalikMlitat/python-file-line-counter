def count_lines(file_path):
    """
    Counts the number of lines in a given file efficiently.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The total number of lines in the file.
    """
    with open(file_path, "r") as file:
        line_count = sum(1 for _ in file)
    return line_count


