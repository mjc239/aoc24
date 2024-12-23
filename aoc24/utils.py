from importlib import import_module
from datetime import datetime, date

# Import solution functions for each day
FUNCS = [
    getattr(import_module(f"aoc24.day{i}"), f"solve_day{i}_puzzle")
    for i in range(1, 26)
]


def read_input(day: int):
    with open(f"../data/day{day}.txt", "r") as f:
        filestring = f.read()

    return filestring


def solve_puzzle(day: int, user_input: str, part: int):
    if not 1 <= day <= 25:
        raise ValueError("day out bounds!")

    if day > len(FUNCS):
        raise NotImplementedError("Day not yet implemented!")

    now = datetime.now()
    if now.date() <= date(2024, 12, day):
        return {"solution": f"Can only access solution once day {day} is over!"}

    solve_func = FUNCS[day - 1]

    # If user_input is empty, read from file
    if not user_input:
        user_input = read_input(day)

    solution = solve_func(user_input, part=part)
    return solution
