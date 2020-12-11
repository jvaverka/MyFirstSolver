# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import unittest
from physics import oned_kinematics as oned

input1 = {
    '1D': {
        'initial_position': 0,
        'velocity_initial': 20,
        'velocity_final': 0,
        'time': 20,
        'acceleration': -1
    }
}
input2 = {
    '1D': {
        'initial_position': 0,
        'final_position': 100,
        'velocity_initial': 30,
        'velocity_final': 0,
        'time': None,
        'acceleration': -3.50
    }
}


class TestOneDimension(unittest.TestCase) :

    def test_displacement_with_acceleration(self) :
        ans = oned.OneDKinematics.displacement_with_acc_and_time(input1['1D'])
        self.assertEqual(ans, 200)
    
    def test_time_to_final_velocity_with_acc(self) :
        time = oned.OneDKinematics.time_to_final_velocity_with_acc(input1['1D'])
        self.assertEqual(time, 20)
    
    def test_time_to_final_position_with_acc(self) :
        time = oned.OneDKinematics.time_to_final_velocity_with_acc(input2['1D'])
        self.assertEqual(time, 4.53)


if __name__ == "__main__":
    unittest.main()