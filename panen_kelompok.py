# Sistem Pencatatan Hasil Panen Digital

data_panen = []

print("Sistem Pencatatan Hasil Panen Digital")
def tampilkan_laporan():
    total = sum(data_panen)

    print("=== LAPORAN HASIL PANEN ===")
    print("Data panen:", data_panen)
    print("Total hasil panen:", total, "kg")
