#!/usr/bin/python3


def canUnlockAll(boxes):
    for i in range(1, len(boxes) - 1):
        check = False
        for j in range(len(boxes)):
            check = (i in boxes[j] and i != j)
            if check:
                break
        if check is False:
            return check
    return True
