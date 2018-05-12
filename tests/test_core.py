# coding: utf-8

import unittest
from test.support import captured_stdout

from brainfuck import BrainFuck


class TestCore(unittest.TestCase):
    def test_hello_world(self):
        bf = BrainFuck()

        with captured_stdout() as stdout:
            bf.run()

        self.assertEqual(stdout.getvalue(), "Hello, world!\n")

    def test_fizzbuzz(self):
        bf = BrainFuck()

        bf.load_file("./tests/fizz_buzz.txt")

        with captured_stdout() as stdout:
            bf.run()

        fizzbuzz_list = list()
        for i in range(1, 101):
            if i % 15 == 0:
                fizzbuzz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzz_list.append("Fizz")
            elif i % 5 == 0:
                fizzbuzz_list.append("Buzz")
            else:
                fizzbuzz_list.append(str(i))
        fizzbuzz_list.append("\n")

        self.assertEqual(stdout.getvalue(), " ".join(fizzbuzz_list))

    def test_set_command(self):
        bf = BrainFuck()

        bf.set_command("にゃにゃ", "にゃー", "にゃっ", "にゃん",
                       "にゃ。", "にゃ、", "「", "」")
        bf.load_file("./tests/hello_world_nya.txt")

        with captured_stdout() as stdout:
            bf.run()

        self.assertEqual(stdout.getvalue(), "Hello, world!\n")


if __name__ == "__main__":
    unittest.main()
