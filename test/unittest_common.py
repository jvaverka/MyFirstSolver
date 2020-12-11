# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import unittest
from physics import common
from physics import oned_kinematics as oned
from physics import twod_kinematics as twod


class TestCommonMathMethods(unittest.TestCase):

    def test_quadratic(self) :
        # check
        self.assertTupleEqual(common.quadratic(1,-2,1), (1.0, 1.0))
        # double check
        self.assertTupleEqual(common.quadratic(-4.9, 20, 10) \
            , (-0.4503174725987147, 4.531950125659939))
        # triple check
        self.assertTupleEqual(common.quadratic(2, 30, -35) \
            ,(1.0877820186588334,-16.087782018658835))

    def test_vector_components(self) :
        # check
        self.assertTupleEqual(common.get_component_vectors(20, 140) \
            , (-15.320888862379558, 12.85575219373079))
        # double check
        self.assertTupleEqual(common.get_component_vectors(30, 20) \
            , (28.190778623577252, 10.260604299770062))
        # triple check
        self.assertTupleEqual(common.get_component_vectors(50, 195) \
            , (-48.29629131445341, -12.94095225512604))
    
    def test_resultant_vector(self) :
        # check
        self.assertTupleEqual(common.get_resultant_vector(3.2799, 6.5701) \
            , (7.343293404188614, 63.470889313636505))
        # double check
        self.assertTupleEqual(common.get_resultant_vector(-54.651, -74.401) \
            , (92.31598237575116, 53.70098432541721))
        # triple check
        self.assertTupleEqual(common.get_resultant_vector(21.63, 4.53) \
            , (22.099271481204983, 11.828570199481405))

if __name__ == '__main__':
    unittest.main()