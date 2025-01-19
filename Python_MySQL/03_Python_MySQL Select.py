import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root$1982",
    database="pysql"
)

#come prendere tutte le righe dal db, per una solo uso "fetchone"
cursor = db.cursor()
sql = "SELECT * FROM clienti"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)

#uso le condizioni
print(">>>>>>>>>>USO LE CONDIZIONI")
cursor = db.cursor()
sql = "SELECT * FROM clienti WHERE cognome = 'Brigati' OR nome = 'Barbara'"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)

#orderby
print(">>>>>>>>>>ORDERBY")
cursor = db.cursor()
sql = "SELECT * FROM clienti ORDER BY nome ASC LIMIT 4"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)


#delete
print(">>>>>>>>>>DELETE")
cursor = db.cursor()
sql = "DELETE FROM clienti WHERE id = 6"
cursor.execute(sql)
db.commit()

print("Numero di righe cancellate: ", cursor.rowcount)

#delete alternativa in modo dinamico
cursor = db.cursor()
sql = "DELETE FROM clienti WHERE nome = %s AND cognome = %s"
valore = ("Paolo", "Gialli") #qua ho messi valori falsi per evitare di cancellare troppe righe
cursor.execute(sql, valore)
db.commit()

print("Numero di righe cancellate: ", cursor.rowcount)

#UPDATE dei dati
print(">>>>>>>>>>UPDATE")
cursor = db.cursor()
sql = "UPDATE clienti SET nome = 'Geronimo' WHERE id = 5"
cursor.execute(sql)
db.commit()
print("Righe modificate ", cursor.rowcount)

#UPDATE dei dati dinamici
cursor = db.cursor()
sql = "UPDATE clienti SET nome = %s WHERE id = %s"
valori = ("Gigio", 5)
cursor.execute(sql, valori)
db.commit()
print("Righe modificate ", cursor.rowcount)