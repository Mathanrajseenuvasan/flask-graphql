# Imports
from flask_sqlalchemy import SQLAlchemy
from graphql_service import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/graphql'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
