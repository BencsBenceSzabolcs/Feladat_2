# 3. feladat
class SzamStatisztika:
    def __init__(self, szamok):
        self.szamok = szamok

    def legnagyobb(self):
        return max(self.szamok)

    def legkisebb(self):
        return min(self.szamok)

    def median(self):
        rendezett = sorted(self.szamok)
        n = len(rendezett)
        if n % 2 == 1:  # páratlan elemszám
            return rendezett[n // 2]
        else:  # páros elemszám
            return (rendezett[n // 2 - 1] + rendezett[n // 2]) / 2

    def paros_paratlan_db(self):
        paros = sum(1 for x in self.szamok if x % 2 == 0)
        paratlan = len(self.szamok) - paros
        return paros, paratlan


# főprogram
szamok = []
for i in range(7):
    szam = int(input(f"Add meg a(z) {i+1}. számot: "))
    szamok.append(szam)

statisztika = SzamStatisztika(szamok)

print("\n--- Statisztika eredmények ---")
print("Beírt számok:", szamok)
print("Legnagyobb szám:", statisztika.legnagyobb())
print("Legkisebb szám:", statisztika.legkisebb())
print("Medián:", statisztika.median())

paros, paratlan = statisztika.paros_paratlan_db()
print("Páros számok száma:", paros)
print("Páratlan számok száma:", paratlan)
