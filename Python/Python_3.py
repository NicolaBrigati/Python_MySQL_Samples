#Modulo DATATIMEPython non ha un suo tipo di dati
print(">>>>>>>>>>>>>>>Modulo DATATIME")
'''
import datetime
print(dir(datetime))
'''


'''
parametri di formattazione
Parametri di formattazione delle date
%Y: Anno con quattro cifre (es. 2025).
%y: Anno con due cifre (es. 25 per il 2025).
%m: Mese con due cifre (01-12).
%B: Nome completo del mese (es. "January").
%b: Nome abbreviato del mese (es. "Jan").
%d: Giorno del mese con due cifre (01-31).
%A: Nome completo del giorno della settimana (es. "Monday").
%a: Nome abbreviato del giorno della settimana (es. "Mon").
%w: Giorno della settimana come numero (0 = domenica, 6 = sabato).
%j: Giorno dell'anno con tre cifre (001-366).
Parametri di formattazione dell'ora
%H: Ora (formato 24 ore, 00-23).
%I: Ora (formato 12 ore, 01-12).
%p: AM/PM (es. "AM" o "PM").
%M: Minuti con due cifre (00-59).
%S: Secondi con due cifre (00-59).
%f: Microsecondi (000000-999999).
%z: Offset del fuso orario UTC (es. "+0100").
%Z: Nome del fuso orario (es. "UTC", "CET").
Parametri di formattazione combinati
%c: Rappresentazione completa di data e ora (es. "Tue Jan 4 14:30:00 2025").
%x: Data nel formato locale (es. "01/04/25" negli USA, "04/01/25" in Italia).
%X: Ora nel formato locale (es. "14:30:00").
%%: Percentuale (%).
'''

import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime(2012, 6, 13)
print(x)

x = datetime.datetime.now()
print(x.strftime("%B"))
print(x.strftime("%c"))
print(x.strftime("%d/%m/%y"))

#Modulo Math
print(">>>>>>>>>>>>>>>Modulo MAth")

#funzioni build in come min max abs pow
# funzini con math come sqrt ceil floor pi

x = 12
y = 5
print(x*y)

x= min(4,0,45)
print(x)

x= abs(-45)
print(x)

x= pow(4, 3)
print(x)

import math
x= math.sqrt(64)
print(x)

x = math.ceil(64.80)
print(x)

x = math.floor(35.78)
print(x)

x = math.log(8, 2)
x = math.ceil(x)
print(x)

print(">>>>>>>>>>>>> Formattare le stringhe")

peso = 65
altezza = 175
frase = "ciao sono Nicola e sono alto " + str(175) + " cm"
print(frase)

#cosi non è bello da veder eocme sopra.
#ma lo stream formatting ti permette di migliorarlo come sotto

peso = 65
altezza = 175
anni = 25
frase = "ciao sono Nicola e sono alto {:.1f} cm e peso {} kg e ho {} anni"
print(frase.format(altezza, peso, anni))

#introduciamo gli indici per semplificare quando ho tanti argomenti
peso = 65
altezza = 175
anni = 25
frase = "ciao sono Nicola e sono alto {0:.1f} cm e peso {1} kg e ho {2} anni"
print(frase.format(altezza, peso, anni))