# import libraries
import numpy as np


def koch_line(start, end, factor):
    """
    Creates fractions of a line to make koch-lines.
    :param tuple start:  (start[0], start[1]) resemble x1,y1 as startingpoints
    :param tuple end: (end[0], end[1]) resemble x2,y2 as endpoints
    :param float factor: multiple or 60°rotations
    :returns tuple: returns all 5 line-fractions and the factor in a tuple
    """
    # linelengthcalculation
    line_length = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)

    # calculating the first third of the line needed in point 3 for further calculations
    first_third = (start[0] + (end[0] - start[0]) / 3., start[1] + (end[1] - start[1]) / 3.)

    return {'1': (start[0], start[1]),
            '2': (start[0] + (end[0] - start[0]) / 3., start[1] + (end[1] - start[1]) / 3.),
            '3': (first_third[0] + line_length / 3. * np.cos(factor * np.pi / 3.),
                  first_third[1] + line_length / 3. * np.sin(factor * np.pi / 3.)),
            '4': (start[0] + 2. * (end[0] - start[0]) / 3., start[1] + 2. * (end[1] - start[1]) / 3.),
            '5': end,
            'factor': factor}


def koch_snowflake(center, degree, s=5.0):
    """
    Generates all koch lines.
    :param tuple center: the center coordinates
    :param int degree: degree of koch-snowflake
    :param float s: initial equilateral triangle length
    :returns list: list of koch-snowflake lines
    """
    # all lines of the snowflake
    line_list = []

    # initial equilateral triangle-vertices
    V1 = (center[0] - s / 2, center[1] - np.sqrt(3) * s / 6)
    V2 = (center[0] + s / 2, center[1] - np.sqrt(3) * s / 6)
    V3 = (center[0], center[1] + np.sqrt(3) * s / 3)

    # set the initial lines
    if degree == 0:
        line_list.append(koch_line(V1, V2, 0))
        line_list.append(koch_line(V2, V3, 2))
        line_list.append(koch_line(V3, V1, 4))
    else:
        line_list.append(koch_line(V1, V2, 5))
        line_list.append(koch_line(V2, V3, 1))
        line_list.append(koch_line(V3, V1, 3))

    for i in range(1, degree):
        # lines produce 4 more lines each
        for _ in range(3 * 4 ** (i - 1)):
            line = line_list.pop(0)
            factor = line['factor']
            line_list.append(koch_line(line['1'], line['2'], factor % 6))  # 1 to 2
            line_list.append(koch_line(line['2'], line['3'], (factor - 1) % 6))  # 2 to 3
            line_list.append(koch_line(line['3'], line['4'], (factor + 1) % 6))  # 3 to 4
            line_list.append(koch_line(line['4'], line['5'], factor % 6))  # 4 to 5

    return line_list
