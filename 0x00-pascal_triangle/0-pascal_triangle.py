#!/usr/bin/python3
"""Pascal Triangle interview challenge"""


def pascal_triangle(n):
    """Func that returns a list of lists
    numbers representing pascal triangle"""
    if n <= 0:
        return []
    
    pascal_triangle = [0] * n
    
    for i in range(n):
        # define a row and fill first and last idx 1
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1
        
        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_row[j] = a + b
                
        pascal_triangle[i] = new_row
        
    return pascal_triangle