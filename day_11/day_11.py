from typing import Callable


class Monkey:
    def __init__(self, number: int, items: list[int], operation_func: Callable, test_func: Callable):
        self.number = number
        self.items = items
        self.operation = operation_func
        self.test = test_func
        self.true_monkey = None
        self.false_monkey = None
        self.inspection_count = 0

    def set_true_target(self, monkey):
        self.true_monkey = monkey        

    def set_false_target(self, monkey):
        self.false_monkey = monkey

    def throw_items(self):
        while self.items:
            worry_value = self.items.pop(0)
            worry_value = self.operation(worry_value)
            self.inspection_count += 1
            worry_value = worry_value // 3
            if self.test(worry_value):
                self._throw_item(worry_value, self.true_monkey)
            else:
                self._throw_item(worry_value, self.false_monkey)

    def _throw_item(self, item: int, throw_to):
        throw_to.catch_item(item)

    def catch_item(self, item: int):
        self.items.append(item)

def execute_rounds(rounds:int, monkeys: list[Monkey]):
    for round in range(rounds):
        for idx, monkey in enumerate(monkeys):
            monkey.throw_items()
        
        inspection_stats = [monkey.inspection_count for monkey in monkeys]
        monkey_items = [monkey.items for monkey in monkeys]

def process_input(filepath: str) -> list:
    monkeys = []
    true_targets = []
    false_targets = []
    with open(filepath, encoding='utf-8', mode='r') as f:
        lines = f.readlines()
        for start in range(1, len(lines), 7):
            monkey_number = int(lines[start-1][7:-2])
            
            starting_items = lines[start].strip().split(': ')[-1]
            starting_items = [int(x) for x in starting_items.split(', ')]

            operation_description = lines[start+1].strip().split('= ')[-1]
            operation = eval('lambda old : ' + operation_description)

            test_divisor = lines[start+2].strip().split()[-1]
            test_func = eval(f'lambda x : (x % {test_divisor}) == 0')

            true_monkey = int(lines[start+3].strip().split()[-1])
            false_monkey = int(lines[start+4].strip().split()[-1])

            # Create monkey
            monkey = Monkey(number = monkey_number,
                            items = starting_items,
                            operation_func = operation, 
                            test_func = test_func)

            true_targets.append(true_monkey)
            false_targets.append(false_monkey)
            
            monkeys.append(monkey)


    for monkey, true_target, false_target in zip(monkeys, true_targets, false_targets):
        monkey.set_true_target(monkeys[true_target])
        monkey.set_false_target(monkeys[false_target])

    return monkeys

def monkey_business(monkeys: list[Monkey]) -> int:
    inspections = [monkey.inspection_count for monkey in monkeys]
    inspections.sort()

    return inspections[-1] * inspections[-2]


def main():
    monkeys = process_input('day_11/input.txt')
    execute_rounds(rounds=20, monkeys=monkeys)

    pt1 = monkey_business(monkeys)
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))


if __name__ == '__main__':
    main()
    