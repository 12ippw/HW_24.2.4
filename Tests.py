import pytest

from Calculator import Calculator

class TestCalc:
    def setup(self):
        self.Calc = Calculator

    def test_adding(self):
        assert self.Calc.adding(self, 1 , 1) == 2

    def test_subtraction(self):
        assert self.Calc.subtraction(self, 5, 3) == 2

    def test_division(self):
        assert self.Calc.division(self, 6, 3) == 2

    def test_multiply(self):
        assert self.Calc.multiply(self, 2, 3) == 6

    def teardown(self):
        print("Выполнение метода TearDown")
