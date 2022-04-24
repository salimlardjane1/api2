import os
from config import db
from models import Person

# Données pour initialiser la base
PEOPLE = [
    {"fname": "Jean", "lname": "Dupont"},
    {"fname": "Louise", "lname": "Durand"},
    {"fname": "Francois", "lname": "Lopez"},
]

# Supprimer la base si elle existe déjà
if os.path.exists("people.db"):
    os.remove("people.db")

# Créer la base de données
db.create_all()

# Remplir la base en itérant sur PEOPLE
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))
    db.session.add(p)

db.session.commit()
