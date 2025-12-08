def find_highest_digits_in_order(seq, number_of_digits):
    original_digits = list(map(lambda x: int(x), list(str(seq))))
    joltage = ''
    start_index = 0
    for _ in range(number_of_digits):
        max_usable_index = len(original_digits) - (number_of_digits - len(joltage))
        digit_sub_set = original_digits[start_index:max_usable_index + 1]
        digit = max(digit_sub_set)
        joltage += str(digit)
        start_index += digit_sub_set.index(digit) + 1

    return int(joltage)
