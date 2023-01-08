from typing import Callable
import time

class Item:
    def __init__(self, value):
        self.value = value
        self.max_item_value = None

    def set_max_item_value(self, value):
        self.max_item_value = value

    def reduce_value(self):
        self.value = self.value % self.max_item_value

    def set_value(self, value):
        self.value = value
        if self.max_item_value:
            self.reduce_value()


class Me:
    def __init__(self, items:list[Item]):
        self.my_stuff = items

    def achieve_zen(self, max_worry_level):
        for item in self.my_stuff:
            item.set_max_item_value(max_worry_level)
            item.reduce_value()      

    def thats_mine_too(self, more_of_my_stuff:list[Item]):
        self.my_stuff += more_of_my_stuff


class Monkey:
    def __init__(self, number: int, operation_func: Callable, test_divisor: int):
        self.number = number
        self.items = []
        self.operation = operation_func
        self.test_divisor = test_divisor
        self.true_monkey = None
        self.false_monkey = None
        self.inspection_count = 0

    def sucks_to_suck(self, items: list[Item]):
        self.items += items

    def set_true_target(self, monkey):
        self.true_monkey = monkey        

    def set_false_target(self, monkey):
        self.false_monkey = monkey

    def throw_items(self, item_breaks:bool):
        while self.items:
            current_item = self.items.pop(0)
            current_item.reduce_value()
            val = current_item.value
            val = self.operation(val)
            self.inspection_count += 1
            if not item_breaks:
                val = val // 3
            current_item.set_value(val)
            if (val % self.test_divisor) == 0:
                self._throw_item(current_item, self.true_monkey)
            else:
                self._throw_item(current_item, self.false_monkey)

    def _throw_item(self, item: Item, throw_to):
        throw_to.catch_item(item)

    def catch_item(self, item: Item):
        self.items.append(item)

def process_input(filepath: str, me: Me) -> list:
    monkeys = []
    true_targets = []
    false_targets = []
    max_worry_value = 1
    with open(filepath, encoding='utf-8', mode='r') as f:
        lines = f.readlines()
        for start in range(1, len(lines), 7):
            monkey_number = int(lines[start-1][7:-2])
            
            starting_items = lines[start].strip().split(': ')[-1]
            starting_items = [Item(int(x)) for x in starting_items.split(', ')]

            operation_description = lines[start+1].strip().split('= ')[-1]
            operation = eval('lambda old : ' + operation_description)

            test_divisor = int(lines[start+2].strip().split()[-1])
            max_worry_value *= test_divisor

            true_monkey = int(lines[start+3].strip().split()[-1])
            false_monkey = int(lines[start+4].strip().split()[-1])

            # Create monkey
            monkey = Monkey(number = monkey_number,
                            operation_func = operation, 
                            test_divisor = test_divisor)

            true_targets.append(true_monkey)
            false_targets.append(false_monkey)
            
            register_items(me, monkey, starting_items)

            monkeys.append(monkey)


    for monkey, true_target, false_target in zip(monkeys, true_targets, false_targets):
        monkey.set_true_target(monkeys[true_target])
        monkey.set_false_target(monkeys[false_target])

    me.achieve_zen(max_worry_value)
    return monkeys

def baseline_worries(me:Me, max_item_value:int):
    for item in me.my_stuff:
        item.set_max_item_value(max_item_value)
        item.reduce_value()

def execute_round(monkeys: list[Monkey], items_break: bool):
    for monkey in monkeys:
        monkey.throw_items(item_breaks=items_break)

def register_items(me: Me, monkey: Monkey, my_stuff: list[Item]):
    monkey.sucks_to_suck(my_stuff)
    me.thats_mine_too(my_stuff)

def monkey_business(monkeys: list[Monkey]) -> int:
    inspections = [monkey.inspection_count for monkey in monkeys]
    inspections.sort()

    return inspections[-1] * inspections[-2]

def main():
    me = Me([]) # don't know what my stuff is yet
    monkeys = process_input(filepath='day_11/input.txt', me=me)
    for round in range(1, 20+1):
        execute_round(monkeys=monkeys, items_break=False)

    pt1 = monkey_business(monkeys)
    print('Part 1: ' + str(pt1))

    
    me = Me([]) # don't know what my stuff is yet
    monkeys = process_input(filepath='day_11/input.txt', me=me)
    for round in range(1, 10_000+1):
        start_time = time.process_time()
        execute_round(monkeys=monkeys, items_break=True)

    pt2 = monkey_business(monkeys)
    print('Part 2: ' + str(pt2))
    


if __name__ == '__main__':
    main()
    