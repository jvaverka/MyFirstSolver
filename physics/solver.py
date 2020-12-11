# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import argparse
from physics import common
from physics import oned_kinematics as oned
from physics import twod_kinematics as twod


def solve(given) :
    env = {
        "1D": {
            "initial_position": 0,
            "final_position": None,
            "velocity_initial": None,
            "velocity_final": None,
            "acceleration": None,
            "time": None
        },
        "x_initial": None,
        "y_initial": None,
        "x_final": None,
        "y_final": None,
        "velocity_initial": None,
        "velocity_final": None,
        "average_velocity": None,
        "acceleration": None,
        "time": None,
        "theta": None,
        "velocity_initial_x": None,
        "velocity_initial_y": None,
        "velocity_final_x": None,
        "velocity_final_y": None
    }
    env.update(given)
    if env['1D']['velocity_initial'] is not None \
         and env['1D']['velocity_final'] is not None \
             and env['1D']['acceleration'] is not None :
        time = oned.OneDKinematics.time_to_final_velocity_with_acc(env['1D'])
        env['1D']['time'] = time
        fp = oned.OneDKinematics.displacement_with_acc_and_time(env['1D'])
        env['1D']['final_position'] = fp
    if env['1D']['velocity_initial'] is not None \
        and env['1D']['velocity_final'] is not None \
            and env['1D']['acceleration'] is not None :
        time = oned.OneDKinematics.time_to_final_velocity_with_acc(env['1D'])
        env['1D']['time'] = time
        vf = oned.OneDKinematics.velocity_with_displacement(env['1D'])
        env['1D']['velocity_final'] = vf

    return env
    