#dk9 104-105
"""
Amikor karakterlánccá átalakitúnk, az str utasításra van szükség.
"""
felhasznalo_kora = 16
print(f"A felhasznalo_kora valtozo tipusa: {type(felhasznalo_kora)}")
felhasznalo_kora = str(felhasznalo_kora)
print(f'A felhasznalo_kora valtozo tipusa: {type(felhasznalo_kora)}')
ilyen = input('És milyen ' + felhasznalo_kora + ' évesnek lenni? ')
olyan = input(f'És milyen {felhasznalo_kora} évesnek lenni?')