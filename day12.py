class Boat(object):
    def __init__(self, direction):
        self.direction = direction
        self.position = {'N': 0, 'E': 0, 'S': 0, 'W': 0}

    def turn_right(self, value):
        turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        for _ in range(int(value / 90)):
            self.direction = turn[self.direction]
        return self.direction

    def turn_left(self, value):
        turn = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
        for _ in range(int(value / 90)):
            self.direction = turn[self.direction]
        return self.direction

    def forward(self, value):
        self.position[self.direction] += value

    def manhattan(self):
        return abs(self.position['N'] - self.position['S']) + abs(self.position['E'] - self.position['W'])

    def __repr__(self):
        return f'Facing {self.direction}, {self.position["N"]}/{self.position["E"]}/{self.position["S"]}/{self.position["W"]}'


def read_file(buff):
    return ((x[0], int(x[1:])) for x in buff.readlines())


if __name__ == '__main__':
    with open('data/day12.txt', 'r') as in_f:
        lines = read_file(in_f)
    boat = Boat('E')
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
            boat.position[action] += value
        print(boat)
        print()
    print(boat.manhattan())
