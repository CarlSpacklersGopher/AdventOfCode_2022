
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
    

    def test_day_07_pt1(self):
        print('e:\n')
        print(self.e)

        print('a:\n')
        print(self.a)

        print('ROOT:\n')
        print(self.ROOT)

    def test_day_07_pt2(self):
        pass

if __name__ == '__main__':
    unittest.main()
