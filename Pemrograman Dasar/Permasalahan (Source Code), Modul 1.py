banyak_air = int(input("masukkan nilai mililiter: "))

galon = banyak_air // 3000
liter = banyak_air % 3000 // 1000
ml    = banyak_air % 3000 % 1000

print("galon:", galon)
print("liter:", liter)
print("mililiter:", ml)