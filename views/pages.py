from flask import render_template, make_response, request, flash, session, g, jsonify, request
from flask_restful import Resource, abort
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import pymysql
#from module import dbModule
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sys', charset='utf8')
cursor = conn.cursor()
cursor2 = conn.cursor()
class Home(Resource):
    def get(self):

        return make_response(render_template('mainpage.html'))
    def post(self):

        return make_response(render_template('mainpage.html'))

class Corporation(Resource):
    def get(self):
        sql = 'select * from company_'
        cursor.execute(sql)
        row =list(cursor.fetchall())

        return make_response(render_template('corporation.html',corp = row))

    def post(self):
        ls = []
        username = request.form['username']
        ls.append(username)
        major = request.form['major']
        ls.append(major)
        
        phone = request.form['phone']
        ls.append(phone)

        region = request.form['region']
        ls.append(region)

        special1 = request.form['special1']
        ls.append(special1)

        special1v = request.form['specialv1']
        ls.append(special1v)
        special2 = request.form['special2']
        ls.append(special2)
        special2v = request.form['specialv2']
        ls.append(special2v)


        sql2 = 'insert into user(user_name,phone,major,region,speciality1,s1_percent,speciality2,s2_percent) values'+'('+'\''+ls[0]+'\''+','+'\''+ls[1]+'\''+','+'\''+ls[2]+'\''+','+'\''+ls[3]+'\''+','+'\''+ls[4]+'\''+','+'\''+ls[5]+'\''+','+'\''+ls[6]+'\''+','+'\''+ls[7]+'\''+')'
        cursor2.execute(sql2)
        conn.commit()
        sql = 'select * from company_'
        cursor.execute(sql)
        row =list(cursor.fetchall())

        return make_response(render_template('corporation.html',corp = row, user = ls))

class Academic(Resource):
    def get(self):

        value = request.form['field_id']
        sql = 'select * from online_material where field_id =\''+value+'\''
        cursor.execute(sql)
        row =list(cursor.fetchall())
        return make_response(render_template('academic.html',material = row))
    def post(self):

        value = request.form['field_id']
        sql = 'select * from online_material where field_id =\''+value+'\''
        cursor.execute(sql)
        row =list(cursor.fetchall())
        return make_response(render_template('academic.html',material = row))

class Spec(Resource):
    def get(self):
        return make_response(render_template('spec.html'))


    def post(self):
        return make_response(render_template('field.html'))

class Field(Resource):
    def get(self):
        return make_response(render_template('field.html'))


    def post(self):
        return make_response(render_template('field.html'))

class Result(Resource):
    def get(self):
        value = request.form['name']
        sql = 'select * from recruit where company_id =\''+value+'\''
        cursor.execute(sql)
        row =list(cursor.fetchall())
        usr = request.form['user']

        return make_response(render_template('result.html',recruit = row))

    def post(self):
        value = request.form['name']
        sql = 'select * from recruit where company_id =\''+value+'\''
        cursor.execute(sql)
        row =list(cursor.fetchall())
        sql2 = 'select * from company_ where company_id =\''+value+'\''
        cursor.execute(sql2)
        company =list(cursor.fetchall())
        usr = request.form['username']
        if(usr=='') : 
            usr='Anonymous'
        sql3 = 'select * from user where user_name =\''+usr+'\'' + 'limit 1'
        cursor2.execute(sql3)
        user =list(cursor2.fetchall())
        for i in range(len(user)):
            user[i]=list(user[i])
        print(user)

        return make_response(render_template('result.html',recruit = row, company=company,user=user))

class Book(Resource):
    def get(self):

        return make_response(render_template('book.html'))

    def post(self):
        value = request.form['book_id']
        sql = 'select * from book where field_id = \'' +value+'\''
        cursor.execute(sql)
        row = list(cursor.fetchall())
        print(row)


        usr = request.form['username']
        print(usr)
        sql3 = 'select * from user where user_name =\''+usr+'\'' + 'limit 1'
        cursor2.execute(sql3)
        user =list(cursor2.fetchall())
        for i in range(len(user)):
            user[i]=list(user[i])
        print(user)
        return make_response(render_template('book.html', book = row, user=user))

class Course(Resource):
    def get(self):

        return make_response(render_template('course.html'))

    def post(self):
        value = request.form['course_id']
        sql = 'select * from course where field_id = \'' +value+'\''
        cursor.execute(sql)
        row = list(cursor.fetchall())
        print(row)
        return make_response(render_template('course.html', course = row))

class Search_result(Resource):
    def get(self):

        return make_response(render_template('search_result.html'))

    def post(self):
        value = request.form['key']
        sql = 'select field_id from keyword where name = \'' +value+'\''
        cursor.execute(sql)
        row = list(cursor.fetchall())
        print(row)
        ls =[]
        for i in range(len(row)):
            ls.append(row[i][0])
        print(ls)
        ls2=[]
        for i in range(len(ls)):
            sql2 = 'select * from recruit r where field_id =' + str(ls[i])
            cursor2.execute(sql2)
            row2 = list(cursor2.fetchall())

            if len(row2) !=0:
                row3 = list(row2[0])
                ls2.append(row3)

        print(len(ls2))
        return make_response(render_template('search_result.html',data = ls2))

class Search(Resource):
    def get(self):

        return make_response(render_template('search.html'))

    def post(self):

        return make_response(render_template('search.html'))
