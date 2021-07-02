import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add)
        self.assertEqual(self.calculator.result)





if __name__ == '__main__':
    unittest.main()
