import re
import itertools
import numpy as np


def find_diagonals(array: list[str]) -> list[str]:
    """
    Function to find the diagonals of a 2D array.
    Args:
        array (list[str]): The 2D array, as a list of strings.
    Returns:
        dict[int, str]: A map from the diagonal index to the diagonal.
    """
    n = len(array)  # Number of rows
    m = len(array[0])  # Number of columns

    # Diagonals from top-left to bottom-right (main diagonals)
    main_diagonals = {}
    for i in range(n):
        for j in range(m):
            k = i - j
            main_diagonals.setdefault(k, []).append(array[i][j])
    main_diagonals = {
        k: "".join([str(x) for x in d]) for k, d in main_diagonals.items()
    }

    return main_diagonals


def find_anti_diagonals(array: list[str]) -> list[str]:
    """
    Function to find the anti-diagonals of a 2D array.
    Args:
        array (list[str]): The 2D array, as a list of strings.
    Returns:
        dict[int, str]: A map from the anti-diagonal index to the anti-diagonal.
    """
    n = len(array)  # Number of rows
    m = len(array[0])  # Number of columns

    # Diagonals from top-right to bottom-left (anti-diagonals)
    anti_diagonals = {}
    for i in range(n):
        for j in range(m):
            k = i + j
            anti_diagonals.setdefault(k, []).append(array[i][j])
    anti_diagonals = {
        k: "".join([str(x) for x in d]) for k, d in anti_diagonals.items()
    }

    return anti_diagonals


def search_words(
    array: list[str], words: list[str]
) -> tuple[int, set[tuple[int, int]]]:
    """Finds the number of occurrences of a list of words in a 2D array, and the indices of letters that form the words.

    Args:
        array (list[str]): The 2D array, as a list of strings.
        words (list[str]): List of words to search for in the array.

    Returns:
        tuple[int, set[tuple[int, int]]]: The number of occurrences of the words in the array, and the indices of the letters that form the words.
    """
    total = 0
    indices = set()
    pattern = "|".join(words)
    m = len(array)
    n = len(array[0])

    # Horizontal search
    for i, line in enumerate(array):
        matches = re.finditer(rf"(?=({pattern}))", line)
        for match in matches:
            total += 1
            new_indices = [(i, match.start() + j) for j in range(4)]
            indices = indices.union(new_indices)

    # Vertical search
    for i, line in enumerate(["".join(a) for a in zip(*array)]):
        matches = re.finditer(rf"(?=({pattern}))", line)
        for match in matches:
            total += 1
            new_indices = [(match.start() + j, i) for j in range(4)]
            indices = indices.union(new_indices)

    # Diagonal search
    # Only works for square arrays
    for imj, line in find_diagonals(array).items():
        matches = re.finditer(rf"(?=({pattern}))", line)
        for match in matches:
            total += 1
            ipj = m - len(line)
            s = match.start()
            start = ((ipj + imj) // 2, (ipj - imj) // 2)
            new_indices = [(start[0] + s + j, start[1] + s + j) for j in range(4)]
            indices = indices.union(new_indices)

    # Anti-diagonal search
    for ipj, line in find_anti_diagonals(array).items():
        matches = re.finditer(rf"(?=({pattern}))", line)
        for match in matches:
            total += 1
            imj = 1 - len(line)
            s = match.start()
            start = ((ipj + imj) // 2, (ipj - imj) // 2)
            new_indices = [(start[0] + s + j, start[1] - s - j) for j in range(4)]
            indices = indices.union(new_indices)

    return total, indices


def mask_array(array: list[str], indices: set[tuple[int, int]]) -> list[str]:
    """Masks the array by replacing the letters not at the given indices with dots.

    Args:
        array (list[str]): Array to mask.
        indices (set[tuple[int, int]]): Indices of the letters to keep.

    Returns:
        list[str]: Masked array.
    """
    m = len(array)
    n = len(array[0])

    masked_array = np.full((m, n), ".")
    for i in range(m):
        for j in range(n):
            if (i, j) in indices:
                masked_array[i, j] = array[i][j]

    return ["".join(row) for row in masked_array]


def parse_day4_input(user_input: str) -> list[str]:
    """
    Function to parse the user input for Day 4.
    Args:
        user_input (str): The user input.
    Returns:

    """
    return user_input.split("\n")


def solve_day4_puzzle_part1(user_input: str) -> int:
    """
    Function to solve part 1 of the puzzle for Day 4.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 1)
    """
    # Parse user input
    array = parse_day4_input(user_input)
    words = ["XMAS", "SAMX"]
    total, indices = search_words(array, words)
    masked_array = mask_array(array, indices)
    return {"solution": total, "masked_array": masked_array}


def solve_day4_puzzle_part2(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 4.
    Args:
        user_input (str): The user input.
    Returns:
        int: The solution to the puzzle (part 2)
    """
    # Parse user input
    array = parse_day4_input(user_input)
    array = [[char for char in line] for line in array]

    tiles = np.lib.stride_tricks.sliding_window_view(array, (3, 3))

    total = 0
    indices = set()
    for i, row in enumerate(tiles):
        for j, tile in enumerate(row):
            joined_tile = "".join(itertools.chain.from_iterable(tile))
            if re.search(
                r"(M.M.A.S.S)|(M.S.A.M.S)|(S.M.A.S.M)|(S.S.A.M.M)", joined_tile
            ):
                total += 1
                indices.add((i, j))
                indices.add((i, j + 2))
                indices.add((i + 1, j + 1))
                indices.add((i + 2, j))
                indices.add((i + 2, j + 2))

    m = len(array)
    n = len(array[0])

    masked_array = np.full((m, n), ".")
    for i in range(m):
        for j in range(n):
            if (i, j) in indices:
                masked_array[i, j] = array[i][j]

    return {"solution": total, "masked_array": ["".join(row) for row in masked_array]}


def solve_day4_puzzle(user_input: str, part: int) -> int:
    """
    Function to solve the puzzle for Day 4.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        int: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day4_puzzle_part1(user_input)
    elif part == 2:
        return solve_day4_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
