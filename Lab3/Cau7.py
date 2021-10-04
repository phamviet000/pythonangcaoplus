from typing import TextIO
from io import StringIO
def read_molecule(reader: TextIO):
    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None
    # Name of the molecule: "COMPND name"
    parts = line.split()
    name = parts[1]
    # Other lines are either "END" or "ATOM num atom_type x y z"
    molecule = [name]
    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            parts = line.split()
            molecule.append(parts[2:])
    return molecule

def read_all_molecules(reader: TextIO):
    # The list of molecule information.
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: # None is treated as False in an if statement
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimol.pdb', 'r')
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)
