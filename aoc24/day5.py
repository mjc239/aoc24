from collections import defaultdict
from itertools import combinations
from graphlib import TopologicalSorter


def parse_day5_input(user_input: str):
    """
    Function to parse the user input for Day 5.
    Args:
        user_input (str): The user input.
    Returns:

    """
    user_input = user_input.split("\n")

    lists = []
    orders = defaultdict(list)
    for line in user_input:
        if "|" in line:
            num1, num2 = line.split("|")
            orders[int(num1)].append(int(num2))
        elif line == "":
            continue
        else:
            lists.append([int(x) for x in line.split(",")])

    return lists, orders


def is_line_ordered(line: list[int], orders: dict[int, int]) -> bool:
    for num1, num2 in combinations(line, 2):
        if num1 in orders[num2]:
            return False
    return True


def solve_day5_puzzle_part1(user_input: str) -> int:
    """
    Function to solve part 1 of the puzzle for Day 5.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 1)
    """
    # Parse user input
    lines, orders = parse_day5_input(user_input)

    # Find the middle element of the sorted line
    total = 0
    for line in lines:
        if is_line_ordered(line, orders):
            total += line[len(line) // 2]
    return {"solution": total}


def solve_day5_puzzle_part2(user_input: str) -> int:
    """
    Function to solve part 1 of the puzzle for Day 5.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 2)
    """
    # Parse user input
    lines, orders = parse_day5_input(user_input)

    # Use topological sort to find the middle element of the sorted line
    total = 0
    for line in lines:
        if not is_line_ordered(line, orders):
            these_orders = {
                k: [i for i in v if i in line] for k, v in orders.items() if k in line
            }
            sorted_line = list(TopologicalSorter(these_orders).static_order())[::-1]
            total += sorted_line[len(sorted_line) // 2]

    return {"solution": total}


def solve_day5_puzzle(user_input: str, part: int) -> int:
    """
    Function to solve the puzzle for Day 5.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        int: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day5_puzzle_part1(user_input)
    elif part == 2:
        return solve_day5_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
