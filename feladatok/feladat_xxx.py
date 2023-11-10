# feladat_014
"""

Kérjuk be a vezetek  es keresztnevunket.
Irassuk ki eljaras segitsegevel a nevunket
pl:
Be: kerem a vezetekneved: szekely
Be: kerem a keresztneved: takacs
Ki: a nevem takacs istvan
"""

vnev = input("Kérem a vezetéknevedet:")
knev = input("Kérem a keresztnevedet:")

def nev(vnev,knev):
    print(f"A nevem {vnev} {knev}.")


nev(vnev,knev)
