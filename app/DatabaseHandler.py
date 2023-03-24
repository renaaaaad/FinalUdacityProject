

import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "postgresql://postgres:12345@localhost:5432/AgencyDB"
#database_path = os.environ.get('DATABASE_URL')

#database_path = 'postgresql://postgres:12345@localhost:5432/trivia'
db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Movie(db.Model):
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    title = Column(String(80), unique=False)
    release_date = Column(String(180), nullable=False)

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': json.loads(self.release_date)
        }

    def __repr__(self):
        return json.dumps(self.short())
    
    def short(self):
       
        return {
            'id': self.id,
            'title': self.title,
            'release_date':  self.release_date
    }
    
class Actor(db.Model):
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    # String Title
    name = Column(String(80), unique=False)
    gender = Column(String(180), nullable=False)
    age = Column(Integer(), nullable=False)

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.gender,
            'gender': self.age
        }
    
    def __repr__(self):
        return json.dumps(self.short())
    
    def short(self):
        
        return {
            'id': self.id,
            'name': self.name,
            'age': self.gender,
            'gender': self.age
    }