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

def get_trees_in_view(coords:tuple, tree_heights:np.ndarray) -> list[list[int]]:
    '''
    Returns a list of the trees north, south, east, and west of the tree at coords.
    Order of trees is from current tree looking outward in each direction.
    Returns a list of lists - [[north],[south],[east],[west]]
    '''
    row, col = coords
    
    north_trees = tree_heights[:row, col].tolist()
    north_trees.reverse()

    south_trees = tree_heights[row+1:,col].tolist()

    east_trees = tree_heights[row, col+1:].tolist()

    west_trees = tree_heights[row, :col].tolist()
    west_trees.reverse()

    return [north_trees, south_trees, east_trees, west_trees]

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

def view_distance(tree_height:int, other_trees:list[int]) -> int:
    '''Gets number of trees visible between this tree and edge or next blocking tree'''
    distance = 0
    for other_height in other_trees:
        distance += 1
        if tree_height <= other_height:
            return distance
    return distance

def scenic_score(coords:tuple, tree_heights:np.ndarray) -> int:
    '''
    Calculates scenic score of the tree at xy coordinates in the tree_heights matrix.
    '''
    tree = tree_heights[coords]
    directions = get_trees_in_view(coords, tree_heights)
    view_distances = []
    for direction in directions:
        view_distances.append(view_distance(tree, direction))
    
    return np.prod(view_distances)

def part2(tree_heights: list[list[int]]) -> int:
    tree_arr = np.array(tree_heights)
    scenic_scores = []
    for row_idx, row in enumerate(tree_heights):
        for col_idx in range(len(row)):
            coords = (row_idx, col_idx)
            scenic_scores.append(scenic_score(coords, tree_arr))

    return max(scenic_scores)





if __name__ == '__main__':
    tree_heights = get_tree_heights('day_08/input.txt')
    pt1 = count_visible_trees(tree_heights)
    print('Part 1: ' + str(pt1))

    pt2 = part2(tree_heights)
    print('Part 2: ' + str(pt2))
    