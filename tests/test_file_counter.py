from file_counter import file_counter
filePath = "testdata/file_with_5_lines.txt"

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines(filePath)

def test_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")

def test_file_with_3_lines():
    assert 3 == file_counter.count_lines("testdata/file_with_3_lines.txt")

def test_file_with_blank_line():
    assert 4 == file_counter.count_lines("testdata/file_with_blank_line.txt")