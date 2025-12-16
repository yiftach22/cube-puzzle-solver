import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# mpl.use('TkAgg')

CUBE_SIZE = 5
PARTS = [
    np.array([[[1, 0], [1, 0], [1, 0], [1, 0], [1, 0]],
              [[0, 0], [1, 1], [1, 1], [1, 1], [1, 0]]]),

    np.array([[[0, 0], [2, 2], [2, 2], [2, 2]],
              [[2, 0], [2, 0], [2, 0], [2, 0]]]),

    np.array([[[0, 0], [7, 0], [7, 0], [7, 0]],
              [[7, 0], [7, 7], [7, 7], [7, 7]]]),

    np.array([[[8, 0], [8, 0], [8, 0], [8, 0]],
              [[8, 0], [8, 8], [8, 8], [8, 8]]]),

    np.array([[[9, 0], [9, 0], [9, 0], [9, 0]],
              [[9, 0], [9, 9], [9, 9], [9, 0]]]),

    np.array([[[0, 0], [10, 0], [10, 0], [10, 0]],
              [[10, 10], [10, 10], [10, 10], [10, 0]]]),

    np.array([[[11, 0], [11, 0], [11, 0]],
              [[11, 11], [11, 11], [11, 11]]]),

    np.array([[[12, 0], [12, 0], [12, 0]],
              [[12, 0], [12, 12], [12, 12]]]),

    np.array([[[0, 0], [0, 0], [13, 13]],
              [[13, 0], [13, 0], [13, 0]]]),

    np.array([[[3, 0], [3, 0], [3, 0], [3, 0]],
              [[0, 0], [3, 3], [3, 3], [3, 3]]]),

    np.array([[[4, 0], [4, 0], [4, 0], [4, 0]],
              [[0, 0], [4, 4], [4, 4], [4, 4]]]),

    np.array([[[5, 0], [5, 0], [5, 0], [5, 0]],
              [[0, 0], [5, 5], [5, 5], [5, 5]]]),

    np.array([[[6, 0], [6, 0], [6, 0], [6, 0]],
              [[0, 0], [6, 6], [6, 6], [6, 6]]]),
]




def check_placement(result , placed_part):
    """
    Check if a placement of a part is legal - it does not overlap other existing parts.
    If the placed part overlaps previews result, the result of this multiplication in the overlapping cells will be
    negative, otherwise it will be zero or positive.
    :return: true if the placement is legal, false otherwise
    """
    return not np.any((placed_part*-1)*result < 0)



def solve(result, current_level, left_parts, run_number):
    """
    A recursive function, getting as params the previews result (a partially solved cube), the current level to work on,
    a list of the parts left to insert and a run_number for debug/process following purposes.
    :param result: a CUBE_SIZE sized partially solved cube, nas a numpy array
    :param current_level: the current level, 0 to CUBE_SIZE-1
    :param left_parts: list of left parts, as a numpy array
    :param run_number: the number of moves done so far
    :return: a solved cube
    """
    # visualize_cube(result)
    empty_spots = np.argwhere(result[:,:,current_level] == 0)
    if empty_spots.size == 0:
        if current_level == CUBE_SIZE -1:
            return result
        return solve(result, current_level + 1, left_parts, run_number)
    spot = empty_spots[0]
    for part_index, part in enumerate(left_parts):
        rotations = all_rotations(part)
        for rotation in rotations:
            for i in range(rotation.shape[0]):
                if spot[0] - i + rotation.shape[0] > CUBE_SIZE or spot[0] -i <0:
                    continue
                for j in range(rotation.shape[1]):
                    if spot[1] - j + rotation.shape[1] > CUBE_SIZE or spot[1] -j <0:
                        continue
                    padded_part = np.zeros((CUBE_SIZE, CUBE_SIZE, CUBE_SIZE))
                    padded_part[:rotation.shape[0], :rotation.shape[1], :rotation.shape[2]] = rotation
                    placed_part = np.roll(padded_part, -i + spot[0], axis=0)
                    placed_part = np.roll(placed_part, -j + spot[1], axis=1)
                    placed_part = np.roll(placed_part, current_level, axis=2)
                    if placed_part[spot[0], spot[1], current_level] == 0:
                        continue
                    if check_placement(result, placed_part):
                        # if run_number[0]%500 == 0:
                            # print(run_number[0])
                            # visualize_cube(result)
                        new_left_parts = left_parts.copy()
                        del new_left_parts[part_index]
                        run_number[0] = run_number[0] + 1
                        new_result =  solve(result + placed_part, current_level, new_left_parts, run_number)
                        if new_result is not None:
                            return new_result
    return None


def all_rotations(part):
    """
    returns a list of all possible rotations of the part.
    :param part: numpy 3D array representing the part.
    :return: parts list
    """
    rotations = []

    def add_if_new(p):
        for r in rotations:
            if np.array_equal(r, p):
                return
        rotations.append(p)


    for k in range(4):
        p = np.rot90(part, k, axes=(1, 2))
        add_if_new(p)
        p2 = np.rot90(p, 1, axes=(0, 2))
        add_if_new(p2)
        p3 = np.rot90(p, 2, axes=(0, 2))
        add_if_new(p3)
        p4 = np.rot90(p, 3, axes=(0, 2))
        add_if_new(p4)
        p5 = np.rot90(p, 1, axes=(0, 1))
        add_if_new(p5)
        p6 = np.rot90(p, 3, axes=(0, 1))
        add_if_new(p6)

    return rotations


def visualize_cube(cube):
    """
    Plots the cube using matplotlib, each part in a different color.
    :param cube: 3D numpy array representing the cube.
    """
    color_list = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
    part_to_color = {}

    filled = cube > 0
    colors = np.empty(cube.shape, dtype=object)

    for idx, label in np.ndenumerate(cube):
        if label > 0:
            if label not in part_to_color:
                part_to_color[label] = color_list[int((label-1) % len(color_list))]
            colors[idx] = part_to_color[label]
        else:
            colors[idx] = 'white'

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(filled, facecolors=colors, edgecolor='k')

    max_range = max(cube.shape)
    ax.set_xlim(0, max_range)
    ax.set_ylim(0, max_range)
    ax.set_zlim(0, max_range)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    plt.show()


def main():
    result = np.zeros((CUBE_SIZE, CUBE_SIZE, CUBE_SIZE), dtype=np.uint8)
    left_parts = PARTS.copy()
    result = solve(result, 0, left_parts, [0])
    print (result)
    visualize_cube(result)
    show_result(result)


def show_result(result):
    """
    Shows the result piece by piece.
    """
    current = np.zeros((CUBE_SIZE, CUBE_SIZE, CUBE_SIZE), dtype=np.uint8)
    level = 0
    while level < CUBE_SIZE:
        empty_spots = np.argwhere(current[:, :, level] == 0)
        if empty_spots.size == 0:
            level += 1
            continue
        spot = empty_spots[0]
        part_number = result[spot[0], spot[1], level]
        part_locations = np.argwhere(result[:,:,:] == part_number)
        for location in part_locations:
            current[location[0], location[1], location[2]] = part_number

        visualize_cube(current)


main()



