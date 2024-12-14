def entry_cost(entry: dict[str, int]) -> int:
    """Compute the cost of an entry.

    Args:
        entry (dict[str, int]): The entry with the following keys:
            - Ax: The amount that button A moves the claw in the x direction.
            - Ay: The amount that button A moves the claw in the y direction.
            - Bx: The amount that button B moves the claw in the x direction.
            - By: The amount that button B moves the claw in the y direction.
            - X: The x coordinate of the target.
            - Y: The y coordinate of the target.

    Returns:
        int: The lowest cost to reach the target.
    """
    # Determinant
    det = entry["Ax"] * entry["By"] - entry["Ay"] * entry["Bx"]

    # If the determinant is 0, the system is either inconsistent
    # (no solution, return 0) or has infinitely many solutions.
    # In the latter case, we can find the cheapest solution by checking
    # the cost of moving the claw to the target using only one of the buttons,
    # and choosing the cheapest one.
    if det == 0:
        if entry["X"] * entry["Ay"] != entry["Y"] * entry["Ax"]:
            # No solution
            return 0
        else:
            if entry["Ax"] > 3 * entry["Bx"]:
                # Use button A
                r = entry["X"] / entry["Ax"]
                return 3 * int(r) if r.is_integer() else 0
            else:
                # Use button B
                r = entry["X"] / entry["Bx"]
                return int(r) if r.is_integer() else 0

    # alpha = number of times button A is pressed
    # beta = number of times button B is pressed
    alpha = (entry["X"] * entry["By"] - entry["Y"] * entry["Bx"]) / det
    beta = (entry["Ax"] * entry["Y"] - entry["Ay"] * entry["X"]) / det

    # Rule out negative values or non-integer values
    if alpha < 0 or beta < 0:
        return 0

    if not alpha.is_integer() or not beta.is_integer():
        return 0

    # Compute total cost using the individual costs of each button
    # (3 units for button A, 1 unit for button B)
    return 3 * int(alpha) + int(beta)


def parse_day13_input(user_input: str, addition: int = 0) -> list[dict[str, int]]:
    """
    Function to parse the user input for Day 13.
    Args:
        user_input (str): The user input.
    Returns:

    """
    entries = []
    for entry in user_input.split("\n\n"):
        entry_dict = {}
        rows = entry.split("\n")
        entry_dict["Ax"] = int(rows[0].split(" ")[2][:-1].split("+")[1])
        entry_dict["Ay"] = int(rows[0].split(" ")[3].split("+")[1])
        entry_dict["Bx"] = int(rows[1].split(" ")[2][:-1].split("+")[1])
        entry_dict["By"] = int(rows[1].split(" ")[3].split("+")[1])
        entry_dict["X"] = int(rows[2].split(" ")[1][:-1].split("=")[1]) + addition
        entry_dict["Y"] = int(rows[2].split(" ")[2].split("=")[1]) + addition

        entries.append(entry_dict)
    return entries


def solve_day13_puzzle_part1(user_input: str) -> dict[str, int]:
    """
    Function to solve part 1 of the puzzle for Day 13.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, int]: The solution to the puzzle (part 1)
    """
    # Parse user input
    parsed_input = parse_day13_input(user_input)

    return sum([entry_cost(entry) for entry in parsed_input])


def solve_day13_puzzle_part2(user_input: str) -> dict[str, int]:
    """
    Function to solve part 1 of the puzzle for Day 13.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, int]: The solution to the puzzle (part 2)
    """
    # Parse user input
    parsed_input = parse_day13_input(user_input, 10000000000000)

    return sum([entry_cost(entry) for entry in parsed_input])


def solve_day13_puzzle(user_input: str, part: int) -> dict[str, int]:
    """
    Function to solve the puzzle for Day 13.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        dict[str, int]: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day13_puzzle_part1(user_input)
    elif part == 2:
        return solve_day13_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
