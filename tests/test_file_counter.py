from file_counter import file_counter


def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")


def test_file_counter_simulate_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    assert 0 == file_counter.count_lines(empty_file)


def test_file_counter_simulate_large_file(tmp_path):
    large_file = tmp_path / "large.txt"
    large_file.write_text("\n".join("line" for _ in range(1000)))
    assert 1000 == file_counter.count_lines(large_file)


def test_file_counter_simulate_blank_lines(tmp_path):
    blank_file = tmp_path / "blank.txt"
    blank_file.write_text("line1\n\nline2\n\nline3\n\nline4")
    assert 7 == file_counter.count_lines(blank_file)
