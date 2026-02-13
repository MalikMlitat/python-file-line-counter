from file_counter import file_counter
import pytest

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty.txt")

def test_file_with_trailing_newline():
    assert 4 == file_counter.count_lines("testdata/trailing_newline.txt")

def test_file_not_found_raises_error():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("this_file_does_not_exist.txt")