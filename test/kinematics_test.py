# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import unittest
from subprocess import check_output

class TestCli(unittest.TestCase):

    def base_test(self):
        cmd = 'python3 src/kinematics.py -i util/base_test.json'.split()
        output = check_output(cmd, shell=False, universal_newlines=True)
        time_in_air = 'time_in_air => 1.7857142857142851 s'
        max_height = 'max_height => 15.624999999999991 meters'

        self.assertIn(time_in_air, output)
        self.assertIn(max_height, output)

    def test_isupper(self):
        pass

    def test_split(self):
        pass

if __name__ == '__main__':
    unittest.main()