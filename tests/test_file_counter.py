import pytest
from file_counter.file_counter import count_lines

def make_file(tmp_path, text):
    path = tmp_path / "test.txt"
    path.write_text(text)
    return str(path)

def test_counts_empty_file(tmp_path):
    file_path = make_file(tmp_path, "")
    assert count_lines(file_path) == 0

def test_counts_single_line(tmp_path):
    file_path = make_file(tmp_path, "Hello world")
    assert count_lines(file_path) == 1

def test_counts_multiple_lines(tmp_path):
    file_path = make_file(tmp_path, "a\nb\nc\n")
    assert count_lines(file_path) == 3

def test_counts_lines_without_trailing_newline(tmp_path):
    file_path = make_file(tmp_path, "a\nb\nc")
    assert count_lines(file_path) == 3

def test_counts_only_newlines(tmp_path):
    file_path = make_file(tmp_path, "\n\n\n")
    assert count_lines(file_path) == 3

def test_raises_error_for_missing_file():
    with pytest.raises(FileNotFoundError):
        count_lines("missing_file.txt")

def test_counts_blank_lines_between_text(tmp_path):
    file_path = make_file(tmp_path, "a\n\nc\n")
    assert count_lines(file_path) == 3
