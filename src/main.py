import sys
import os
import csv

from day_one.safe import Safe
from day_two.functions import inclusive_range_from_string, validate_id
from day_three.functions import find_highest_digits_in_order

args = sys.argv
DATA_DIR = os.path.join(os.getcwd(), 'data')

match args[1]:
    case 'day-one':
        input_file = 'day-one.txt'
        with open(os.path.join(DATA_DIR, input_file)) as file:
            movements = [line.rstrip() for line in file]

        safe = Safe(50)
        zero_position_sum = 0

        for movement in movements:
            _, zero_count = safe.rotate_dial(movement)
            zero_position_sum += zero_count

        print(f'The password is: {zero_position_sum}')

    case 'day-two':
        input_file = 'day-two.csv'
        with open(os.path.join(DATA_DIR, input_file)) as file:
            sum_of_invalid_ids = sum(
                [
                    product_id for product_id_ranges in csv.reader(file)
                        for product_id_range in product_id_ranges
                            for product_id in inclusive_range_from_string(product_id_range)
                            if not validate_id(product_id)
                ]
            )

        print(f'The sum of invalid product ids is: {sum_of_invalid_ids}')

    case 'day-three':
        input_file = 'day-three.txt'
        with open(os.path.join(DATA_DIR, input_file)) as file:
            total_joltage = sum([find_highest_digits_in_order(line.rstrip(),2) for line in file])
        print(f'The total joltage is: {total_joltage}')



