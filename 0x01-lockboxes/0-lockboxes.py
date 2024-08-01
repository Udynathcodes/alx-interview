#!/usr/bin/python3


def canUnlockAll(boxes):
    n = len(boxes)
    opened = set()
    stack = [0]  # Start with the first box

    while stack:
        box_index = stack.pop()
        if box_index not in opened:
            opened.add(box_index)
            for key in boxes[box_index]:
                if key < n:
                    stack.append(key)

    return len(opened) == n
