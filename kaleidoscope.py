import sys

from snowflake import koch_snowflake
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

snowflakes = []  # List for snowflakes
snowflake_colors = []  # Related list for the color of the snowflakes
num_snowflakes = 100  # [INPUT] The number of generated snowflakes. Default value is 100
colors = []  # [INPUT] The list for possible colors
rotate = False  # [INPUT] If the kaleidoscope should rotate or not
changing_colors = False  # [INPUT] If the kaleidoscope should change colors or not
change_speed = 100  # [INPUT] The change speed for the kaleidoscope (milliseconds). Default value is 100


def collision(other_centers, other_sizes, center, size):
    """
    Determines if a snowflake with the center "center" and the size "size" collides with
    one of the other snowflakes
    :param other_centers: The centers of the other snowflakes.
    :param other_sizes: The sizes of the other snowflakes.
    :param center: The center of the snowflake in question.
    :param size: The size of the snowflake in question.
    :return: True if the snowflake in question collides with other snowflakes.
    """
    for i in range(len(other_centers)):
        distance = ((other_centers[i][0] - center[0]) ** 2 + (other_centers[i][1] - center[1]) ** 2) ** 0.5
        if distance <= (other_sizes[i] + size) / 2.2:
            return True
    return False


def rotate_coordinates(x, y, angle_deg):
    """
    Rotates
    :param x:
    :param y:
    :param angle_deg: The angle of rotation in degree
    :return:
    """
    angle_rad = np.radians(angle_deg)
    new_x = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    new_y = x * np.sin(angle_rad) + y * np.cos(angle_rad)
    return new_x, new_y


def generate_kaleidoscope():
    """
    Initializes the kaleidoscope.
    :return: nothing.
    """
    global snowflakes
    global snowflake_colors
    global num_snowflakes
    global colors
    global rotate
    global change_speed

    ax.clear()  # Clear the plot for each frame

    used_centers = []
    used_sizes = []
    successfully_drawn = 0
    for i in range(num_snowflakes):
        center = (np.random.randint(-100, 100), np.random.randint(-100, 100))
        size = np.random.randint(10, 40)
        success = False
        for trys in range(1000):  # Versuche die Schneeflocke zu platzieren
            if collision(used_centers, used_sizes, center, size):
                center = (np.random.randint(-100, 100), np.random.randint(-100, 100))
                if trys % 100 == 0:
                    size = np.random.randint(4, 40 - trys * 0.035)
            else:
                new_snowflake = koch_snowflake(center=center, degree=np.random.randint(1, 5), s=size)
                snowflakes.append(new_snowflake)
                snowflake_colors.append(np.random.choice(colors))
                used_centers.append(center)
                used_sizes.append(size)
                successfully_drawn += 1
                success = True
                break
        if not success:
            print("Not all snowflakes fit the screen! Drawn " + str(successfully_drawn) + " snowflakes.")
            break

    for i, snowflake in enumerate(snowflakes):
        # extract the line coordinates
        x, y = np.empty(len(snowflake) * 5), np.empty(len(snowflake) * 5)
        for b, line in enumerate(snowflake):
            x[b * 5:b * 5 + 5] = [line['a'][0], line['b'][0], line['c'][0], line['d'][0], line['e'][0]]
            y[b * 5:b * 5 + 5] = [line['a'][1], line['b'][1], line['c'][1], line['d'][1], line['e'][1]]

        ax.fill(x, y, color=snowflake_colors[i])

    return tuple()


def update(frame):
    """
    Updates the kaleidoscope.
    :param frame: the current frame.
    :return: nothing.
    """
    global snowflakes
    global num_snowflakes
    global colors
    global rotate
    global change_speed

    ax.clear()  # Clear the plot for each frame

    for i, snowflake in enumerate(snowflakes):
        # extract the line coordinates
        x, y = np.empty(len(snowflake) * 5), np.empty(len(snowflake) * 5)
        for b, line in enumerate(snowflake):
            x[b * 5:b * 5 + 5] = [line['a'][0], line['b'][0], line['c'][0], line['d'][0], line['e'][0]]
            y[b * 5:b * 5 + 5] = [line['a'][1], line['b'][1], line['c'][1], line['d'][1], line['e'][1]]

        if rotate:
            x, y = rotate_coordinates(x, y, 12 * frame)

        if changing_colors:
            ax.fill(x, y, color=np.random.choice(colors))
        else:
            ax.fill(x, y, color=snowflake_colors[i])

        ax.axis('off')
        ax.set_xlim(-80, 80)
        ax.set_ylim(-80, 80)
        ax.autoscale(False)

    return tuple()


if __name__ == "__main__":
    # INPUTS:
    num_snowflakes = int(input("Enter the number of snowflakes (~300 is recommended): "))
    colors = input("Enter colors for snowflakes (comma-separated): ").replace(" ", "").split(",")
    rotate = input("Rotate kaleidoscope? (yes/no): ").lower() == "yes"
    changing_colors = input("Should the kaleidoscope change colors? (yes/no): ").lower() == "yes"
    change_speed = float(input("Enter kaleidoscope change speed in milliseconds (~100ms is recommended): "))

    # Setting up the matplotlib figure
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.axis("square")

    animation = FuncAnimation(fig, update, frames=10, init_func=generate_kaleidoscope, blit=False,
                              interval=change_speed)

    print("Starting calculations... Please don't end the program.")

    #  Saving the plot as gif
    animation.save('Output/animation.gif', writer='imagemagick')

    print("Animation successfully saved!")
