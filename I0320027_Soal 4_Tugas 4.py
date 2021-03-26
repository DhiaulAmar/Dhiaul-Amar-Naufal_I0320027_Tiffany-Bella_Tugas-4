usia = int(input("Berapa usia kamu: "))
kualifikasi = input("Apakah kamu sudah lulus ujian klasifikasi? [Y/T}")

if (usia > 21 and kualifikasi == "Y"):
    print("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")