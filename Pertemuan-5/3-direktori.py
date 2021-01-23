import os
import shutil

## Mendapatkan Direktori sekarang
# print(os.getcwd())

## Merubah Direktori
# os.chdir('../')
# print("Direktori : " + os.getcwd())

## Membuat Direktor Baru
# os.mkdir("New")

## Merubah Nama Direktori
# os.rename("New", "Baru")

## Remove File
# f = open("junk.txt", "w+")
# f.close
# os.remove("junk.txt")

## Remove Directory
# os.rmdir("Baru")

## Remove non-Empty Directory
# os.mkdir("New")
# os.chdir("./New/")
# f = open("New.txt", "w+")
# f.close()
shutil.rmtree("New")



## List Direktori
# print(type(list))
# print(list)
# ls = os.listdir()
# for i in ls:
#     print(i)