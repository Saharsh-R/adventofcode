# Day 17, Year 2024
# put example test cases here in 1.txt in the same folder
# by default is input.txt

import pytest

from utils.generic_functions import obtain_lines
import re


def get_int(s: str) -> tuple[int, int]:
    matches = re.findall(r"\d+", s)
    return [int(match) for match in matches]


def extract_data(day_input: list[str]):
    a = get_int(day_input[0])[0]
    b = get_int(day_input[1])[0]
    c = get_int(day_input[2])[0]
    program = get_int(day_input[4])
    return a, b, c, program


def test_extract_data():
    result = extract_data(obtain_lines("1"))
    assert result == (729, 0, 0, [0, 1, 5, 4, 3, 0])
    result = extract_data(obtain_lines())
    assert result == (35200350, 0, 0, [2, 4, 1, 2, 7, 5, 4, 7, 1, 3, 5, 5, 0, 3, 3, 0])


class Pro:
    def __init__(self, a:int,b:int,c:int, program: list[int]):
        self.a: int = a
        self.b: int=  b
        self.c :int= c
        self.output :list[int]= []
        self.i = 0
        self.program:list[int] = program

    def is_looking_good(self):
        if not self.output:
            return True
        if len(self.output) > len(self.program):
            return False
        i = len(self.output) -1
        return self.output[i] == self.program[i]

    def get_operand_value(self, operand: int):
        if operand in (0,1,2,3):
            return operand
        if operand == 4:
            return self.a
        if operand == 5:
            return self.b
        if operand == 6:
            return self.c
        assert False, f"Value is {operand}"
    def halt(self):
        while True:
            try:
                self.perform()
            except Exception as e:
                return
    def get_final(self):
        self.halt()
        return self.output




    def perform(self):

        opcode = self.program[self.i]
        if opcode == 0:
            combo_operand =self.get_operand_value( self.program[self.i + 1])
            result = self.a // (2 ** combo_operand)
            self.a = result

        elif opcode == 1:
            literal_operand =self.program[self.i + 1]
            self.b = self.b ^ literal_operand

        elif opcode == 2:
            combo_operand =self.get_operand_value( self.program[self.i + 1])
            self.b = combo_operand % 8

        elif opcode == 3:
            if self.a != 0:
                literal_operand =self.program[self.i + 1]
                self.i = literal_operand
                self.i -= 2

        elif opcode == 4:
            self.b = self.b ^ self.c

        elif opcode == 5:

            combo_operand =self.get_operand_value( self.program[self.i + 1])
            result = combo_operand % 8
            self.output.append(result)

        elif opcode == 6:
            combo_operand =self.get_operand_value( self.program[self.i + 1])
            self.b = self.a // (2 ** combo_operand)

        elif opcode == 7:
            combo_operand =self.get_operand_value( self.program[self.i + 1])
            self.c = self.a // (2 **combo_operand)
        else:
            assert False, f"unknown opcode {opcode}"

        self.i += 2

    def get_output(self):
        return ','.join([str(x) for x in self.output])

class TestExampleCases:
    def test_case1(self):
        case = Pro(0,0,9, [2, 6])
        case.perform()
        assert case.b == 1
    def test_case2(self):
        case = Pro(10,0,0, [5,0,5,1,5,4])
        case.perform()
        case.perform()
        case.perform()
        assert case.get_output() == '0,1,2'

    def test_case3(self):
        case = Pro(2024,0,0, [0,1,5,4,3,0])
        case.halt()
        assert case.a ==0
        assert case.get_output() == '4,2,5,6,7,7,7,7,3,1,0'


    def test_case4(self):
        case = Pro(0,29,0, [1,7])
        case.perform()
        assert case.b == 26

    def test_case5(self):
        case = Pro(0,2024 ,43690, [4,0])
        case.perform()
        assert case.b == 44354



def get_p1(day_input: list[str]):
    a,b,c,program = extract_data(day_input)
    pro = Pro(a,b,c,program)
    return pro.get_final()






@pytest.mark.parametrize(
    "day_input, output",
    [
        # (obtain_lines("1"), "4,6,3,5,6,3,5,2,1,0"),
        (obtain_lines(), '2,7,4,7,2,1,7,5,1'),
        # (obtain_lines('2'), '0,3,5,4,3,0'),
        # (obtain_lines('3'), '0,3,5,4,3,0'),
    ],
)
def test_d17_y2024_p1(day_input: list[str], output: str):
    assert get_p1(day_input) == output


def get_p2(day_input: list[str]):
    a,b,c,program = extract_data(day_input)
    todo = [(1, 0)]
    for i, x in todo:
        for a in range(x, x + 8):
            pro = Pro(a, 0, 0, program)
            if pro.get_final() == program[-i:]:
                todo.append((i + 1, a << 3))
                if len(program) == i:
                    return a




@pytest.mark.parametrize(
    "day_input, output",
    [
        (obtain_lines('2'), 117440),
        (obtain_lines(), 37221274271220),
    ],
)
def test_d17_y2024_p2(day_input: list[str], output: int):
    assert get_p2(day_input) == output
