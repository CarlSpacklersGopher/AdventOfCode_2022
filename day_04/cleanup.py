import collections

Sectors = collections.namedtuple('Sectors', ['start', 'end'])

def cleanup(filepath:str) -> int:
    redundant_searches = 0
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            search1, search2 = line.split(',')

            sectors1 = get_sectors(search1)
            sectors2 = get_sectors(search2)

            redundant_searches += is_search_redundant(sectors1, sectors2)

    return redundant_searches
        
def get_sectors(search_str) -> Sectors:
    start, end = search_str.split('-')
    return Sectors(int(start), int(end))

def is_search_redundant(sectors1:Sectors, sectors2:Sectors) -> bool:
    '''
    Returns if one sector is completely contained within the other sector
    '''
    lowest_start = min(sectors1.start, sectors2.start)
    highest_end = max(sectors1.end, sectors2.end)

    test_sector = Sectors(lowest_start, highest_end)

    return (test_sector == sectors1) or (test_sector == sectors2)

if __name__ == '__main__':
    redundancies = cleanup('day_04/input.txt')
    print(f'Part 1: {redundancies}')