def russian_peasant_multiplication(x, y):
    result = 0

    while y > 0:
        if y % 2 == 1:
            result += x
        x *= 2
        y //= 2

    return result

# Meminta input dari pengguna
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

# Menampilkan hasil perkalian menggunakan algoritma Russian Peasant
print("Hasil perkalian menggunakan algoritma Russian Peasant Multiplication adalah:", russian_peasant_multiplication(x, y))
