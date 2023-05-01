import mysql.connector

connection_params = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "database" : "gesetudiant"
}

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c :
        pass