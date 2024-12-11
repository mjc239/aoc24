from functools import cache


def parse_day11_input(user_input: str) -> list[int]:
    """
    Function to parse the user input for Day 11.
    Args:
        user_input (str): The user input.
    Returns:
        list[int]: The parsed user input.
    """
    return [int(x) for x in user_input.split(" ")]


@cache
def num_stones(n: int, steps: int) -> int:
    """Compute the number of stones after a given number of steps, starting
    with a single stone with the number n on it.

    Args:
        n (int): Starting number on the stone.
        steps (int): Number of steps to take.

    Returns:
        int: Number of stones after the given number of steps.
    """
    if steps == 0:
        return 1
    else:
        if n == 0:
            # Replace stone 0 with stone 1
            return num_stones(1, steps - 1)
        elif len(str(n)) % 2 == 0:
            # Replace stone n with stones n1n2
            s = str(n)
            length = len(s) // 2
            num1 = int(s[:length])
            num2 = int(s[length:])
            return num_stones(num1, steps - 1) + num_stones(num2, steps - 1)
        else:
            # Replace stone n with stone 2024*n
            return num_stones(2024 * n, steps - 1)


def solve_day11_puzzle_part1(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 11.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 1)
    """
    # Parse user input
    stones = parse_day11_input(user_input)

    total = 0
    for i in stones:
        total += num_stones(i, 25)

    return {"solution": total}


def solve_day11_puzzle_part2(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 11.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 2)
    """
    # Parse user input
    stones = parse_day11_input(user_input)

    total = 0
    for i in stones:
        total += num_stones(i, 75)

    return {"solution": total}


def solve_day11_puzzle(user_input: str, part: int) -> dict[str, any]:
    """
    Function to solve the puzzle for Day 11.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        dict[str, any]: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day11_puzzle_part1(user_input)
    elif part == 2:
        return solve_day11_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
