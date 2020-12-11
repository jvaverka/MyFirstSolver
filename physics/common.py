# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import math

def quadratic(a, b, c) :
    # Solve quadratic equation.
    pos = (-b + math.sqrt(b**2 - (4 * a * c))) / (2*a)
    neg = (-b - math.sqrt(b**2 - (4 * a * c))) / (2*a)
    return pos, neg

def get_component_vectors(magnitude, direction) :
    # Break a given vector down into its 2D components.
    # Note: direction measured as degrees above horizontal.
    x_component = magnitude * math.cos(math.radians(direction))
    y_component = magnitude * math.sin(math.radians(direction))
    return x_component, y_component

def get_resultant_vector(x_magnitude, y_magnitude) :
    # Given a vector's 2D components, find the resultant vector.
    # Note: direction measured as degrees above horizontal.
    r_magnitude = math.sqrt(x_magnitude**2 + y_magnitude**2)
    r_direction = math.degrees(math.atan(abs(y_magnitude) / abs(x_magnitude)))
    return r_magnitude, r_direction