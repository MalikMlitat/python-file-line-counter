import pytest
from file_counter.file_counter import count_lines

def test_empty_file(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("")
    assert count_lines(str(f)) == 0

def test_one_line_no_newline(tmp_path):
    f = tmp_path / "one.txt"
    f.write_text("hello")
    assert count_lines(str(f)) == 1

def test_multiple_lines_with_trailing_newline(tmp_path):
    f = tmp_path / "multi.txt"
    f.write_text("a\nb\nc\n")
    assert count_lines(str(f)) == 3

def test_multiple_lines_without_trailing_newline(tmp_path):
    f = tmp_path / "multi_no_last_newline.txt"
    f.write_text("a\nb\nc")
    assert count_lines(str(f)) == 3

def test_blank_lines_are_counted(tmp_path):
    f = tmp_path / "blanks.txt"
    f.write_text("a\n\nb\n")
    assert count_lines(str(f)) == 3

def test_missing_file_raises():
    with pytest.raises(Exception):
        count_lines("definitely_missing_file_123.txt")
