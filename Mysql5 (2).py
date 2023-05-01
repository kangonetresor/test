import mysql.connector

connection_params = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "database" : "gesetudiant"
}

request = "select * from etudiant"

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c :
        c.execute(request)
        resultat = c.fetchall()
        for etudiant in resultat : 
            print(etudiant)