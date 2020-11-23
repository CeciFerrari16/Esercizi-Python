# Esercizio 27 p.73
print("Casello autostradale")
print("Inserisci '0' quando hai finito di inserire i dati")
num = [] #numero veicoli
gg = 0 #numero giorni
while True:
    veicoli = int(input("Quanti veicoli sono entrati oggi?"))
    if veicoli != 0:
        gg += 1
        num.append(veicoli)
        tot = sum(num)
    else:
        break

print("In autostrada sono entrati", tot, "veicoli in", gg, "giorni")
