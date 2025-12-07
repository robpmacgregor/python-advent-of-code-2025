def find_highest_digits_in_order(seq, number_of_digits):
    original_digits = list(map(lambda x: int(x), list(str(seq))))
    joltage = ''
    start_index = 0
    for _ in range(number_of_digits):
        digit_sub_set = original_digits[start_index:]
        sorted_digits = sorted(digit_sub_set, reverse=True)
        for digit in sorted_digits:
            max_usable_index = len(original_digits) - (number_of_digits - len(joltage))
            digit_index = digit_sub_set.index(digit)
            if digit_index <= max_usable_index:
                joltage += str(digit)
                start_index = digit_index + 1
                break

    return int(joltage)





    #
    # i = 0
    # joltage = ''
    # for _ in range(number_of_digits):
    #     digit_sub_set = digits[i:]
    #     max_digit = max(digit_sub_set)
    #     i = digit_sub_set.index(max_digit) + 1
    #     joltage += str(max_digit)
    # return int(joltage)