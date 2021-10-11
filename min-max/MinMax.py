def get_min_max(ints):
    if ints is None or len(ints) == 0:
        raise ValueError("Could not extract minimum and maximum from empty array")

    if len(ints) == 1:
        return ints[0], ints[0]

    minimum = ints[0]
    maximum = ints[0]

    for number in ints[1:]:
        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number

    return minimum, maximum
