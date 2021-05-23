from flask import render_template, make_response, request, flash, session, g, jsonify
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta


class Home(Resource):
    def get(self):
        return make_response(render_template('mainpage.html'))

class Corporation(Resource):
    def get(self):
        return make_response(render_template('corporation.html'))

class Academic(Resource):
    def get(self):
        return make_response(render_template('academic.html'))

class Spec(Resource):
    def get(self):
        return make_response(render_template('spec.html'))

class Field(Resource):
    def get(self):
        return make_response(render_template('field.html'))

class Result(Resource):
    def get(self):
        return make_response(render_template('result.html'))
