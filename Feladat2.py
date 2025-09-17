# 2. feladat
szamok = []
for i in range(7):
    szam = int(input(f"Add meg a(z) {i+1}. számot: "))
    szamok.append(szam)

pozitiv = sum(1 for x in szamok if x > 0)
negativ = sum(1 for x in szamok if x < 0)

print("\nBeírt számok:", szamok)
print("Pozitív számok száma:", pozitiv)
print("Negatív számok száma:", negativ)
print("Legnagyobb szám:", max(szamok))
print("Legkisebb szám:", min(szamok))
