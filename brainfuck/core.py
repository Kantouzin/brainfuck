# coding: utf-8

from typing import Dict


class BrainFuck:
    """
    Brainfuck interpreter class

    Commands:
        ">" :
            Increment the data pointer.
        "<" :
            Decrement the data pointer.
        "+" :
            Increment the byte at the data pointer.
        "-" :
            Decrement the byte at the data pointer.
        "." :
            Output the byte at the data pointer.
        "," :
            Accept one byte of input, storing its value in the byte at the data pointer.
        "[" :
            If the byte at the data pointer is zero,
            then instead of moving the instruction pointer forward to the next command,
            jump it forward to the command after the matching ] command.
        "]" :
            If the byte at the data pointer is nonzero,
            then instead of moving the instruction pointer forward to the next command,
            jump it back to the command after the matching [ command.

    Attributes
    ----------
    _tape : str
        String storing the program
    _command_dict : dict
        Dictionary for replacing eight commands with another string
    _jump_dict : dict
        Dictionary of program counter corresponding to commands of "[" and "]"
    """

    def __init__(self) -> None:
        # Hello, world!
        self._tape = """
            +++++++++[>++++++++>+++++++++++>+++++<<<-]>.>++.+++++++..+
            ++.>-.------------.<++++++++.--------.+++.------.--------.>+.
        """

        self._command_dict = {
            ">": ">", "<": "<", "+": "+", "-": "-", ".": ".", ",": ",", "[": "[", "]": "]"
        }

        self._jump_dict = dict()

    def run(self) -> None:
        """
        Run brainfuck.
        """
        self._jump_dict = self._generate_jump_dict()

        memory = [0 for _ in range(1000)]
        pc = 0
        ptr = 0

        while pc < len(self._tape):
            inst_index = float("inf")
            selected_inst = None

            for inst in self._command_dict.values():
                tmp_inst_index = self._tape[pc:].find(inst)

                if tmp_inst_index == -1:
                    continue

                if tmp_inst_index < inst_index:
                    inst_index = tmp_inst_index
                    selected_inst = inst

            if selected_inst is None:
                break

            inst = None
            for key, value in self._command_dict.items():
                if selected_inst == value:
                    inst = key

            if inst is None:
                break

            if inst == ">":
                ptr += 1

            elif inst == "<":
                ptr -= 1
                if ptr < 0:
                    raise ValueError("error !")

            elif inst == "+":
                memory[ptr] += 1

            elif inst == "-":
                memory[ptr] -= 1

            elif inst == ".":
                print(chr(memory[ptr]), end="")

            elif inst == ",":
                memory[ptr] = int(input())

            elif inst == "[":
                if memory[ptr] == 0:
                    pc = self._jump_dict[pc]

            elif inst == "]":
                if memory[ptr] != 0:
                    pc = self._jump_dict[pc]

            pc += inst_index + len(selected_inst)

        print()

    def _generate_jump_dict(self) -> Dict[str, str]:
        """
        Generate the dictionary of program counter corresponding to commands of "[" and "]".

        Returns
        -------
        jump_dict : dict
            Dictionary of program counter corresponding to commands of "[" and "]"
        """
        jump_dict = dict()
        left_index_list = list()

        tape_index = 0
        while tape_index < len(self._tape):
            inst_index = float("inf")
            selected_inst = None

            for inst in ["[", "]"]:
                tmp_inst_index = self._tape[tape_index:].find(self._command_dict[inst])

                if tmp_inst_index == -1:
                    continue

                if tmp_inst_index < inst_index:
                    inst_index = tmp_inst_index
                    selected_inst = inst

            if selected_inst is None:
                break

            tape_index += inst_index

            if selected_inst == '[':
                left_index_list.append(tape_index)
            elif selected_inst == ']':
                if not left_index_list:
                    raise RuntimeError("There are too many \"]\"")

                left_index = left_index_list.pop()
                right_index = tape_index

                jump_dict[left_index] = right_index
                jump_dict[right_index] = left_index

            tape_index += 1

        if left_index_list:
            raise RuntimeError("There are too many \"[\"")

        return jump_dict

    def load_file(self, filepath: str) -> None:
        """
        Load brainfuck code.

        Parameters
        ----------
        filepath : str
            Path of file that brainfuck code is described
        """
        with open(filepath, mode="r", encoding="utf-8") as f:
            self._tape = f.read()

    def set_command(self, plus: str, minus: str, greater_than: str, less_than: str,
                    dot: str, comma: str, left_bracket: str, right_bracket: str) -> None:
        """
        Set eight commands of brainfuck.

        Parameters
        ----------
        greater_than : str
            Commands corresponding to ">"
        less_than : str
            Commands corresponding to "<"
        plus : str
            Commands corresponding to "+"
        minus : str
            Commands corresponding to "-"
        dot : str
            Commands corresponding to "."
        comma : str
            Commands corresponding to ","
        left_bracket : str
            Commands corresponding to "["
        right_bracket : str
            Commands corresponding to "]"
        """
        self._command_dict["+"] = plus
        self._command_dict["-"] = minus
        self._command_dict[">"] = greater_than
        self._command_dict["<"] = less_than
        self._command_dict["."] = dot
        self._command_dict[","] = comma
        self._command_dict["["] = left_bracket
        self._command_dict["]"] = right_bracket
