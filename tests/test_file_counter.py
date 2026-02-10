from file_counter.file_counter import count_lines

def test_file_with_5_lines():
    assert count_lines("testdata/file_with_5_lines.txt") == 5

def test_empty_file(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("")
    assert count_lines(str(f)) == 0

def test_one_line(tmp_path):
    f = tmp_path / "b.txt"
    f.write_text("hello")
    assert count_lines(str(f)) == 1

def test_multiple_lines(tmp_path):
    f = tmp_path / "c.txt"
    f.write_text("a\nb\nc\n")
    assert count_lines(str(f)) == 3
