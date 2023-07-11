#!/usr/bin/python3
"""Define pascal traingle """

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given n value.

    Args:
        n (int): The number of items in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    if n >= 2:
        for i in range(1, n):
            item = [1]
            prev_item = triangle[i - 1]
            for j in range(1, i):
                item.append(prev_item[j - 1] + prev_item[j])
            item.append(1)
            triangle.append(item)

    return triangle
