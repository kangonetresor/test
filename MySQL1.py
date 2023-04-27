import mysql.connector # Pour travailler sur une BD MySQL

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = " ",
    database = "gesetudiant"
)

# faire quelque chose d'utile avec la connexion

db.close()