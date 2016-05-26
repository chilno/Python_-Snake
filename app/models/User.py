from system.core.model import Model
import re
from datetime import datetime, date, timedelta
import urllib2
from flask import flash,json

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        query = "SELECT email FROM users WHERE email = :email"
        data = {
        'email': info['email']
        }
        email_db = self.db.query_db(query, data)
        print email_db

        if not info['fname']:
            errors.append("First Name cannot be blank")
        elif len(info['fname']) < 2:
            errors.append("First Name must be at least 2 characters long")
        if not info['lname']:
            errors.append("Last Name cannot be blank")
        elif len(info['lname']) < 2:
            errors.append("Last Name must be at least 2 characters long")
        if not info['bdate']:
            errors.append("Birth Date cannot be blank")
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if email_db:
            errors.append('Email already exists in database')
        if not info['password']:
            errors.append('Password cannot be empty')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        if not info['confirm_password']:
            errors.append('Confirmation cannot be empty')
        elif info['password'] != info['confirm_password']:
            errors.append('Confirmation must match!')

        if errors:
            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            create_query = "INSERT INTO users (first_name, last_name, birth_date, email, password, user_level, created_at, updated_at) VALUES (:first_name, :last_name, :birth_date, :email, :password, :user_level, NOW(), NOW())"
            data = {
            'first_name': info['fname'],
            'last_name': info['lname'],
            'birth_date': info['bdate'],
            'email': info['email'],
            'password': pw_hash,
            'user_level': 8
            }
            self.db.query_db(create_query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return{"status":True, "users": users}

    def login(self, info):
        errors=[]
        login_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        data ={
        'email': info['username']
        }
        user = self.db.query_db(login_query, data)
        if not user:
            errors.append("Username doesn't exist!")
            return {'status': False, "errors":errors}
        elif self.bcrypt.check_password_hash(user[0]['password'], info['password']):
            return {'status': True, 'user':user}
        else:
            errors.append('Wrong Password!')
            return {'status': False, "errors":errors}

    def show_users(self, id):
        query = "SELECT * FROM users"
        data = {
        'id': id
        }
        return self.db.query_db(query, data)

    def show_user(self, id):
        query = "SELECT * FROM users WHERE id= :id"
        data = {
        'id': id
        }
        return self.db.query_db(query, data)

    def get_messages(self, id):
        msg_query = "SELECT users.id, messages.id AS message_id, messages.user_id, message, first_name, last_name, messages.created_at, reciever_id FROM wall.users JOIN wall.messages ON users.id = messages.user_id WHERE reciever_id = :id ORDER BY messages.created_at DESC"
        data = {
        'id': id
        }
        return self.db.query_db(msg_query,data)

    def get_comments(self):
        cmt_query = "SELECT users.id, comments.user_id, message_id, comment, first_name, last_name, comments.created_at FROM wall.users JOIN wall.comments ON users.id = comments.user_id ORDER BY comments.created_at ASC"
        return self.db.query_db(cmt_query)

    def update_user(self, user_data):
        text=[]
        query = "UPDATE users SET first_name= :first_name, last_name= :last_name, birth_date = :birth_date, email = :email, user_level = :user_level WHERE id= :id"
        data = {
        'id': user_data['id'],
        'first_name': user_data['first_name'],
        'last_name': user_data['last_name'],
        'birth_date': user_data['birth_date'],
        'email': user_data['email'],
        'user_level': user_data['user_level']
        }
        self.db.query_db(query, data)
        text.append("Informations Updated")
        return {'status':True, 'text':text}
        # else:
        #     text.append("Oops Try again!")
        #     return {'status':False, 'text':text}

    def update_pass(self, user_data):
        text=[]
        pw_hash = self.bcrypt.generate_password_hash(user_data['password'])
        if user_data['password'] == user_data['confirm_data']:
            query = "UPDATE users SET password= :password, updated_at = NOW() WHERE id= :id"
            data = {
            'password': pw_hash
            }
            self.db.query_db(query, data)
            text.append("Password Updated")
            return {'status':True, 'text':text}
        else:
            text.append("Password not matching!")
            return {'status':False, 'text':text}

    def update_desc(self, user_data):
        text =[]
        if len(user_data['description'])>1:
            query = "UPDATE users SET description= :description, updated_at = NOW() WHERE id= :id"
            data = {
            'description': user_data['description'],
            'id': user_data['id']
            }
            self.db.query_db(query, data)
            text.append("Description changed")
            return {'status':True, 'text':text}
        else:
            text.append('Description must be at least 2 charachters')
            return {'status':False, 'text':text}

    def delete(self, id):
        print "bullshit"
        query = "DELETE FROM users WHERE id = :id"
        data = {
        'id': id
        }
        self.db.query_db(query, data)
        return True


    def get_data(self, user_dest):
        key = 'AIzaSyDtUacD4feeXpYF3Fg_XkSAGqa7ZehTk2c'
        locality = user_dest.replace(' ', '%20')
        url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        if user_dest:
            final_url = url+'address='+locality+'&key='+key
#         else:
#             final_url = url+'latlng='+

        json_obj =  urllib2.urlopen(final_url)
        test = json_obj.read()
        data = json.loads(test)
        print data
#        test = json.load(json_obj)
##        data =json.dumps(test)
        return data


    def get_marker(self, user_dest):
        key = 'AIzaSyDtUacD4feeXpYF3Fg_XkSAGqa7ZehTk2c'
        locality = user_dest.replace(' ', '%20')
        url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        if user_dest:
            final_url = url+'address='+locality+'&key='+key
#         else:
#             final_url = url+'latlng='+

        json_obj =  urllib2.urlopen(final_url)
        test = json_obj.read()
        data = json.loads(test)
        print data
#        test = json.load(json_obj)
##        data =json.dumps(test)
        return data