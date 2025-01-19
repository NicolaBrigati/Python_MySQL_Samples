#classi e oggetti
print(">>>>>>>>>>>>> CLASSI, OGGETTI, ISTANZA, METODI, COSTRUTTORE, PARAMETRO SELF ")

#la programmazione ad oggetti va a prendere oggetti e identità nel mondo reale e le trasforma nel ns programma
#quindi si creano degli stampini (la ns classe, ad esempio le persone) della vita reale

class Persona:
    nome = "Nicola"
    cognome = "Brigati"

#creo un oggetto, come creo degli stampi per dei biscotti
persona1 = Persona()
persona2 = Persona()

#l'istanza è quella determinata persona. Un oggetto è dell'istanza persona
print(persona1.nome)

#introduciamo il COSTRUTTORE
#self = riferimento a se stesso
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

persona1 = Persona("Nicola", "Brigati")
persona2 = Persona("Mario", "Rossi")

print(persona2.nome)

#Metodi, è un azione come qua sotto "saluta"
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("ciao sono " + self.nome)

persona1 = Persona("Nicola", "Brigati")
persona2 = Persona("Mario", "Rossi")
persona2.saluta()

#parametro self, ci aiuta a capire di che oggetto stiamo parlando
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("ciao sono " + self.nome + " " + self.cognome)

persona1 = Persona("Nicola", "Brigati")
persona2 = Persona("Mario", "Rossi")
persona2.saluta()
persona1.saluta()

#cambio nome
persona2.nome = "Maria"
persona2.saluta()

#rimuovere
del persona2.nome

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        nome = self.nome if hasattr(self, 'nome') else "Manca il nome"
        cognome = self.cognome if hasattr(self, 'cognome') else "Manca il cognome"
        print("ciao sono " + nome + " " + cognome)

persona1 = Persona("Nicola", "Brigati")
persona2 = Persona("Mario", "Rossi")

# Saluti iniziali
persona2.saluta()
persona1.saluta()

# Cambio nome
persona2.nome = "Maria"
persona2.saluta()

# Rimuovere
del persona2.nome
persona1.saluta()
persona2.saluta()

#continuiamo con la programmazione ad oggetit
print(">>>>>>>>>>>>>>>>>>> EREDITARIETà") #classi che derivano da altre classi ereditano

class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono " + self.nome)

class Insegnante(Persona):  #vado a scivere per erditar eil costruttore
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)  #super dice che eredita da sopra

persona1 = Persona("Nicola", "Brigati")
insegnante1 = Insegnante("Barbara", "Luraghi")

persona1.saluta()
insegnante1.saluta()

print(">>>>>>>>>>>>>>>CLASSE FIGLIA")
#proprietà esclusive della classe Figlia
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono " + self.nome)
    def presentazioni_persona(self):
        print("Sono uno studente di questa scuola")
    def risposta_furba_persona(self):
        print("Vado bene in tutte")

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia): #aggiungo materia
        super().__init__(nome, cognome)
        self.materia = materia
    def saluta(self):
        print("Buongiorno sono " + self.nome + " " + self.cognome)
    def dai_voto(self):
        print("Bravo, un bel 8")
    def promozione(self):
        print("Sei stato promosso")
    def altre_materie(self):
        print("Nelle altre materie come siamo messi?")

persona1 = Persona("Nicola", "Brigati")
insegnante1 = Insegnante("Barbara", "Luraghi", "Matematica")
insegnante2= Insegnante("Berry", "Vecchio", "Italiano")

persona1.saluta()
persona1.presentazioni_persona()
insegnante1.saluta()
print("e insegno" + " " + insegnante1.materia)
insegnante1.dai_voto()
insegnante1.promozione()
insegnante2.saluta()
print("e insegno" + " " + insegnante2.materia)
insegnante2.altre_materie()
persona1.risposta_furba_persona()

print(">>>>>>>>>>>>>>>SCOPE")
#Lo scope è la disponibilità della variabile dentro una funzione, può essere locale o globale

def funzione():
    x = 400
    print(x)
funzione()

#altro esempio con sottofunzione con scope locale
def funzione():
    x = 400
    def sottofunzione():
        print(x)
    sottofunzione()
funzione()

#scope globale, in questo caso la varaibile x è esterna
x = 400
def funzione():
    print(x)
funzione()

x = 400
def funzione():
    global x #la x che uso qua fa riferimento a quella sotto
    x = 100
    print(x)
funzione()
print(x)  #in questo caso la x passa da 400 a 100, ecco perchè mi stampa 2 volte 100

print(">>>>>>>>>>>>>>>>>Moduli = ovvero una libreria")
#Modulo #cos'è e come crarlo #funzioni e variabili in un modulo
#creare un alias #moduli built #funzione dir()

import miomodulo
miomodulo.saluta("Nicola")
x = miomodulo.persona1["nome"]
miomodulo.saluta(x)

#come creo un alias per il mio modulo (numpy è "np")
import miomodulo as mm
mm.saluta("Nicola")
x = mm.persona1["nome"]
mm.saluta(x)

#per vedere tutte le funzioni di un modulo esempio in math
#import math
#print(dir(math))

