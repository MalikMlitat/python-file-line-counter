import pytest
from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_file_counter_empty_file(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    assert file_counter.count_lines(str(f)) == 0

def test_count_lines_one_line_no_newline(tmp_path):
    f = tmp_path / "one.txt"
    f.write_text("hello")
    assert file_counter.count_lines(str(f)) == 1

def test_count_lines_three_lines_with_trailing_newline(tmp_path):
    f = tmp_path / "three.txt"
    f.write_text("a\nb\nc\n")
    assert file_counter.count_lines(str(f)) == 3

def test_count_lines_three_lines_without_trailing_newline(tmp_path):
    f = tmp_path / "three2.txt"
    f.write_text("a\nb\nc")
    assert file_counter.count_lines(str(f)) == 3

def test_count_lines_file_not_found():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("no_such_file_123456.txt")
