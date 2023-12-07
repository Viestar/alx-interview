#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ # Initialize a set to keep track of visited boxes """
    visited = set()

    """ Define a DFS function to explore boxes """
    def dfs(box):
        """ Mark the current box as visited """
        visited.add(box)

        """ Explore keys in the current box """
        for key in boxes[box]:
            """ If the key opens an unvisited box, recursively explores it """
            if key not in visited:
                dfs(key)

    # Start DFS from the first box
    dfs(0)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)


"""# def canUnlockAll(boxes):
#     Determines if all boxes can be opened
#     counter = 0
#     for boxList in boxes:
#         counter += 1
#         for key in boxList:
#             if int(key) == counter:
#                 continue
#             return False
#         return True
"""
