import numpy as np

def get_tree_heights_from_file(file:str) -> list[list[int]]:
    '''
    Reads the provided file of tree heights into a 2D list of tree heights
    '''
    pass

def get_tree_visibilities(heights:list[int]) -> list[bool]:
    '''
    Determines if each listed tree is visible
    '''
    pass

def get_visibility_from_north(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from north, looking south.
    '''
    pass

def get_visibility_from_south(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from south, looking north.
    '''
    pass

def get_visibility_from_east(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from east, looking west.
    '''
    pass

def get_visibility_from_west(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from west, looking east.
    '''
    pass

def count_visible_trees(tree_heights:list[list[int]]) -> int:
    '''
    Returns a count of the trees visible from any direction
    '''
    pass



if __name__ == '__main__':
    pt1 = None
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))
    