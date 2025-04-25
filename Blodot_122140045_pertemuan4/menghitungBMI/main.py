print(f"Selamat Datang di Perhitungan Body Mass Index (BMI)")

beratBadan = float(input("Masukkan berat badan (kg): "))
tinggiBadan = float(input("Masukkan tinggi badan (m): "))

rumusBMI = beratBadan / (tinggiBadan * tinggiBadan)
if rumusBMI < 18.5:
    kategori = "Berat badan kurang"
elif 18.5 <= rumusBMI < 25:
    kategori = "Berat badan normal"
elif 25 <= rumusBMI < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

print(f"Nilai BMI Anda adalah: {rumusBMI:.2f}, Kategori: {kategori}")

