from __future__ import print_function, division
import numpy as np
import datetime
import matplotlib.pylab as plt
import matplotlib.mlab as mlab


def count_larger(the_list, num):
    return sum(np.asarray(the_list) > num)


def sum_square_difference(num):
    square_of_sums = sum(range(1, num+1))**2
    sum_of_squares = sum(np.asarray(range(1, num+1))**2)

    return square_of_sums - sum_of_squares


def middle_of_elements(elements):
    new_arr = []
    for i in range(1, len(elements)):
        new_arr.append((elements[i-1] + elements[i]) / 2.0)
    return new_arr


def is_friday_13(d):
    return d.isoweekday() == 5 and d.day == 13


def get_fridays_13():
    base = datetime.datetime.now().date()
    ten_years_earlier = datetime.date(base.year-10, base.month, base.day)
    day_diff = base - ten_years_earlier
    date_list = [base - datetime.timedelta(days=x)
                 for x in range(0, day_diff.days)]
    vec = np.vectorize(is_friday_13)
    return np.asarray(date_list)[vec(date_list)]


def random_num():
    numbers = np.random.randn(10000)
    numbers.sort()
    plt.hist(numbers, bins=100,normed=True)
    plt.plot(numbers, mlab.normpdf(numbers, np.mean(numbers), np.std(numbers)))
    plt.show()


"""
    bin_array = np.arange(min(numbers), max(numbers), (max(numbers) - min(numbers)) / 99)

    bin_values = []
    prev_sum = 0
    for i in range(0, 99):
        s = sum(np.where(np.sort(numbers) < bin_array[i])[0])
        bin_values.append(s - prev_sum)
        prev_sum = s

    plt.plot(bin_array, bin_values)
    plt.show()
"""

def creative():
    matrix = np.zeros((10, 10))
    matrix[1:2, 1:2] = 1
    matrix[1:2, -2:-1] = 1

    matrix[4:6, 4:6] = 1

    matrix[-2:-1, 1:-1] = 1

    plt.spy(matrix)
    plt.show()

random_num()