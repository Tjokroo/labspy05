# labspy05
## BAHASA PEMOGRAMAN
### Latihan 1
#### Membuat daftar kontak menggunakan dictionary di python

```python
jadi kali ini kita akan membuat daftar kontak menggunakan dictionary dan berikut langkah dan keterangan nya
```
- Keterangan
```python
daftarkontak = {"Nama":"Nomor Telepon"}
kontak = {"Agung Hapsah":"085888247531", "Tjokro winata":"085156705457"}
```
- Berikut merupakan programnya

![gambar1](ss/ss1.png)

#### Kondisi 1
```python
print("="*50)
print("   Nama              |    Nomor Telepon   " )
print("="*50)
print(" # Agung Hapsah      |   ", kontak["Agung Hapsah"])
print(" # Tjokro winata     |   ", kontak["Tjokro winata"])
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil dari programnya
![gambar2](ss/s1.PNG)
### kondisi 2
```python
print("Menampilkan Kontak Arjun Syah")
print("="*50)
print(" # Arjun Syah        |   ", kontak["Arjun Syah"])
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil programnya
![gambar3](ss/s2.PNG)
### Kondisi 3
```python
print("Menambahkan kontak dengan Nama Haikal")
print("dengan Nomor telepon 085215376070")
kontak["Haikal"]="085215376070"
print("="*50)
print(" # Haikal            |   ", kontak["Haikal"])
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil programnya
![gambar4](ss/s3.PNG)
### kondisi 4
```python
print("Mengubah Nomor Siti Nuraisah dengan Nomor 08521267890")
print("="*50)
print(" # Siti Nuraisah     |    ", kontak["Siti Nuraisah"])
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil programnya
![gambar5](ss/s4.PNG)
### Kondisi 5
```python
# Menampilkan semua Nama
print("Menampilkan Semua Nama dalam Kontak")
print("="*50)
print(kontak.keys())
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil programnya
![gambar6](ss/s5.PNG)
### Kondisi 6
```python
print("Menampilkan semua Nomor dalam Konntak")
print("="*50)
print(kontak.values())
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil programnya
![gambar7](ss/s6.PNG)
### kondisi 7
```python
print("Menampilkan Semua Daftar Kontak")
print("="*50)
print(kontak.items())
print("-"*50)
print()
print()
print("="*50)
```
### Berikut hasil programnnya
![gambar8](ss/s7.PNG)
### Kondisi 8
```python
print("Hapus Kontak Haikal")
print("="*50)
kontak.pop("Haikal") 
print(kontak.items())
print("-"*50)
print()
print()
```
### Berikut hasil programnya
![gambar9](ss/s8.PNG)
## latihan1 selesai