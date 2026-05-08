#PPD6, example 4

#list mula-mula
buah = ["apel", "anggur", "mangga", "jeruk"]

#menentukan berapa jumlah buah baru
jumlah_buah = (int(input("Masukkan jumlah buah baru: ")))

#menambahkan nama buah baru
for i in range(jumlah_buah):
    new_buah = input("Masukkan nama buah baru: ")
    buah.append(new_buah)

#tampilkan
for nama_buah in buah:
    print(nama_buah)

