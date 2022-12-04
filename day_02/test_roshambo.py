import unittest
import roshambo as r

class TestRoshambo(unittest.TestCase):

    def test_decoder_opponent(self):
        # Convert returned zip to list so we can access by index - avoiding for loop in test
        # interpretation for opponent same between Pt 1 or Pt 2
        decoded = list(r.decode_strategy_guide('day_02/testinput.txt', 1)) 
        
        # Test opponent input decoded
        self.assertEqual(decoded[0][0], 'Rock')
        self.assertEqual(decoded[1][0], 'Paper')
        self.assertEqual(decoded[2][0], 'Scissors')
    
    def test_decoder_you_pt1(self):
        decoded = list(r.decode_strategy_guide('day_02/testinput.txt',1))
        
        # Test your input decoded
        self.assertEqual(decoded[0][1], 'Paper')
        self.assertEqual(decoded[1][1], 'Rock')
        self.assertEqual(decoded[2][1], 'Scissors')
    
    def test_decoder_you_pt2(self):
        decoded = list(r.decode_strategy_guide('day_02/testinput.txt',2))

        # Test your input decoded
        self.assertEqual(decoded[0][1], 'Draw')
        self.assertEqual(decoded[1][1], 'Lose')
        self.assertEqual(decoded[2][1], 'Win')

    def test_get_your_shape(self):
        # No need to do full combinations as game outcomes tested elsewhere.
        self.assertEqual(r.get_your_shape(r.ROCK, 'Win'), r.ROCK.loses_against)
        self.assertEqual(r.get_your_shape(r.ROCK, 'Lose'), r.ROCK.wins_against)
        self.assertEqual(r.get_your_shape(r.ROCK, 'Draw'), r.ROCK.shape)

        self.assertEqual(r.get_your_shape(r.PAPER, 'Win'), r.PAPER.loses_against)
        self.assertEqual(r.get_your_shape(r.PAPER, 'Lose'), r.PAPER.wins_against)
        self.assertEqual(r.get_your_shape(r.PAPER, 'Draw'), r.PAPER.shape)


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
    
    def test_tournament_score_pt1(self):
        self.assertEqual(r.play_tournament('day_02/testinput.txt', 1), 15)
    
    def test_tournament_score_pt2(self):
        self.assertEqual(r.play_tournament('day_02/testinput.txt', 2), 12)


if __name__ == '__main__':
    unittest.main()