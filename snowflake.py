# import libraries
import numpy as np


def koch_line(start, end, factor):
    """
    Segments a line to Koch line, creating fractals.

    :param tuple start:  (x, y) coordinates of the starting point
    :param tuple end: (x, y) coordinates of the end point
    :param float factor: the multiple of sixty degrees to rotate
    :returns tuple: tuple of all points of segmentation
    """

    # coordinates of the start
    x1, y1 = start[0], start[1]

    # coordinates of the end
    x2, y2 = end[0], end[1]

    # the length of the line
    l = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # first point: same as the start
    a = (x1, y1)

    # second point: one third in each direction from the first point
    b = (x1 + (x2 - x1) / 3., y1 + (y2 - y1) / 3.)

    # third point: rotation for multiple of 60 degrees
    c = (b[0] + l / 3. * np.cos(factor * np.pi / 3.), b[1] + l / 3. * np.sin(factor * np.pi / 3.))

    # fourth point: two thirds in each direction from the first point
    d = (x1 + 2. * (x2 - x1) / 3., y1 + 2. * (y2 - y1) / 3.)

    # the last point
    e = end

    return {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'factor': factor}


def koch_snowflake(center, degree, s=5.0):
    """
    Generates all lines for a Koch Snowflake with a given degree.

    :param tuple center: the center of the koch snowflake
    :param int degree: how deep to go in the branching process
    :param float s: the length of the initial equilateral triangle
    :returns list: list of all lines that form the snowflake
    """
    # all lines of the snowflake
    lines = []

    # we rotate in multiples of 60 degrees
    sixty_degrees = np.pi / 3.

    # vertices of the initial equilateral triangle
    A = (center[0] - s / 2, center[1] - np.sqrt(3) * s / 6)
    B = (center[0] + s / 2, center[1] - np.sqrt(3) * s / 6)
    C = (center[0], center[1] + np.sqrt(3) * s / 3)

    # set the initial lines
    if degree == 0:
        lines.append(koch_line(A, B, 0))
        lines.append(koch_line(B, C, 2))
        lines.append(koch_line(C, A, 4))
    else:
        lines.append(koch_line(A, B, 5))
        lines.append(koch_line(B, C, 1))
        lines.append(koch_line(C, A, 3))

    for i in range(1, degree):
        # every lines produce 4 more lines
        for _ in range(3 * 4 ** (i - 1)):
            line = lines.pop(0)
            factor = line['factor']

            lines.append(koch_line(line['a'], line['b'], factor % 6))  # a to b
            lines.append(koch_line(line['b'], line['c'], (factor - 1) % 6))  # b to c
            lines.append(koch_line(line['c'], line['d'], (factor + 1) % 6))  # d to c
            lines.append(koch_line(line['d'], line['e'], factor % 6))  # d to e

    return lines
