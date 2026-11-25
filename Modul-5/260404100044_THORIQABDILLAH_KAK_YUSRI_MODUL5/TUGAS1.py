def pelanggan(n):
    if n <= 0:
        return "angka harus bulat positif"

    if n == 1 or n == 2:
        return 1
    else:
        hasil = pelanggan(n - 1) + pelanggan(n - 2)
        return hasil

hari = int(input("Masukkan hari ke: "))
print("Jumlah pelanggan:", pelanggan(hari))
