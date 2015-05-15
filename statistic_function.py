__author__ = 'marcellovirzi'

# Statistical concepts and market returns


def sum_value(list_of_numbers):
    """ Return the sum of all the value in the list.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        sum_of_values = float()

        # sum of the values of the sample
        for i in list_of_numbers:
            sum_of_values += i

        return sum_of_values


def sample_mean(list_of_numbers):
    """ Return the sample mean as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:

        return sum_value(list_of_numbers) / float(len(list_of_numbers))


def weighted_mean(list_of_numbers, weights):
    """ Return the weighted mean as float number

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    weights -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        if len(list_of_numbers) == len(weights):

            return sum_value([list_of_numbers[i] * weights[i] for i in range(len(list_of_numbers))])
        else:
            print("The size of both vectors must be equal !!")


def median(list_of_numbers):
    """ Return the median as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        sorted_list = sorted(list_of_numbers)

    if len(list_of_numbers) % 2 == 0:
        return 0.5 * (sorted_list[int(len(sorted_list) / 2 - 1)] + sorted_list[int(len(sorted_list) / 2)])
    else:
        return sorted_list[int(len(sorted_list) / 2)]


def geom_mean(list_of_numbers):
    """ Return geometric mean as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        factors = 1.0

        for i in list_of_numbers:
            factors *= (1 + i)

        return round(factors ** (1 / len(list_of_numbers)) - 1, 5)


def harm_mean(list_of_numbers):
    """ Return harmonic mean as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        denominator = float()

        for i in list_of_numbers:
            denominator += (1.0 / i)

        return round(float(len(list_of_numbers)) / denominator, 4)


def percentile_position(list_of_numbers, percentile):
    """ Return the position of the specified percentile as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    percentile -- int number
    """
    if list_of_numbers:

        return (float(len(list_of_numbers)) + 1) * percentile / 100


def simple_range(list_of_numbers):
    """ Return the range as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:

        return max(list_of_numbers) - min(list_of_numbers)


def mean_abs_dev(list_of_numbers):
    """ Return the mean absolute deviation as float number.

    Keyword arguments:
    list_of_numbers --  vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        mean = sample_mean(list_of_numbers)
        numerator = float()

        for i in list_of_numbers:
            numerator += abs(i - mean)

        return numerator / len(list_of_numbers)