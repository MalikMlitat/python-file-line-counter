import os
from file_counter.file_counter import count_lines

def test_file_with_5_lines():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "testdata", "file_with_5_lines.txt")

    assert count_lines(file_path) == 5