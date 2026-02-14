def count_lines(file_path):
    """
    Counts all lines in a file correctly, including empty lines,
    and returns 0 for truly empty files.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
        # إذا الملف فارغ فعليًا
        if len(lines) == 1 and lines[0] == "":
            return 0
        return len(lines)
