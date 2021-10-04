def process_file(reader):
    reader1 = open(reader,'r')
    def skip_header(reader1):
        line = reader1.read(152)
        return line
    line = skip_header(reader1).strip()
    print(line)
    print(" ")
    print("******")
    print(reader1.read())
    reader1.close()





    
print(process_file('textfile.txt'))
 
