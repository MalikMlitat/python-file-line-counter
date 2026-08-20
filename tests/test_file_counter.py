from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")

#check if its give invalid when its invalid 
def test_file_counter_invalid_file():
    assert 6 !=file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_empty_file():
    assert 0 ==file_counter.count_lines("testdata/empty_file.txt")

#test invalid path file => failed => no exception to handle this
def test_invalid_path_file():
    result =file_counter.count_lines("testdat/file_with_5_lines.txt")
    assert "invalid" in result