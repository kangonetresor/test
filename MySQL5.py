import mysql.connector # Pour travailler sur une BD MySQL

connection_params = {
    "host" : "localhost",
    "user" : "root",
    "password" : " ",
    "database" : "gesetudiant"
    }

request = "select * from etudiant"

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c:
        c.execute(request)
        resultats = c.fetchall()
        for etudiant in resultats:
            print(etudiant)