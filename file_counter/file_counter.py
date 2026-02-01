def count_lines(file_path):
    """
    Counts the number of lines in a given file efficiently.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The total number of lines in the file.
    """

    with open(file_path) as file:
        line_count = sum(1 for line in file if len(line.strip()) > 1)
    return line_count

