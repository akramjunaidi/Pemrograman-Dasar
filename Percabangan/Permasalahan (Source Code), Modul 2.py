print("Toko PSTI Store")
print("Kode paket yang tersedia: TLN, TMD, AXB, AXS, IMD")
kode = input("Masukkan kode paket: ")
jumlah = int(input("Masukkan jumlah paket yang dibeli: "))

nama = "" 
harga = 0
diskon_awal = 0
diskon_tambahan = 0
min_beli = 0

if kode == "TLN":
    nama = "TELKOMSEL LITE"
    harga = 35000
    min_beli = 100000
    diskon_awal = 8
elif kode == "TMD":
    nama = "TELKOMSEL MID"
    harga = 60000
    min_beli = 200000
    diskon_awal = 10 
elif kode == "AXB":
    nama = "AXIS BRONZE"
    harga = 25000
    min_beli = 100000
    diskon_awal = 8 
elif kode == "AXS":
    nama = "AXIS SILVER"
    harga = 50000
    min_beli = 200000
    diskon_awal = 10 
elif kode == "IMD":
    nama = "INDOSAT DATA PREMIUM"
    harga = 80000
    min_beli = 300000
    diskon_awal = 12 
else:
    print("Kode paket tidak valid!") 
exit()

total_awal = harga * jumlah 
print("Nama Paket	:", nama) 
print("Jumlah Pembelian :", jumlah) 
print("Harga per Paket : Rp", harga)
print("Total Awal	: Rp", total_awal)
     
if total_awal >= min_beli:
    print(f"Dapat diskon awal {diskon_awal}%") 
    dapat_diskon_awal = True
else:
    print("Tidak dapat diskon awal") 
    dapat_diskon_awal = False

if total_awal >= (2 * min_beli): 
    print("Dapat tambahan diskon 7%") 
    diskon_tambahan = 7
else:
    print("Tidak dapat diskon tambahan")

harga_setelah_diskon_awal = total_awal 
nominal_diskon_awal = 0
nominal_diskon_tambahan = 0
persen_diskon_total = 0

if dapat_diskon_awal:
    nominal_diskon_awal = (total_awal * diskon_awal) / 100
    harga_setelah_diskon_awal = total_awal - nominal_diskon_awal 
    persen_diskon_total += diskon_awal

if diskon_tambahan > 0:
    nominal_diskon_tambahan = (harga_setelah_diskon_awal * diskon_tambahan) / 100
    total_bayar = harga_setelah_diskon_awal - nominal_diskon_tambahan
    persen_diskon_total += diskon_tambahan 
else:
    total_bayar = harga_setelah_diskon_awal

nominal_diskon_total = nominal_diskon_awal + nominal_diskon_tambahan

print("STRUK PEMBELIAN")
print("Total harga sebelum diskon : Rp", total_awal) 
print("Diskon Awal	: Rp", int(nominal_diskon_awal), f"({diskon_awal}%)") 
print("Harga setelah Diskon Awal : Rp", int(harga_setelah_diskon_awal))
print("Diskon Tambahan	: Rp", int(nominal_diskon_tambahan), f"({diskon_tambahan}%)") 
print("Potongan harga Total	: Rp", int(nominal_diskon_total))
print("Total bayar : Rp", int(total_bayar), "")