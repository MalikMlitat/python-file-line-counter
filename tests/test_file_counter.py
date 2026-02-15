from file_counter import file_counter
import pytest
file_path= "testdata/large-lines.txt"
with open(file_path,"w",encoding="utf-8") as f: #write 1000 line
  for i in range(1,1001):
     f.write(f"Line {i}\n") 

def test_file_counter_valid_file():
    assert 5== file_counter.count_lines("testdata/file_with_5_lines.txt")

def test_empty_file():
    assert 0 == file_counter.count_lines("testdata/empty.txt")  

def test_short_lines():
    assert 0 == file_counter.count_lines("testdata/short-lines.txt") 

def test_missing_file():
    with pytest.raises(FileNotFoundError):
     file_counter.count_lines("testdata/missing.txt") 

def test_Mixed_TC():
    assert 3 == file_counter.count_lines("testdata/mixed-Lines.txt")

def test_Mixed_Ara_English_char():
    assert 3 == file_counter.count_lines("testdata/mixed-Ara&Eng.txt") 
def test_Large_lines():
    assert 1000 == file_counter.count_lines("testdata/Large-lines.txt")     



