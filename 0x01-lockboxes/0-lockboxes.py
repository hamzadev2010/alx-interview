#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Cheking whether all lockboxes can be opened.

    Args:
        boxes (list of lists): Lockboxes and their respective keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    opened_boxes = {0}

    def open_box(box_index):
        opened_boxes.add(box_index)
        for key in boxes[box_index]:
            if key not in opened_boxes:
                open_box(key)

    open_box(0)
    
    return len(opened_boxes) == len(boxes)
