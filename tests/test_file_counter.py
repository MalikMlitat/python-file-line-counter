import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_counter.file_counter import count_lines

class TestFileCounter(unittest.TestCase):
    
    def test_file_with_5_lines(self):
        path = "testdata/file_with_5_lines.txt"
        self.assertEqual(count_lines(path), 5)

    def test_empty_file(self):
        # اختبار الملف الفارغ
        self.assertEqual(count_lines("empty.txt"), 0)

    def test_small_file(self):
        # اختبار ملف صغير (سطرين) موجود في المجلد الرئيسي
        self.assertEqual(count_lines("small.txt"), 2)
        
    def test_file_not_found(self):
        """اختبار سلوك الدالة عند محاولة فتح ملف غير موجود نهائياً"""
        with self.assertRaises(FileNotFoundError):
            count_lines("non_existent_file_999.txt")

    def test_very_large_file_performance(self):
        """اختبار أداء الدالة مع ملف يحتوي على 10,000 سطر"""
        path = "performance_test.txt"
        line_count = 10000
        with open(path, "w") as f:
            for i in range(line_count):
                f.write("Performance test line\n")
        
        result = count_lines(path)
        os.remove(path)
        self.assertEqual(result, line_count)

if __name__ == "__main__":
    unittest.main(exit=False)