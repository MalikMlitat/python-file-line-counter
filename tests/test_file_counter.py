import inspect

import pytest

from file_counter import file_counter


def test_file_counter_valid_file():
    assert 5 == file_counter.count_lines("testdata/file_with_5_lines.txt")


def test_count_lines_interface_has_single_file_path_parameter():
    signature = inspect.signature(file_counter.count_lines)
    assert ["file_path"] == list(signature.parameters)


def test_count_lines_returns_int():
    line_count = file_counter.count_lines("testdata/file_with_5_lines.txt")

    assert isinstance(line_count, int)


def test_count_lines_raises_file_not_found_error_for_missing_path():
    with pytest.raises(FileNotFoundError):
        file_counter.count_lines("testdata/missing_file.txt")


def test_count_lines_counts_blank_and_single_character_lines():
    assert 3 == file_counter.count_lines(
        "testdata/file_with_blank_and_single_character_lines.txt"
    )


def test_count_lines_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty_file.txt")


def test_count_lines_large_file():
    assert 1000 == file_counter.count_lines("testdata/big_file.txt")


def test_count_lines_binary_file():
    assert 2 == file_counter.count_lines("testdata/binary_file.bin")
