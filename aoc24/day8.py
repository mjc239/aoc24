from collections import defaultdict
from itertools import combinations


def parse_day8_input(user_input: str):
    """
    Function to parse the user input for Day 8.
    Args:
        user_input (str): The user input.
    Returns:

    """
    return user_input.split("\n")


def solve_day8_puzzle_part1(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 8.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 1)
    """
    # Parse user input
    array = parse_day8_input(user_input)

    m, n = len(array), len(array[0])
    antinodes = set()
    antennae = defaultdict(list)

    # Find antennae positions
    for i in range(m):
        for j in range(n):
            if array[i][j] != ".":
                antennae[array[i][j]].append((i, j))

    # Find antinodes
    for freq, ants in antennae.items():
        for ant1, ant2 in combinations(ants, 2):
            i1, j1 = ant1
            i2, j2 = ant2
            antinode_1 = (2 * i1 - i2, 2 * j1 - j2)
            antinode_2 = (2 * i2 - i1, 2 * j2 - j1)
            for antinode in [antinode_1, antinode_2]:
                if 0 <= antinode[0] < m and 0 <= antinode[1] < n:
                    antinodes.add(antinode)

    return {"solution": len(antinodes), "antinodes": antinodes}


def solve_day8_puzzle_part2(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 8.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 2)
    """
    # Parse user input
    array = parse_day8_input(user_input)

    m, n = len(array), len(array[0])
    antinodes = set()
    antennae = defaultdict(list)

    # Find antennae positions
    for i in range(m):
        for j in range(n):
            if array[i][j] != ".":
                antennae[array[i][j]].append((i, j))

    # Find antinodes
    for freq, ants in antennae.items():
        for ant1, ant2 in combinations(ants, 2):
            i1, j1 = ant1
            i2, j2 = ant2

            # Find the vector between the two antennae
            v = (i2 - i1, j2 - j1)

            # Find the maximum number of steps to reach the edge of the grid
            s = max(m // abs(v[0]) + 1, n // abs(v[1]) + 1)

            # Find all antinodes along the vector
            for k in range(-s, s + 1):
                antinode = (i2 + k * v[0], j2 + k * v[1])
                if 0 <= antinode[0] < m and 0 <= antinode[1] < n:
                    antinodes.add(antinode)

    return {"solution": len(antinodes), "antinodes": antinodes}


def solve_day8_puzzle(user_input: str, part: int) -> dict[str, any]:
    """
    Function to solve the puzzle for Day 8.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        dict[str, any]: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day8_puzzle_part1(user_input)
    elif part == 2:
        return solve_day8_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
