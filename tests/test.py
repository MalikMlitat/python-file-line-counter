import os
import sys

sys.path.append(os.getcwd())
from file_counter import file_counter

def run_tests():

    if os.path.exists("testdata/file_with_5_lines.txt"):
        print("Test 1 (File Exists): PASSED")
    else:
        print("Test 1: FAILED - File does not exist")
        return

    res2 = file_counter.count_lines("testdata/empty_file.txt")
    assert res2 == 0
    print(f"Test 2 (Empty File): PASSED")

    
    res3 = file_counter.count_lines("testdata/one_line_file.txt")
    assert res3 == 1
    print(f"Test 3 (1 Line): PASSED")

if __name__ == "__main__":
    run_tests()
