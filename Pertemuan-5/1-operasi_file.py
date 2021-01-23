# Open File
f = open('belajar.txt','w+')

# Write File
f.write("Baris pertama \r")

f.close()

# Append File
append = open ("belajar.txt", "a")
append.write("Baris kedua")

append.close()

# Read
fr = open("belajar.txt", "r")
if(fr.mode == 'r'):
    contents = fr.read()
    print(contents)

f.close()

# Close File
# f.close()