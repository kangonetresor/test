import mysql.connector
connection_params = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "database" : "gesetudiant"
}

request = "select * from etudiant where NomPrenoms=%s"
params = ("Adama Landry",)
with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c :
        c.execute(request, params)
        resultats = c.fetchall()
        for etudiant in resultats :
            print(etudiant)

        