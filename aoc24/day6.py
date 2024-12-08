import numpy as np


def find_start(array: list[str]) -> tuple[int, int]:
    """
    Function to find the starting position of the guard.
    Args:
        array (list[str]): The grid.
    Returns:
        tuple[int, int]: The starting position of the guard."""
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell in ["^", ">", "v", "<"]:
                return (i, j)


def escape_path(row: int, col: int, direction: str, array: list[str]) -> dict[str, any]:
    """
    Determine if the guard can escape the grid, and the path taken.
    Args:
        row (int): The starting row.
        col (int): The starting column.
        direction (str): The starting direction.
        array (list[str]): The grid.
    Returns:
        dict[str, any]: A dictionary containing the following:
            - can_escape (bool): Whether the guard can escape the grid.
            - visited (set[tuple[int, int, str]]): The path taken by the guard.
    """
    m = len(array)
    n = len(array[0])

    visited = {(row, col, direction)}

    # Keep moving until we reach the edge of the grid
    while True:
        # Check if we need to change direction
        # else keep moving in the same direction
        match direction:
            case "^":
                if array[row - 1][col] == "#":
                    direction = ">"
                else:
                    row = row - 1
            case ">":
                if array[row][col + 1] == "#":
                    direction = "v"
                else:
                    col = col + 1
            case "v":
                if array[row + 1][col] == "#":
                    direction = "<"
                else:
                    row = row + 1
            case "<":
                if array[row][col - 1] == "#":
                    direction = "^"
                else:
                    col = col - 1

        # Check if we have visited this cell/direction before
        if (row, col, direction) in visited:
            return {"can_escape": False, "visited": visited}

        visited.add((row, col, direction))

        # Check if we have reached the edge of the grid
        if direction == "^" and row == 0:
            return {"can_escape": True, "visited": visited}
        if direction == ">" and col == n - 1:
            return {"can_escape": True, "visited": visited}
        if direction == "v" and row == m - 1:
            return {"can_escape": True, "visited": visited}
        if direction == "<" and col == 0:
            return {"can_escape": True, "visited": visited}


def parse_day6_input(user_input: str):
    """
    Function to parse the user input for Day 6.
    Args:
        user_input (str): The user input.
    Returns:

    """
    return user_input.split("\n")


def solve_day6_puzzle_part1(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 6.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 1)
    """
    # Parse user input
    array = parse_day6_input(user_input)

    # Find the starting position of the guard
    start_row, start_col = find_start(array)
    start_direction = array[start_row][start_col]

    # Find the path taken by the guard
    path = escape_path(start_row, start_col, start_direction, array)["visited"]

    # Find the number of unique cells visited (without the direction)
    unique_visited = set([(row, col) for row, col, _ in path])

    visited_array = np.array(
        [
            [
                int(char.replace(".", "0").replace("#", "1").replace("^", "2"))
                for char in row
            ]
            for row in user_input
        ]
    )
    for row, col in unique_visited(user_input):
        visited_array[row, col] = 2

    return {"solution": len(unique_visited), "visited_array": visited_array}


def solve_day6_puzzle_part2(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 6.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 2)
    """
    # Parse user input
    array = parse_day6_input(user_input)

    # Find the starting position of the guard
    start_row, start_col = find_start(user_input)
    start_direction = user_input[start_row][start_col]

    # Find the path taken by the guard (without additional obstacles)
    visited_with_dirs = escape_path(start_row, start_col, start_direction, user_input)[
        "visited"
    ]
    visited = set([(row, col) for row, col, _ in visited_with_dirs])

    # Find the number of additional obstacles that can be placed to prevent the guard from escaping
    total = 0
    for i, j in visited:
        if array[i][j] in ["^", ">", "v", "<"]:
            continue
        else:
            copy_array = array.copy()
            copy_array[i] = copy_array[i][:j] + "#" + copy_array[i][j + 1 :]
            if not escape_path(start_row, start_col, start_direction, copy_array)[
                "can_escape"
            ]:
                total += 1
    return {"solution": total}


def solve_day6_puzzle(user_input: str, part: int) -> dict[str, any]:
    """
    Function to solve the puzzle for Day 6.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        int: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day6_puzzle_part1(user_input)
    elif part == 2:
        return solve_day6_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
