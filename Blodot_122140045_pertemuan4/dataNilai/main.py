# Tabel untuk rentang grade
grade_rentang = [
    {'Rentang': '80 - 100', 'Grade': 'A'},
    {'Rentang': '70 - 79', 'Grade': 'B'},
    {'Rentang': '60 - 69', 'Grade': 'C'},
    {'Rentang': '50 - 59','Grade': 'D'},
    {'Rentang': '0 - 49','Grade': 'E'},
]
print("\nDaftar Grade Nilai")
print("=" * 30)
print(f"{'Rentang Nilai':<15} {'GRADE':<5}")
print("=" * 30)
for grade in grade_rentang:
    print(f"{grade['Rentang']:<16} {grade['Grade']:<5}")
print("=" * 30)

# Data acak mahasisa
data_mahasiswa = [
    {'nama': 'Rizali', 'nim': '126140001', 'nilai_uts': 85, 'nilai_uas': 90, 'nilai_tugas': 75},
    {'nama': 'Sambe', 'nim': '126140011', 'nilai_uts': 44, 'nilai_uas': 92, 'nilai_tugas': 80},
    {'nama': 'Ara', 'nim': '126140111', 'nilai_uts': 70, 'nilai_uas': 86, 'nilai_tugas': 70},
    {'nama': 'Tegar', 'nim': '126140101', 'nilai_uts': 40, 'nilai_uas': 50, 'nilai_tugas': 85},
    {'nama': 'Antoni', 'nim': '126140110', 'nilai_uts': 82, 'nilai_uas': 58, 'nilai_tugas': 86},
]

# untuk menghitung nilai akhir
for mahasiswa in data_mahasiswa:
    nilai_akhir = (0.3 * mahasiswa['nilai_uts']) + (0.4 * mahasiswa['nilai_uas']) + (0.3 * mahasiswa['nilai_tugas'])
    mahasiswa['nilai_akhir'] = nilai_akhir
# untuk menentukan grade
    if nilai_akhir >= 80:
        mahasiswa['grade'] = 'A'
    elif nilai_akhir >= 70:
        mahasiswa['grade'] = 'B'
    elif nilai_akhir >= 60:
        mahasiswa['grade'] = 'C'
    elif nilai_akhir >= 50:
        mahasiswa['grade'] = 'D'
    else:
        mahasiswa['grade'] = 'E'

# Menampilkan tabel data mahasiswa
print("\nTABEL DATA MAHASISWA")
print("=" * 70)
print(f"{'NAMA':<13} {'NIM':<12} {'UTS':<7} {'UAS':<7} {'TUGAS':<7} {'NILAI AKHIR':<12} {'GRADE':<5}")
print("=" * 70)
for mahasiswa in data_mahasiswa:
    print(
        f"{mahasiswa['nama']:<10} {mahasiswa['nim']:<15} {mahasiswa['nilai_uts']:<7} {mahasiswa['nilai_uas']:<8} {mahasiswa['nilai_tugas']:<9} {mahasiswa['nilai_akhir']:<11.2f} {mahasiswa['grade']:<5}")
print("=" * 70)

# untuk mencari nilai tertinggi dan terendah
nilai_akhir_list = [mahasiswa['nilai_akhir'] for mahasiswa in data_mahasiswa]
nilai_tertinggi = max(nilai_akhir_list)
nilai_terendah = min(nilai_akhir_list)

mahasiswa_tertinggi = [m for m in data_mahasiswa if m['nilai_akhir'] == nilai_tertinggi]
mahasiswa_terendah = [m for m in data_mahasiswa if m['nilai_akhir'] == nilai_terendah]

# untuk nilai tertingi
print("\nMAHASISWA DENGAN NILAI TERTINGGI")
for m in mahasiswa_tertinggi:
    print(f"Nama: {m['nama']} | NIM: {m['nim']} | Nilai Akhir: {m['nilai_akhir']:.2f} | Grade: {m['grade']} ")

# untuk nilai terendah
print("\nMAHASISWA DENGAN NILAI TERENDAH")
for m in mahasiswa_terendah:
    print(f"Nama: {m['nama']} | NIM: {m['nim']} | Nilai Akhir: {m['nilai_akhir']:.2f} | Grade: {m['grade']} ")