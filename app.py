from flask import Flask, render_template, url_for, flash, redirect
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask import Flask, render_template, url_for, flash, redirect
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# --------------------------------- [edit] ---------------------------------- #
def proced():
    print("proced")
def create_app():
    app = Flask(__name__)
    api = Api(app)





    # ORM
#    database = create_engine('mysql://root:1234@localhost/sys', encoding ='utf-8')
#    app.database = database




    from .views.pages import Home, Corporation, Spec, Field, Academic, Result, Book, Course, Search, Search_result
    api.add_resource(Home, '/mainpage')
    api.add_resource(Corporation, '/corporation')
    api.add_resource(Academic, '/academic')
    api.add_resource(Spec, '/spec')
    api.add_resource(Field, '/field')
    api.add_resource(Result, '/result')
    api.add_resource(Book, '/book')
    api.add_resource(Course, '/course')
    api.add_resource(Search, '/search')
    api.add_resource(Search_result, '/search_result')
    return app
