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

opponent_decoder = {'A':'Rock',
                    'B':'Paper',
                    'C':'Scissors'}

your_decoder_pt1 = {'X':'Rock',
                    'Y':'Paper',
                    'Z':'Scissors'}

your_decoder_pt2 = {'X':'Lose',
                    'Y':'Draw',
                    'Z':'Win'}

rps_lookup = {'Rock'     :ROCK,
              'Paper'    :PAPER,
              'Scissors' :SCISSORS}

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


def decode_strategy_guide(filepath:str, pt1_2:int) -> zip:
    '''
    Translates Strategy Guide to Human Readable Format
    Returns zip object - first object for each is opponent, second is you
    '''
    opponent_inputs = []
    your_inputs = []
    if pt1_2 == 1:
        your_decoder = your_decoder_pt1
    else:
        your_decoder = your_decoder_pt2

    with open(filepath, 'r') as file:
        for line in file:
            opponent_code, your_code = line.strip().split()
            opponent_inputs.append(opponent_decoder[opponent_code])
            your_inputs.append(your_decoder[your_code])
    
    return zip(opponent_inputs, your_inputs, strict=True)

def get_your_shape(opponent:Shape, your_strategy:str) -> str:
    '''
    Returns the name of the shape you need to throw based on what opponent is throwing and your strategy
    '''
    your_shape = None
    if your_strategy == 'Draw':
        your_shape = opponent.shape
    elif your_strategy == 'Lose':
        your_shape = opponent.wins_against
    else: # Win
        your_shape = opponent.loses_against
    return your_shape

def play_tournament(filepath:str, pt1_2:int) -> int:
    '''
    Returns your total score for all games in Rock Paper Scissors tournament
    '''
    game_scores = []
    strategy_guide = decode_strategy_guide(filepath, pt1_2)
    for opponent_shape_str, strategy in strategy_guide:
        opponent = rps_lookup[opponent_shape_str] # Get Shape object from name
        if pt1_2 == 1:
            # Pt 1, strategy is direct - get shape object
            you = rps_lookup[strategy]
        else:
            # Pt 2, need to figure out which shape to throw
            you = rps_lookup[get_your_shape(opponent, strategy)]
        
        game_score = calculate_score(opponent, you)
        game_scores.append(game_score)
    return sum(game_scores)

if __name__ == '__main__':
    tourney_score1 = play_tournament('day_02/input.txt', 1)
    tourney_score2 = play_tournament('day_02/input.txt', 2)
    print('Tournament Score Pt 1: ' + str(tourney_score1))
    print('Tournament Score Pt 2: ' + str(tourney_score2))