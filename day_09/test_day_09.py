
import unittest
import day_09

class TestDay09(unittest.TestCase):

    def setUp(self):
        self.moves = day_09.read_moves('day_09/pt1_testinput.txt')
        self.rope = day_09.Rope(length=2)

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
        day_09.move_rope(self.rope, [(day_09.Direction.RIGHT, 4)])

        unique_locations = self.rope.get_unique_positions()
        self.assertEqual(unique_locations[0], head_locations)
        self.assertEqual(unique_locations[-1], tail_locations)


    def test_day_09_pt1(self):
        day_09.move_rope(self.rope, self.moves)

        self.assertEqual(len(self.rope.get_unique_positions()[1]), 13)

    def test_day_09_pt2(self):
        self.rope = day_09.Rope(length=10)
        self.moves = day_09.read_moves('day_09/pt2_testinput.txt')

        day_09.move_rope(self.rope, self.moves)

        tail_positions = self.rope.get_unique_positions()[-1]
        self.assertEqual(len(tail_positions), 36)

class TestMoveCardinalDirections(unittest.TestCase):

    def setUp(self):
        self.moves = day_09.read_moves('day_09/pt1_testinput.txt')
        self.rope = day_09.Rope(length=2)


    def test_move_up(self):
        move_dir = day_09.Direction.UP
        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_knot = self.rope.trailing_knots[-1]
        tail_position = tail_knot.position

        self.assertEqual(head_position, (0, 1))
        self.assertEqual(tail_position, (0, 0))

        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_position = tail_knot.position

        self.assertEqual(head_position, (0, 2))
        self.assertEqual(tail_position, (0, 1))

    def test_move_down(self):
        move_dir = day_09.Direction.DOWN
        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_knot = self.rope.trailing_knots[-1]
        tail_position = tail_knot.position

        self.assertEqual(head_position, (0, -1))
        self.assertEqual(tail_position, (0, 0))

        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_position = tail_knot.position

        self.assertEqual(head_position, (0, -2))
        self.assertEqual(tail_position, (0, -1))

    def test_move_left(self):
        move_dir = day_09.Direction.LEFT
        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_knot = self.rope.trailing_knots[-1]
        tail_position = tail_knot.position

        self.assertEqual(head_position, (-1, 0))
        self.assertEqual(tail_position, (0, 0))

        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_position = tail_knot.position

        self.assertEqual(head_position, (-2, 0))
        self.assertEqual(tail_position, (-1, 0))

    def test_move_right(self):
        move_dir = day_09.Direction.RIGHT
        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_knot = self.rope.trailing_knots[-1]
        tail_position = tail_knot.position

        self.assertEqual(head_position, (1, 0))
        self.assertEqual(tail_position, (0, 0))

        self.rope.move(move_dir, 1)
        head_position = self.rope.head_knot.position
        tail_position = tail_knot.position

        self.assertEqual(head_position, (2, 0))
        self.assertEqual(tail_position, (1, 0))


class TestTailMoveDiagonal(unittest.TestCase):

    def setUp(self):
        self.moves = day_09.read_moves('day_09/pt1_testinput.txt')
        self.rope = day_09.Rope(length=2)

    def test_move_up_right(self):
        setup_moves = [
            (day_09.Direction.UP, 1),
            (day_09.Direction.RIGHT, 1),
        ]
        for direction, distance in setup_moves:
            self.rope.move(direction, distance)

        # Current positions:
        # Head: (1, 1)
        # Tail: (0, 0)
        self.rope.move(day_09.Direction.RIGHT, 1)

        # Current Head Position: (2, 1)
        tail_knot = self.rope.trailing_knots[-1]
        self.assertEqual(tail_knot.position, (1, 1))

    def test_move_up_left(self):
        setup_moves = [
            (day_09.Direction.UP, 1),
            (day_09.Direction.LEFT, 1),
        ]
        for direction, distance in setup_moves:
            self.rope.move(direction, distance)

        # Current positions:
        # Head: (-1, 1)
        # Tail: (0, 0)
        self.rope.move(day_09.Direction.LEFT, 1)

        # Current Head Position: (-2, 1)
        tail_knot = self.rope.trailing_knots[-1]
        self.assertEqual(tail_knot.position, (-1, 1))

    def test_move_down_left(self):
        setup_moves = [
            (day_09.Direction.DOWN, 1),
            (day_09.Direction.LEFT, 1),
        ]
        for direction, distance in setup_moves:
            self.rope.move(direction, distance)

        # Current positions:
        # Head: (-1, -1)
        # Tail: (0, 0)
        self.rope.move(day_09.Direction.LEFT, 1)

        # Current Head Position: (-2, -1)
        tail_knot = self.rope.trailing_knots[-1]
        self.assertEqual(tail_knot.position, (-1, -1))

    def test_move_down_right(self):
        setup_moves = [
            (day_09.Direction.DOWN, 1),
            (day_09.Direction.RIGHT, 1),
        ]
        for direction, distance in setup_moves:
            self.rope.move(direction, distance)

        # Current positions:
        # Head: (1, -1)
        # Tail: (0, 0)
        self.rope.move(day_09.Direction.RIGHT, 1)

        # Current Head Position: (2, -1)
        tail_knot = self.rope.trailing_knots[-1]
        self.assertEqual(tail_knot.position, (1, -1))


if __name__ == '__main__':
    unittest.main()
