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
    pass

def determine_win_pts(opponent:str, you:str) -> int:
    '''
    Returns points earned from result of the game of Rock Paper Scissors
    Loss: 0, Draw: 3, Win: 6
    '''
    pass

def decode_strategy_guide(filepath:str) -> enumerate:
    '''
    Translates Strategy Guide to Human Readable Format
    Returns enumerate object - first object for each is opponent, second is you
    '''
    pass

def play_tournament(filepath:str) -> int:
    '''
    Returns your total score for all games in Rock Paper Scissors tournament
    '''
    pass

if __name__ == '__main__':
    pass