# Panjang menjadi 20
s = "Strikes and awesome!"
print("Panjang dari s :  %d" % len(s))

# Huruf a ada di index 8
print("Kmunculan pertama a : %d" % s.index("a"))

# Jumlah huruf a ada 2
print("a muncul sebanyak %d kali" % s.count("a"))

# Memotong string berdasarkan index
print("Lima karakter pertama adalah '%s'" % s[:5])
print("Lima karakter berikutnya adalah '%s'" % s[5:10])
print("Karakter ketiga belas adalah '%s'" % s[12])
print("Karakter dengan index ganjil adalah '%s'" % s[1::2])
print("Lima karakter terakhir adalah '%s'" % s[-5:])

# Konversi ke upppercase
print("String dalam huruf besar : '%s'" % s.upper())

# konversi ke lowercase
print("String dalam huruf kecil '%s': " % s.lower())

# Cek bagaimana string itu dimulai
if s.startswith("Str"):
    print("String dimulai dengan 'str' . Good!")

# Cek bagaimana string itu diakhiri
if s.endswith("ome!"):
    print("String diakhiri dengan 'ome! . Good!")

# Pisahkan string menjadi tiga string yang terpisah
# Masing - masing hanya berisi satu kata
print("Pisahkan kata-kata sting tersebut menjadi : %s" % s.split())
