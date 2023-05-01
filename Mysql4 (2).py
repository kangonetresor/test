import datetime
import mysql.connector

connection_params = {
    "host": "localhost",
    "user" : "root",
    "password" : "",
    "database" : "gesetudiant"
}

request = """insert into etudiant 
            (Matricule, NomPrenoms, Classe, DateInscription) 
            values(%s, %s, %s, %s)""" 
params = [("CI0119376468","Adama Landry", "Licence 3", datetime.date.today()),
          ("CI0118330826", "Kouamé Yves", "Licence 1", datetime.date.today()),
          ("CI0117324072", "Maro Elavi", "Licence 1", datetime.date.today()),
          ("CI0115289594", "Touri Alasco", "Master 1", datetime.date.today()),
          ("CI0119365659", "Yakoue Boris", "Master 2", datetime.date.today()),
          ("CI0116453054", "Aka-De Naomi", "Licence 3", datetime.date.today()),
          ("CI0119363434", "Diakité Amarou", "Licence 3", datetime.date.today()),
          ("CI0118340270", "Amani Bakou Brice", "Doctorat", datetime.date.today()),
          ("CI0118764642", "Amiano Rock", "Licence 1", datetime.date.today()),
          ("CI0115697434", "Yapo Noel", "Licence 3", datetime.date.today()),
          ("CI0119546704", "Traore Oumar", "Licence 2", datetime.date.today()),
          ("CI0122422258", "Taboh Issouf", "Licence 3", datetime.date.today()),
          ("CI0121392926", "Kangone Bi Tresor", "Master 2", datetime.date.today()),
          ("CI0120381917", "Kate Shadrack", "Licence 3", datetime.date.today()),
          ("CI0120381232", "Chonou Oriane", "Master 2", datetime.date.today()),
          ("CI0119371757", "Georges St-Pierre", "Master 2", datetime.date.today()),
          ("CI0118184335", "Affi Cynthia", "Doctorat", datetime.date.today()),
          ("CI0119361708", "Soro Kayazin", "Licence 1", datetime.date.today()),
          ("CI0132396080", "Taylor DuBoi", "Licence 3", datetime.date.today())
        ]

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c :
        c.executemany(request, params)
        db.commit()
        print("Nombre de lignes insérées :", c.rowcount)