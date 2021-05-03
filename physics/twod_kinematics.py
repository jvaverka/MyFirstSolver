# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import math
from physics.common import get_component_vectors

class TwoDKinematics:

    @staticmethod
    def displacement_with_constant_velocity(params) :
        # x_final_position = x_initial_position \
        #                   + velocity_x_component * time
        try:
            return params['x_initial'] * \
                get_component_vectors( \
                    params['velocity_initial'], params['angle'])[0] \
                        * params['time']
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def velocity_with_no_acceleration(params) :
        # velocity_x_component = velocity_initial * cos(theta)
        try:
            return get_component_vectors( \
                params['velocity_initial'],params['angle'])[0]
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def displacement_with_non_constant_velocity(params) :
        # y_final_position = y_initial_position \
        #                   + velocity_y_component \
        #                   + (1/2)(acceleration)(time**2)
        try:
            y_velocity = get_component_vectors(\
                params['velocity_initial'], params['angle'])[1]
            return params['y_initial'] \
                + (y_velocity * params['time']) \
                    + (0.5 * params['acceleration'] * params['time']**2)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def velocity_with_constant_acceleration(params) :
        # velocity_y_final = velocity_y_initial + \
        #                   + acceleration * time
        try:
            return get_component_vectors(\
                params['velocity_initial'], params['angle'])[1] \
                    + (params['acceleration'] * params['time'])
        except Exception as e:
            print(e)
            return None
