__author__ = 'marcellovirzi'

# The class ListStat gives basic statistics information about the list provided


class NumberListStat(object):
    def __init__(self, list_of_numbers, weights=None):
        """ Initialize an instance.

        Optional arguments weights is used for calculating weighted_mean().
        """
        self.list_of_numbers = list_of_numbers
        self.weights = weights

    def get_list(self):
        """ Returns list of numbers."""
        return self.list_of_numbers

    def get_weights(self):
        """ Returns vector of weights."""
        return self.weights

    def sample_mean(self):
        """ Returns the sample mean as float number."""
        return sum(self.list_of_numbers) / float(len(self.list_of_numbers))

    def weighted_mean(self):
        """ Returns the weighted mean as float number"""
        if not self.weights:
            return self.sample_mean()
        else:
            if len(self.list_of_numbers) == len(self.weights):

                return sum([self.list_of_numbers[i] * self.weights[i] for i in range(len(self.list_of_numbers))])
            else:
                print("Different size of vectors. They must be equals !!")

    def median(self):
        """ Returns the median as float number."""
        sorted_list = sorted(self.list_of_numbers)

        if len(self.list_of_numbers) % 2 == 0:
            return float(0.5 * (sorted_list[int(len(sorted_list) / 2 - 1)] + sorted_list[int(len(sorted_list) / 2)]))
        else:
            return float(sorted_list[int(len(sorted_list) / 2)])

    def geom_mean(self):
        """ Returns geometric mean as float number."""
        factors = 1.0

        for i in self.list_of_numbers:
            factors *= (1 + i)

        return round(factors ** (1 / len(self.list_of_numbers)) - 1, 5)

    def harm_mean(self):
        """ Returns harmonic mean as float number."""
        denominator = float()

        for i in self.list_of_numbers:
            if i != 0:
                denominator += (1.0 / i)

        return round(float(len(self.list_of_numbers)) / denominator, 4)

    def simple_range(self):
        """ Returns the range as float number."""
        return float(max(self.list_of_numbers) - min(self.list_of_numbers))

    def mean_abs_dev(self):
        """ Returns the mean absolute deviation as float number."""
        mean = self.sample_mean()
        numerator = float()

        for i in self.list_of_numbers:
            numerator += abs(i - mean)

        return round(numerator / len(self.list_of_numbers), 5)

    def variance(self, typology='s'):
        """ Returns the population variance (sigma**2) as float number.

        Optional arguments typology specifies the type of variance: population 'p' or sample 's' (default 's')
        """
        mean = self.sample_mean()
        numerator = float()

        for i in self.list_of_numbers:
            numerator += (i - mean) ** 2

        if typology == 's':
            return round(numerator / (len(self.list_of_numbers) - 1), 5)
        else:
            return round(numerator / len(self.list_of_numbers), 5)

    def st_deviation(self, typology='s'):
        """ Returns the population standard deviation as float number.

        Optional arguments typology specifies the type of variance: population 'p' or sample 's' (default 's')
        """
        population_variance = self.variance(typology)

        return round(population_variance ** 0.5, 5)

    def coeff_var(self):
        """ Returns the coefficient of variation as float number."""
        return self.st_deviation() / self.sample_mean()

    def sharpe_ratio(self, p_return, risk_free, p_st_deviation):
        """ Returns the portfolio Sharpe Ratio.

        Keyword arguments:
        p_return -- portfolio return
        risk_free -- risk free return
        p_st_deviation -- standard deviation of portfolio return
        """
        return (p_return - risk_free) / p_st_deviation

    def s_skewness(self):
        """ Returns the sample skewness of the distribution"""
        mean = self.sample_mean()
        numerator = float()

        for i in self.list_of_numbers:
            numerator += (i - mean) ** 3

        return (1/len(self.list_of_numbers)) * (numerator / (self.st_deviation() ** 3))

    def s_kurtosis(self):
        """ Returns the sample kurtosis of the distribution."""
        mean = self.sample_mean()
        numerator = float()

        for i in self.list_of_numbers:
            numerator += (i - mean) ** 4

        return (1/len(self.list_of_numbers)) * (numerator / (self.st_deviation() ** 4))


#my_list = ListStatistics([i for i in range(10)])

#print(my_list.get_list())
#print(my_list.sample_mean())
#print(my_list.weighted_mean())
#print(my_list.median())
#print(my_list.geom_mean())
#print(my_list.harm_mean())
#print(my_list.simple_range())
#print(my_list.mean_abs_dev())
#print(my_list.variance())
#print(my_list.st_deviation())
#print(my_list.coeff_var())
#print(my_list.sharpe_ratio(my_list.weighted_mean([0.1 for i in range(10)]), 0.01, my_list.st_deviation()))
#print(my_list.s_skewness())
#print(my_list.s_kurtosis())
