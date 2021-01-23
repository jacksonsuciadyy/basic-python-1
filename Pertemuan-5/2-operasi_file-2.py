f = open("list.txt", "w+")

# Write
for i in range(10):
    f.write(f"Ini baris ke-{i}\r")
f.close()

fr = open("list.txt","r")
print(fr.read())