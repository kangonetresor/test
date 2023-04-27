import mysql.connector # Pour travailler sur une BD MySQL

connection_params = {
    "host" : "localhost",
    "user" : "root",
    "password" : " ",
    "database" : "gesetudiant"
    }

with mysql.connector(**connection_params) as db :
    # faire quelque chose d'utile avec la connexion
    pass