import pytest
from pathlib import Path
from file_counter import count_lines  

@pytest.fixture
def tmp_files(tmp_path):
    file_normal = tmp_path / "normal.txt"
    file_normal.write_text("Hello\nWorld\n")  

    file_empty = tmp_path / "empty.txt"
    file_empty.write_text("")  

    return file_normal, file_empty

def test_count_normal_file(tmp_files):
    file_normal, _ = tmp_files
    assert count_lines(file_normal) == 2

def test_count_empty_file(tmp_files):
    _, file_empty = tmp_files
    assert count_lines(file_empty) == 0

def test_count_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        count_lines("does_not_exist.txt")
