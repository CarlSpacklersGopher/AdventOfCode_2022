
class CRT:
    def __init__(self, rows: int, pixels_per_row: int):
        self.dot_matrix = []
        self.current_row = 0
        self.current_pixel = 0
        self.pixels_per_row = pixels_per_row
        for _ in range(rows):
            self.dot_matrix.append([' '] * pixels_per_row)

    def draw_pixel(self, cycle: int, sprite_position: int):
        current_row = cycle // self.pixels_per_row
        current_pixel = cycle % self.pixels_per_row

        pixel_lit = sprite_position - 1 <= current_pixel <= sprite_position + 1

        if pixel_lit:
            self.dot_matrix[current_row][current_pixel] = '#'

        #print('During Cycle   '+str(cycle)+': CRT draws pixel in position '+str(current_pixel))
        #print('Current CRT row: ' + ''.join(self.screen[current_row])[:current_pixel+1])
        #print()

    def __str__(self) -> str:
        screen_str = ''
        for row in self.dot_matrix:
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
        #print('Start cycle   '+str(self.cycles)+': begin executing addx '+str(x))
        self.tick()
        self.register += x
        #print('End of cycle  '+str(self.cycles)+': finish executing addx '+str(x)+' (Register X is now '+str(self.register))

    def tick(self):
        #sprite_pos = '.' * 40
        #sprite_pos = sprite_pos[:self.register-1] + '###' + sprite_pos[self.register + 2:]
        #print('Sprite Position: '+ sprite_pos)
        self.screen.draw_pixel(self.cycles, self.register)
        self.cycles += 1
        # will be executed every cpu cycle, time intensive
        if self.cycles in self.interesting_cycles:
            self.interesting_signal_strengths.append(self.signal_strength)


def read_instructions(filepath:str) -> list[tuple]:
    instructions = []
    with open(filepath, encoding='utf-8',mode='r') as f:
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
