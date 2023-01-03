from enum import Enum

class Direction(Enum):
    # values are unit x,y moves
    UP = (0, 1) 
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
        

class Plank:
    def __init__(self, length: int=1):
        self.length = length
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.head_history = []
        self.tail_history = []

    def move(self, direction: Direction, distance:int) -> None:
        for _ in range(distance):
            self._move_head(direction, distance)
            if self._tail_should_move():
                self._move_tail()

            self.log_positions()
    
    def _move_head(self, direction: Direction, distance:int) -> None:
        new_x = self.head_position[0] + direction.value[0]
        new_y = self.head_position[1] + direction.value[1]
        self.head_position = (new_x, new_y)


    def _move_tail(self):
        # tail follows head around
        self.tail_position = self.head_history[-1]

    def _tail_should_move(self) -> bool:
        return (abs(self.head_position[0] - self.tail_position[0]) > self.length or
                abs(self.head_position[1] - self.tail_position[1]) > self.length)
            
    def log_positions(self) -> None:
        self.head_history.append(self.head_position)
        self.tail_history.append(self.tail_position)

    def get_unique_positions(self) -> tuple[set]:
        return (set(self.head_history), set(self.tail_history))


def read_moves(filepath:str) -> list[tuple]:
    moves = []
    with open(filepath, 'r') as f:
        for line in f:
            abbreviation, distance = line.split()
            direction = direction_lookup(abbreviation)
            moves.append((direction, int(distance)))
    return moves

def move_plank(plank:Plank, moves: list[tuple]):
    for direction, distance in moves:
        plank.move(direction, distance)

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
    plank = Plank(length=1)
    move_plank(plank, moves)
    pt1 = len(plank.get_unique_positions()[1])
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))


if __name__ == '__main__':
    main()
    