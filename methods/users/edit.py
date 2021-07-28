from imports import app , mysql
from flask import Blueprint , request
from status import * 
import json

edit = Blueprint("edit", __name__)

@edit.route("/users/edit" , methods= ["POST"])
def  home():
    #fetching input type
    if (request.content_type == 'application/json'):
        inputt = request.json
    else:
        inputt = request.form
    id = inputt['id']
    new_email = inputt.get('email')
    new_password = inputt.get('password')
    new_position = inputt.get('position')
    new_user_name = inputt.get('user_name')
    new_first_name = inputt.get('first_name')
    new_last_name = inputt.get('last_name')
    new_national_id = inputt.get('national_id')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s ",(id,))
    results = cur.fetchall()
    for row in results:
        email = row['email']
        password = row['password']
        position = row['position']
        user_name = row['user_name']
    if (results != 0 ):
        if (new_email != None):
            email = new_email
        if ( new_password != None):
            password = new_password
        if ( new_position != None):
            position = new_position
        if ( new_user_name != None):
            user_name = new_user_name
        if ( new_first_name != None):
            first_name = new_first_name
        if ( new_last_name != None):
            last_name = new_last_name
        if ( new_national_id != None):
            national_id = new_national_id
            
        
        cur.execute("UPDATE users SET email = %s , password = %s , position = %s , user_name = %s , first_name = %s , last_name = %s , national_id = %s WHERE id = %s" , (email,password,position,user_name,first_name,last_name,national_id,id))
        mysql.connection.commit()        
        
        return{
            "status" : successful,
            "id" : id,
            "email" : email,
            "password" : password,
            "posistion" : position,
            "user_name" : user_name,
            "first_name" : first_name,
            "last_name" : last_name,
            "national_id" : national_id
            }
    else:
        return{
            "status" : edit_faild
        }