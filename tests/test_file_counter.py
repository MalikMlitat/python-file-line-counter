

import pytest
from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")

def test_file_with_spaces():
    assert 0 == file_counter.count_lines("testdata/file_with_spaces.txt")

def test_file_with_single_char():
    assert 0 == file_counter.count_lines("testdata/file_with_single_char.txt")

def test_file_with_mult_lines():
    assert 6 == file_counter.count_lines("testdata/file_with_mult_lines.txt")
    
def test_file_with_all_cases():
    assert 4 == file_counter.count_lines("testdata/file_with_all_cases.txt")
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("testdata/not_exist.txt")
