import numpy as np


def define_regions(board, deep, deep_map, player_point, player_number):
    if deep_map[player_point[0]][player_point[1]] > deep:
        board[player_point[0]][player_point[1]] = player_number
        deep_map[player_point[0]][player_point[1]] = deep
    elif deep_map[player_point[0]][player_point[1]] == deep and \
            board[player_point[0]][player_point[1]] != player_number:
        board[player_point[0]][player_point[1]] = -5
        return
    else:
        return

    x, y = player_point
    x_max, y_max = len(board), len(board[0])
    define_regions(board, deep+1, deep_map, [(x+1) % x_max, y], player_number)
    define_regions(board, deep+1, deep_map, [(x-1) % x_max, y], player_number)
    define_regions(board, deep+1, deep_map, [x, (y+1) % y_max], player_number)
    define_regions(board, deep+1, deep_map, [x, (y-1) % y_max], player_number)


if __name__ == "__main__":
    matrix = np.zeros((10, 10))
    deep_matrix = np.zeros((10, 10)) + 99

    for i in range(len(matrix[0])):
        matrix[4][i] = -1
        deep_matrix[4][i] = 0

    define_regions(matrix, 0, deep_matrix, [2, 1], 1)
    define_regions(matrix, 0, deep_matrix, [8, 2], 2)
    define_regions(matrix, 0, deep_matrix, [2, 8], 3)
    define_regions(matrix, 0, deep_matrix, [8, 8], 4)
    print(matrix)
