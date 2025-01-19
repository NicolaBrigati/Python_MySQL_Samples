print(">>>>>>>>>>>>>>>>>Come lavorare con i file")
#file handling, read, append, write, create (rawx)
#aprire, leggere, creare, scrivere, eliminare un file


f = open("testo.txt", "r")
for riga in f:
    print(riga)
    print(f.read(7))
    print(f.read())
f.close()

#con append possiamo aggiunger
f = open("testo.txt", "a")
f.write("Dentro scriviamo quello che vogliamo")
f.close()
f = open("testo.txt", "r")
print(f.read())

#con w cancella il resto
f = open("testo.txt", "w")
f.write("Dentro scriviamo quello che vogliamo")
f.close()
f = open("testo.txt", "r")
print(f.read())

#come creare eun file
f = open("prova.txt", "w")
# w ti cancella tutto quello che hai e sovrascrive

#per rimuove il file
# import os
# os.remove("testo.txt")

#per capire se c'è un file
# if os.path.exists("prova.txt"):
#    os.remove("prova.txt")
# else:
#    print("non esiste un file con questo nome")


