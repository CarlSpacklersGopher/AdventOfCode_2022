import unittest
import roshambo as r

class TestRoshambo(unittest.TestCase):
    def test_decoder(self):
        decoded = r.decode_strategy_guide('day_02/testinput.txt')
        
        # Test opponent input decoded
        self.assertEqual(decoded[0][0], 'Rock')
        self.assertEqual(decoded[0][1], 'Paper')
        self.assertEqual(decoded[0][2], 'Scissors')

        # Test your input decoded
        self.assertEqual(decoded[1][0], 'Paper')
        self.assertEqual(decoded[1][1], 'Rock')
        self.assertEqual(decoded[1][2], 'Scissors')


    def test_game_outcome(self):
        # Test win
        self.assertEqual(r.determine_win_pts('Scissors', 'Rock'), 6)
        self.assertEqual(r.determine_win_pts('Rock', 'Paper'), 6)
        self.assertEqual(r.determine_win_pts('Paper', 'Scissors'), 6)

        # Test loss
        self.assertEqual(r.determine_win_pts('Paper', 'Rock'), 0)
        self.assertEqual(r.determine_win_pts('Scissors', 'Paper'), 0)
        self.assertEqual(r.determine_win_pts('Rock', 'Scissors'), 0)

        # Test draw
        self.assertEqual(r.determine_win_pts('Rock', 'Rock'), 3)
        self.assertEqual(r.determine_win_pts('Paper', 'Paper'), 3)
        self.assertEqual(r.determine_win_pts('Scissors', 'Scissors'), 3)

    def test_total_game_score(self):
        # No need to do full combinations as game outcome points are tested above.
        # Only need to have game outcome points change to show any specific case is not hardcoded

        # Test Rock
        self.assertEqual(r.calculate_score('Paper', 'Rock'), 1) # Loss
        self.assertEqual(r.calculate_score('Rock', 'Rock'), 1 + 3) # Draw

        # Test Paper
        self.assertEqual(r.calculate_score('Scissors', 'Paper'), 2) # Loss
        self.assertEqual(r.calculate_score('Paper', 'Paper'), 2 + 3) # Draw

        # Test Scissors
        self.assertEqual(r.calculate_score('Rock', 'Scissors'), 3) # Loss
        self.assertEqual(r.calculate_score('Scissors', 'Scissors'), 3 + 3) # Draw
    
    def test_tournament_score(self):
        self.assertEqual(r.play_tournament('day_02/testinput.txt'), 15)


if __name__ == '__main__':
    unittest.main()