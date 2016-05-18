from system.core.model import Model
import re
from datetime import datetime, date, timedelta

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def create_msg(self, info):
    	query = "INSERT INTO messages (user_id, message, reciever_id, created_at, updated_at) VALUES(:user_id, :message, :reciever_id, NOW(), NOW())"
    	data = {
    	'user_id': info['user_id'],
    	'message': info['message'],
    	'reciever_id': info['reciever_id']
    	}
    	self.db.query_db(query, data)
    	return True;

    def create_cmt(self, info):
    	query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES(:message_id, :user_id, :comment, NOW(), NOW())"
    	data = {
    	'message_id': info['message_id'],
    	'user_id': info['user_id'],
    	'comment': info['comment']
    	}
    	self.db.query_db(query, data)
    	return True