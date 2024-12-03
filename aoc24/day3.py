def parse_day3_input(user_input: list[str]):
    """
    Function to parse the user input for Day 3.
    Args:
        user_input (list[str]): The user input.
    Returns:

    """
    pass


def solve_day3_puzzle_part1(user_input: list[str]) -> int:
    """
    Function to solve part 1 of the puzzle for Day 3.
    Args:
        user_input (list[str]): The user input.
    Returns:
        int: The solution to the puzzle (part 1)
    """
    # Parse user input
    pass


def solve_day3_puzzle_part2(user_input: list[str]) -> int:
    """
    Function to solve part 1 of the puzzle for Day 3.
    Args:
        user_input (list[str]): The user input.
    Returns:
        int: The solution to the puzzle (part 2)
    """
    # Parse user input
    pass


def solve_day3_puzzle(user_input: list[str], part: int) -> int:
    """
    Function to solve the puzzle for Day 3.
    Args:
        user_input (list[str]): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        int: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day3_puzzle_part1(user_input)
    elif part == 2:
        return solve_day3_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")


sum(
    [
        prod([int(num) for num in pattern.strip("mul")[1:-1].split(",")])
        for pattern in findall(r"mul\(\d+,\d+\)", user_input)
    ]
)
