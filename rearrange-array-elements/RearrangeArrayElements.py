def rearrange_digits(input_list):
    if len(input_list) == 0:
        return 0, 0

    if len(input_list) == 1:
        return input_list[0], 0

    number_frequencies = [0 for _ in range(10)]

    for number in input_list:
        number_frequencies[number] += 1

    first_number, second_number = 0, 0
    is_first = True

    for number in range(10):
        while number_frequencies[9 - number] > 0:

            if is_first:
                first_number *= 10
                first_number += 9 - number
                is_first = False

            else:
                second_number *= 10
                second_number += 9 - number
                is_first = True

            number_frequencies[9 - number] -= 1

    return first_number, second_number
