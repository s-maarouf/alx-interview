#!/usr/bin/python3
'''A module for working with lockboxes.'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.'''
    if not boxes:
        return False

    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    keys = [0]

    while keys:
        box_index = keys.pop()
        box = boxes[box_index]
        for key in box:
            if 0 <= key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
