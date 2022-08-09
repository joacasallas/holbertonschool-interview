#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened"""
def canUnlockAll(boxes):
    """function to check if key exists"""
    key = 0
    while boxes:
        key = key + 1
    if key == (len(boxes) -1):
        return true
    else:
        return false
