import math_operations as mo
from math_operations import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit
)

def main():
    # untuk menampilkan perhitungan geometri
    print("\n=== HASIL PERHITUNGAN GEOMETRI ===")
    print(f"Luas persegi (sisi=6): {mo.square_area(6)}")
    print(f"Keliling persegi (sisi=6): {mo.square_perimeter(6)}")
    print(f"Luas persegi panjang (5x4): {mo.rectangle_area(5, 4)}")
    print(f"Keliling persegi panjang (5x4): {mo.rectangle_perimeter(5, 4)}")
    print(f"Luas lingkaran (r=7): {mo.circle_area(7):.2f}")
    print(f"Keliling lingkaran (r=7): {mo.circle_circumference(7):.2f}\n")

    # untuk menampilkan konversi suhu
    print("=== HASIL KONVERSI SUHU ===")
    c_temp = 48
    print(f"{c_temp}°C = {celsius_to_fahrenheit(c_temp):.2f}°F")
    print(f"{c_temp}°C = {celsius_to_kelvin(c_temp):.2f}K\n")

    f_temp = 86
    print(f"{f_temp}°F = {fahrenheit_to_celsius(f_temp):.2f}°C")
    print(f"{f_temp}°F = {fahrenheit_to_kelvin(f_temp):.2f}K\n")

    k_temp = 300
    print(f"{k_temp}K = {kelvin_to_celsius(k_temp):.2f}°C")
    print(f"{k_temp}K = {kelvin_to_fahrenheit(k_temp):.2f}°F")

if __name__ == "__main__":
    main()