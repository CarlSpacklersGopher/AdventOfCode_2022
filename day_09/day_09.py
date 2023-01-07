from enum import Enum
import math

class Direction(Enum):
    # values are unit x,y moves
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Rope:
    def __init__(self, length: int):
        self.head_knot = Knot()
        self.trailing_knots = []

        for _ in range(length - 1):
            self.trailing_knots.append(Knot())

    def move(self, direction: Direction, distance:int) -> None:
        for _ in range(distance):
            self.head_knot.move_direction(direction)
            leading_knot_position = self.head_knot.position
            for knot in self.trailing_knots:
                if knot.should_move(leading_knot_position):
                    knot.follow_leading_knot(leading_knot_position)
                leading_knot_position = knot.position

            self.log_positions()

    def log_positions(self) -> None:
        self.head_knot.log_position()
        for knot in self.trailing_knots:
            knot.log_position()

    def get_unique_positions(self) -> list[set]:
        histories = [set(self.head_knot.history)]
        for knot in self.trailing_knots:
            histories.append(set(knot.history))
        return histories

class Knot:

    def __init__(self):
        self.position = (0, 0)
        self.history = [self.position]

    def move_direction(self, direction: Direction):
        new_x = self.position[0] + direction.value[0]
        new_y = self.position[1] + direction.value[1]
        self.position = (new_x, new_y)

    def follow_leading_knot(self, leading_knot_position: tuple):
        relative_x = leading_knot_position[0] - self.position[0]
        relative_y = leading_knot_position[1] - self.position[1]

        x_to_move = relative_x
        y_to_move = relative_y

        if abs(relative_x) > 1: # Need to move in this direction.
            x_to_move = math.copysign(1, relative_x) # Can only move 1 space in any direction
        if abs(relative_y) > 1:
            y_to_move = math.copysign(1, relative_y)

        new_tail_x = self.position[0] + int(x_to_move)
        new_tail_y = self.position[1] + int(y_to_move)

        self.position = (new_tail_x, new_tail_y)

    def should_move(self, other_position: tuple):
        return (abs(other_position[0] - self.position[0]) > 1 or
                abs(other_position[1] - self.position[1]) > 1)

    def log_position(self):
        self.history.append(self.position)


def read_moves(filepath:str) -> list[tuple]:
    moves = []
    with open(filepath, 'r') as f:
        for line in f:
            abbreviation, distance = line.split()
            direction = direction_lookup(abbreviation)
            moves.append((direction, int(distance)))
    return moves

def move_rope(rope:Rope, moves: list[tuple]):
    for direction, distance in moves:
        rope.move(direction, distance)

def direction_lookup(abbreviation:str):
    if abbreviation == 'U':
        return Direction.UP
    elif abbreviation == 'D':
        return Direction.DOWN
    elif abbreviation == 'L':
        return Direction.LEFT
    elif abbreviation == 'R':
        return Direction.RIGHT



def main():
    moves = read_moves('day_09/input.txt')
    rope = Rope(length=2)
    move_rope(rope, moves)
    pt1 = len(rope.get_unique_positions()[-1])
    print('Part 1: ' + str(pt1))

    rope = Rope(length=10)
    move_rope(rope, moves)
    pt2 = len(rope.get_unique_positions()[-1])
    print('Part 2: ' + str(pt2))


if __name__ == '__main__':
    main()
