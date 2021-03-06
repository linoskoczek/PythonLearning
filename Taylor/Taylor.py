from cmath import sin, pi
from math import radians
from random import random


def approximation_error(x, x0):
    if x0 == 0:
        return x * 100
    return abs((x - x0) / x0) * 100


def convert_num_if_needed(given_input, given_option):
    if given_option == '1':
        return decrease_radian_value(given_input)
    elif given_option == '2':
        return radians(decrease_degree_value(given_input))
    else:
        raise ValueError('Wrong option given!')


def decrease_radian_value(rad):
    return rad % (2*pi)


def decrease_degree_value(deg):
    return deg % 180


def reduce_to_pi_by_two(x):
    if x <= pi:  # positive values
        if x < pi / 2:
            return x
        else:
            return pi - x
    else:  # negative values
        if x <= 3 * pi / 2:
            return -(x - pi)
        else:
            return -(2 * pi - x)


def taylor_sin(x, iter_number):
    x = reduce_to_pi_by_two(x)
    square = x
    factorial = 1
    result = 0
    for i in range(0, iter_number):
        factorial = factorial * (i * 2 + 1)
        if i != 0:
            factorial *= i * 2
        if i % 2 == 0:
            result += square / factorial
        else:
            result -= square / factorial
        square = square * x * x

    return result


def test_radians():
    for i in range(100):
        x = decrease_radian_value(random() * 1000)
        val1 = taylor_sin(x, 7)
        val2 = sin(x)
        error = approximation_error(val1, val2)
        # print("For", x, "error is equal to", approximation_error(val1, val2))
        assert error < 0.01
    print("Radians test finished")


def test_degrees():
    for i in range(100):
        x = radians(decrease_degree_value(random() * 1000))
        val1 = taylor_sin(x, 7)
        val2 = sin(x)
        error = approximation_error(val1, val2)
        # print("For", x, "error is equal to", approximation_error(val1, val2))
        assert error < 0.01
    print("Degrees test finished")


def app():
    option = input("Please choose - (1) Radians, (2) Degrees:\n")
    input_x = float(input("Please give X:\n"))
    input_x = convert_num_if_needed(input_x, option)
    iterations = int(input("Please tell how many taylor iterations you want to make:"))

    taylor_result = taylor_sin(input_x, iterations)
    native_sin = sin(input_x)
    print("Calculation of sin(", input_x, ") gave result:", taylor_result)
    print("Result of native sin(", input_x, ")", native_sin)
    print("Approximation error compared to native sin :", '%f' % approximation_error(taylor_result, native_sin), '%')


test_degrees()
test_radians()
app()
