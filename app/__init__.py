from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma 
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
CORS(app) #Security, page in notebook

app.register_blueprint(site) #site, routes.py, Line 3
app.register_blueprint(auth) #authentication, routes.py Line 4
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config) #config.py
root_db.init_app(app) #models.py, Line 8--->from models import db as root_db, login_manager, ma 
login_manager.init_app(app) #models.py, Line 8--->from models import db as root_db, login_manager, ma
ma.init_app(app) #models.py, Line 8--->from models import db as root_db, login_manager, ma
migrate = Migrate(app, root_db) #from flask_migrate import Migrate

# if __name__ == '__main__':
#     create_app().run(host='0.0.0.0', port=5000, debug=True)