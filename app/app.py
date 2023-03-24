# -*- coding: utf-8 -*-

from flask import Flask, request, abort , jsonify
from DatabaseHandler import db_drop_and_create_all, setup_db, Movie , Actor, db
import json
from AuthHandler import AuthError, requires_auth
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)
    
    db_drop_and_create_all()
    CORS(app)
    cors = CORS(app, resources={r"*": {"origins": "*"}})



    @app.after_request
    def after_request(response):
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
            return response
    
    @app.route('/home' , methods=['GET'])
    def home():
        return "Welcome to home page !"
    
    
    @app.route('/movies' , methods=['GET'])
    #@requires_auth('get:movies')
    def getMovies():
       result = db.session.query(Movie).all()
       
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = [json.loads(s.__repr__()) for s in result]
       return jsonify(response)


    @app.route('/actors' , methods=['GET'])
    #@requires_auth('get:actors')
    def getActors():
        
       result = db.session.query(Actor).all()
            
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = [json.loads(s.__repr__()) for s in result]
       return jsonify(response)

    
    
    @app.route('/actor' , methods=['POST'])
    #@requires_auth('post:actor')
    def AddActor():
       data = request.json
       if(data.get('name')==None or data.get('gender')==None or data.get('age')==None):
           abort(400)
       actor = Actor(name=data.get('name') , gender=data.get('gender'),age=data.get('age'))
       db.session.add(actor)
       db.session.commit()
       
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = json.loads(actor.__repr__())
       return jsonify(response)

    
    
    @app.route('/movie' , methods=['POST'])
    #@requires_auth('post:movie')
    def AddMovie():
       data = request.json
       if(data.get('title')==None or data.get('release_date')==None):
           abort(400)
       
       movie = Movie(title=data.get('title') , release_date=data.get('release_date'))
       db.session.add(movie)
       db.session.commit()
            
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = json.loads(movie.__repr__())
       return jsonify(response)
    
    
    @app.route('/movie/<int:id>' , methods=['DELETE'])
    #@requires_auth('delete:movie')
    def deleteMovie(id):
       requstId = id 
       count = Movie.query.filter_by(id=requstId).count()
       if count == 0:
          abort(400)
       db.session.query(Movie).filter(Movie.id ==requstId).delete()
       db.session.commit()
            
               
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = 'SUCCESSFULLY DELETED'
       return jsonify(response)
    
    
    @app.route('/actor/<int:id>' , methods=['DELETE'])
    #@requires_auth('delete:actor')
    def deleteActor(id):
       requstId = id 
       count = Actor.query.filter_by(id=requstId).count()
       if count == 0:
          abort(400)
       db.session.query(Actor).filter(Actor.id ==requstId).delete()
       db.session.commit()
            
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = 'SUCCESSFULLY DELETED'
       return jsonify(response)
    
    @app.route('/actor/<int:id>' , methods=['PATCH'])
    #@requires_auth('patch:actor')
    def getActor(id):
       requstId = id 
       data = request.json
       if(data.get('name')==None or data.get('gender')==None or data.get('age')==None):
           abort(400)
       actor = Actor.query.filter_by(id=requstId).first()
       if(actor is None):
        abort(400)
        
       actor.id = data.get('id')
       actor.name = data.get('name')
       actor.gender = data.get('gender')
       actor.age = data.get('age')
    
       db.session.commit()

       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = json.loads(actor.__repr__())
       return jsonify(response)
    
    @app.route('/movie/<int:id>' , methods=['PATCH'])
   # @requires_auth('patch:movie')
    def getMovie(id):
       requstId = id 
       data = request.json
       if(data.get('title')==None or data.get('release_date')==None ):
           abort(400)
       movie = Movie.query.filter_by(id=requstId).first()
       if(movie is None):
           abort(400)
        
    
       movie.title = data.get('title')
       movie.release_date = data.get('release_date')
    
       db.session.commit()
            
       response = {}
       response["status"]= 'SUCCESS'
       response["errorResponse"]= None
       response["successResponse"] = json.loads(movie.__repr__())
       return jsonify(response)
    
    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            "status": "FAILURE",
            "errorResponse": "Bad Request",
            "successResponse": None
        }), 400
    return app
    
    @app.errorhandler(401)
    def unauthrized(error):
        return jsonify({
            "status": "FAILURE",
            "errorResponse": "UnAuthorized",
            "successResponse": None
        }), 401
    return app
    
    @app.errorhandler(500)
    def internalServerErrro(error):
        return jsonify({
            "status": "FAILURE",
            "errorResponse": "Internal Server Error",
            "successResponse": None
        }), 500
    return app
    
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
