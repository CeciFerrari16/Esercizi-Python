# Esercizio 25 p.73
nomi = []
punti = []

a = input("Inserisci il nome del primo candidato:").upper()
num1 = int(input("Inserisci il suo punteggio:"))
nomi.append(a)
punti.append(num1)

b = input("Inserisci il nome del secondo candidato:").upper()
num2 = int(input("Inserisci il suo punteggio:"))
nomi.append(b)
punti.append(num2)

print("Elenco dei candidati in ordine alfabetico:")
nomi.sort()
print(nomi)

input()

print("Elenco dei candidati in ordine decrescente rispetto al punteggio:")
if num1 > num2:
    nomi.clear()
    nomi.append(a)
    nomi.append(b)
    print(nomi)
elif num1 < num2:
    nomi.clear()
    nomi.append(b)
    nomi.append(a)
    print(nomi)
else:
    print("Probabilmente è un pareggio")
    print(punti)

#oppure semplicemente:
'''
if num1 > num2:
    print(a, b)
elif num1 < num2:
    print(b, a)
else:
    print("Probabilmente è un pareggio")
    print(punti)
'''