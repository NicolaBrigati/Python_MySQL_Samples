from asyncio.events import BaseDefaultEventLoopPolicy
from os import supports_follow_symlinks
from statistics import median

x = 5
y = 2
print(x+y)
print(x-y)
print(x // y) #divisione approssimata ad inter
print(x / y) #divisione
print(x%y) #restituisce il resto
print (x|y) #conta i bit
print(x**y) #esponenziale

x += 10 #sommiamo allo stesso valore di x (puoi usarlo anche con * / ...)
print(x)

import math #importo il primo modulo math per min-max-abs-sqrt
z = 16
print(math.sqrt(z))
print(abs(z))

c = [1,2,4,6,7,8]
print(min(c), max(c))
print(median(c))

#opertaori di comparazione
x = 6
if x == 5:
    print ("X è 5")
else:
    print ("X è sicuramente altro")

x = 5
is_online = False
if is_online:
    print("is online")
else:
    print("è altrove")

#if else elif  != not equal
x = 6
if x==5:
    print("x è 5")
elif x == 6:
    print("x è 6")
else:
    print("x è altro")

x = 7
if x != 8:
    print("x è diverso")
elif x == 8:
    print("x è 8")
elif x >= 8:
    print("x è maggiore di 8")
else:
    print("x diverso da 8")

#operatori logici and - or - not
x = 8
if x > 3 or x < 7:
    print("ok")

#nested if (if dentro if dentro if...)
x = 4
if x % 2 == 0:
    print("è un numero pari")
    if x > 3:
        print ("è maggiore di 3")
    else:
        print("è minore di 3")

# cicli o loop - while, break, continue, else. Un ciclo esegue la stessa funzione una serie di volte = automatizza
# i è la variabile iteratore, che si mette a contare un numero di volte

print(">>>>>cicli o loop while, break, continue, else")

i =  1
while i < 3:
    print(i)
    i+=1
else:
    print(str(i) + " non è minore di 3")

i =  1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i =  1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

#ciclo for
print(">>>>>ciclo for")

prodotti = ["pane", "nutella", "estathè"]
for prodotto in prodotti: #prodotto e prodotti potrebbero essere anche x & y
    print(prodotto)


prodotti = ["pane", "nutella", "estathè"]
aggettivi = ["caro", "economico", "normale"]
for prodotto in prodotti:
    for aggettivo in aggettivi:
        print(prodotto + " " + aggettivo)

print(str(">>>>>Introduciamo le liste"))
#liste, creazione, lettura, modifica,
#range di elementi
#inserire elementi
#rimuovere elementi
# le liste sono ordinate modificabili e con duplicati, index

citta = ["Milano", "Torino", "Bologna", "Bologna"]
print(citta)
print(citta[0]) #printo le index
citta[3] = "Venezia" #modifico la 3 città con Venezia
print(citta)
print(citta[0:2]) #printo un range
citta.insert(0, "Roma") #inserisco DOVE va inserita nella lista
print(citta)
citta.append("Roma") #append mem lo mette in coda
print(citta)
citta.insert(4, "Napoli")
print(citta)
citta.remove("Roma")
print(citta)
citta.pop()
print(citta)
citta.insert(0, "Roma")
print(citta)

#calcolo la lunghezza, è diversa dall'indice
print(len(citta))

#loop
for citta in citta:
    print(citta)
    if citta == "Bologna":
        break

print(">>>>>> RANGE")
#varie opzioni possibili tra i range, introduzione, elementi, iunizio, fine,salto
#possiamo accedere a dei range solo con i LOOP

x = range(5)
for numero in x:
    print(numero)
    if numero ==  2:
        break

x = range(5, 10)
for numero in x:
    print(numero)

#salto
x = range(0, 10, 3) #l'ultimo numero mi da il salto
for numero in x:
    print(numero)

print(">>>>>>>>>>>>>TUPLE")
#TUPLE, creare, accedere, modifica, spacchettare
#loop
#count, #index
#sono ordinate, IMMUTABILI con Duplicati >> LISTA Costante

citta = ("Milano", "Torino", "Bologna")
print(citta)
print(citta[1])

#da tupla a lista
x=list(citta) #usiamo il costrutturo lista, come se facessimo un cast
x.append("Roma")
citta= tuple(x)
print(citta)

#spacchettiamo la tuple
citta = ("Milano", "Torino", "Bologna")
(x,y,z) = citta
print(x)
print(y)
print(z)

x= "miao"
print(x)

#loop
citta = ("Milano", "Torino", "Bologna")
for citta in citta:
    print(citta)

#count
citta = ("Milano", "Torino", "Bologna", "Bologna")
print(citta.count("Bologna"))

#index
print(citta.index("Milano"))

print(">>>>>>>>>>>SET")
#i SET NON sono ordinati, NON INDEXATI, NON MODIFICABILI, NO DUPLICATI
#comodi per città con cap e dati univoci

citta = {"Milano", "Torino", "Bologna"}
#non puoi cercare l'index, non puoi duplicare

citta.add("Roma") #lo mette a caso nella lista
print(citta)

#possiamo fare il merge dei set:
altre_citta = {"Napoli", "Venezia"}
citta.update(altre_citta)
print(citta)

#clear pulisce tutto, remove lo toglie, discard nonmi da errore se non c'è il valore che voglio rimuovere
citta.remove("Napoli")
citta.discard("Venezia")
for citta in citta:
    print(citta)

print(">>>>>>>>>>>Dictionary")
#sono ordinati, modificabili e non accettono duplicati > ricorda gli oggetti di Javascript
#relazione chiave valore

persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}
print(persona.get("nome"))
print(persona.keys())
print(persona.values())

