""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)
    """
    def get_users(self):
        query = "SELECT * from users "
        # data = {'email': data['info']}
        display_users=self.db.query_db(query)
        # print "this is", display_users
        return display_users

    def get_user(self, info):
        query = "SELECT * from users WHERE email =:email"
        data = {'email': info['email']}
        display_user=self.db.query_db(query, data)
        return display_user

    def register_user(self, info):
        query="INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :password, NOW())"
        data={
             'first_name':info['first_name'],
             'last_name':info['last_name'],
             'email':info['email'],
             'password':info['password']
             }   
        insert_users=self.db.query_db(query, data)
        return insert_users
 

    """
    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """