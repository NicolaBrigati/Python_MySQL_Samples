import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root$1982",
    database="pysql"
)

#inserisco i campi nelle citta

#cursor = db.cursor()
#sql = "INSERT INTO citta (nome_citta) VALUES (%s)"
#values = [
#    ("Milano",),("Roma",),("Napoli",),("Torino",)]  # Lista di tuple
#cursor.executemany(sql, values)
#db.commit()


#Joint
cursor = db.cursor()
sql = "SELECT \
       nome, cognome, citta.nome_citta \
       FROM clienti \
       INNER JOIN citta ON clienti.citta = citta.id"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)


#Joint Left
cursor = db.cursor()
sql = "SELECT \
       nome, cognome, citta.nome_citta \
       FROM clienti \
       RIGHT JOIN citta ON clienti.citta = citta.id"
cursor.execute(sql)
result = cursor.fetchall()

for riga in result:
    print(riga)


#elimino e creo tab
cursor = db.cursor()
sql = "DROP TABLE IF EXISTS temporanea"
cursor.execute(sql)


