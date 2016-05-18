"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        return self.load_view('index.html')

    def start(self):
        return self.load_view('/sign_in.html')

    def register(self):
        return self.load_view('/register.html')

    def display_admin(self):
        users=self.models['User'].get_users()
        return self.load_view('dashboard_admin.html', users=users)

    def display_user(self):
        users=self.models['User'].get_users()
        return self.load_view('user_dashboard.html', users=users)

    def admin_user_add(self):
        data={
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':request.form['password'],
            'user_level':request.form['user_level']
        }
        self.models['User'].admin_new_user(data)
        return self.load_view('admin_user_add.html')

    def sign_in(self):
        data={
            'email':request.form['email'],
            'password':request.form['password']
        }
        user = self.models['User'].get_user(data)
        if user[0]['id']==1:
            return redirect('/dashboard/admin')
        else:
            return redirect('/dashboard')

    # def sign_in(self):
    #     data={
    #         'email':request.form['email'],
    #         'password':request.form['password']
    #     }
    #     result=self.models['User'].get_user(data)
        

    #     return self.load_view('/user_dashboard.html')
    #     #there will be an if condition here, so that if user level is admin it goes to admin 
    #     #dashboard or otherwise it goes to user dashboard
    #     # return self.load_view('/dashboard_admin.html')
    def register_user(self):
        data={
            
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':request.form['password']
        }
        self.models['User'].register_user(data)
        return redirect('/dashboard')














