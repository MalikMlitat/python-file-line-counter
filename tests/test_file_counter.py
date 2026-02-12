from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")
    
def test_file_counter_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")

def test_file_counter_file_with_only_newlines():
    assert 3 == file_counter.count_lines("testdata/file_with_only_newlines.txt")


def test_file_counter_nonexistent_file(): 
    try: 
        file_counter.count_lines("testdata/nonexistent_file.txt") 
        assert False, "Expected FileNotFoundError" 
    except FileNotFoundError: 
        assert True