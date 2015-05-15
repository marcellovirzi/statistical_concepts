__author__ = 'marcellovirzi'

# Statistical concepts and market returns


def sum_value(list_of_numbers):
    """ Returns the sum of all the value in the list.

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
    """ Returns the sample mean as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:

        return sum_value(list_of_numbers) / float(len(list_of_numbers))


def weighted_mean(list_of_numbers, weights):
    """ Returns the weighted mean as float number

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
    """ Returns the median as float number.

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
    """ Returns geometric mean as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        factors = 1.0

        for i in list_of_numbers:
            factors *= (1 + i)

        return round(factors ** (1 / len(list_of_numbers)) - 1, 5)


def harm_mean(list_of_numbers):
    """ Returns harmonic mean as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        denominator = float()

        for i in list_of_numbers:
            denominator += (1.0 / i)

        return round(float(len(list_of_numbers)) / denominator, 4)


def percentile_position(list_of_numbers, percentile):
    """ Returns the position of the specified percentile as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    percentile -- int number
    """
    if list_of_numbers:

        return (float(len(list_of_numbers)) + 1) * percentile / 100


def simple_range(list_of_numbers):
    """ Returns the range as float number.

    Keyword arguments:
    list_of_numbers -- vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:

        return max(list_of_numbers) - min(list_of_numbers)


def mean_abs_dev(list_of_numbers):
    """ Returns the mean absolute deviation as float number.

    Keyword arguments:
    list_of_numbers --  vectors 1 x n of both int and float numbers
    """
    if list_of_numbers:
        mean = sample_mean(list_of_numbers)
        numerator = float()

        for i in list_of_numbers:
            numerator += abs(i - mean)

        return round(numerator / len(list_of_numbers), 5)


def variance(list_of_numbers, typology='s'):
    """ Returns the population variance, sigma**2 as float number.

    Keyword arguments:
    list_of_numbers --  vectors 1 x n of both int and float numbers
    typology -- specify the type of variance: population 'p' or sample 's' (default 's')
    """
    if list_of_numbers:
        mean = sample_mean(list_of_numbers)
        numerator = float()

        for i in list_of_numbers:
            numerator += (i - mean) ** 2

        if typology == 's':
            return round(numerator / (len(list_of_numbers) - 1), 5)
        else:
            return round(numerator / len(list_of_numbers), 5)


def st_deviation(list_of_numbers, typology='s'):
    """ Returns the population standard deviation as float number.

    Keyword arguments:
    list_of_numbers --  vectors 1 x n of both int and float numbers
    typology -- specify the type of variance, population 'p' or sample 's' (default 's')
    """
    if list_of_numbers:
        population_variance = variance(list_of_numbers, typology)

        return round(population_variance ** 0.5, 5)


def chebyshev_ineq(k):
    """ Returns the minimum percentage of any distribution that will lie within +-(k) st dev.

    Keyword arguments:
    k -- standard deviation as float number
    """
    if k:
        return 1 - (1 / k) ** 2


def coeff_var(standard_deviation, mean):
    """ Returns the coefficient of variation as float number.

    Keyword arguments:
    standard_deviation -- standard deviation
    mean -- mean
    """
    if standard_deviation and mean:
        return standard_deviation / mean


def sharpe_ratio(p_return, risk_free, p_st_deviation):
    """ Returns the portfolio Sharpe Ratio.

    Keyword arguments:
    p_return -- portfolio return
    risk_free -- risk free return
    p_st_deviation -- standard deviation of portfolio return
    """
    if p_return and risk_free and p_st_deviation:
        return (p_return - risk_free) / p_st_deviation


def s_skewness(list_of_numbers, s_st_deviation):
    """ Returns the sample skewness of the distribution

    Keyword arguments:
    list_of_numbers --  vectors 1 x n of both int and float numbers
    s_st_deviation -- sample standard deviation
    """
    if list_of_numbers and s_st_deviation:
        mean = sample_mean(list_of_numbers)
        numerator = float()

        for i in list_of_numbers:
            numerator += (i - mean) ** 3

        return (1/len(list_of_numbers)) * (numerator / (s_st_deviation ** 3))


def s_kurtosis(list_of_numbers, s_st_deviation):
    """ Returns the sample kurtosis of the distribution.

    Keyword arguments:
    list_of_numbers --  vectors 1 x n of both int and float numbers
    s_st_deviation -- sample standard deviation
    """
    if list_of_numbers and s_st_deviation:
        mean = sample_mean(list_of_numbers)
        numerator = float()

        for i in list_of_numbers:
            numerator += (i - mean) ** 4

        return (1/len(list_of_numbers)) * (numerator / (s_st_deviation ** 4))
