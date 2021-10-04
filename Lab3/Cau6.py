from typing import TextIO
from io import StringIO
#import time_series
def skip_header(reader: TextIO):
    line = reader.readline()
    line = reader.readline()
        
    while line.startswith('#'):
        line= reader.readline()

    return line
def smallest_value_skip(reader: TextIO):
    line = skip_header(reader).strip()
    smallest = int(line)
    line = reader.readline().strip()
    while line != '-':
        value = int(line)
        smallest = min(smallest, value)
        line = reader.readline().strip()
    while line != '-':
        value = int(line)
        smallest = min(smallest, value)
        line = reader.readline().strip()
    return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))
