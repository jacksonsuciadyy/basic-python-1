class Person:
    def __init__(self,name,age, alamat):
        self.name = name
        self.age = age
        self.alamat = alamat

name = input("Masukkan Nama Anda: ")
age = int(input("Masukkan Umur Anda: "))
alamat = input("Masukkan Alamat Anda: ")

p1 = Person(name, age, alamat)
print("Biodata")
print("-------")
print("Person 1 :")
print("  Nama: "+ p1.name)
print(f"  Umur: {p1.age}")
print("  Alamat: "+ p1.alamat)
print(" ")
print(" ")

name = input("Masukkan Nama Anda: ")
age = int(input("Masukkan Umur Anda: "))
alamat = input("Masukkan Alamat Anda: ")

p2 = Person(name, age, alamat)

print(" ")
print("Person 2 :")
print("  Nama: "+ p2.name)
print(f"  Umur: {p2.age}")
print("  Alamat: "+ p2.alamat)

