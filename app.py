import unittest

# Function with intentional bug
def add(a, b):
    return a - b   # ❌ BUG (should be +)

# Test cases
class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
