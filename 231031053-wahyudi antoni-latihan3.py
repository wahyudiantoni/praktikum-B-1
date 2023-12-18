nama = str (input('nama karyawan :'))
pendapatan = float(input("Masukkan pendapatan karyawan: "))

if pendapatan >= 1000:
    status = "kamu berhak."
else:
    status = "kamu tidak berhak."

print(status)
