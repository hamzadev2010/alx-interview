#!/usr/bin/python3
'''LockBoxes'''

def canUnlockAll(boxes):
    """
    Checking if all lockboxes can be opened.

    Parameters
        boxes (list of lists): Boxes and their keys.

    Returns
        bool: True if all boxes can be opened, False otherwise.
    """

    opened_boxes = set()

    def open_box(box_index):
        if box_index in opened_boxes:
            return
        opened_boxes.add(box_index)
        for key in boxes[box_index]:
            open_box(key)

    open_box(0)
    
    return len(opened_boxes) == len(boxes)
