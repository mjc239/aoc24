from aoc24.day1 import solve_day1_puzzle
from aoc24.day2 import solve_day2_puzzle
from aoc24.day3 import solve_day3_puzzle
from aoc24.day4 import solve_day4_puzzle
from aoc24.day5 import solve_day5_puzzle
from aoc24.day6 import solve_day6_puzzle
from aoc24.day7 import solve_day7_puzzle
from aoc24.day8 import solve_day8_puzzle
from aoc24.day9 import solve_day9_puzzle
from aoc24.day10 import solve_day10_puzzle
from aoc24.day11 import solve_day11_puzzle
from aoc24.day12 import solve_day12_puzzle
from aoc24.day13 import solve_day13_puzzle
from aoc24.day14 import solve_day14_puzzle
from aoc24.day15 import solve_day15_puzzle
from aoc24.day16 import solve_day16_puzzle
from aoc24.day17 import solve_day17_puzzle
from aoc24.day18 import solve_day18_puzzle
from aoc24.day19 import solve_day19_puzzle
from aoc24.day20 import solve_day20_puzzle
from aoc24.day21 import solve_day21_puzzle
from aoc24.day22 import solve_day22_puzzle
from aoc24.day23 import solve_day23_puzzle
from aoc24.day24 import solve_day24_puzzle
from aoc24.day25 import solve_day25_puzzle
from datetime import datetime, date

FUNCS = [
    solve_day1_puzzle,
    solve_day2_puzzle,
    solve_day3_puzzle,
    solve_day4_puzzle,
    solve_day5_puzzle,
    solve_day6_puzzle,
    solve_day7_puzzle,
    solve_day8_puzzle,
    solve_day9_puzzle,
    solve_day10_puzzle,
    solve_day11_puzzle,
    solve_day12_puzzle,
    solve_day13_puzzle,
    solve_day14_puzzle,
    solve_day15_puzzle,
    solve_day16_puzzle,
    solve_day17_puzzle,
    solve_day18_puzzle,
    solve_day19_puzzle,
    solve_day20_puzzle,
    solve_day21_puzzle,
    solve_day22_puzzle,
    solve_day23_puzzle,
    solve_day24_puzzle,
    solve_day25_puzzle,
]


def read_input(day: int):
    with open(f"../data/day{day}.txt", "r") as f:
        filestring = f.read()

    return filestring.split("\n")


def solve_puzzle(day: int, user_input: str, part: int):
    if not 1 <= day <= 25:
        raise ValueError("day out bounds!")

    if day > len(FUNCS):
        raise NotImplementedError("Day not yet implemented!")

    now = datetime.now()
    if now.date() <= date(2024, 12, day):
        return f"Can only access solution once day {day} is over!"

    solve_func = FUNCS[day - 1]

    # If user_input is empty, read from file
    if not user_input:
        user_input = read_input(day)

    id
    solution = solve_func(user_input, part=part)
    return solution
