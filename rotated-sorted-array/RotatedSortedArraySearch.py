def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        return -1

    return binary_search_helper(input_list, number, 0, len(input_list) - 1)


def binary_search_helper(input_list, number_to_find, start, end):
    if start > end:
        return -1

    middle = (start + end) // 2

    if input_list[middle] == number_to_find:
        return middle

    if input_list[middle] <= input_list[end]:

        if input_list[middle] <= number_to_find <= input_list[end]:
            return binary_search_helper(input_list, number_to_find, middle + 1, end)
        else:
            return binary_search_helper(input_list, number_to_find, start, middle - 1)

    elif number_to_find >= input_list[middle] or number_to_find <= input_list[end]:
        return binary_search_helper(input_list, number_to_find, middle + 1, end)

    else:
        return binary_search_helper(input_list, number_to_find, start, middle - 1)
