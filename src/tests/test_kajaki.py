import string
import unittest
import kajaki


class InputParser(unittest.TestCase):
    def test_should_parse_input_line_to_tuple(self):
        input_string = '2 5\n' \
                       '3 4\n' \
                       '1 3'
        expected_pairs = [(2, 5), (3, 4), (1, 3)]
        for index, line in enumerate(string.split(input_string, '\n'), start=0):
            actual = kajaki.parse_line_to_tuple(line)
            expected = expected_pairs[index]

            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
