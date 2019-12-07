import unittest
import os
import day6 as d

class Test(unittest.TestCase):
    '''TestCases'''
    data = [
            ("example.txt", 42),
            ("example2.txt", 42),
            ("input.txt", 162816)
            ]
    data2 = [
            ("example3.txt", 4),
            ("input.txt", 304)
            ]

    def test_count_checksums(self):
        for [test, expected] in self.data:
            FILEPATH = test
            if not os.path.isfile(FILEPATH):
                print("File path {} does not exist. Exiting...".format(FILEPATH))
                pass

            # create orbit map from input file
            orbit_map = d.mapping_orbits(FILEPATH)
            actual = d.count_total_orbits(orbit_map)
            self.assertEqual(actual, expected)

    def test_minimum_transfers(self):
        for [test, expected] in self.data2:
            FILEPATH = test
            if not os.path.isfile(FILEPATH):
                print("File path {} does not exist. Exiting...".format(FILEPATH))
                pass

            # create orbit map from input file
            orbit_map = d.mapping_orbits(FILEPATH)
            actual = d.minimum_number_of_orbital_transfers(orbit_map)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
