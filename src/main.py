import sys
import os

from day_one.safe import Safe

args = sys.argv
DATA_DIR = os.path.join(os.getcwd(), 'data')

match args[1]:
    case "day-one":
        input_file = 'day-one.txt'
        with open(os.path.join(DATA_DIR, input_file)) as file:
            movements = [line.rstrip() for line in file]

        safe = Safe(50)
        zero_position_count = 0
        counter = 1

        for movement in movements:
            zero_position_count += 1 if safe.rotate_dial(movement) == 0 else 0

        print(f'The password is: {zero_position_count}')
