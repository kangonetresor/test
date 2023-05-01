import mysql.connector
connection_params = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "database" : "gesetudiant"
}

request = "updata etudiant set classe = %s where NomPrenoms = %s"
params = ("M1 CIO", "Adama Landry")
with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c :
        c.execute(request, params)
        db.commit()
        print("Nombre de lignes mises a jour :", c.rowcount)
        
        