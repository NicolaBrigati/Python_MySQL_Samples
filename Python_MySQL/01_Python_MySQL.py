print(">>>>>>>>>>>>>>>>>MYSQL")
#come creare database e tabelle

import mysql.connector

# Esempio di connessione a un database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root$1982",
    database=""
)
#verifica connessione
print(db)

#oppure per verificare i dettagli di una tabella (metti ilnome del database sopra):
cursor =db.cursor()
cursor.execute("Show tables;")
print(cursor.fetchall())

#creare db, il cursone è qualcosa che punta, che mi permetta di spostarmi dentro al db
cursor = db.cursor()
cursor.execute("CREATE DATABASE pysql") #se lo rifaccio mi da errore perchè lo ha già creato

#per vedere il db
cursor = db.cursor()
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

