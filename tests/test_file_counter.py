from file_counter import file_counter
import pytest

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_file_counter_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")


def test_file_counter_single_line():
    assert 1 == file_counter.count_lines("testdata/file_with_1_line.txt")


def test_file_counter_non_existing_file():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("testdata/file_not_exist.txt")
