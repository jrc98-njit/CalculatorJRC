from Calculator import Calculator
from Stats.Mean import mean
from Stats.Median import median

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





