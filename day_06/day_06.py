import re

def find_message_start(datastream:str, marker_length:int) -> int:
    '''
    Given datastream, returns the index that the message starts (not including the marker)
    '''
    message_start = -1
    for i in range(len(datastream)):
        potential_marker = datastream[i: i + marker_length]
        if len(set(potential_marker)) == marker_length: # unique
            return i + marker_length


if __name__ == '__main__':
    datastream = None
    with open('day_06/input.txt', 'r') as f:
        datastream = f.readline().strip() # only 1 line
    
    pt1 = find_message_start(datastream, 4)
    print('Part 1: ' + str(pt1))

    pt1 = find_message_start(datastream, 14)
    print('Part 1: ' + str(pt1))
    