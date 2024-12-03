from collections import Counter


def parse_day1_input(user_input: str):
    """
    Function to parse the user input for Day 1.
    """
    processed_file = [
        [int(x) for x in line.strip("\n").split("   ")]
        for line in user_input.split("\n")
    ]
    first_list, second_list = list(map(list, zip(*processed_file)))

    return first_list, second_list


def solve_day1_puzzle_part1(user_input: str):
    """
    Function to solve part 1 of the puzzle for Day 1.
    """
    # Parse user input
    first_list, second_list = parse_day1_input(user_input)

    # Code to compute solution goes here
    first_list, second_list = sorted(first_list), sorted(second_list)
    diffs = [abs(a - b) for a, b in zip(first_list, second_list)]
    return sum(diffs)


def solve_day1_puzzle_part2(user_input: str):
    """
    Function to solve part 2 of the puzzle for Day 1.
    """
    # Parse user input
    first_list, second_list = parse_day1_input(user_input)

    # Code to compute solution goes here
    list_counter = Counter(second_list)
    total = sum([num * list_counter[num] for num in first_list])

    return total


def solve_day1_puzzle(user_input: str, part: int):
    """
    Function to solve the puzzle for Day 1.
    """
    if part == 1:
        return solve_day1_puzzle_part1(user_input)
    elif part == 2:
        return solve_day1_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
