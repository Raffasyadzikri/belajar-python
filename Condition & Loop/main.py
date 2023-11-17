number = 6 
number = int(input("Masukkan angka pertama: "))
mod = number % 2

if mod == 0:
    print(f"{number} adalah angka genap")
else:
    print(f"{number} adalah angka ganjil")

print("Skor Range")

score = int(input("Masukkan nilai anda: "))

if score >= 85 and score <= 100:
    print("Kamu mendapatkan A")
elif score >=70 and score <=84:
    print("Kamu mendapatkan B")
elif score >=60 and score <=69:
    print("Kamu mendapatkan C")
else:
    print("Kamu mendapatkan D")

