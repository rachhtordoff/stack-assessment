import unittest
from src.main import process_command


class TestStackOperators(unittest.TestCase):
    def test_operators_pass(self):
        stack = [5, 3, 8, 6]
        process_command('+', stack)
        self.assertEqual(stack, [5, 3, 14])

        stack = [5, 3, 8, 6]
        process_command('-', stack)
        self.assertEqual(stack, [5, 3, 2])

        stack = [5, 3, 8, 6]
        process_command('*', stack)
        self.assertEqual(stack, [5, 3, 48])

        stack = [5, 3, 12, 6]
        process_command('/', stack)
        self.assertEqual(stack, [5, 3, 2])

    def test_operators_fail(self):
        stack = [5, 3, 8, 6]
        process_command('+', stack)
        self.assertNotEqual(stack, [5, 3, 8, 6])

        stack = [5, 3, 8, 6]
        process_command('-', stack)
        self.assertNotEqual(stack, [5, 3, 8, 6])

        stack = [5, 3, 8, 6]
        process_command('*', stack)
        self.assertNotEqual(stack, [5, 3, 8, 6])

        stack = [5, 3, 8, 6]
        process_command('/', stack)
        self.assertNotEqual(stack, [5, 3, 8, 6])


class TestStackCommands(unittest.TestCase):
    def test_commands_pass(self):
        stack = [5, 3, 12, 6]
        process_command('PUSH 1', stack)
        self.assertEqual(stack, [5, 3, 12, 6, 1])

        stack = [5, 3, 12, 6]
        process_command('POP', stack)
        self.assertEqual(stack, [5, 3, 12])

        stack = [5, 3, 12, 6]
        process_command('SWAP', stack)
        self.assertEqual(stack, [5, 3, 6, 12])

        stack = [5, 3, 12, 6]
        process_command('DUP', stack)
        self.assertEqual(stack, [5, 3, 12, 6, 6])

    def test_commands_fail(self):
        stack = [5, 3, 12, 6]
        process_command('PUSH 1', stack)
        self.assertNotEqual(stack, [5, 3, 12, 6])

        stack = [5, 3, 12, 6]
        process_command('POP', stack)
        self.assertNotEqual(stack, [5, 3, 12, 6])

        stack = [5, 3, 12, 6]
        process_command('SWAP', stack)
        self.assertNotEqual(stack, [5, 3, 12, 6])

        stack = [5, 3, 12, 6]
        process_command('DUP', stack)
        self.assertNotEqual(stack, [5, 3, 12, 6])


if __name__ == '__main__':
    unittest.main()
