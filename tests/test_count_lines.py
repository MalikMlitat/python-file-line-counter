import pytest
from file_counter.file_counter import count_lines

def test_count_lines_normal_file(tmp_path):
    file = tmp_path / "normal.txt"
    file.write_text("line1\nline2\nline3")
    assert count_lines(file) == 3

def test_count_lines_empty_file(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")
    assert count_lines(file) == 0

def test_count_lines_single_line(tmp_path):
    file = tmp_path / "single.txt"
    file.write_text("only one line")
    assert count_lines(file) == 1

def test_count_lines_newline_last_line(tmp_path):
    file = tmp_path / "newline_last.txt"
    file.write_text("line1\nline2\n")
    assert count_lines(file) == 2

def test_count_lines_file_not_exist():
    file = "does_not_exist.txt"
    with pytest.raises(FileNotFoundError):
        count_lines(file)
