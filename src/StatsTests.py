import unittest
from Statistics import Statistics
from CsvReader import CsvReader
from Stats.GetSample import getSample


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_getData(self):
        self.assertEqual(len(self.getData()),20)

    def test_getSample(self):
        data = getSample(self.getData(),10)
        self.assertEqual(len(data),10)

    def getData(self):
        test_Data = CsvReader('/src/Data/UT_SampleData.csv').data
        data = []
        for row in test_Data:
            data.append(row['Value'])
        return data


def test_results_property(self):
    self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
