import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from Main import create_app
from DatabaseHandler import db_drop_and_create_all, setup_db, Movie , Actor, db

class TestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "AgencyDB"
        self.database_path = 'postgresql://postgres:12345@localhost:5432/AgencyDB'

        setup_db(self.app)
        self.updatedMovie =  {
    "title":"The lion king",
     "release_date":"June 24, 1994"}
        self.updatedActor =  {
    "name":"sandra bullock",
     "age":58,
     "gender":"female"}
        self.addActor =  {
    "name":"angelina jolie",
     "age":47,
     "gender":"female"}
        self.addMovie =  {
    "title":"Maleficent",
     "release_date":"May 28, 2014"}



    def testUpdateSpcificMovieFailuer(self):
        res = self.client().patch("/movies/9999")
        self.assertEqual(res.status_code, 400)  
        
    def testUpdateSpcificActorFailuer(self):
        res = self.client().patch("/actors/9999")
        self.assertEqual(res.status_code, 400)  
        
    def testAddNewMovieSuccess(self):
         res = self.client().post("/movie" ,json =self.addMovie)
         self.assertEqual(res.status_code, 200)
         
    def testAddNewActorSuccess(self):
         res = self.client().post("/actor" ,json =self.addActor)
         self.assertEqual(res.status_code, 200)
         
    def testUpdateSpcificMovieSuccess(self):
        res = self.client().patch("/movie/1" ,json =self.updatedMovie)
        self.assertEqual(res.status_code, 200)  
        
    def testUpdateSpcificActorSuccess(self):
        res = self.client().patch("/actor/1" ,json =self.updatedActor)
        self.assertEqual(res.status_code, 200)  
        
    def testAddNewMovieFailuer(self):
         res = self.client().post("/movie" ,json =None)
         self.assertEqual(res.status_code, 400)
         
    def testAddNewActorFailuer(self):
         res = self.client().post("/actor" ,json =None)
         self.assertEqual(res.status_code, 400)

    def testDeleteActorFailuer(self):
         res = self.client().delete("/actor/99999" ,json =None)
         self.assertEqual(res.status_code, 400)
         
    def testDeleteMovieFailuer(self):
              res = self.client().delete("/movie/99999" ,json =None)
              self.assertEqual(res.status_code, 400)

    def testDeleteMovieSuccess(self):
              res = self.client().delete("/movie/1" ,json =None)
              self.assertEqual(res.status_code, 200)

    def testDeleteActorSuccess(self):
              res = self.client().delete("/actor/1" ,json =None)
              self.assertEqual(res.status_code, 200)
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
