import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))

# Créer l'instance connexion
connex_app = connexion.App(__name__, specification_dir=basedir)

# Récupérer l'instance Flask
app = connex_app.app

# Définir l'URL SQLite pour SQLAlchemy
sqlite_url = "sqlite:////" + os.path.join(basedir, "people.db")

# Configurer SQLAlchemy
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Créer l'instance SQLAlchemy
db = SQLAlchemy(app)

# Initialiser Marshmallow
ma = Marshmallow(app)
