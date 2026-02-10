from file_counter import file_counter

def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")


def test_file_counter_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")

def test_file_counter_second_line_content():
    with open("testdata/file_with_5_lines.txt", "r") as f:
        lines = f.readlines()
    assert lines[1].strip() == "and this is line 2"

def test_file_counter_last_line_content():
    with open("testdata/file_with_5_lines.txt", "r") as f:
        lines = f.readlines()
    assert lines[-1].strip() == "last line is 5"