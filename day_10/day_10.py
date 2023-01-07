
class CRT:
    def __init__(self, rows: int, pixels_per_row: int):
        self.screen = []
        self.current_row = 0
        self.current_pixel = 0
        self.pixels_per_row = pixels_per_row
        for _ in range(rows):
            self.screen.append(['.'] * pixels_per_row)

    def draw_pixel(self, cycle: int, sprite_position: int):
        current_row = (cycle - 1) // self.pixels_per_row
        current_pixel = (cycle - 1) % self.pixels_per_row

        pixel_lit = sprite_position - 1 <= cycle <= sprite_position + 1

        if pixel_lit:
            self.screen[current_row][current_pixel] = '#'

    def __str__(self) -> str:
        screen_str = ''
        for row in self.screen:
            screen_str += ''.join(row) + '\n'
        return screen_str

class CPU:
    def __init__(self, interesting_cycles: list[int], screen: CRT):
        self.register = 1
        self.cycles = 0
        self.interesting_cycles = interesting_cycles
        self.interesting_signal_strengths = []
        self.screen = screen

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
        self.screen.draw_pixel(self.cycles, self.register)
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
    screen = CRT(rows=6, pixels_per_row=40)
    cpu = CPU(interesting_cycles=range(20, 220+1, 40), screen=screen)
    instructions = read_instructions('day_10/input.txt')
    execute_instructions(cpu, instructions)
    pt1 = sum_signal_strengths(cpu)
    print('Part 1: ' + str(pt1))

    print('Part 2: \n' + str(screen))


if __name__ == '__main__':
    main()
