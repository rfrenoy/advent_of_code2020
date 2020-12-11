import numpy as np
import copy


char_values = {'L': 0,
               '.': 0,
               '#': 1,
               '0.0': 0}

def read_file(buff):
    return np.array([np.array([y for y in x[:-1]]) 
        for x in buff.readlines()])

def occupied_neighboor(mat, i, j):
    res = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if k == l == 0:
                continue
            res += char_values[mat[i+k][j+l]]
    return res

def nb_adjacent_occupied_seats(mat):
    work = copy.deepcopy(mat)
    work = np.vstack([np.zeros(work.shape[1]), work, np.zeros(work.shape[1])])
    work = np.hstack([np.zeros((work.shape[0], 1)), work, np.zeros((work.shape[0], 1))])
    res = []
    for i in range(1, work.shape[0]-1):
        line = []
        for j in range(1, work.shape[1]-1):
            line.append(occupied_neighboor(work, i, j))
        res.append(line)
    return np.array(res)

def occupied_seats(mat):
    res = 0
    for l in mat:
        for c in l:
            if c == '#':
                res += 1
    return res
            
def new_mat(occupied, mat):
    res = copy.deepcopy(mat)
    for i in range(occupied.shape[0]):
        for j in range(occupied.shape[1]):
            if mat[i][j] == 'L' and occupied[i][j] == 0:
                res[i][j] = '#'
            if mat[i][j] == '#' and occupied[i][j] >= 4:
                res[i][j] = 'L'
    return res


if __name__ == '__main__':
    with open('data/day11.txt', 'r') as in_f:
        arr = read_file(in_f)
        new_arr = copy.deepcopy(arr)
        while True:
            arr = new_arr
            occupied = nb_adjacent_occupied_seats(arr)
            new_arr = new_mat(occupied, arr)
            if (arr == new_arr).all():
                break
        print(occupied_seats(arr))
