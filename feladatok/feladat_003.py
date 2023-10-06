# feladat_003
# dk9 95-oldal
print(f'Üdv néked!')
évek_száma = input('Hány éves vagy? ')
évek_száma = int(évek_száma)
if évek_száma == 0:
 print(f"Még nem születtél meg!")
elif évek_száma < 6:
     print(f"{évek_száma} éves vagy, még nem jársz általánosba.")
elif évek_száma >= 6 and évek_száma <= 14:
     print(f"{évek_száma} éves vagy. Általános iskolába jársz.")
elif évek_száma > 14 and évek_szá0ma <= 65:
     print(f"{évek_száma} éves vagy. Tanulsz vagy dolgozol!")
else:
    print(f"{évek_száma} éves vagy. Nyugdíjas.")
# else:
# print(f"Egy év múlva {évek_száma+1} éves leszel.")
# print(f"Nem általános iskolába jársz.")