#come vedere se un achiave è dentro un valore
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}
if "nome" in persona:
    print("ok")
if "scuola" in persona:
    print("ok")
else:
    print("non è presente")

#metodo
persona["scuola"] = "Istituto Scientifico"
print(persona)
persona.update({"scuola":"elementare"})
print(persona)

#loop
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}
for x in persona.values():
    print(x)

#dictionarie nasted
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
    "indirizzo": {
        "nazione" : "Italia",
        "regione" : "Lombardia",
        "citta" : "Milano",
        "via" : "Piazza Gorini 9",
        "CAP" : "20133"
    }
}
print(persona["indirizzo"]["nazione"])

print(">>>>>>>>>>>>>>>>>> FUNZIONI")
#codice che vogliamo ripetere in continuazione
#associarlo a parola chiave

def saluta(): #def = definisci la funzione
    print("ciao")
saluta()

#è troppo generica quindi va definita meglio, arrivano i parametri
def saluta(nome):
    print("ciao sono" + " " + nome)
saluta("Nicola")

#parametro di default
def saluta(nome="Nicola"):
    print("ciao sono" + " " + nome)
saluta()

#cos'è il return, valore di ritorno
def calcolo (x,y):
    somma = x + y
print(calcolo(2,3)) #è sbagliato perchè non gli chiediamo di restituirci un valore

#quindi uso il return
x = 10
y = 5
def calcolo (x,y):
    somma = x + y
    return somma
print(calcolo(x,y))

#altri esempi di funzioni
#funzioni = blocco di codice con ll'interndo delle funzioni che avremo delle cose da richiamare
#esempio > processo per far eun piatto di pasta

def fai_la_pasta():
    print("metti l'acqua")
    print("fai bollire")
    print("metti la pasta")
fai_la_pasta() #per stampare, diversamente avremmo avuto bisogno di scrivere print per tutte le volt che richiamo una funzione

#andiamo a mettere dei parametri per andare a prendere degli "ARGOMENTI", come il tipo di pasta

def fai_la_pasta(tipo_pasta): #questo è il parametro
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)  #questo è l'argomento
fai_la_pasta("spaghetti")

#possiamo avere diversi tipi di argomenti (arbitrari, keywords, extra)

def fai_la_pasta(tipo_pasta, metti_sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if metti_sugo:
        print("prepara sugo")
fai_la_pasta("fusilli", True)

print(">>>>>>>>>>>>>>>>>>>>>Arbitrary arguments")
#Arbitrari Arguments, quando non sappiamo quale mettere

def fai_la_pasta(*opzioni):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + opzioni[0])
    if opzioni[1]:
        print("prepara sugo")

fai_la_pasta("penne", True)

#keywords argument

def fai_la_pasta(tipo_pasta, sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("prepara sugo")

fai_la_pasta(sugo=True, tipo_pasta="fusilli")


#parametri di default
def fai_la_pasta(tipo_pasta = "spaghetti", sugo = True):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("sugo")
fai_la_pasta("fusilli", True)

#return dei valori
def fai_somma(num1, num2):
    somma = num1 + num2
    return somma
x = fai_somma(2,2)
print(x)











