def canUnlockAll(boxes):
    '''LockBoxes Challenge'''

  """
    Checking if all lockboxes can be opened.

    Parameters:
        boxes (list of lists): Boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked initially
    stack = [0]  # Start with the first box

    # Explore boxes using Depth-First Search
    while stack:
        current_box = stack.pop()
        for next_box in boxes[current_box]:
            if next_box < len(boxes) and not unlocked[next_box]:
                unlocked[next_box] = True
                stack.append(next_box)

    # Check if all boxes are unlocked
    return all(unlocked)
