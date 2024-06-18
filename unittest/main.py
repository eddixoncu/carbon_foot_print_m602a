import unittest


class Operations:
    def average(self, numbers: [float]):
        n = len(numbers)
        total = 0
        for number in numbers:
            total = total + number

        avg = total / n
        return avg


def division( dividend: float, divisor: float):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")

    return dividend / divisor





class TestOperations(unittest.TestCase):
    operation = Operations()

    def test_average(self):
        numbers = [1, 2, 6]
        self.assertEqual(self.operation.average(numbers), 3)

    def test_average_goes_wrong(self):
        numbers = [1, 2, 7]
        self.assertNotEqual(self.operation.average(numbers), 3)

    def test_division(self):
        self.assertEqual(division(10,5), 2)

    def test_division_wrong(self):
        self.assertNotEqual(division(10,5), 3)

    def test_division_by_zero_1(self):
        with self.assertRaises(ValueError):
            division(10,0)

    def test_division_by_zero_2(self):
        with self.assertRaises(ZeroDivisionError):
            division(10,0)


if __name__ == "__main__":
    unittest.main()
