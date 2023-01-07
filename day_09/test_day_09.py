
import unittest
import day_09

class TestDay09(unittest.TestCase):

    def setUp(self):
        self.moves = day_09.read_moves('day_09/testinput.txt')
        self.plank = day_09.Plank()

    def test_location_logging(self):
        head_locations = {
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0)
        }
        tail_locations = {
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        }
        day_09.move_plank(self.plank, [(day_09.Direction.RIGHT, 4)])

        unique_locations = self.plank.get_unique_positions()
        self.assertEqual(unique_locations[0], head_locations)
        self.assertEqual(unique_locations[1], tail_locations)


    def test_day_09_pt1(self):
        day_09.move_plank(self.plank, self.moves)

        self.assertEqual(len(self.plank.get_unique_positions()[1]), 13)

    def test_day_09_pt2(self):
        pass

class TestMoveCardinalDirections(unittest.TestCase):

    def setUp(self):
        self.moves = day_09.read_moves('day_09/testinput.txt')
        self.plank = day_09.Plank()


    def test_move_up(self):
        move_dir = day_09.Direction.UP
        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (0, 1))
        self.assertEqual(tail_position, (0, 0))

        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (0, 2))
        self.assertEqual(tail_position, (0, 1))
        self.plank = day_09.Plank()

    def test_move_down(self):
        move_dir = day_09.Direction.DOWN
        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (0, -1))
        self.assertEqual(tail_position, (0, 0))

        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (0, -2))
        self.assertEqual(tail_position, (0, -1))
        self.plank = day_09.Plank()

    def test_move_left(self):
        move_dir = day_09.Direction.LEFT
        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (-1, 0))
        self.assertEqual(tail_position, (0, 0))

        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (-2, 0))
        self.assertEqual(tail_position, (-1, 0))
        self.plank = day_09.Plank()

    def test_move_right(self):
        move_dir = day_09.Direction.RIGHT
        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (1, 0))
        self.assertEqual(tail_position, (0, 0))

        self.plank.move(move_dir, 1)
        head_position = self.plank.head_position
        tail_position = self.plank.tail_position

        self.assertEqual(head_position, (2, 0))
        self.assertEqual(tail_position, (1, 0))


class TestTailMoveDiagonal(unittest.TestCase):

    def setUp(self):
        self.moves = day_09.read_moves('day_09/testinput.txt')
        self.plank = day_09.Plank()

    def test_move_up_right(self):
        setup_moves = [
            (day_09.Direction.UP, 1),
            (day_09.Direction.RIGHT, 1),
        ]
        for direction, distance in setup_moves:
            self.plank.move(direction, distance)

        # Current positions:
        # Head: (1, 1)
        # Tail: (0, 0)
        self.plank.move(day_09.Direction.RIGHT, 1)

        # Current Head Position: (2, 1)
        self.assertEqual(self.plank.tail_position, (1, 1))
        self.plank = day_09.Plank()

    def test_move_up_left(self):
        setup_moves = [
            (day_09.Direction.UP, 1),
            (day_09.Direction.LEFT, 1),
        ]
        for direction, distance in setup_moves:
            self.plank.move(direction, distance)

        # Current positions:
        # Head: (-1, 1)
        # Tail: (0, 0)
        self.plank.move(day_09.Direction.LEFT, 1)

        # Current Head Position: (-2, 1)
        self.assertEqual(self.plank.tail_position, (-1, 1))
        self.plank = day_09.Plank()

    def test_move_down_left(self):
        setup_moves = [
            (day_09.Direction.DOWN, 1),
            (day_09.Direction.LEFT, 1),
        ]
        for direction, distance in setup_moves:
            self.plank.move(direction, distance)

        # Current positions:
        # Head: (-1, -1)
        # Tail: (0, 0)
        self.plank.move(day_09.Direction.LEFT, 1)

        # Current Head Position: (-2, -1)
        self.assertEqual(self.plank.tail_position, (-1, -1))
        self.plank = day_09.Plank()

    def test_move_down_right(self):
        setup_moves = [
            (day_09.Direction.DOWN, 1),
            (day_09.Direction.RIGHT, 1),
        ]
        for direction, distance in setup_moves:
            self.plank.move(direction, distance)

        # Current positions:
        # Head: (1, -1)
        # Tail: (0, 0)
        self.plank.move(day_09.Direction.RIGHT, 1)

        # Current Head Position: (2, -1)
        self.assertEqual(self.plank.tail_position, (1, -1))


if __name__ == '__main__':
    unittest.main()
