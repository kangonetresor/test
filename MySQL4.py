import datetime
import mysql.connector # Pour travailler sur une BD MySQL

connection_params = {
    "host" : "localhost",
    "user" : "root",
    "password" : " ",
    "database" : "gesetudiant"
    }

request = """insert into etudiant
            (id_etud, matricule, NomPrenoms, classe, dateinscription)
            values (%s, %s, %s, %s)"""
params = ("CI0210033533", "KONE Siriki", "M2 CIO", datetime.date.today())
with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c:
        c.execute(request, params)
        db.commit()