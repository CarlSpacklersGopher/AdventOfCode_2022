
class CPU:
    def __init__(self, interesting_cycles: list[int]):
        self.register = 1
        self.cycles = 0
        self.interesting_cycles = interesting_cycles
        self.interesting_signal_strengths = []

    @property
    def signal_strength(self):
        return self.register * self.cycles

    def noop(self):
        self.tick()

    def addx(self, x: int):
        self.tick()
        self.tick()
        self.register += x

    def tick(self):
        self.cycles += 1
        # will be executed every cpu cycle, time intensive
        if self.cycles in self.interesting_cycles:
            self.interesting_signal_strengths.append(self.signal_strength)


def read_instructions(filepath:str) -> list[tuple]:
    instructions = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('noop'):
                instructions.append(('noop', None))
            elif line.startswith('addx'):
                command, value = line.split()
                instructions.append((command, int(value)))
    return instructions

def execute_instructions(cpu: CPU, instructions: list[tuple]):
    for instruction in instructions:
        # This isn't great - this function duplicates the if checks in read_instructions
        # also needs to be modified any time there is a new instruction type added
        if instruction[0] == 'noop':
            cpu.noop()
        elif instruction[0] == 'addx':
            cpu.addx(instruction[1])

def sum_signal_strengths(cpu: CPU) -> int:
    return sum(cpu.interesting_signal_strengths)

def main():
    cpu = CPU(range(20, 220+1, 40))
    instructions = read_instructions('day_10/input.txt')
    execute_instructions(cpu, instructions)
    pt1 = sum_signal_strengths(cpu)
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))


if __name__ == '__main__':
    main()
