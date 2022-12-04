import unittest
import roshambo as r

class TestRoshambo(unittest.TestCase):
    def test_decoder(self):
        # Convert returned zip to list so we can access by index - avoiding for loop in test
        decoded = list(r.decode_strategy_guide('day_02/testinput.txt'))
        
        # Test opponent input decoded
        self.assertEqual(decoded[0][0], r.ROCK)
        self.assertEqual(decoded[1][0], r.PAPER)
        self.assertEqual(decoded[2][0], r.SCISSORS)

        # Test your input decoded
        self.assertEqual(decoded[0][1], r.PAPER)
        self.assertEqual(decoded[1][1], r.ROCK)
        self.assertEqual(decoded[2][1], r.SCISSORS)


    def test_game_outcome(self):
        # Test win
        self.assertEqual(r.determine_win_pts(r.SCISSORS, r.ROCK), 6)
        self.assertEqual(r.determine_win_pts(r.ROCK, r.PAPER), 6)
        self.assertEqual(r.determine_win_pts(r.PAPER, r.SCISSORS), 6)

        # Test loss
        self.assertEqual(r.determine_win_pts(r.PAPER, r.ROCK), 0)
        self.assertEqual(r.determine_win_pts(r.SCISSORS, r.PAPER), 0)
        self.assertEqual(r.determine_win_pts(r.ROCK, r.SCISSORS), 0)

        # Test draw
        self.assertEqual(r.determine_win_pts(r.ROCK, r.ROCK), 3)
        self.assertEqual(r.determine_win_pts(r.PAPER, r.PAPER), 3)
        self.assertEqual(r.determine_win_pts(r.SCISSORS, r.SCISSORS), 3)

    def test_total_game_score(self):
        # No need to do full combinations as game outcome points are tested above.
        # Only need to have game outcome points change to show any specific case is not hardcoded

        # Test Rock
        self.assertEqual(r.calculate_score(r.PAPER, r.ROCK), 1) # Loss
        self.assertEqual(r.calculate_score(r.ROCK, r.ROCK), 1 + 3) # Draw

        # Test Paper
        self.assertEqual(r.calculate_score(r.SCISSORS, r.PAPER), 2) # Loss
        self.assertEqual(r.calculate_score(r.PAPER, r.PAPER), 2 + 3) # Draw

        # Test Scissors
        self.assertEqual(r.calculate_score(r.ROCK, r.SCISSORS), 3) # Loss
        self.assertEqual(r.calculate_score(r.SCISSORS, r.SCISSORS), 3 + 3) # Draw
    
    def test_tournament_score(self):
        self.assertEqual(r.play_tournament('day_02/testinput.txt'), 15)


if __name__ == '__main__':
    unittest.main()