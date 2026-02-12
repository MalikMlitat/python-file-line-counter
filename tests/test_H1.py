
from file_counter.file_counter import count_lines

#  Empty file
def test_count_lines_empty_file(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")
    assert count_lines(file) == 0


#  File with one line
def test_count_lines_one_line(tmp_path):
    file = tmp_path / "one.txt"
    file.write_text("line1")
    assert count_lines(file) == 1


#  File with multiple lines
def test_count_lines_multiple_lines(tmp_path):
    file = tmp_path / "multi.txt"
    file.write_text("Line 1\nLine 2\nLine 3\n")
    assert count_lines(file) == 3


#  File with empty lines inside
def test_count_lines_with_empty_lines(tmp_path):
    file = tmp_path / "empty_lines.txt"
    file.write_text("Line 1\n\nLine 3\n")
    assert count_lines(file) == 2


#  Large file (1000 lines)
def test_count_lines_large_file(tmp_path):
    file = tmp_path / "large.txt"
    file.write_text("\n".join(["Line"] * 1000))
    assert count_lines(file) == 1000
