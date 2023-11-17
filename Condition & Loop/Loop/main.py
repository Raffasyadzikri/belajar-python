loop = int(input("Mau Berapa?"))

for x in range(1,loop+1):
    print(f"santri ke-{x}")

print("Tabel Perkalian")

number = int(input("Mau perkalian berapa?: "))
loop = int(input("Mau berapa banyak?: "))

for x in range(1,loop+1):
    result = number * x
    print(f"{number} x {x} = {result}")
