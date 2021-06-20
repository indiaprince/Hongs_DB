from flask import Flask, render_template, url_for, flash, redirect
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)
    api = Api(app)


    # ORM
#    db.init_app(app)
#    migrate.init_app(app, db)
#    from . import models



    from .views.pages import Home, Corporation, Spec, Field, Academic, Result
    api.add_resource(Home, '/')
    api.add_resource(Corporation, '/corporation')
    api.add_resource(Academic, '/academic')
    api.add_resource(Spec, '/spec')
    api.add_resource(Field, '/field')
    api.add_resource(Result, '/result')
    return app
