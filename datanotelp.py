daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Agung Hapsah":"085888247531", "Tjokro winata":"085156705457"}

print("="*50)
print("   Nama              |    Nomor Telepon   " )
print("="*50)
print(" # Agung Hapsah      |   ", kontak["Agung Hapsah"])
print(" # Tjokro winata     |   ", kontak["Tjokro winata"])
print("-"*50)
print()
print()
print("="*50)

# Menampilkan kontak Arjun Syah
print("Menampilkan Kontak Arjun Syah")
print("="*50)
print(" # Agung Hapsah      |   ", kontak["Aguung hapsah"])
print("-"*50)
print()
print()
print("="*50)

# Menambahkan kontak dengna nama haikal 
print("Menambahkan kontak dengan Nama Risfiani")
print("dengan Nomor telepon 085215376070")
kontak["Risfiani"]="085215376070"
print("="*50)
print(" # Risfiani          |   ", kontak["Risfiani"])
print("-"*50)
print()
print()
print("="*50)

# Mengubah Nomor Siti Nuraisah dengan Nomor baru
print("Mengubah Nomor Tjokro winata dengan Nomor 081234567890")
print("="*50)
print(" # Tjokro winata     |    ", kontak["Tjokro winata"])
print("-"*50)
print()
print()
print("="*50)


# Menampilkan semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.keys())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan semua Nomor
print("Menampilkan semua Nomor dalam Konntak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)

# Menampilkan semua daftar kontak
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)


# Menghapus Salah satu Kontak
print("Hapus Kontak Risfiani")
print("="*50)
kontak.pop("Risfiani") 
print(kontak.items())
print("-"*50)
print()
print() 