#!/usr/bin/python3
'''LockBoxes'''

def canUnlockAll(boxes):
    """
    Checking whether all lockboxes can be opened.

    Args:
        boxes : A list have lockboxes, each represented as a list of keys.

    Returns:
        bool: True if boxes can be opened; False.
    """
    # Initialize a set to keep track of opened boxes
    unlocked_boxes = set([0])

    # Function to recursively open boxes
    def open_box(box_index):
        # Mark the current box as opened
        unlocked_boxes.add(box_index)

        # Open all the boxes that can be opened from the current box
        for key in boxes[box_index]:
            if key not in unlocked_boxes and key < len(boxes):
                open_box(key)

    # Start by opening the first box
    open_box(0)

    # Check if all boxes are either opened or reachable
    return len(unlocked_boxes) == len(boxes)
