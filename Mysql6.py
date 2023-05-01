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
            etudiant = c.fetchone()
            if etudiant is None:
                break
            print(etudiant)