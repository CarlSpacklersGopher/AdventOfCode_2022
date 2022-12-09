
import unittest
import day_06

class TestDay06(unittest.TestCase):

    def test_day_06_pt1(self):
        self.assertEqual(day_06.find_message_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb'), 7)
        self.assertEqual(day_06.find_message_start('bvwbjplbgvbhsrlpgdmjqwftvncz'), 5)
        self.assertEqual(day_06.find_message_start('nppdvjthqldpwncqszvftbrmjlhg'), 6)
        self.assertEqual(day_06.find_message_start('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 10)
        self.assertEqual(day_06.find_message_start('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 11)
        

    def test_day_06_pt2(self):
        pass

if __name__ == '__main__':
    unittest.main()
