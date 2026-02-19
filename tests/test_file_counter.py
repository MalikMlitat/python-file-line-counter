import pytest
from file_counter import file_counter

from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_empty_file():
  assert 0 == file_counter.count_lines("testdata/empty_CaseFile.txt")

def test_file_not_found():
  with pytest.raises(FileNotFoundError):
    file_counter.count_lines("testdata/not_existing.txt") 

def test_single_character_line():
  assert 0 == file_counter.count_lines("testdata/one_CharCase.txt")

def test_spaces_only_file():
  assert 0 == file_counter.count_lines("testdata/spaces_only.txt")


def test_mixed_content_file():
  assert 3 == file_counter.count_lines("testdata/charswith_spaces.txt")
