def sign(n: int) -> int:
    """Function to return the sign of a number.
    Args:
        n (int): The number to check the sign of.
    Returns:
        int: 1 if n > 0, -1 if n < 0, 0 if n == 0.
    """
    if n == 0:
        return 0
    else:
        return 1 if n > 0 else -1


def remove(num_list: list[int], idx: int) -> list[int]:
    """Function to remove an element from a list.
    Args:
        num_list (list[int]): The list of numbers.
        idx (int): The index of the element to remove.
    Returns:
        list[int]: The list with the element removed.
    """
    return num_list[:idx] + num_list[idx + 1 :]


def is_report_safe_part1(nums: list[int]) -> bool:
    """
    Function to check if a report is safe (part 1).
    Args:
        nums (list[int]): The list of numbers in the report.
    Returns:
        bool: True if the report is safe, False otherwise.
    """
    # Check if the first difference is 0
    first_diff = nums[1] - nums[0]
    if first_diff == 0:
        return False
    else:
        first_sign = sign(first_diff)

    # Loop through the rest of the list, checking if the differences are safe
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if sign(diff) != first_sign or abs(diff) > 3 or diff == 0:
            return False

    return True


def is_report_safe_part2(nums: list[int]) -> bool:
    """
    Function to check if a report is safe (part 2).
    Args:
        nums (list[int]): The list of numbers in the report.
    Returns:
        bool: True if the report is safe, False otherwise.
    """
    # Check if the first difference is 0, and try removing the first element if it is
    first_diff = nums[1] - nums[0]
    if first_diff == 0:
        return is_report_safe_part1(remove(nums, 0))
    else:
        first_sign = sign(first_diff)

    # Loop through the rest of the list, checking if the differences are safe
    for i in range(1, len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if sign(diff) != first_sign or abs(diff) > 3 or diff == 0:
            return (
                is_report_safe_part1(remove(nums, i - 1))
                or is_report_safe_part1(remove(nums, i))
                or is_report_safe_part1(remove(nums, i + 1))
            )

    return True


def parse_day2_input(user_input: str):
    """
    Function to parse the user input for Day 2.
    Args:
        user_input (str): The user input.
    Returns:
        list[int]: The parsed user input
    """
    return [[int(x) for x in report.split(" ")] for report in user_input.split("\n")]


def solve_day2_puzzle_part1(user_input: str):
    """
    Function to solve part 1 of the puzzle for Day 2.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 1)
    """
    # Parse user input
    parsed_input = parse_day2_input(user_input)

    return sum([is_report_safe_part1(report) for report in parsed_input])


def solve_day2_puzzle_part2(user_input: str):
    """
    Function to solve part 2 of the puzzle for Day 2.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 2)
    """
    # Parse user input
    parsed_input = parse_day2_input(user_input)

    return sum([is_report_safe_part2(report) for report in parsed_input])


def solve_day2_puzzle(user_input: str, part: int):
    """
    Function to solve the puzzle for Day 2.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        int: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day2_puzzle_part1(user_input)
    elif part == 2:
        return solve_day2_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
