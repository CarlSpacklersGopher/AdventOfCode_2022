ELF_DELIMITER = -1


def get_processed_input(file_name: str) -> list[int]:
    
    return_list = []
    with open(file_name, 'r') as f:
        for line in f:
            if line == '\n':
                return_list.append(ELF_DELIMITER)
            else:
                return_list.append(int(line.strip()))
    
    return_list.append(ELF_DELIMITER) # Ensure final elf gets totaled up
    return return_list


def get_calories_per_elf(food_list: list[int]) -> list[int]:
    '''
    Returns list of calories carried by each elf in descending order
    '''

    elf_calories = []
    calorie_counter = 0

    for calories in food_list:
        if calories == ELF_DELIMITER:
            elf_calories.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += calories
    elf_calories.sort(reverse=True) # Descending Order
    return elf_calories
        

def get_most_calories(calories_per_elf: list[int], num_elves: int=1) -> list[int]:
    return calories_per_elf[:num_elves]


if __name__ == '__main__':
    
    calorie_list = get_processed_input("day_01/input_pt1.txt")
    calories_per_elf = get_calories_per_elf(calorie_list)

    print(f'Part 1: {get_most_calories(calories_per_elf)}')
    print(f'Part 2: {get_most_calories(calories_per_elf, num_elves=3)}')
    