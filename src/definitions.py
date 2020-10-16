# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import math

def can_solve(needed, params) :
    for item in needed :
        if not item in params :
            print(f'Missing parameter, {item}!')
            return False
    return True

def displacement_with_constant_velocity(params) :
    needed = ['x0', 'v0', 't']
    if not can_solve(needed, params) :
        return None
    return params['x0'] + params['v0']*params['t']

def velocity_with_acc_and_time(params) :
    needed = ['v0', 'a', 't']
    if not can_solve(needed, params) :
        return None
    return params['v0'] + params['a']*params['t']

def displacement_with_acc_and_time(params) :
    needed = ['x0', 'v0', 't', 'a']
    if not can_solve(needed, params) :
        return None
    return params['x0'] + params['v0']*params['t'] + 0.5*params['a']*params['t']**2

def velocity_with_displacement(params) :
    needed = ['v0', 'a', 'xf', 'x0']
    if not can_solve(needed, params) :
        return None
    return math.sqrt(params['v0']**2 + 2*params['a']*(params['xf']-params['x0']))

class Definitions:
    
    def __init__(self, v0:float, vf:float,
                angle:float, time:float,
                x:float, y:float,
                v0x:float, v0y:float,
                vfx:float, vfy:float,
                acceleration:float,
                x0=0, y0=0, radians=False):
        # knowns
        self.x0 = x0
        self.y0 = y0
        self.g = -9.8
        self.radians = radians
        # unknowns
        self.v0 = v0
        self.vf = vf
        if angle:
            if self.radians:
                self.ang = math.degrees(angle)
            else:
                self.ang = angle
        # optionals
        if time:
            self.t = time
        if x:
            self.x = x
        if y:
            self.y = y
        if v0x:
            self.v0x = v0x
        if v0y:
            self.v0y = v0y
        if vfx:
            self.vfx = vfx
        if vfy:
            self.vfy = vfy
        if acceleration:
            self.acc = acceleration

    # TOOLBOX 1
    def x_pos(self):
        if not hasattr(self,'v0') or not hasattr(self,'ang') or not hasattr(self,'t'):
            return 'sorry, not enough info given'
        # x = v0*cos(theta)*time
        return self.v0 * math.cos(self.ang) * self.t

    # TOOLBOX 2
    def x_vel(self):
        if not hasattr(self,'v0') or not hasattr(self,'ang'):
            return 'sorry, not enough info given'
        # vx = v0*cos(theta)
        return self.v0 * math.cos(self.ang)

    # TOOLBOX 3
    def y_pos(self):
        if not hasattr(self,'t') or not hasattr(self,'v0') or not hasattr(self,'ang') or not hasattr(self,'y0'):
            return 'sorry, not enough info given'
        # y = 1/2*g*t^2 + v0*sin(theta)*t + y0
        return (0.5 * self.g * self.t**2) + (self.v0 * math.sin(math.radians(self.ang)) * self.t) + self.y0

    # TOOLBOX 4
    def y_vel(self):
        if not hasattr(self,'v0') or not hasattr(self,'ang') or not hasattr(self,'t'):
            return 'sorry, not enough info given'
        # vy = v0*sin(theta) + g*t
        return (self.v0 * math.sin(self.ang)) + (self.g * self.t)

    # ORIGINAL 1
    def xf_pos(self):
        if not hasattr(self,'x0') or not hasattr(self,'v0x') or not hasattr(self,'t'):
            return 'sorry, not enough info given'
        # x = x0 + v0*t
        return self.x0 + (self.v0x * self.t)

    # ORIGINAL 2
    def delta_v(self):
        if not hasattr(self,'v0') or not hasattr(self,'acc') or not hasattr(self,'t'):
            return 'sorry, not enough info given'
        # vf = v0 + at
        return self.v0 + (self.acc * self.t)

    # ORIGINAL 3
    def xf_pos_w_acc(self):
        if not hasattr(self,'x0') or not hasattr(self,'v0') or not hasattr(self,'t') or not hasattr(self,'acc'):
            return 'sorry, not enough info given'
        # xf = x0 + v0*t + 1/2*a*t^2
        return self.x0 + (self.v0 * self.t) + (0.5 * self.acc * self.t**2)

    # ORIGINAL 4
    def delta_x(self):
        if not hasattr(self,'vf') or not hasattr(self,'v0') or not hasattr(self,'acc'):
            return 'sorry, not enough info given'
        # vf**2 = v0**2 + 2a(xf-x0)
        return ((self.vf**2 - self.v0**2) / (2 * self.acc))

    def find_time(self):
        pass

    def time_in_air(self):
        if hasattr(self,'vf') and hasattr(self,'v0') and hasattr(self,'g') and not hasattr(self,'t'):
            self.t = (self.vf - self.v0*math.sin(math.radians(self.ang))) / self.g
            return self.t
        else:
            self.t = 0
            return self.t

    def max_height(self):
         return self.y_pos()
