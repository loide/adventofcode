import unittest
import os
import day2 as d


class Test(unittest.TestCase):
    '''TestCases'''
    data = [
            ("example1.txt", 3500),
            ("input.txt", 574684),
            ("input_changed.txt", 4462686)
            ]

    def test_process_opcode(self):
        for [test, expected] in self.data:
            FILEPATH = test
            if not os.path.isfile(FILEPATH):
                print("File path {} does not exist. Exiting...".format(
                    FILEPATH
                    ))
                pass

            # create intcode map from input file
            intcode_map = d.load_intcode(FILEPATH)
            d.process_opcode(intcode_map)
            actual = intcode_map[0]
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
