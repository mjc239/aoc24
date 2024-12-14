from itertools import combinations
import networkx as nx
import numpy as np


def compute_components(
    user_input: list[str],
) -> tuple[list[set[tuple[int, int]]], set[tuple[int, int]]]:
    """
    Function to compute the connected regions of the garden.
    Args:
        user_input (list[str]): The user input.
    Returns:
        tuple[list[tuple[int, int]], set[tuple[int, int]]]: The connected components and the edges.
    """
    graph = nx.Graph()

    for i, row in enumerate(user_input):
        for j, char in enumerate(row):
            graph.add_node((i, j))
            if i > 0 and user_input[i - 1][j] == char:
                graph.add_edge((i, j), (i - 1, j))
            if j > 0 and user_input[i][j - 1] == char:
                graph.add_edge((i, j), (i, j - 1))

    return list(nx.connected_components(graph)), set(graph.edges)


def num_sides(component: set[tuple[int, int]]) -> int:
    """Find the number of sides of a connected component.

    Args:
        component (set[tuple[int, int]]): The connected component.

    Returns:
        int: The number of sides of the connected component.
    """
    # Find the bounding box of the component
    arr = np.array(list(component))
    miny, minx = arr.min(axis=0)
    maxy, maxx = arr.max(axis=0)

    n_sides = 0
    # Check each 4x4 square in the bounding box
    for i in range(miny - 1, maxy + 1):
        for j in range(minx - 1, maxx + 1):
            # Check if the square intersects the component
            # A square consists of 4 points and is defined by the
            # top-left corner (i, j)
            square = set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
            intersection = square.intersection(component)

            # We can count the number of sides by counting the number
            # of corners. A corner occurs when the square intersects
            # the component at an odd number of points. If the square
            # intersects the component at 2 points, we have a 2 corners
            # if the two points are diagonally opposite.
            if len(intersection) % 2 == 1:
                # Odd number of intersections = corner
                n_sides += 1
            elif (
                len(intersection) == 2
                and (i + 1, j) in component
                and (i, j + 1) in component
            ):
                # Two intersections at diagonally opposite points
                n_sides += 2
            elif (
                len(intersection) == 2
                and (i, j) in component
                and (i + 1, j + 1) in component
            ):
                # Two intersections at diagonally opposite points
                n_sides += 2

    return n_sides


def parse_day12_input(user_input: str) -> list[str]:
    """
    Function to parse the user input for Day 12.
    Args:
        user_input (str): The user input.
    Returns:
        list[str]: The parsed user input.
    """
    return user_input.split("\n")


def solve_day12_puzzle_part1(user_input: str) -> dict[str, int]:
    """
    Function to solve part 1 of the puzzle for Day 12.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, int]: The solution to the puzzle (part 1)
    """
    # Parse user input
    parsed_input = parse_day12_input(user_input)

    # Compute connected components and edges
    components, edges = compute_components(parsed_input)

    price = 0
    for component in components:
        # Compute area, number of edges and number of borders
        area = len(component)
        num_edges = sum(
            [
                1
                for (i, j) in combinations(component, 2)
                if (i, j) in edges or (j, i) in edges
            ]
        )
        num_borders = 4 * area - 2 * num_edges

        # Update price
        price += area * num_borders

    return {"solution": price}


def solve_day12_puzzle_part2(user_input: str) -> dict[str, int]:
    """
    Function to solve part 1 of the puzzle for Day 12.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, int]: The solution to the puzzle (part 2)
    """
    # Parse user input
    parsed_input = parse_day12_input(user_input)

    components, _ = compute_components(parsed_input)

    return {
        "solution": sum(
            [num_sides(component) * len(component) for component in components]
        )
    }


def solve_day12_puzzle(user_input: str, part: int) -> dict[str, int]:
    """
    Function to solve the puzzle for Day 12.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        dict[str, int]: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day12_puzzle_part1(user_input)
    elif part == 2:
        return solve_day12_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
