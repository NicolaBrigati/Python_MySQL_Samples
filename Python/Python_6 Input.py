# Chiedi all'utente di inserire un numero
numero = float(input("Inserisci un numero: "))
# Moltiplica il numero per 2
risultato = numero * 2
# Mostra il risultato
print("Il risultato di", numero, "moltiplicato per 2 è", risultato)


# Chiedi una risposta tra le opzioni
risposta = input("Scegli una risposta (opzioni: A, B, C): ")

# Controlla se la risposta è corretta
if risposta.upper() == "A":
    print("Hai scelto la risposta corretta!")
elif risposta.upper() == "B" or risposta.upper() == "C":
    print("Hai scelto una risposta errata, ma il programma continua...")
else:
    print("Risposta non valida. Uscita dal programma.")
    exit()  # Termina il programma


##cicli semplici:
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ciclo for annidato per iterare sulle righe e sulle colonne della matrice
for riga in matrice:
    for elemento in riga:
        print(elemento, end=" ")
    print()  # Aggiunge una nuova riga per ogni riga della matrice


# Definizione di un array (lista) con alcuni numeri
numeri = [1, 2, 3, 4, 5]
# Ciclo for per iterare su ogni elemento della lista
for numero in numeri:
    print(f"Il numero è: {numero}")