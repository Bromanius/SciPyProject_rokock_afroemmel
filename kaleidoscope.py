from snowflake import koch_snowflake
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

snowflakes = []
snowflake_colors = []
num_snowflakes = 1
colors = []
rotate = False
change_speed = 50


def collision(used_centers, used_sizes, center, size):
    """
    asdf
    :param used_centers:
    :param used_sizes:
    :param center:
    :param size:
    :return:
    """
    for i in range(len(used_centers)):
        distance = ((used_centers[i][0] - center[0]) ** 2 + (used_centers[i][1] - center[1]) ** 2) ** 0.5
        if distance <= (used_sizes[i] + size) / 2.2:
            return True
    return False


def rotate_coordinates(x, y, angle_deg):
    """
    asdf
    :param x:
    :param y:
    :param angle_deg:
    :return:
    """
    angle_rad = np.radians(angle_deg)
    new_x = x * np.cos(angle_rad) - y * np.sin(angle_rad)
    new_y = x * np.sin(angle_rad) + y * np.cos(angle_rad)
    return new_x, new_y


def generate_kaleidoscope():
    """
    asdf
    :return:
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
                size = np.random.randint(4, 40)
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
            print("Drawn " + str(successfully_drawn) + " snowflakes until the first didn't fit anymore!")
            break

    for i, snowflake_lines in enumerate(snowflakes):
        # extract the line coordinates
        x, y = [], []
        for line in snowflake_lines:
            x.extend([line['a'][0], line['b'][0], line['c'][0], line['d'][0], line['e'][0]])
            y.extend([line['a'][1], line['b'][1], line['c'][1], line['d'][1], line['e'][1]])

        ax.fill(x, y, color=snowflake_colors[i])

    return tuple()


def update(frame):
    """
    asdf
    :param frame:
    :return:
    """
    global snowflakes
    global num_snowflakes
    global colors
    global rotate
    global change_speed

    ax.clear()  # Clear the plot for each frame

    for i, snowflake_lines in enumerate(snowflakes):
        # extract the line coordinates
        x, y = [], []
        for line in snowflake_lines:
            x.extend([line['a'][0], line['b'][0], line['c'][0], line['d'][0], line['e'][0]])
            y.extend([line['a'][1], line['b'][1], line['c'][1], line['d'][1], line['e'][1]])

        x = np.array(x)
        y = np.array(y)
        for j in range(len(x)):
            x[j], y[j] = rotate_coordinates(x[j], y[j], 12 * frame)

        ax.fill(x, y, color=snowflake_colors[i])
        ax.axis('off')
        'wenn circular vancas auf = spawnsizes setzen'
        ax.set_xlim(-80, 80)  # Setze die x-Achse von 0 bis 10
        ax.set_ylim(-80, 80)  # Setze die y-Achse von -1 bis 1
        # Deaktiviere automatische Anpassung der Achsenskalierung
        ax.autoscale(False)

    return tuple()


if __name__ == "__main__":
    num_snowflakes = int(input("Enter the number of snowflakes: "))
    colors = input("Enter colors for snowflakes (comma-separated): ").split(",")
    rotate = input("Rotate kaleidoscope? (yes/no): ").lower() == "yes"
    change_speed = float(input("Enter kaleidoscope change speed (milliseconds): "))

    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.axis("square")

    if rotate:
        animation = FuncAnimation(fig, update, frames=1000, init_func=generate_kaleidoscope, blit=False,
                                  interval=change_speed)
    else:
        generate_kaleidoscope()

    plt.show()
