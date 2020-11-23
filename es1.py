# Esercizio 24 p.73
print("Elezioni: ballottaggio tra due candidati")
a = int(input("Inserisci il numero di voti per il primo candidato:"))
b = int(input("Inserisci il numero di voti per il secondo candidato:"))
tot = a + b
perc1 = round(100 * a / tot)
perc2 = round(100 * b / tot) 

if a == b:
    print("Il risultato delle elezioni è un pareggio")
    print(perc1, perc2)
else:
    print("La percentuale del primo candidato è:", perc1, "%")
    print("La percentuale del secondo candidato è:", perc2, "%")
