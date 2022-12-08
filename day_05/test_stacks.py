import unittest
import stacks as s

class TestStacks(unittest.TestCase):
    
    def test_stack_read(self):
        actual_stacks = s.get_starting_stacks('day_05/testinput.txt')
        anticipated_stacks = [
            [],
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]
        self.assertEqual(actual_stacks[0], anticipated_stacks[0])
        self.assertEqual(actual_stacks[1], anticipated_stacks[1])
        self.assertEqual(actual_stacks[2], anticipated_stacks[2])
        self.assertEqual(actual_stacks[3], anticipated_stacks[3])

    def test_instruction_read(self):
        move1 = s.Move(source=2, destination=1, boxes=1)
        move2 = s.Move(source=1, destination=3, boxes=3)
        move3 = s.Move(source=2, destination=1, boxes=2)
        move4 = s.Move(source=1, destination=2, boxes=1)
        
        actual_moves = s.get_moves('day_05/testinput.txt')

        self.assertEqual(actual_moves[0], move1)
        self.assertEqual(actual_moves[1], move2)
        self.assertEqual(actual_moves[2], move3)
        self.assertEqual(actual_moves[3], move4)

    def test_move1package_individually(self):
        stacks = [
            [],
            ['Z', 'N'],
            ['M', 'C', 'D'],
        ]

        anticipated_stacks = [
            [],
            ['Z'],
            ['M', 'C', 'D', 'N'],
        ]

        move = s.Move(source=1, destination=2, boxes=1)
        s.move_packages_individually(stacks, move)

        self.assertEqual(stacks[1], anticipated_stacks[1])
        self.assertEqual(stacks[2], anticipated_stacks[2])
    
    def test_move_multiple_packages_individually(self):
        stacks = [
            [],
            ['Z', 'N'],
            ['M', 'C', 'D'],
        ]

        anticipated_stacks = [
            [],
            ['Z', 'N', 'D', 'C'],
            ['M'],
        ]

        move = s.Move(source=2, destination=1, boxes=2)
        s.move_packages_individually(stacks, move)

        self.assertEqual(stacks[1], anticipated_stacks[1])
        self.assertEqual(stacks[2], anticipated_stacks[2])
    
    def test_move1package_stack(self):
        stacks = [
            [],
            ['Z', 'N'],
            ['M', 'C', 'D'],
        ]

        anticipated_stacks = [
            [],
            ['Z'],
            ['M', 'C', 'D', 'N'],
        ]

        move = s.Move(source=1, destination=2, boxes=1)
        s.move_package_stacks(stacks, move)

        self.assertEqual(stacks[1], anticipated_stacks[1])
        self.assertEqual(stacks[2], anticipated_stacks[2])
    
    def test_move_multiple_packages_stacks(self):
        stacks = [
            [],
            ['Z', 'N'],
            ['M', 'C', 'D'],
        ]

        anticipated_stacks = [
            [],
            ['Z', 'N', 'C', 'D'],
            ['M'],
        ]

        move = s.Move(source=2, destination=1, boxes=2)
        s.move_package_stacks(stacks, move)

        self.assertEqual(stacks[1], anticipated_stacks[1])
        self.assertEqual(stacks[2], anticipated_stacks[2])
    
    def test_top_boxes(self):
        stacks = [
            [],
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]

        actual_top_boxes = s.get_top_boxes(stacks)

        self.assertEqual(actual_top_boxes, 'NDP')

    def test_rearrange_pt1(self):
        actual_top_boxes = s.rearrange_crates('day_05/testinput.txt', 1)

        self.assertEqual(actual_top_boxes, 'CMZ')

    def test_rearrange_pt2(self):
        actual_top_boxes = s.rearrange_crates('day_05/testinput.txt', 2)

        self.assertEqual(actual_top_boxes, 'MCD')
    

if __name__ == '__main__':
    unittest.main()