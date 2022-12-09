
import unittest
import day_06

class TestDay06(unittest.TestCase):

    def test_day_06_pt1(self):
        self.assertEqual(day_06.find_message_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4), 7)
        self.assertEqual(day_06.find_message_start('bvwbjplbgvbhsrlpgdmjqwftvncz', 4), 5)
        self.assertEqual(day_06.find_message_start('nppdvjthqldpwncqszvftbrmjlhg', 4), 6)
        self.assertEqual(day_06.find_message_start('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4), 10)
        self.assertEqual(day_06.find_message_start('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4), 11)
        

    def test_day_06_pt2(self):
        self.assertEqual(day_06.find_message_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14), 19)
        self.assertEqual(day_06.find_message_start('bvwbjplbgvbhsrlpgdmjqwftvncz', 14), 23)
        self.assertEqual(day_06.find_message_start('nppdvjthqldpwncqszvftbrmjlhg', 14), 23)
        self.assertEqual(day_06.find_message_start('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14), 29)
        self.assertEqual(day_06.find_message_start('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14), 26)

if __name__ == '__main__':
    unittest.main()
