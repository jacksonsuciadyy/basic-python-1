# import camelcase

# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt)) # Hello World


# ## Generator
# # def operasiBilangan(a, b):
# def operasiBilangan():
#     a = 7
#     b = 8
#     yield a + b

#     x = 19
#     y = 90
#     yield x - y

#     c = 80
#     d = 90
#     yield c * d

#     e = 999
#     f = 10
#     yield e / f

# # oprGen = operasiBilangan(10, 5)
# oprGen = operasiBilangan()

# for i in oprGen:
#     print(i)

# print(" ")
# print(" ")

# def operasiHuruf():
#     yield "Hello World"
#     yield "Selamat Pagi"
#     yield "Selamat Siang"
#     yield "Selamat Sore"
#     yield "Selamat Malam"

# for i in operasiHuruf():
#     print(i)


## Closure
def angka(x):
    y = 8
    def kali(y):
        return x * y
    return kali(y)

print(angka(10))