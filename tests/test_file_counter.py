from file_counter.file_counter import count_lines

def test_file_with_5_lines():
    assert count_lines("testdata/file_with_5_lines.txt") == 5


def test_empty_file():
    assert count_lines("testdata/empty.txt") == 0