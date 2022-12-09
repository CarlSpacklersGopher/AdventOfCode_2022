import re

def find_message_start(datastream:str) -> int:
    '''
    Given datastream, returns the index that the message starts (not including the marker)
    '''
    marker_length = 4
    message_start = -1
    for i in range(len(datastream)):
        potential_marker = datastream[i: i + marker_length]
        if len(set(potential_marker)) == marker_length: # unique
            message_start = i + marker_length
            break
    return message_start


if __name__ == '__main__':
    datastream = None
    with open('day_06/input.txt', 'r') as f:
        datastream = f.readline().strip() # only 1 line
    
    pt1 = find_message_start(datastream)
    print('Part 1: ' + str(pt1))

    pt2 = None
    print('Part 1: ' + str(pt1))
    