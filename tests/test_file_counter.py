import pytest
from file_counter import file_counter


def test_file_counter_valid_file(tmp_path):

    test_file = tmp_path / "file_with_5_lines.txt"
    test_file.write_text("Line1\nLine2\nLine3\nLine4\nLine5\n")
    
   
    assert file_counter.count_lines(str(test_file)) == 5

#Empty file
def test_file_counter_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    assert file_counter.count_lines(str(empty_file)) == 0

# File not found
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("not_existing_file.txt")

