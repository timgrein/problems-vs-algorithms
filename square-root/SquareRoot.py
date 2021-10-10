
def sqrt(number):
    if number is None:
        raise ValueError("Can not compute square root of None value")

    if number < 0:
        raise ValueError("The square root of a negative number does not exist among the set of real numbers.")

    if number < 2:
        return number

    result = 0

    start = 1
    end = number // 2

    while start <= end:

        mid = (start + end) // 2
        square = mid * mid

        if square == number:
            return mid

        elif square > number:
            end = mid - 1

        else:
            start = mid + 1
            result = mid

    return result
