from typing import TextIO
from io import StringIO
def skip_header(reader: TextIO):
    line = reader.readline()
    line = reader.readline()
        
    while line.startswith('#'):
        line= reader.readline()

    return line
def process_file(reader: TextIO):
    line = skip_header(reader).strip()
    for line in reader:
        line = line.strip()
        print(line)


if __name__ == '__main__':
    with open('textfile.txt', 'r') as input_file:
        process_file(input_file)
 
