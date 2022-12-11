
import unittest
import day_07

class TestDay07(unittest.TestCase):

    def setUp(self):
        # Build Tree
        self.ROOT = day_07.Node('/')
        self.a = day_07.Node('a')
        self.e = day_07.Node('e')
        self.i = day_07.Node('i', 584)
        self.f = day_07.Node('f', 29116)
        self.g = day_07.Node('g', 2557)
        self.h_lst = day_07.Node('h.lst', 62596)
        self.b_txt = day_07.Node('b.txt', 14848514)
        self.c_dat = day_07.Node('c.dat', 8504156)
        self.d = day_07.Node('d')
        self.j = day_07.Node('j', 4060174)
        self.d_log = day_07.Node('d.log', 8033020)
        self.d_ext = day_07.Node('d.ext', 5626152)
        self.k = day_07.Node('k', 7214296)

        self.ROOT.add_child(self.a)
        self.ROOT.add_child(self.b_txt)
        self.ROOT.add_child(self.c_dat)
        self.ROOT.add_child(self.d)

        self.a.add_child(self.e)
        self.a.add_child(self.f)
        self.a.add_child(self.g)
        self.a.add_child(self.h_lst)
        
        self.e.add_child(self.i)

        self.d.add_child(self.j)
        self.d.add_child(self.d_log)
        self.d.add_child(self.d_ext)
        self.d.add_child(self.k)
    
    def test_tree_build(self):
        day_07.build_file_tree('day_07/testinput.txt')
        self.assertEqual(day_07.ROOT, self.ROOT)

    def test_get_child(self):
        # Get direct child
        self.assertEqual(self.e.get_child('e/i'), self.i) # only child
        self.assertEqual(self.ROOT.get_child('/d'), self.d) # child dir
        self.assertEqual(self.a.get_child('a/g'), self.g) # child file

        # Get distant child
        self.assertEqual(self.ROOT.get_child('/a/e/i'), self.i) # only child
        self.assertEqual(self.ROOT.get_child('/a/e'), self.e) # child dir
        self.assertEqual(self.ROOT.get_child('/d/d.log'), self.d_log) # child file
    
    def test_size(self):
        # test single file
        self.assertEqual(self.i.get_size(), 584) # return size no matter what
        self.assertEqual(self.i.get_size(583), 0) # limit < size
        self.assertEqual(self.i.get_size(585), 584) # limit > size

        # test one layer directory
        dirsize = 4_060_174 + 8_033_020 + 5_626_152 + 7_214_296
        self.assertEqual(self.d.get_size(), dirsize)

        self.d.children_edited = True # force trigger of recalculation
        self.assertEqual(self.d.get_size(8_000_000), dirsize - 8_033_020)

        # test multi-layer directory
        dirsize = 584 + 29_116 + 2557 + 62_596
        self.assertEqual(self.a.get_size(), dirsize)
    
    def test_get_dirs_to_delete(self):
        # test file - should return empty list since not dir
        max_dir_size = self.i.get_size() - 1 # ensure file should be deleted
        deletions = day_07.get_dirs_to_delete(self.i, max_dir_size)
        self.assertEqual(deletions, [])

        # single layer - maxsize > dir size -> delete
        max_dir_size = self.d.get_size() + 1
        deletions = day_07.get_dirs_to_delete(self.d, max_dir_size)
        self.assertEqual(deletions, [self.d])

        # single layer - maxsize == dir size -> delete
        max_dir_size = self.d.get_size()
        deletions = day_07.get_dirs_to_delete(self.d, max_dir_size)
        self.assertEqual(deletions, [self.d])

        # single layer - maxsize < dir size -> don't delete
        max_dir_size = self.d.get_size() - 1
        deletions = day_07.get_dirs_to_delete(self.d, max_dir_size)
        self.assertEqual(deletions, [])

        # multiple layers
        max_dir_size = self.a.get_size() + 1
        deletions = day_07.get_dirs_to_delete(self.a, max_dir_size)
        self.assertEqual(deletions, [self.a, self.e])

        max_dir_size = 100_000
        deletions = day_07.get_dirs_to_delete(self.ROOT, max_dir_size)
        self.assertEqual(deletions, [self.a, self.e])

    def test_day_07_pt1(self):
        actual_size = day_07.get_space_savings(self.ROOT, 100_000)
        self.assertEqual(actual_size, 95437)

    def test_day_07_pt2(self):
        pass

if __name__ == '__main__':
    unittest.main()
