def sort_012(input_list):
    if len(input_list) <= 0:
        return input_list

    zero_index = 0
    index = 0
    two_index = len(input_list) - 1

    while zero_index <= two_index:
        if input_list[two_index] == 2:
            two_index -= 1
            continue

        if input_list[zero_index] == 0:
            input_list[zero_index] = input_list[index]
            input_list[index] = 0

            zero_index += 1
            index += 1

        elif input_list[zero_index] == 2:
            input_list[zero_index] = input_list[two_index]
            input_list[two_index] = 2

            two_index -= 1

        else:
            zero_index += 1

    return input_list
