opponent_decoder = {'A':'Rock',
                    'B':'Paper',
                    'C':'Scissors'}

your_decoder = {'X':'Rock',
                'Y':'Paper',
                'Z':'Scissors'}

def calculate_score(opponent:str, you:str) -> int:
    '''
    Calculates your score for a given game of Rock Paper Scissors
    '''
    # There's an easier way to do this than if/else chains in 2 separate functions
    points = determine_win_pts(opponent, you)
    if you == 'Rock':
        points += 1
    elif you == 'Paper':
        points += 2
    elif you == 'Scissors':
        points += 3
    return points

def determine_win_pts(opponent:str, you:str) -> int:
    '''
    Returns points earned from result of the game of Rock Paper Scissors
    Loss: 0, Draw: 3, Win: 6
    '''
    win_points = 6
    draw_points = 3
    loss_points = 0

    # This stinks
    if you == opponent:
        return draw_points
    elif you == "Rock" and opponent == "Scissors":
        return win_points
    elif you == "Paper" and opponent == "Rock":
        return win_points
    elif you == "Scissors" and opponent == "Paper":
        return win_points
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
    tourney_score = play_tournament('day_02/testinput.txt')
    print('Tournament Score: ' + str(tourney_score))