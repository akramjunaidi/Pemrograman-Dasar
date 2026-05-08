#PPD6, Tugas 

#list mula-mula
umur_list = []

#jumlah inputan manusia
jumlah = int(input("Masukkan jumlah manusia: "))

#menambahkan umur manusia
for i in range(jumlah):
    umur = int(input("Masukkan umur manusia ke-{i+1}: "))
    umur_list.append(umur)

#tampilkan
for umur in umur_list:
    if umur > 40:
        print("maka tampil tua")
    else:

        print("maka tampil muda")
