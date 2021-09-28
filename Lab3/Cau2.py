alkaline_metals = []
for line in open('metal.txt'):
    alkaline_metals.append(line.strip().split(' '))
print(alkaline_metals)
