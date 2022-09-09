'''
Jawaban Soal Ujian Praktikum
Buatlah sintaks menghitung volume bangun ruang
'''

print("\n1.Volume Balok")
print("\n")
panjang_b = int(input("Masukan Input Panjang:"))
lebar_b = int(input("Masukan Input Lebar:"))
tinggi_b = int(input("Masukan Input Tinggi:"))
volume_b = panjang_b * lebar_b * tinggi_b

print("Volume Balok adalah",volume_b)

print("\n2.Volume Kubus")
print("\n")      
sisi = int(input("Masukan Input Sisi:"))
volume_k = sisi * sisi * sisi

print("Volume Kubus Adalah",volume_k)

print("\n3.Volume Limas")
print("\n")
la_psisi = int(input("Masukan Input Luas Alas Persegi Sisi:"))
tinggi_l = int(input("Masukan Input Tinggi Limas:"))
volume_l = 1/3 * (la_psisi * la_psisi) * tinggi_l

print("Volume Limas Adalah",volume_l)

print("\n4.Volume Tabung")
print("\n")
phi = 22/7
r = int(input("Masukan Input r:"))
t = int(input("Masukan Input t:"))
volume_t = phi * r * t

print("Volume Tabung Adalah",volume_t)

print("\nCelcius to Reamur")
print("\n")
c = int(input("Masukan Input Celcius:"))
rem = 4/5 * c
print("Reamurnya Adalah",rem)
        
    
