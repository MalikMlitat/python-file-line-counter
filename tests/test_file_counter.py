# tests/test_file_counter.py
import pytest
from file_counter.file_counter import count_lines


def test_empty_file(tmp_path):
    """Test counting lines in an empty file."""
    file_path = tmp_path / "empty.txt"
    file_path.write_text("")
    assert count_lines(str(file_path)) == 0


def test_one_line_no_trailing_newline(tmp_path):
    """Test counting lines in a file with one line and no trailing newline."""
    file_path = tmp_path / "one_line.txt"
    file_path.write_text("hello world")
    assert count_lines(str(file_path)) == 1


def test_one_line_with_trailing_newline(tmp_path):
    """Test counting lines in a file with one line and a trailing newline."""
    file_path = tmp_path / "one_line_nl.txt"
    file_path.write_text("hello world\n")
    assert count_lines(str(file_path)) == 1


def test_two_lines_no_trailing_newline(tmp_path):
    """Test counting lines in a file with two lines and no trailing newline."""
    file_path = tmp_path / "two_lines.txt"
    file_path.write_text("line1\nline2")
    assert count_lines(str(file_path)) == 2


def test_two_lines_with_trailing_newline(tmp_path):
    """Test counting lines in a file with two lines and a trailing newline.
    
    This test may reveal a bug if the SUT miscounts due to trailing newlines.
    """
    file_path = tmp_path / "two_lines_nl.txt"
    file_path.write_text("line1\nline2\n")
    assert count_lines(str(file_path)) == 2


def test_only_newline(tmp_path):
    """Test counting lines in a file containing only a newline."""
    file_path = tmp_path / "only_nl.txt"
    file_path.write_text("\n")
    assert count_lines(str(file_path)) == 1


def test_multiple_newlines(tmp_path):
    """Test counting lines in a file with multiple newlines."""
    file_path = tmp_path / "multi_nl.txt"
    file_path.write_text("\n\n\n")
    assert count_lines(str(file_path)) == 3


def test_nonexistent_file():
    """Test that a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        count_lines("nonexistent_file.txt")


def test_directory_path(tmp_path):
    """Test that providing a directory path raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        count_lines(str(tmp_path))