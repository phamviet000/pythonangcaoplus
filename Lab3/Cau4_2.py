def process_file(reader):
    with open(reader, 'r') as rd:
        rd.readline()
        data= rd.readline().strip()
        while data.startswith('#'):
            data= rd.readline().strip()
        print(data)
        for data in rd:
            print(data.rstrip())




    
print(process_file('textfile.txt'))
 
