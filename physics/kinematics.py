# ###################################### #
# ><><><><>< kinematic solver ><><><><>< #
# ###################################### #
import argparse
import physics.definitions
import json
import math
from pathlib import Path

parser = argparse.ArgumentParser(
    prog='kinematic_solver',
    description='Solver kinematic problems from intro Physics courses',
    add_help=True,
    epilog='Provide initial conditions in structured json file & produce answers!',
    allow_abbrev=True
)
parser.add_argument('-i', '--input', type=str, help='initial conditions json file', nargs=1)
parser.add_argument('--version', action='version', version=f'JV\'s Kinematic Solver v0.0.1')
args = parser.parse_args()

if __name__ == "__main__":
    print('''
    ><><><><>< kinematic solver ><><><><><
    ''')
    if args.input:
        file = Path(args.input[0])
        try:
            with open(file, 'r') as f:
                print(f'converting initial conditions from {file.name}')
                input = json.load(f)
        except Exception as e:
            print(e)

    # pretty_json = json.dumps(input, indent=4)
    # print(pretty_json)

    print('''
    ...Initializing given conditions...
    ''')
    env = physics.definitions.Definitions(
        v0=input['given']['initial_velocity'],
        vf=input['given']['final_velocity'],
        angle=input['given']['theta'],
        time=input['given']['time'],
        x0=input['given']['initial_x_position'],
        y0=input['given']['initial_y_position'],
        x=input['given']['x_position'],
        y=input['given']['y_position'],
        v0x=input['given']['initial_x_velocity'],
        v0y=input['given']['initial_y_velocity'],
        vfx=input['given']['final_x_velocity'],
        vfy=input['given']['final_y_velocity'],
        acceleration=input['given']['acceleration'],
        radians=input['given']['radians']
        )
    print('Done. Environment set.')

    solutions = []
    for k,v in input['solve'].items():
        if v:
            solutions.append(k)

    print(f'''
    Now we're ready to solve for {solutions}
    ''')

    if 'time_in_air' in solutions:
        print(f'time_in_air => {env.time_in_air()} s')

    if 'max_height' in solutions:
        print(f'max_height => {env.max_height()} meters')

    if 'x_displacement' in solutions:
        print(f'x_final_position => {env.x_pos()} meters')

    if 'y_displacement' in solutions:
        print(f'y_final_position => {env.y_pos()} meters')

    print('''
    Congratulations, you're done with homework.
    
    ><><><><>< now go outside ><><><><><
    ''')

    # TODO: brains that read given values, 
    # and calculate all possible base values.
    # TODO: can_calculate() -> checks for values
    # TODO: nested calculations for all branches
    # TODO: test cases using real hw problems