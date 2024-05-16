from calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_sub(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_mul(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result == expected

    def test_div(self):
        # arrange
        a = 1234
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 617
        assert result == expected

    # def test_div_0(self):
    #     # arrange
    #     a = 1234
    #     b = 0
    #     cal = Calculator()

    #     # act
    #     with pytest.raises(ZeroDivisionError) as exc_info:
    #         cal.divide(a, b)
    
    #     # Check the error message if needed
    #     assert str(exc_info.value) == "Division by zero error"