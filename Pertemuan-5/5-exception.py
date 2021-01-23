# a = ""
# b = 1

# try:
#     print(1/0)
# except TypeError:
#     a += "Error Type "
# except ZeroDivisionError:
#     a += "Error Zero Division "
# except:
#     a += "Error "
# else:
#     # Dijalankan kalau tidak error
#     a += "Tidak Ada Error "
# finally:
#     # Dijalankan meskipun error / tidak
#     a += "Bro"
# print(a)

try:
    f = open("list.txt","r")
    f.write("Hai")
except IOError:
    print("Error IO")
except:
    print("Error")
else:
    print("Sukses!")
finally:
    print("Selesai")
    f.close()