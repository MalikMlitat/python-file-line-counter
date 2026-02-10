from file_counter.file_counter import count_lines

def test_file_with_5_lines():
    assert count_lines("testdata/file_with_5_lines.txt") == 5

def test_empty_file():
    assert count_lines("testdata/empty_file.txt") == 0

def test_one_line_file():
    assert count_lines("testdata/file_with_1_line.txt") == 1
