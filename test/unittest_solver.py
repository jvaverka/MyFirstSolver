# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import unittest
from physics import solver

class TestSolver(unittest.TestCase) :

    def test_solver_1(self) :
        input = {
            '1D': {
                'initial_position': 0,
                'velocity_initial': 20,
                'velocity_final': 0,
                'time': 40,
                'acceleration': -1
            }
        }
        full_solution = solver.solve(input)
        oned_soln = full_solution['1D']
        self.assertEqual(oned_soln['time'], 20)
        self.assertEqual(oned_soln['final_position'], 200)

    def test_solver_2(self) :
        input = {
            '1D': {
                'initial_position': 0,
                'final_position': 100,
                'velocity_initial': 30,
                'velocity_final': None,
                'time': None,
                'acceleration': -3.5
            }
        }
        full_solution = solver.solve(input)
        oned_soln = full_solution['1D']
        self.assertEqual(oned_soln['time'], 4.53)

if __name__ == '__main__':
    unittest.main()