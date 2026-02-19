import pytest
from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_valid_file_path_type():
    file_path = "tests/test_files/file_with_5_lines.txt"
    assert type(file_path)== str

def test_Invalid_file_path_type():
    file_path = 88733
    assert type(file_path)== int

def test_endwit_txt():
    file_path = "tests/test_files/file_with_5_lines.txt"
    assert file_path.endswith('.txt')

def test_endwit_notTxt():
    file_path = "tests/test_files/file_with_5_lines.txt"
    assert not file_path.endswith('pdf')

def test_file_counter_empty_file():
    assert 0==file_counter.count_lines('./testdata/empty_file.txt')

def test_file_counter_notEmpty_file():
    assert 0!=file_counter.count_lines('./testdata/file_with_5_lines.txt')

# middle line is empty and ignored due to line.strip()
def test_line_blank_line():
    assert 2==file_counter.count_lines('./testdata/line_blank_line.txt')

def test_single_line():
    assert 1==file_counter.count_lines('./testdata/file_with_single_line.txt')

#len>1
def test_single_char_line():
    assert 0==file_counter.count_lines('./testdata/file_with_one_char.txt')

def test_line_one_char_two_one_char():
    assert 1==file_counter.count_lines('./testdata/line_one_char_two_one_char.txt')

def test_file_with_special_char():
    assert 2==file_counter.count_lines('./testdata/file_with_special_char.txt')

def test_unicode_lines():
    assert 4 == file_counter.count_lines('./testdata/file_with_unicode.txt')

#python -m pytest