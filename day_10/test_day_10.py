
import unittest
import day_10

class TestDay10(unittest.TestCase):

    def setUp(self):
        self.cpu = day_10.CPU(list(range(20, 220+1, 40)))
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


    def test_day_10_pt1(self):
        day_10.execute_instructions(self.cpu, self.instructions)
        sum_signals = day_10.sum_signal_strengths(self.cpu)
        self.assertEqual(sum_signals, 13140)

    def test_day_10_pt2(self):
        pass

if __name__ == '__main__':
    unittest.main()
