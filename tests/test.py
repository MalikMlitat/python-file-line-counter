from file_counter import file_counter

def run_tests():

    result1 = file_counter.count_lines("testdata/file_with_5_lines.txt")
    assert result1 == 5
    print("Test 1 (Exact Line Count): PASSED")

    result2 = file_counter.count_lines("testdata/file_with_5_lines.txt")
    assert result2 > 0
    print("Test 2 (File Not Empty): PASSED")

    print("\nAll tests passed successfully!")

if __name__ == "__main__":
    run_tests()
