import numpy as np


def parse_day9_input(user_input: str) -> list[int]:
    """
    Function to parse the user input for Day 9.
    Args:
        user_input (str): The user input.
    Returns:
        list[int]: The parsed user input
    """
    return [int(x) for x in user_input]


def blocks_to_list(blocks: list[dict[str, int]]) -> list[any]:
    end = []
    for block in blocks:
        end += block["file_length"] * [block["idx"]]
        end += block["spaces"] * ["."]
    return end


def solve_day9_puzzle_part1(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 9.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 1)
    """
    # Parse user input
    parsed_input = parse_day9_input(user_input)

    # Convert input into disk representation
    disk = []
    i = 0
    for i, n in enumerate(parsed_input):
        if i % 2 == 0:
            disk += n * [i // 2]
        else:
            disk += n * ["."]

    # Find the space indices
    space_idx = [i for i, x in enumerate(disk) if x == "."]
    space_idx_rev = space_idx[::-1]

    # Move the disk data one slot at a time
    while len(disk) > space_idx_rev[-1]:
        this = disk.pop()
        if this != ".":
            idx = space_idx_rev.pop()
            disk[idx] = this

    return {"solution": sum([i * d for i, d in enumerate(disk)])}


def solve_day9_puzzle_part2(user_input: str) -> dict[str, any]:
    """
    Function to solve part 1 of the puzzle for Day 9.
    Args:
        user_input (str): The user input.
    Returns:
        dict[str, any]: The solution to the puzzle (part 2)
    """
    # Parse user input
    parsed_input = parse_day9_input(user_input)

    # Make sure the input is even in length by adding a 0 if necessary
    if len(parsed_input) % 2 != 0:
        parsed_input.append(0)

    # Create list of block representations
    # of form (block_length, spaces, idx)
    blocks = []
    for i, (block, spaces) in enumerate(
        np.reshape(parsed_input, (len(parsed_input) // 2, 2))
    ):
        blocks.append({"file_length": int(block), "spaces": int(spaces), "idx": i})

    # Take the blocks from the right one at a time, and see if they can be moved
    # to the left. If not, add them to the fixed list.
    moved_idx = []
    fixed = []

    while len(blocks) > 0:
        end_block = blocks.pop()

        # If there are no blocks left, add the end block to the fixed list
        if len(blocks) == 0:
            fixed.append(end_block)
            continue

        # If the end block has already been moved, add it to the fixed list
        if end_block["idx"] in moved_idx:
            fixed.append(end_block)
            continue

        # Try to move the end block to the left
        for i, b in enumerate(blocks):
            if end_block["file_length"] <= b["spaces"]:
                blocks[-1]["spaces"] += end_block["file_length"] + end_block["spaces"]
                end_block["spaces"] = b["spaces"] - end_block["file_length"]
                b["spaces"] = 0
                blocks.insert(i + 1, end_block)
                moved_idx.append(end_block["idx"])
                break
        else:
            # If the end block cannot be moved to the left, add it to the fixed list
            fixed.append(end_block)

    # Reverse the fixed list back to the original order
    fixed = fixed[::-1]

    return {
        "solution": sum(
            [i * b for i, b in enumerate(blocks_to_list(fixed)) if b != "."]
        )
    }


def solve_day9_puzzle(user_input: str, part: int) -> dict[str, any]:
    """
    Function to solve the puzzle for Day 9.
    Args:
        user_input (str): The user input.
        part (int): The part of the puzzle to solve.
    Returns:
        dict[str, any]: The solution to the puzzle for the given part.
    """
    if part == 1:
        return solve_day9_puzzle_part1(user_input)
    elif part == 2:
        return solve_day9_puzzle_part2(user_input)
    else:
        raise ValueError(f"Invalid value {part} for part. Part must be 1 or 2.")
