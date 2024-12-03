from re import findall


def solve_day3_puzzle_part1(user_input: str) -> int:
    """
    Function to solve part 1 of the puzzle for Day 3.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 1)
    """
    # Find all patterns of the form "mul(a,b)"
    found_patterns = findall(r"mul\(\d+,\d+\)", user_input)

    # Calculate the sum of the products
    total = 0
    for pattern in found_patterns:
        num1, num2 = [int(x) for x in pattern.strip("mul")[1:-1].split(",")]
        total += num1 * num2

    return total


def solve_day3_puzzle_part2(user_input: str) -> int:
    """
    Function to solve part 1 of the puzzle for Day 3.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 2)
    """
    # Find all patterns of the form "mul(a,b)", "do", and "don't"
    patterns = findall("mul\(\d+,\d+\)|don't|do(?!xy)", user_input)

    # Keep track of enabled status
    enabled = True
    total = 0

    # Calculate the sum of the products, only if enabled
    for pattern in patterns:
        if "mul" in pattern and enabled:
            num1, num2 = [int(x) for x in pattern.strip("mul()").split(",")]
            total += num1 * num2
        elif pattern == "do":
            enabled = True
        elif pattern == "don't":
            enabled = False

    return total


def solve_day3_puzzle(user_input: str, part: int) -> int:
    """
    Function to solve the puzzle for Day 3.
    Args:
        user_input (str): The user input.
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
