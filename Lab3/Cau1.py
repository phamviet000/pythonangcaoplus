filename = input('nhap vao file muon luu: ')  #chua co file nen bao loi
new_filename = filename + '.bak'
backup = open(new_filename, 'w')
for line in  open(filename):
  backup.write(line)
backup.close()
