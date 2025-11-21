import os
import tempfile
import unittest

from lab2 import count_paint_bottles


class TestCountPaintBottles(unittest.TestCase):
    def create_temp_file(self, content: str):
        """Helper: create a temporary test file containing given text."""
        temp = tempfile.NamedTemporaryFile(delete=False, mode="w+t")
        temp.write(content)
        temp.close()
        return temp.name

    def read_file(self, filename: str) -> str:
        """Helper: read whole file as string."""
        with open(filename, "r") as f:
            return f.read()

    def test_basic_count(self):
        input_content = (
            "Pink,85\n"
            "Red,44\n"
            "Maroon,80\n"
            "Red,6\n"  # tests accumulation
        )

        input_file = self.create_temp_file(input_content)
        output_file = tempfile.NamedTemporaryFile(delete=False).name

        count_paint_bottles(input_file, output_file)

        result = self.read_file(output_file)

        # Convert to a dictionary for comparison (order doesn't matter)
        lines = [line.strip() for line in result.split("\n") if line.strip()]
        result_dict = dict(line.split(":") for line in lines)

        expected = {"Pink": "85", "Red": "50", "Maroon": "80"}

        self.assertEqual(result_dict, expected)

        os.remove(input_file)
        os.remove(output_file)

    def test_single_line(self):
        input_content = "Blue,100\n"

        input_file = self.create_temp_file(input_content)
        output_file = tempfile.NamedTemporaryFile(delete=False).name

        count_paint_bottles(input_file, output_file)

        result = self.read_file(output_file).strip()
        self.assertEqual(result, "Blue:100")

        os.remove(input_file)
        os.remove(output_file)

    def test_multiple_duplicates(self):
        input_content = "Green,10\nGreen,20\nGreen,30\n"

        input_file = self.create_temp_file(input_content)
        output_file = tempfile.NamedTemporaryFile(delete=False).name

        count_paint_bottles(input_file, output_file)

        result = self.read_file(output_file).strip()
        self.assertEqual(result, "Green:60")

        os.remove(input_file)
        os.remove(output_file)


if __name__ == "__main__":
    unittest.main()
