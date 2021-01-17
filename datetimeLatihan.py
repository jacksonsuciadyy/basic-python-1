from datetime import datetime
from datetime import date

# Waktu Sekarang
# x = date.today() # Tgl
# print(x)
# x = datetime.now() # Tgl + Waktu
# print(x)

#Format Tanggal
time = datetime.now()
print(time)

# %y/%Y -> Year, %b/%B -> Month, %a/%A -> Week, %d -> Day
print(time.strftime("Tahun: %Y, Bulan: %B, Tanggal: %d"))

# %c = Local time date, %x = local date, %X = local time
print(time.strftime("Sekarang: %c"))
print(time.strftime("Sekarang: %X"))
print(time.strftime("Sekarang: %x"))

# hari apa sekarang?
# 0 = Monday, 6 = Sunday
print(now.weekday())
days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabut', 'Ahad']
print(f"Hari ini adalah {days[now.weekday()]}")

# Time Formatting
# %I = jam format 12, %H = jam format 24, %M = Menit, %S = Detik, %P = AM/PM
print(time.strftime("Sekarang Pukul %I, menit ke %M, detik ke %S, %P"))