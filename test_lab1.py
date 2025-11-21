import os
import tempfile
import unittest

from lab1 import computer_average


class TestComputerAverage(unittest.TestCase):
    def create_temp_file(self, content: str):
        """Helper to create a temporary test file."""
        temp = tempfile.NamedTemporaryFile(delete=False, mode="w+t")
        temp.write(content)
        temp.close()
        return temp.name

    def test_basic_average(self):
        content = "5\n10\n20\n30\n40\n50\n"
        filename = self.create_temp_file(content)

        result = computer_average(filename)
        self.assertEqual(result, 30.0)

        os.remove(filename)

    def test_with_floats(self):
        content = "3\n1.5\n2.5\n3.0\n"
        filename = self.create_temp_file(content)

        result = computer_average(filename)
        self.assertAlmostEqual(result, 2.3333333, places=6)

        os.remove(filename)

    def test_single_number(self):
        content = "1\n99\n"
        filename = self.create_temp_file(content)

        result = computer_average(filename)
        self.assertEqual(result, 99.0)

        os.remove(filename)

    def test_empty_list_should_fail(self):
        content = "0\n"
        filename = self.create_temp_file(content)

        with self.assertRaises(ZeroDivisionError):
            computer_average(filename)

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
