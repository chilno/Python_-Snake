from system.core.controller import *
from time import strftime, gmtime
from flask import flash,json,request
from datetime import datetime, date, timedelta
import urllib2
import sys

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        # self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def register(self):
        return self.load_view('register.html')

    def show(self, id):
        users = self.models['User'].show_user(id)
        messages = self.models['User'].get_messages(id)
        comments = self.models['User'].get_comments()
        return self.load_view('map.html', users = users, messages = messages, comments=comments)

    def dashboard(self):
        users = self.models['User'].show_users(session['id'])
        return self.load_view('dash.html', users = users)

    def delete(self, id):
        self.models['User'].delete(id)
        return redirect('/dashboard')

    def create(self):
        user_info = {
        'fname' : request.form['first_name'],
        'lname' : request.form['last_name'],
        'bdate' : request.form['bdate'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password']
        }

        create_status = self.models['User'].create_user(user_info)
        if create_status["status"] == True:
            session['first_name'] = create_status['users'][0]['first_name']
            session['id'] = str(create_status['users'][0]['id'])
            url="/user/show/"+session['id']
            return redirect(url)

        else: 
            for message in create_status['errors']:
                flash(message, 'reg')
            return redirect('/register')

    def login(self):
        user_info ={
        "username": request.form['username'],
        "password": request.form['passphrase']
        }

        create_status = self.models['User'].login(user_info)
        
        if create_status['status'] == True:
            session['first_name'] = create_status['user'][0]['first_name']
            session['id'] = str(create_status['user'][0]['id'])
            session['user_level'] = create_status['user'][0]['user_level']
            url="/user/show/"+session['id']
            return redirect(url)
        else:
            for message in create_status['errors']:
                flash(message, 'username')
            return redirect('/')


    def post(self, id):
        user_info = {
        'user_id': session['id'],
        'message': request.form['message'],
        'reciever_id': id
        }
        self.models['Message'].create_msg(user_info)
        url="/user/show/"+id
        return redirect(url)

    def comment(self, id, msg_id):
        user_info = {
        'user_id': session['id'],
        'comment': request.form['comment'],
        'message_id': msg_id
        }
        self.models['Message'].create_cmt(user_info)
        url="/user/show/"+id
        return redirect(url)

    def edit(self, id):
        user = self.models['User'].show_user(id)
        return self.load_view('edit.html', user = user[0])

    def update_info(self, id):
        user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'birth_date': request.form['bdate'],
        'email': request.form['email'],
        'user_level': request.form['user_level'],
        'id': id
        }
        display = self.models['User'].update_user(user_data)
        if display['status'] == True:
            for message in display['text']:
                flash(message, 'log')
            return redirect('/edit/'+id)
        else:
            for message in display['text']:
                flash(message, 'log')
            return redirect('/edit/'+id)
        
    def update_password(self, id):
        user_data = {
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password'],
        'id': id
        }
        display = self.models['User'].update_pass(user_data)
        if display['status'] == True:
            for message in display['text']:
                flash(message, 'log')
            return redirect('/edit/'+id)
        else:
            for message in display['text']:
                flash(message, 'log')
            return redirect('/edit/'+id)

    def update_description(self, id):
        user_data = {
        'description': request.form['description'],
        'id': id
        }
        display = self.models['User'].update_desc(user_data)
        
        if display['status'] == True:
            for message in display['text']:
                flash(message, 'log')
            return redirect('/edit/'+id)
        else:
            for message in display['text']:
                flash(message, 'log')
            return redirect('/edit/'+id)
        
    def add_user(self):
        user_info = {
        'fname' : request.form['first_name'],
        'lname' : request.form['last_name'],
        'bdate' : request.form['bdate'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password']
        }

        create_status = self.models['User'].create_user(user_info)
        if create_status["status"] == True:
            return redirect('/dashboard')

        else: 
            print create_status['errors']
            for message in create_status['errors']:
                flash(message, 'reg')
            return redirect('/dashboard')

    def clear(self):
        session.clear()
        return redirect('/')
    
    def show_map(self):
        return self.load_view('map.html')

    
    def locate(self):
        if request.form['destination']:
            print "dest"
            user_dest = request.form['destination']
            if user_dest:
                data =self.models['User'].get_data(user_dest)
        else:
            print "else"
            if request.form['userCords[longitude]']:
                userCordsLng = request.form['userCords[longitude]']
                userCordsLat = request.form['userCords[latitude]']
                userPos = {
                    'lng': userCordsLng,
                    'lat': userCordsLat
                }
                data=self.models['User'].get_data(userPos)
        # if 'type' in request.form:
        #     userType = request.form['type']
        if request.form['type']:
            userType = request.form['type']

        
        # else:
            
        return self.load_view('/partials/marker.html', data=data, type=userType)
    
    def marker(self):
        user_dest = request.form['destination']
        print user_dest
        data =self.models['User'].get_data(user_dest)
        print data
        return self.load_view('/partials/marker.html', data=data)
    
    
