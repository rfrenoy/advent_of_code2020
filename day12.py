import numpy as np
import math


class Boat(object):
    def __init__(self, waypoint):
        self.waypoint = np.array(waypoint)
        self.position = np.array([0, 0])

    def rotation(self, theta):
        self.waypoint = np.matmul(
            np.array([
                np.array([math.cos(theta), -math.sin(theta)]),
                np.array([math.sin(theta), math.cos(theta)])
            ]), self.waypoint)

    def turn_right(self, value):
        for _ in range(int(value / 90)):
            self.rotation(-math.pi / 2)

    def turn_left(self, value):
        for _ in range(int(value / 90)):
            self.rotation(math.pi / 2)

    def forward(self, value):
        self.position = self.position + value * self.waypoint

    def manhattan(self):
        return np.absolute(self.position).sum()

    def __repr__(self):
        return f'Facing {self.waypoint}, {self.position}'


def read_file(buff):
    return ((x[0], int(x[1:])) for x in buff.readlines())


if __name__ == '__main__':
    with open('data/day12.txt', 'r') as in_f:
        lines = read_file(in_f)
    boat = Boat((10, 1))
    for action, value in lines:
        print(boat)
        print(action, value)
        if action == 'L':
            boat.turn_left(value)
        elif action == 'R':
            boat.turn_right(value)
        elif action == 'F':
            boat.forward(value)
        else:
            args = {'N': [1, 1], 'S': [1, -1], 'W': [0, -1], 'E': [0, 1]}
            idx = args[action][0]
            mul = args[action][1]
            boat.waypoint[idx] = boat.waypoint[idx] + mul * value
        print(boat)
        print()
    print(f'Final result is {boat.manhattan()}')
