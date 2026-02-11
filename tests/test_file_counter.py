from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_file_counter_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_lines.txt")

def test_single_counter_file():
    
    assert 1 == file_counter.count_lines("testdata/single_line.txt")

def test_file_counter_not_exiting_file():
    assert 0 == file_counter.count_lines("testdata/not_existing.txt")