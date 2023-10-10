#!/usr/bin/python3
"""pascal triangle"""

def pascal_triangle(n):
    """gets pascal triangle for n,
    of list of values representing triangle
    """
    triang = []
    for i in range(0, n):
        mat_len = len(triang)
        if mat_len <= 1:
            triang.append([1 for q in range(0, mat_len + 1)])
        else:
            new_row = []
            for j in range(0, len(triang[i - 1]) + 1):
                if j == 0 or j == len(triang[i - 1]):
                    new_row.append(1)
                else:
                    new_row.append(triang[i - 1][j - 1] + triang[i - 1][j])
            triang.append(new_row)
    return triang
