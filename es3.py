# Esercizio 26 p.73
count = 0
lista = []
print("La media degli stipendi")
print("Inserisci '-1' quando hai finito di inserire gli stipendi")

while True:
    stipendio = int(input("Inserisci lo stipendio:"))
    if stipendio != -1:
        count += 1
        lista.append(stipendio)
        tot = sum(lista)
        media = tot / count
    else:
        break

print("La media è", round(media, 2))