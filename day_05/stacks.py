from dataclasses import dataclass
import re

@dataclass
class Move:
    source: int # stack number
    destination: int # stack number
    boxes: int # num boxes to move from source to destination

def get_starting_stacks(filepath:str) -> list[list]:
    '''
    Reads the provided input file - returns list of package stacks
    '''
    stacks_lines = []
    with open (filepath, 'r') as f:
        for line in f:
            if line == '\n':
                # newline separates stacks description from move instructions
                break
            else:
                stacks_lines.append(line.strip('\n'))
    
    stack_num_str = stacks_lines.pop().split() # Get list of stack numbers
    stack_nums = [int(num) for num in stack_num_str]
    stack_idx_list = [(4*i - 3) for i in stack_nums] # idx in string of box letter: 4x-3
    
    # Stacks listed from top-down, but are built from bottom-up
    stacks = [[] for _ in range(stack_nums[-1] + 1)]
    stacks_lines.reverse()

    for stack_level in stacks_lines:
        for stack_num, stack_idx in zip(stack_nums, stack_idx_list):
            box_id = stack_level[stack_idx]
            if box_id != ' ': # box id is ' ' if no box is there.
                stacks[stack_num].append(box_id)
    return stacks

        

def get_moves(filepath:str) -> list[Move]:
    '''
    Reads the provided input file - returns list of package moves
    '''
    moves = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('move'):
                boxes, source, destination = re.findall(r'\d+', line.strip())
                moves.append(Move(int(source), int(destination), int(boxes)))
    return moves
            

def move_package(package_stacks:list, instruction:Move):
    '''
    Moves package from one stack to another based on instruction
    '''
    for repetition in range(instruction.boxes):
        box_to_move = package_stacks[instruction.source].pop()
        package_stacks[instruction.destination].append(box_to_move)

def get_top_boxes(package_stacks:list) -> str:
    '''
    Returns the box on top of each stack, in order
    '''
    top_boxes = ''
    for stack in package_stacks:
        if stack:
            top_boxes += stack[-1]
    return top_boxes

def rearrange_crates(filepath:str) -> str:
    '''
    Rearranges the stacks of crates based on the list of instructions
    Returns string of the top crate from each stack, in order
    '''
    stacks = get_starting_stacks(filepath)
    moves = get_moves(filepath)

    for move in moves:
        move_package(stacks, move)

    return get_top_boxes(stacks)

if __name__ == '__main__':
    filepath = 'day_05/input.txt'
    pt1 = rearrange_crates(filepath)
    print(f'Part 1: {pt1}')

    pt2 = None
    print(f'Part 2: {pt2}')