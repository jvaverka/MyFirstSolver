# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import math
from physics import common

class OneDKinematics:

    @staticmethod
    def average_speed(params) :
        try:
            return (params['initial_position'], params['final_position']) \
                / params['time']
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def displacement_with_constant_velocity(params) :
        # x_final_position = x_initial_position + (velocity_initial * time)
        try:
            return params['initial_position'] \
                + params['velocity_initial']*params['time']
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def velocity_with_acc_and_time(params) :
        # velocity_final = velocity_initial + (acceleration * time)
        try:
            return params['velocity_initial'] \
                + params['acceleration']*params['time']
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    def time_to_final_velocity_with_acc(params) :
        try:
            return (params['velocity_final']-params['velocity_initial']) \
                / params['acceleration']
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def displacement_with_acc_and_time(params) :
        # y_final_position = y_initial_position 
        #                   + (velocity_initial * time) 
        #                   + (1/2)(acceleration)(time**2)
        try:
            return params['initial_position'] \
                + (params['velocity_initial'] * params['time']) \
                    + ((0.5) * (params['acceleration']) * (params['time']**2))
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def velocity_with_displacement(params) :
        # velocity_final**2 = velocity_initial**2 
        #                    + 2(acceleration)(displacement_delta)
        try:
            return math.sqrt( \
                params['velocity_initial']**2 + \
                    (2 * params['acceleration'] * \
                        (params['final_position']-params['initial_position'])))
        except Exception as e:
            print(e)
            return None
