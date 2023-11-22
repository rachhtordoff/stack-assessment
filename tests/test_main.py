import unittest
from src.main import process_command

class TestStackOperators(unittest.TestCase):
    def test_addition(self):
        stack = [5, 3, 8, 6]
        process_command('+', stack)
        self.assertEqual(stack, [5, 3, 14])

    def test_subtract(self):
        stack = [5, 3, 8, 6]
        process_command('-', stack)
        self.assertEqual(stack, [5, 3, 2])

    def test_multiply(self):
        stack = [5, 3, 8, 6]
        process_command('*', stack)
        self.assertEqual(stack, [5, 3, 48])

    def test_divide(self):
        stack = [5, 3, 12, 6]
        process_command('/', stack)
        self.assertEqual(stack, [5, 3, 2])

class TestStackCommands(unittest.TestCase):
    def test_push(self):
        stack = [5, 3, 12, 6]
        process_command('PUSH 1', stack)
        self.assertEqual(stack, [5, 3, 12, 6, 1])

    def test_pop(self):
        stack = [5, 3, 12, 6]
        process_command('POP', stack)
        self.assertEqual(stack, [5, 3, 12])

    def test_swap(self):
        stack = [5, 3, 12, 6]
        process_command('SWAP', stack)
        self.assertEqual(stack, [5, 3, 6, 12])

    def test_dup(self):
        stack = [5, 3, 12, 6]
        process_command('DUP', stack)
        self.assertEqual(stack, [5, 3, 12, 6, 6])

if __name__ == '__main__':
    unittest.main()
