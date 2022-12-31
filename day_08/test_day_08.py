
import unittest
import numpy as np
import day_08

class TestDay08(unittest.TestCase):

    def setUp(self):
        self.trees = [
            [3, 0, 3, 7, 3],
            [2, 5, 5, 1, 2],
            [6, 5, 3, 3, 2],
            [3, 3, 5, 4, 9],
            [3, 5, 3, 9, 0],
        ]

    def test_file_read(self):
        filepath = 'day_08/testinput.txt'
        actual = day_08.get_tree_heights(filepath)
        self.assertEqual(actual, self.trees)

    def test_tree_visibility(self):
        # test single row visibility
        first_row = self.trees[0]
        expected_vis = [True, False, False, True, False]
        actual_vis = day_08.get_row_visibilities(first_row)
        self.assertEqual(actual_vis, expected_vis)

        # test 2D map visibility
        expected_vis = [
            [True, False, False, True,  False],
            [True, True,  False, False, False],
            [True, False, False, False, False],
            [True, False, True,  False, True ],
            [True, True,  False, True,  False]
        ]
        actual_vis = day_08.get_tree_visibilities(self.trees)
        self.assertEqual(actual_vis, expected_vis)


    def test_visibility_from_north(self):        
        expected_vis = [
            [True,  True,  True,  True,  True ],
            [False, True,  True,  False, False],
            [True,  False, False, False, False],
            [False, False, False, False, True ],
            [False, False, False, True,  False]
        ]
        actual_vis = day_08.get_visibility_from_north(self.trees)
        self.assertEqual(actual_vis, expected_vis)
    
    def test_visibility_from_south(self):
        expected_vis = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [True,  False, False, False, False],
            [False, False, True,  False, True ],
            [True,  True,  True,  True,  True ]
        ]
        actual_vis = day_08.get_visibility_from_south(self.trees)
        self.assertEqual(actual_vis, expected_vis)
        
    def test_visibility_from_east(self):
        expected_vis = [
            [False, False, False, True,  True],
            [False, False, True,  False, True],
            [True,  True,  False, True,  True],
            [False, False, False, False, True],
            [False, False, False, True,  True]
        ]
        actual_vis = day_08.get_visibility_from_east(self.trees)
        self.assertEqual(actual_vis, expected_vis)
    
    def test_visibility_from_west(self):
        expected_vis = [
            [True, False, False, True,  False],
            [True, True,  False, False, False],
            [True, False, False, False, False],
            [True, False, True,  False, True ],
            [True, True,  False, True,  False]
        ]
        actual_vis = day_08.get_visibility_from_west(self.trees)
        self.assertEqual(actual_vis, expected_vis)

    def test_view_distance(self):
        #test edge
        self.assertEqual(day_08.view_distance(3, []), 0)

        north_trees = [3]
        south_trees = [3, 5, 3]
        east_trees = [1, 2]
        west_trees = [5, 2]

        self.assertEqual(day_08.view_distance(5, north_trees), 1)
        self.assertEqual(day_08.view_distance(5, south_trees), 2)
        self.assertEqual(day_08.view_distance(5, east_trees), 2)
        self.assertEqual(day_08.view_distance(5, west_trees), 1)


    def test_day_08_pt1(self):
        self.assertEqual(day_08.count_visible_trees(self.trees), 21)

    def test_day_08_pt2(self):
        pass

if __name__ == '__main__':
    unittest.main()
