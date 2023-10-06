szam1=input("Irj be egy szamot /szam1/: ")
szam2=input('Irj be masodik szamot /szam2/: ')
szam1=int(szam1)
szam2=int(szam2)

if szam1 > szam2:
    print(f'A szam1 kisebb mint a szam2')
elif szam2 < szam1:
    print(f'A szam2 kisebb mint a szam1')
elif szam1 == szam2:
    print(f'A szamok egyenloek.')

"""
if szam1 == szam2:
    print(f'A ket szam egyenlo')
if szam1 < szam2:
    print(f'A masodik szam a nagyobb')
if szam1 > szam2:
    print(f'Az elso szam a nagyobb')
"""

