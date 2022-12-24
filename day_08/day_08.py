import numpy as np
import copy

def get_tree_heights(file:str) -> list[list[int]]:
    '''
    Reads the provided file of tree heights into a 2D list of tree heights
    '''
    tree_map = []
    with open(file,'r') as f:
        for line in f.readlines():
            tree_map.append([int(x) for x in line.strip()])
    
    return tree_map


def get_tree_visibilities(heights:list[list[int]]) -> list[bool]:
    '''
    Determines if each listed tree is visible
    '''
    visibilities = []
    for tree_row in heights:
        visibilities.append(get_row_visibilities(tree_row))
    return visibilities

def get_row_visibilities(heights:list[int]) -> list[bool]:
    tallest = -1
    visibilities = []
    for height in heights:
        visible = height > tallest
        visibilities.append(visible)
        if visible:
            tallest = height
    return visibilities

def reverse_elements(list2D:list[list[int]]):
    '''
    Reverses the elements of the provided 2D list
    '''
    for row in list2D:
        row.reverse()

def get_visibility_from_north(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from north, looking south.
    '''
    # looking from north - Transpose rows and columns
    map_from_north = np.array(tree_heights).T

    visibilities = get_tree_visibilities(map_from_north)
    # Re-transform
    visibilities = np.array(visibilities).T.tolist()

    return visibilities

def get_visibility_from_south(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from south, looking north.
    '''
    # looking from south - Transpose rows and columns, then reverse
    map_from_south = np.array(tree_heights).T.tolist()
    reverse_elements(map_from_south)

    visibilities = get_tree_visibilities(map_from_south)
    # Re-transform
    reverse_elements(visibilities)
    visibilities = np.array(visibilities).T.tolist()

    return visibilities

def get_visibility_from_east(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from east, looking west.
    '''
    # looking from east - reverse rows
    map_from_east = copy.deepcopy(tree_heights)
    reverse_elements(map_from_east)

    visibilities = get_tree_visibilities(map_from_east)
    # Re-transform
    reverse_elements(visibilities)

    return visibilities

def get_visibility_from_west(tree_heights:list[list[int]]) -> list[list[bool]]:
    '''
    Generates matrix of booleans that indicates if each tree is visible from west, looking east.
    '''
    # No need for transformation actions
    return get_tree_visibilities(tree_heights)

def count_visible_trees(tree_heights:list[list[int]]) -> int:
    '''
    Returns a count of the trees visible from any direction
    '''
    north_vis = get_visibility_from_north(tree_heights)
    south_vis = get_visibility_from_south(tree_heights)
    east_vis = get_visibility_from_east(tree_heights)
    west_vis = get_visibility_from_west(tree_heights)

    ns_vis = np.bitwise_or(north_vis, south_vis)
    ew_vis = np.bitwise_or(east_vis, west_vis)

    visible_trees = np.bitwise_or(ns_vis, ew_vis)
    return np.count_nonzero(visible_trees)



if __name__ == '__main__':
    tree_heights = get_tree_heights('day_08/input.txt')
    pt1 = count_visible_trees(tree_heights)
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))
    