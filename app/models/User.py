from system.core.model import Model
import re
from datetime import datetime, date, timedelta

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def create_user(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['fname']:
            errors.append("First Name cannot be blank")
        elif len(info['fname']) < 2:
            errors.append("First Name must be at least 2 characters long")
        if not info['lname']:
            errors.append("Last Name cannot be blank")
        if len(info['lname']) < 2:
            errors.append("Last Name must be at least 2 characters long")
        if not info['bdate']:
            errors.append("Birth Date cannot be blank")
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['confirm_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            form_date = datetime.strptime(info['bdate'], "%d/%m/%Y")
            create_query = "INSERT INTO users (first_name, last_name, birth_date, email, password, user_level, created_at, updated_at) VALUES (:first_name, :last_name, :birth_date, :email, :password, :user_level, NOW(), NOW())"
            data = {
            'first_name': info['fname'],
            'last_name': info['lname'],
            'birth_date': form_date,
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
        # if len("user['username']") == 0:
            errors.append('Wrong Username!')
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

    def update_info(self, user_data):
        text=[]
        query = "UPDATE users SET first_name= :first_name, last_name= :last_name, email = :email WHERE id= :id"
        data = {
        'id': user_data['id'],
        'first_name': user_data['first_name'],
        'last_name': user_data['last_name'],
        'birth_date': user_data['birth_date'],
        'email': user_data['email'],
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


        
