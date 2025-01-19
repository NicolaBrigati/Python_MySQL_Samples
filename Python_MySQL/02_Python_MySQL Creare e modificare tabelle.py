import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root$1982",
    database="pysql"
)

cursor = db.cursor()
cursor.execute("CREATE TABLE clienti (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")

#se vogliamo vedere se la tabelal esiste
cursor = db.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)

#inserire i valori della tabella
cursor = db.cursor()
sql = "INSERT INTO clienti (nome, cognome) VALUES (%s, %s)"
values = ("Nicola", "Brigati")
cursor.execute(sql, values)
db.commit()

#inserimento multiplo
cursor = db.cursor()
sql = "INSERT INTO clienti (nome, cognome) VALUES (%s, %s)"
values = [
    ("Barbara", "Luraghi"),
    ("Franci", "Scotti"),
    ("Anna", "Neri"),
    ("Giorgio", "Rossi")
]
cursor.executemany(sql, values)
db.commit()

#ricevere id inserita
cursor = db.cursor()
sql = "INSERT INTO clienti (nome, cognome) VALUES (%s, %s)"
values = ("rfr", "frfrf")
cursor.execute(sql, values)
db.commit()
print ("id riga inserita: ", cursor.lastrowid)
