def count_calories(food_list: list[str]) -> int:
    elf_calories = [0]
    calorie_counter = 0

    food_list_copy = food_list.copy()
    food_list_copy.append('') # Ensure last elf gets total added up

    for calories in food_list_copy:
        calories = calories.strip()
        # Calories added up when empty line is found
        if not calories:
            elf_calories.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += int(calories)
    return max(elf_calories)

if __name__ == '__main__':
    
    calorie_list=[]
    with open("day_01/input_pt1.txt", 'r') as f:
        calorie_list = f.readlines()
    print(count_calories(calorie_list))
    