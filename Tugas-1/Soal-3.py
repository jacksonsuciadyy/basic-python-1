nilai_teori = int(input("Masukkan nilai Ujian Teori Anda : "))
nilai_praktek = int(input("Masukkan nilai Ujian Praktek Anda : "))

if(nilai_teori >= 70 and nilai_praktek >= 70):
    print("Selamat, Anda lulus!")
elif (nilai_teori < 70 and nilai_praktek < 70):
    print("Anda harus mengulang Ujian Teori & Praktek!")
elif (nilai_teori >= 70 and nilai_praktek < 70):
    print("Anda harus mengulang Ujian Praktek!")
elif (nilai_teori < 70 and nilai_praktek >= 70):
    print("Anda harus mengulang Ujian Teori!")