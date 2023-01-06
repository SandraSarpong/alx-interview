#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            seen_boxes.add(boxIdx)
            unseen_boxes = unseen_boxes.union(set(boxes[boxIdx]).difference(seen_boxes))
    return n == len(seen_boxes)
