def process_file(reader):
    def skip_header(reader):
        reader = open(reader,'r')
        line ='# ' + reader.readline() 
        reader.close
        return line
    line = skip_header(reader).strip()
    reader = open(reader,'r')
    print(line)
    print("" , reader.read())
    reader.close()


    
print(process_file('metal.txt'))
