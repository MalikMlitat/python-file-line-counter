import pytest
from file_counter import file_counter

# Happy path
def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_file_not_empty():
    assert file_counter.count_lines("testdata/file_with_5_lines.txt") > 0 

def test_counts_lines_in_valid_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("line1\nline2\nline3\n")
    assert file_counter.count_lines(str(file)) == 3

def test_counts_lines_without_trailing_newline(tmp_path):
    file = tmp_path / "no_trailing_newline.txt"
    file.write_text("line1\nline2\nline3")  # no \n at the end
    assert file_counter.count_lines(str(file)) == 3

# Edge Cases
def test_counts_empty_lines_as_valid_lines(tmp_path):
    file = tmp_path / "blank_line.txt"
    file.write_text("line1\nline2\nline3\n\n")
    assert file_counter.count_lines(str(file)) == 4

def test_counts_single_character_lines(tmp_path):
    file = tmp_path / "single_char_lines.txt"
    file.write_text("a\nb\nc\n")
    assert file_counter.count_lines(str(file)) == 3

#Error Handling
def test_raises_error_for_missing_file():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("file_that_does_not_exist.txt")
        
# Boundary Case
def test_counts_empty_file(tmp_path):
    file = tmp_path / "empty_file.txt"
    file.write_text("")  # completely empty file
    assert file_counter.count_lines(str(file)) == 0


