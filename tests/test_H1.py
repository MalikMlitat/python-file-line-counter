import unittest
from file_counter.file_counter import count_lines

class TestCountLines(unittest.TestCase):

    def test_file_with_5_lines(self):
        result = count_lines("testdata/file_with_5_lines.txt")
        self.assertEqual(result, 5)

    def test_file_lines_content(self):
        with open("testdata/file_with_5_lines.txt", "r") as f:
            lines = f.readlines()
        
        for line in lines:
            self.assertTrue(line.strip() != "", "Found empty line or line with only spaces")

if __name__ == "__main__":
    unittest.main()
