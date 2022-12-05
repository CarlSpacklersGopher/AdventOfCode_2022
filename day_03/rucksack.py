import numpy as np

PRIORITY_UNICODE_OFFSET_LOWER = 96 # puts 'a' at 1
PRIORITY_UNICODE_OFFSET_UPPER = 64 # puts 'A' at 1
CAPS_OFFSET = 26 # Prompt states 'A' should be at 27

def part1(filepath:str) -> int:
    '''
    '''
    with open(filepath, 'r') as file:
        priorities = []
        for line in file: # Each line is a rucksack
            items = line.strip()
            compartment_split = len(items) // 2
            compartment1 = items[:compartment_split]
            compartment2 = items[compartment_split:]

            compartment1_contents = get_item_priorities(compartment1)
            compartment2_contents = get_item_priorities(compartment2)

            common_items = np.where(compartment1_contents & compartment2_contents)
            priorities.append(common_items[0][0])
        
        return sum(priorities)

def part2(filepath:str) -> int:
    group_contents = []
    group_sums = 0
    linecount = 0
    with open(filepath, 'r') as file:
        for line in file:
            linecount += 1
            items = line.strip()
            group_contents.append(get_item_priorities(items))

            if linecount == 3:
                common_items = group_contents[0] & group_contents[1] & group_contents[2]
                priority = np.where(common_items)
                group_sums += priority[0][0]
                
                linecount = 0
                group_contents = []
    return group_sums

def get_item_priorities(items:str) -> list[bool]:
    contents = np.array([False] * 53)
    for character in items:
        if character.isupper():
            # Get priority
            priority = ord(character) - PRIORITY_UNICODE_OFFSET_UPPER + CAPS_OFFSET
        else: # lowercase
            priority = ord(character) - PRIORITY_UNICODE_OFFSET_LOWER
        contents[priority] = True
    return contents

if __name__ == '__main__':
    print('Part 1: ' + str(part1('day_03/input.txt')))
    print('Part 2: ' + str(part2('day_03/input.txt')))