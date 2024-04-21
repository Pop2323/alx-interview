#!/usr/bin/python3

def canUnlockAll(boxes):
    for i in range(1, len(boxes)):
        check = False
        for j in range(len(boxes)):
            if i in boxes[j] and i != j:
                check = True
                break
            if not check:
                return False
        return True
