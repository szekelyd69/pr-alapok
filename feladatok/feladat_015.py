# feladat 015

"""
Kérjuk be a vezetek  es keresztnevunket.
Irassuk ki fuggveny segitsegevel a nevunket
pl:
Be: kerem a vezetekneved: szekely
Be: kerem a keresztneved: takacs
Ki: a nevem takacs istvan
"""

vnev = input("Kérem a vezetéknevedet:")
knev = input("Kérem a keresztnevedet:")

def nevf(vnev,knev):
   nevem = vnev + ' ' + knev
   return nevem 

print(f"A nevem: {nevf(vnev, knev)}")