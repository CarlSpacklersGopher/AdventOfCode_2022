import sys
import os

def make_files(day_str:str):

    contents_testdayx = f'''
import unittest
import day_{day_str}

class TestDay{day_str}(unittest.TestCase):

    def test_day_{day_str}_pt1(self):
        pass

    def test_day_{day_str}_pt2(self):
        pass

if __name__ == '__main__':
    unittest.main()
'''

    contents_dayx = '''

def process_input(filepath: str) -> list:
    input = []
    with open(filepath, encoding='utf-8', mode='r') as f:
        for line in f:
            pass

    return input

def main():
    pt1 = None
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 2: ' + str(pt2))


if __name__ == '__main__':
    main()
    '''


    folder_name = 'day_' + day_str
    files = [(folder_name + '_prompt.txt',''),
             (folder_name + '.py', contents_dayx),
             ('test_' + folder_name + '.py', contents_testdayx),
             ('input.txt', ''),
             ('testinput.txt', '')]

    os.mkdir(folder_name)
    for file_name, contents in files:
        with open (os.path.join(folder_name, file_name), encoding='utf-8', mode='w') as f:
            f.write(contents)

def make_prompt_readable(day:str, line_chars:int = 100):
    folder_name = f'day_{day}'
    prompt_file = f'day_{day}_prompt.txt'
    prompt_path = os.path.join(folder_name, prompt_file)

    with open (prompt_path, encoding='utf-8', mode='r+') as f:
        long_lines = f.readlines()
        broken_up_lines = []
        for long_line in long_lines:
            words = long_line.split(' ')
            this_line_words = []
            char_count = 0
            for word in words:
                char_count += len(word)
                last_word = word.endswith('\n') # last words always have newline after
                if not last_word and (char_count < line_chars):
                    this_line_words.append(word)
                    char_count += 1 # account for space between words
                else:
                    if last_word:
                        this_line_words.append(word)
                        eol_append = ''
                    else:
                        eol_append = '\n'

                    short_line = ' '.join(this_line_words) + eol_append
                    broken_up_lines.append(short_line)
                    char_count = 0
                    this_line_words = [word] # overflow word onto next line
        f.seek(0)
        f.writelines(broken_up_lines)
        f.truncate()



if __name__ == '__main__':
    day_num_str = sys.argv[1]
    if len(sys.argv) == 2:
        make_files(day_num_str)
    else:
        make_prompt_readable(day_num_str)

