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
        while True:
            resultats = c.fetchmany(10)  
            if not resultats:
                break
            for utilisateur in resultats:
                print(utilisateur)
