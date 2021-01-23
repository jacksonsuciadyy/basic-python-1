import os
from os import path
from datetime import datetime as dt
import time

## Cek OS 
# name = os.name()
# print(name)

## Cek apakah file ini ada atau tidak
# print(path.isfile("3-direktori.py"))
# print(path.isdir("New"))

## Work with file path
# dir = path.realpath("list.txt")
# print(dir)
# dir = path.split(path.realpath("list.txt")) # Return Tuple Type Data
# print(dir) 
# for i in dir:
#     print(i)
# print(f"Nama File: {dir[1]}")
# print(f"Path: {dir[0]}")

## Melihat waktu modifikasi file
# t = time.ctime(path.getmtime("list.txt"))
# print(t)
# t = time.ctime(path.getatime("list.txt"))
# print(t)

## Get Modification Time Difference
# t = time.ctime(path.getmtime("1-operasi_file.py"))
# print(t)
# print(dt.fromtimestamp(path.getmtime("1-operasi_file.py")))

## Get Modification Time Difference From Last Modification
td = dt.now() - dt.fromtimestamp(path.getmtime("1-operasi_file.py"))
print(td)
print(td.total_seconds)
