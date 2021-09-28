newlist = []
for line in open('metal.txt'):
    newlist.append(line.strip())
for line in reversed(newlist):
    print(line)
