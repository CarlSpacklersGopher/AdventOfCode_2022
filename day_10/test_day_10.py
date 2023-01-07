
import unittest
import day_10

class TestDay10(unittest.TestCase):

    def setUp(self):
        self.screen = day_10.CRT(rows=6, pixels_per_row=40)
        self.cpu = day_10.CPU(interesting_cycles=list(range(20, 220+1, 40)), screen=self.screen)
        self.instructions = day_10.read_instructions('day_10/testinput.txt')


    def test_noop(self):
        self.cpu.noop()
        self.assertEqual(self.cpu.cycles, 1)

    def test_addx(self):
        self.cpu.addx(15)
        self.assertEqual(self.cpu.register, 1 + 15)

        self.cpu.addx(-4)
        self.assertEqual(self.cpu.register, 1 + 15 - 4)

    def test_strength_logging(self):
        for _ in range(15):
            self.cpu.tick()

        self.cpu.addx(3) # Ticks = 17, register updated
        self.assertEqual(self.cpu.interesting_signal_strengths, []) # Verify not logged

        self.cpu.addx(4) # Ticks = 19, register updated
        self.cpu.tick()
        self.assertEqual(self.cpu.interesting_signal_strengths, [(1 + 3 + 4) * 20]) # Verify logged

    def test_screen_print(self):
        expected = ''
        for _ in range(6):
            expected += '.' * self.screen.pixels_per_row + '\n'

        self.assertEqual(str(self.screen), expected)

    def test_draw_pixel(self):
        expected_screen = ['#......................................#',
                           '#.......................................',
                           '........................................',
                           '........................................',
                           '.....#..................................',
                           '........................................']

        self.screen.draw_pixel(cycle=0, sprite_position=1) # first row, first pixel lit
        self.screen.draw_pixel(cycle=39, sprite_position=38) # first row, last pixel lit
        self.screen.draw_pixel(cycle=40, sprite_position=1) # second row, first pixel lit
        self.screen.draw_pixel(cycle=165, sprite_position=5) # fifth row, sixth pixel lit

        self.screen.draw_pixel(cycle=166, sprite_position=164) # not lit
        self.screen.draw_pixel(cycle=166, sprite_position=168) # not lit

        expected_screen = '\n'.join(expected_screen) + '\n'

        self.assertEqual(str(self.screen), expected_screen)


    def test_day_10_pt1(self):
        day_10.execute_instructions(self.cpu, self.instructions)
        sum_signals = day_10.sum_signal_strengths(self.cpu)
        self.assertEqual(sum_signals, 13140)



    def test_day_10_pt2(self):
        expected = ['##..##..##..##..##..##..##..##..##..##..',
                    '###...###...###...###...###...###...###.',
                    '####....####....####....####....####....',
                    '#####.....#####.....#####.....#####.....',
                    '######......######......######......####',
                    '#######.......#######.......#######.....']

        expected_str = '\n'.join(expected) + '\n'
        day_10.execute_instructions(self.cpu, self.instructions)
        self.assertEqual(str(self.screen), expected_str)

if __name__ == '__main__':
    unittest.main()
