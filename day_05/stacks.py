from dataclasses import dataclass

@dataclass
class Move:
    self.source: int # stack number
    self.destination: int # stack number
    self.boxes: int # num boxes to move from source to destination

def get_starting_stacks(filepath:str) -> list[list]:
    '''
    Reads the provided input file - returns list of package stacks
    '''
    pass

def get_moves(filepath:str) -> list[Move]:
    '''
    Reads the provided input file - returns list of package moves
    '''
    pass

def move_package(stacks:list, instruction:Move):
    '''
    Moves package from one stack to another based on instruction
    '''
    pass

def get_top_boxes(stacks:list) -> str:
    '''
    Returns the box on top of each stack, in order
    '''
    pass

def rearrange_crates(filepath:str) -> str:
    '''
    Rearranges the stacks of crates based on the list of instructions
    Returns string of the top crate from each stack, in order
    '''

if __name__ == '__main__':
    filepath = 'day_05/testinput.txt'
    pt1 = None
    print(f'Part 1: {pt1}')

    pt2 = None
    print(f'Part 2: {pt2}')