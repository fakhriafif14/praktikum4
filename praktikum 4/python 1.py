# Buat list dengan 5 elemen
list_A = [10, 20, 30, 40, 50]

# Akses list
# Tampilkan elemen ke 3
print("Elemen ke-3:", list_A[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen ke-2 sampai ke-4:", list_A[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", list_A[-1])

# Ubah elemen list
# Ubah elemen ke-4 dengan nilai lainnya
list_A[3] = 99
print("List setelah mengubah elemen ke-4:", list_A)

# Ubah elemen ke-4 sampai dengan elemen terakhir
list_A[3:] = [100, 200, 300]
print("List setelah mengubah elemen ke-4 sampai dengan elemen terakhir:", list_A)

# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke-2 (B)
list_B = list_A[:2]
print("List B:", list_B)

# Tambah list B dengan nilai string
list_B.append("Hello")
print("List B setelah menambahkan nilai string:", list_B)

# Tambah list B dengan 3 nilai
list_B.extend([7, 8, 9])
print("List B setelah menambahkan 3 nilai:", list_B)

# Gabungkan list B dengan list A
list_C = list_A + list_B
print("List C (gabungan list A dan B):", list_C)
