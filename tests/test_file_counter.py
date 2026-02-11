import pytest
from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_file_counter_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")

def test_file_counter_with_blank_lines_file():
    assert 3 == file_counter.count_lines("testdata/file_with_blank_lines.txt")

def test_file_counter_invalid_file():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("invalid_file.txt")

def test_file_counter_with_single_char_lines_file():
    assert 5 == file_counter.count_lines("testdata/file_with_single_char_lines.txt")

def test_file_counter_with_mixed_lines_file():
    assert 5 == file_counter.count_lines("testdata/file_with_mixed_lines.txt")

def test_file_counter_with_special_chars_file():
    assert 5 == file_counter.count_lines("testdata/file_with_special_chars.txt")

def test_file_counter_with_non_text_file():
    assert 2 == file_counter.count_lines("testdata/non_text_file.bin")

def test_file_counter_with_large_file():
    assert 100 == file_counter.count_lines("testdata/large_file.txt")

def test_file_counter_with_arabic_file():
    assert 4 == file_counter.count_lines("testdata/file_with_arabic.txt")