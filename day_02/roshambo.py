import collections

Shape = collections.namedtuple('Shape', ['shape', 'points', 'wins_against', 'loses_against'])

ROCK = Shape(shape         = 'Rock', 
             points        = 1,
             wins_against  = 'Scissors',
             loses_against = 'Paper')

PAPER = Shape(shape         = 'Paper', 
              points        = 2,
              wins_against  = 'Rock',
              loses_against = 'Scissors')

SCISSORS = Shape(shape         = 'Scissors', 
                 points        = 3,
                 wins_against  = 'Paper',
                 loses_against = 'Rock')


opponent_decoder = {'A':ROCK,
                    'B':PAPER,
                    'C':SCISSORS}

your_decoder = {'X':ROCK,
                'Y':PAPER,
                'Z':SCISSORS}

def calculate_score(opponent:Shape, you:Shape) -> int:
    '''
    Calculates your score for a given game of Rock Paper Scissors
    '''
    return determine_win_pts(opponent, you) + you.points

def determine_win_pts(opponent:Shape, you:Shape) -> int:
    '''
    Returns points earned from result of the game of Rock Paper Scissors
    Loss: 0, Draw: 3, Win: 6
    '''
    win_points = 6
    draw_points = 3
    loss_points = 0

    if you == opponent:
        return draw_points
    elif opponent.shape == you.wins_against:
        return win_points
    else:
        return loss_points


def decode_strategy_guide(filepath:str) -> zip:
    '''
    Translates Strategy Guide to Human Readable Format
    Returns zip object - first object for each is opponent, second is you
    '''
    opponent_inputs = []
    your_inputs = []
    with open(filepath, 'r') as file:
        for line in file:
            opponent_code, your_code = line.strip().split()
            opponent_inputs.append(opponent_decoder[opponent_code])
            your_inputs.append(your_decoder[your_code])
    
    return zip(opponent_inputs, your_inputs, strict=True)


def play_tournament(filepath:str) -> int:
    '''
    Returns your total score for all games in Rock Paper Scissors tournament
    '''
    game_scores = []
    strategy_guide = decode_strategy_guide(filepath)
    for opponent, you in strategy_guide:
        game_score = calculate_score(opponent, you)
        game_scores.append(game_score)
    return sum(game_scores)

if __name__ == '__main__':
    tourney_score = play_tournament('day_02/input.txt')
    print('Tournament Score: ' + str(tourney_score))