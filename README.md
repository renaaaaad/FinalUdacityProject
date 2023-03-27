# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:11:30 2023

@author: renad
"""

# Introduction
 The Casting Agency models a company that is responsible for 
 creating movies and managing and assigning actors to those movies. 
 You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
 
# Motivation
 This Project is for the final Undacoty project for the nanodegree program
 
# Tech Stack
 The main is Flask and SQLAlchemy
 
# Installation instructions
 just download all the libaries in requirements.txt and make sure to 
 set database libary in system enviroment under the name "DATABASE_URL"
 
# Testing instructions
  just download all the libaries in requirements.txt and make sure to 
  set database libary in system enviroment under the name "DATABASE_URL"
  
# Roles and the permissions
 1- Casting Assistant
        Can view actors and movies
 2- Casting Director
        All permissions a Casting Assistant has 
        Add or delete an actor from the database
        Modify actors or movies
 3- Executive Producer
        All permissions a Casting Director has 
        Add or delete a movie from the database
  
# APIs
 1- GET /actors 
   Body: None
   Response: 
   {
    "errorResponse": null,
    "status": "SUCCESS",
    "successResponse": [
        {
    "name": "angelina jolie",
    "age": 47,
    "gender": "female"
        }
    ]
}
 
 2- GET /movies
   Body: None
   Response:
   {
    "errorResponse": null,
    "status": "SUCCESS",
    "successResponse": [
        {
            "id": 1,
            "release_date": "03/24/2023",
            "title": "The lion King"
        }
    ]
}

 3- POST /actor
   Body:
        {
    "name": "angelina jolie",
    "age": 47,
    "gender": "female"
        }
   Response:
       {
    "errorResponse": null,
    "status": "SUCCESS",
    "successResponse":
           {
        "name": "angelina jolie",
        "age": 47,
        "gender": "female"
            }
        }
        
        
 4- POST /movie
   Body:
       {
    "title":"The lion King",
    "release_date":"03/24/2023"
        }
   Response:
          {
       "errorResponse": null,
       "status": "SUCCESS",
       "successResponse":
       {
    "title":"The lion King",
    "release_date":"03/24/2023"
        }
          }

 5- DELETE /movie/id
   Body: None
   Response:
          {
       "errorResponse": null,
       "status": "SUCCESS",
       "successResponse": "SUCCESSFULLY DELETED"
           }
 6- DELETE /actor/id
   Body: None
   Response:
             {
          "errorResponse": null,
          "status": "SUCCESS",
          "successResponse": "SUCCESSFULLY DELETED"
              }
              
 7- PATCH /actor/id
   Body:
        {
    "name": "angelina jolie",
    "age": 47,
    "gender": "female"
        }
   Response:
       {
    "errorResponse": null,
    "status": "SUCCESS",
    "successResponse":
           {
        "name": "angelina jolie",
        "age": 47,
        "gender": "female"
            }
        }

 8- PATCH /movie/id
    Body:
        {
     "title":"The lion King",
     "release_date":"03/24/2023"
         }
    Response:
           {
        "errorResponse": null,
        "status": "SUCCESS",
        "successResponse":
        {
     "title":"The lion King",
     "release_date":"03/24/2023"
         }
           }
           
 9- ERROR
   if there is any error (400 , 401 , 500 ,..) you will recive the same exact 
   response body:
              {
           "errorResponse": "FAILURE",
           "status": "SUCCESS",
           "successResponse":None
           "errorResponse": error message
   
# Heroku
 You can access the depolyed project in Heroku useing the 
 following link:
 https://render-deployment-example-u8tq.onrender.com/
 *Note: the code deplyed on hekaru dosnt apply any role and permissions
  its an easy access so you can test the priject on dummy database