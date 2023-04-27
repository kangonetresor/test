import mysql.connector # Pour travailler sur une BD MySQL

connection_params = {
    "host" : "localhost",
    "user" : "root",
    "password" : " ",
    "database" : "gesetudiant"
    }

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as C:
        # faire quelque chose d'utile avec la connexion
        pass