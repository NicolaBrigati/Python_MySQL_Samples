#JSON - JavaScript Object Notation,
# è un formato leggero per lo scambio di dati,
# # facile da leggere e scrivere sia per le persone che per le macchine.
# # È basato su una sintassi simile agli oggetti di JavaScript, ma è indipendente dal linguaggio di programmazione, il che lo rende ampiamente utilizzato per la comunicazione tra applicazioni.

#leggere JSON in python
#da python a JSON
#dati convertibili in Json: dict list tuple strng int float true/false None
#formattare e ordinare JSOn
'''
Caratteristiche principali di JSON
Formato Testuale: I dati sono rappresentati come stringhe di testo in formato chiaro e leggibile.
Struttura a Chiave-Valore: I dati sono organizzati in coppie di chiavi e valori.
Portabilità: JSON può essere utilizzato in qualsiasi linguaggio di programmazione.
Semplice e Leggero: È più semplice e meno verboso rispetto a formati come XML
'''
from xml.sax.expatreader import version

print(">>>>>>>>>>>>>>>JSON")

import json

x = '{"nome": "Nicola", "cognome": "Brigati", "eta": 25}'
y = json.loads(x)
print(type(y))
print(y)
print(y["nome"])

#x = '{"nome": "Nicola", "cognome": "Brigati", "eta": 25}'

x = {
     "nome": "Nicola",
     "cognome": "Brigati",
     "eta": 25,
     "isOnLine": False,
     "Interessi": ["Calcio", "Basket", "Pallanuoto"],
     "monetineInTasca": 4.56,
     "Fidanzata": None
}
print(x["cognome"])

#creiamo un Json
y = json.dumps(x)
print(y)
print(type(y))#genera una stringa

#proviamo una lista
y = json.dumps(["roma", "napoli", "milano"])
print(y)

#formattimao il Jason per renderlo più leggibile
y = json.dumps(x, indent=4, separators=(", ", "= "))
print(y)

#come ordinare le chiavi (ordine alfabetico)
y =json.dumps(x, indent=4, sort_keys=True, separators=(", ", "= ") )
print(y)


#PIP e pacchetti
print(">>>>>>>>>>>>>>>>>>>>Introduzione a Pip e pacchetti")
#pip = un package manager che possimao itallare e disistallare, come un modulo

#verifica se istallato, verificalo dal terminale
#python3 get-pip.py
#pip --version
#per istallare i pacchetti pypi.org (circa)
#installiamo camelcase da terminale con "pip install camelcase" e importo:

import camelcase
c = camelcase.CamelCase()
frase = "Ciao Sono Nic"
print(c.hump(frase))

print(">>>>>>>>>>>try except e finally")
#come gestire le exception, else finally raise/throw
#try esegue un blocco di codice per testare
#except ci permette di raccogliere l errore da try
#finally ci permette di eseguir u naltro tipo di codice

#x = 5
#print(x)

try:
     print(x)
except:
     print("problema")
finally:
     print("problems")

x = 5
try:
     print(x + "ciao")
except NameError:
     print("x non definita")
except:
     print("non è name error")
else:
     print("nessun problema")

x = "10 "
try:
     print(x + "ciao")
except NameError:
     print("x non definita")
except:
     print("non è name error")
else:
     print("nessun problema")


x = "10 "
try:
     print(x + "ciao")
except NameError:
     print("x non definita")
except:
     print("non è name error")
else:
     print("nessun problema")
finally:
     print("finally")

#lanciamo noi un errore con rais eexception :
#z = -1
#if z < 0:
#     raise Exception("Numero min di 0")

print(">>>>>>>>>>>>>>>>>>>input dati")
#user , creare persona, tupla , operazioni
#x = input("cosa vuoi fare")
#print(x)


print(">>>>>>>>>>>>>>>>>>>input dati - ESERCIZIO")

persona = {
    "nome": "Luca",
    "cognome": "Brigati",
    "eta": 25
}

operazioni = ("aggiungere", "modificare", "eliminare", "esci")

def start():
    operazione = input(f"Cosa vuoi fare? ({', '.join(operazioni)}): ")
    if operazione == "esci":
        print("Uscita dal programma.")
        return False  # Indica che si vuole uscire dal ciclo
    elif operazione == "aggiungere":
        x = input("Aggiungi chiave:valore separati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione == "modificare":
        x = input("Modifica chiave:valore separati da una virgola: ")
        modifica(x.split(","))
    elif operazione == "eliminare":
        x = input("Elimina chiave: ")
        elimina(x)
    else:
        print("Operazione non riconosciuta. Riprova.")
    return True  # Indica che il ciclo deve continuare

def aggiungi(param):
    if len(param) < 2:
        print("Formato non valido. Usa 'chiave,valore'.")
        return
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

def modifica(param):
    if len(param) < 2:
        print("Formato non valido. Usa 'chiave,valore'.")
        return
    chiave = param[0]
    valore = param[1]
    if chiave in persona:
        persona[chiave] = valore
        print(persona)
    else:
        print(f"Chiave '{chiave}' non trovata per la modifica.")

def elimina(param):
    chiave = param
    if chiave in persona:
        del persona[chiave]
        print(persona)
    else:
        print(f"Chiave '{chiave}' non trovata nella persona.")

while True:
    if not start():
        break



