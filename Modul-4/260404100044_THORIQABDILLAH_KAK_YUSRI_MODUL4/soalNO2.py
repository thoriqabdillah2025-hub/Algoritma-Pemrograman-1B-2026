
total_gaji = 0
gaji_per_hari = 100000

for hari in range(1, 8):
    print(f"\nHari ke-{hari}")

    # Validasi jam lembur
    while True:
        lembur = int(input("Masukkan jam lembur (0-8): "))

        if lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("Jam lembur tidak sesuai ketentuan!")
            print("Masukkan 0, 1, 2, 3, 4, 6, atau 8 jam.")

    # Menentukan upah lembur
    if lembur == 0:
        upah_lembur = 0
    elif 1 <= lembur <= 3:
        upah_lembur = lembur * 25000
    elif lembur == 4:
        upah_lembur = 100000
    elif lembur == 6:
        upah_lembur = 200000
    elif lembur == 8:
        upah_lembur = 300000

    # Memeriksa shift malam
    shift = input("Apakah bekerja shift malam? (ya/tidak): ").lower()

    if shift == "ya":
        tambahan_shift = 50000
    else:
        tambahan_shift = 0

    # Menghitung gaji harian
    gaji_harian = gaji_per_hari + upah_lembur + tambahan_shift
    total_gaji += gaji_harian

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")

print("\n===== RINGKASAN GAJI MINGGUAN =====")
print(f"Total gaji selama 7 hari: Rp{total_gaji:,}")
