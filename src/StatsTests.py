import unittest
from Statistics import Statistics
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_addition(self):
        test_Data = CsvReader('/src/UT_Addition.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']),int(row['Result']))

    def test_subtraction(self):
        test_Data1 = CsvReader('/src/UT_Subtraction.csv').data
        for row1 in test_Data1:
            self.assertEqual(self.calculator.subtract(row1['Value 1'], row1['Value 2']),int(row1['Result']))

    def test_multiply(self):
        test_Data = CsvReader('/src/UT_Multiply.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_division(self):
        test_Data = CsvReader('/src/UT_Division.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_square(self):
        test_Data = CsvReader('/src/UT_Square.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))

    def test_square(self):
        test_Data = CsvReader('/src/UT_SquareRoot.csv').data
        for row in test_Data:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), float(row['Result']))


def test_results_property(self):
    self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
