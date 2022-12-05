import numpy as np

PRIORITY_UNICODE_OFFSET_LOWER = 96 # puts 'a' at 1
PRIORITY_UNICODE_OFFSET_UPPER = 64 # puts 'A' at 1
CAPS_OFFSET = 26 # Prompt states 'A' should be at 27

def get_priority_sum(filepath:str):
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



def get_item_priorities(compartment:str) -> list[bool]:
    compartment_contents = np.array([False] * 53)
    for character in compartment:
        if character.isupper():
            # Get priority
            priority = ord(character) - PRIORITY_UNICODE_OFFSET_UPPER + CAPS_OFFSET
        else: # lowercase
            priority = ord(character) - PRIORITY_UNICODE_OFFSET_LOWER
        compartment_contents[priority] = True
    return compartment_contents





if __name__ == '__main__':
    print(get_priority_sum('day_03/input.txt'))