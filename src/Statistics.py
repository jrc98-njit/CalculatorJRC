from random import random
from Calculator import Calculator
from Stats.Mean import mean
from Stats.Median import median
from Stats.Variance import variance
from Stats.StandardDeviation import standardDeviation
from Calc.Addition import addition
from Calc.Division import division
from Stats.GetSample import getSample
from Stats.Mode import mode

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def standard_deviation(self, a):
        self.result = standardDeviation(a)
        return self.result

    def variance(self, a):
        self.result = variance(a)
        return self.result

    def mode(self, a):
        self.result = mode(a)
        return self.result

    def sample_mean(data, sample_size):
        total = 0
        #check that sample size is not 0
        if (sample_size <= 0):
            raise Exception('sample size should be > 0. The value of sample_size was: {}'.format(sample_size))
        #check that sample size is not larger than the population
        if (sample_size > len(data)):
            raise Exception('sample size should not be larger than the popuation. The value of sample_size was: {}'.format(sample_size))

        sample = getSample(data, sample_size)
        num_values = len(sample)
        #check that get sample returns the proper number of samples
        if (num_values != sample_size):
            raise Exception('unexpected error: sample size is not the same size as length of sample')

        for num in sample:
            total = addition(total, num)
        return division(total, num_values)

