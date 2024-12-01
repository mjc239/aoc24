from aoc24.day1 import solve_day1_puzzle
from aoc24.day2 import solve_day2_puzzle

FUNCS = [solve_day1_puzzle, solve_day2_puzzle]


def read_input(day: int):
    with open(f"../data/day{day}.txt", "r") as f:
        filestring = f.read()

    return filestring.split("\n")


def solve_puzzle(day: int, user_input: str):
    if not 1 <= day <= 25:
        raise ValueError("day out bounds!")

    if day > len(FUNCS):
        raise NotImplementedError("Day not yet implemented!")

    solve_func = FUNCS[day - 1]

    # If user_input is empty, read from file
    if not user_input:
        user_input = read_input(day)
    else:
        user_input = user_input.split("\n")

    solution = solve_func(user_input)
    return solution
