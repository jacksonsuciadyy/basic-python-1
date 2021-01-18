import os
clear = lambda: os.system('cls')

option = 0
cntContact = 0
# contacts = {
#     cntContact: {
#         'Name': 'Jackson',
#         'Telp': '087888330463',
#     }
# }
contacts = {}

def returnToMenu():
    print(" ")
    print(" ")
    print(" ")
    optionReturn = input("Kembali ke Menu?(y/n) ")
    while optionReturn != "y" and optionReturn != "Y" and optionReturn != "n" and optionReturn != "N":
        optionReturn = input("Kembali ke Menu?(y/n) ")
    if(optionReturn == "y" or optionReturn == "Y"):
        main()
    else:
        clear()
        print(" ")
        print(" ")
        print("Program selesai, sampai jumpa!")
        print(" ")
        print(" ")
        return

def menu():
    print("Selamat Datang")
    print(" ")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def contactList():
    clear()
    print("Daftar Kontak")
    print("-------------")
    print(" ")
    # print(type(contacts))
    for key, value in contacts.items():
        # print(key, value)
        for key, data in value.items():
            if(key == "Name"):
                print(f"Nama: {data}")
            else:
                 print(f"No. Telepon: {data}")
    returnToMenu()

def contactAdd():
    clear()
    print("Tambah Kontak")
    print("-------------")
    print(" ")
    Name = input("Nama: ")
    Telp = input("No. Telepon: ")
    global cntContact
    cntContact += 1
    contacts[cntContact] = {
        "Name": Name,
        "Telp": Telp
    }
    print(" ")
    print(" ")
    print("Kontak berhasil ditambahkan!")
    print(" ")
    print(" ")
    returnToMenu()
    

def chooseMenu(i):
    switcher={
        1: contactList()
    }

def main():
    clear()
    menu()
    option = int(input("Pilih menu: "))
    if(option == 1):
        contactList()
    elif(option == 2):
        contactAdd()
    elif(option == 3):
        clear()
        print(" ")
        print(" ")
        print("Program selesai, sampai jumpa!")
        print(" ")
        print(" ")
        return
    else:
        clear()
        print("Menu tidak tersedia")
        returnToMenu()

main()

