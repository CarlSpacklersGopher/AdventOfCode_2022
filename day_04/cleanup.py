class Search:
    def __init__(self, start:int, end:int):
        self.start = start
        self.end = end
        self.sectors = set(range(start, end + 1))

def cleanup(filepath:str, criteria) -> int:
    '''
    Reads in pairs of cleanup assignments and evaluates the pairs
    against the provided criteria function.

    Returns: Number of search pairs that meet criteria
    '''
    matching_searches = 0
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            assignment1, assignment2 = line.split(',')

            search1 = get_search(assignment1)
            search2 = get_search(assignment2)

            matching_searches += criteria(search1, search2)

    return matching_searches
        
def get_search(search_str) -> Search:
    start, end = search_str.split('-')
    return Search(int(start), int(end))

def is_search_redundant(search1:Search, search2:Search) -> bool:
    '''
    Returns if one sector is completely contained within the other sector
    '''
    sectors1 = search1.sectors
    sectors2 = search2.sectors
    
    return sectors1.issubset(sectors2) or sectors2.issubset(sectors1)

def is_search_overlapping(search1:Search, search2:Search) -> bool:
    '''
    Returns if there is any overlap between the two searches
    '''
    sectors1 = search1.sectors
    sectors2 = search2.sectors

    # Returns true if any items in one set are in the other
    return not sectors1.isdisjoint(sectors2)


if __name__ == '__main__':
    redundancies = cleanup('day_04/input.txt', is_search_redundant)
    print(f'Part 1: {redundancies}')

    overlaps = cleanup('day_04/input.txt', is_search_overlapping)
    print(f'Part 2: {overlaps}')