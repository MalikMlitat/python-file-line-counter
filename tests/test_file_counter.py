from file_counter.file_counter import count_lines
import pytest

def test_count_lines_with_text_file():
    with open("test_file.txt", "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")
    assert count_lines("test_file.txt") == 3

def test_count_lines_empty_file():
    with open("empty_file.txt", "w"):
        pass
    assert count_lines("empty_file.txt") == 0

def test_count_lines_with_empty_lines():
    with open("file_with_empty_lines.txt", "w") as f:
        f.write("Line 1\n")
        f.write("\n")
        f.write("Line 2\n")
        f.write("\n")
    assert count_lines("file_with_empty_lines.txt") == 2

def test_count_lines_file_not_found():
    with pytest.raises(FileNotFoundError):
        count_lines("non_existing_file.txt")


