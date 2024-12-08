import operator


def test_equation(equation: tuple[int, list[int]], operators: list[callable]) -> bool:
    """
    Function to test if an equation can be solved using the given operators.
    Args:
        equation (tuple): A tuple containing the desired total and a list of numbers.
        operators (list): A list of operator functions.
    Returns:
        bool: True if the equation can be solved, False otherwise
    """
    target = equation[0]
    nums = equation[1]

    # Stack of (total, operator, current index)
    stack = [(nums[0], op, 0) for op in operators]

    while len(stack) > 0:
        total, op, i = stack.pop()

        # Combine the current total with the next number
        total = op(total, nums[i + 1])

        # If the total is greater than the target, skip this iteration
        if total > target:
            continue
        else:
            if i == len(nums) - 2:
                # If we are at the last number, check if the total is equal to the target
                if total == target:
                    return True
            else:
                for op in operators:
                    # Add the new total to the stack, along with the operator and the next index
                    stack.append((total, op, i + 1))

    return False


def concatenate(a: int, b: int) -> int:
    return int(f"{a}{b}")


def parse_day7_input(user_input: str) -> list[tuple[int, list[int]]]:
    """
    Function to parse the user input for Day 7.
    Args:
        user_input (str): The user input.
    Returns:
        list: A list of tuples, where the first element is the desired total and the second element is a list of numbers.
    """
    lines = user_input.split("\n")

    equations = []
    for line in lines:
        nums = line.split(" ")
        this_equation = (int(nums[0][:-1]), [int(x) for x in nums[1:]])
        equations.append(this_equation)

    return equations


def solve_day7_puzzle_part1(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 7.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 1)
    """
    # Parse user input
    parsed_input = parse_day7_input(user_input)

    total = 0
    for equation in parsed_input:
        if test_equation(equation, [operator.add, operator.mul]):
            total += equation[0]

    return {"solution": total}


def solve_day7_puzzle_part2(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 7.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 2)
    """
    # Parse user input
    parsed_input = parse_day7_input(user_input)

    total = 0
    for equation in parsed_input:
        if test_equation(equation, [operator.add, operator.mul, concatenate]):
            total += equation[0]

    return {"solution": total}


def solve_day7_puzzle(user_input: str, part: int) -> dict[str, any]:
    """
    Function to solve the puzzle for Day 7.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        dict[str, any]: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day7_puzzle_part1(user_input)
    elif part == 2:
        return solve_day7_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
