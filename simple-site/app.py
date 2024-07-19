# You must have already installed:
# Flask (pip install Flask)
# MySQL
# SQLAlchemy (pip install SQLAlchemy)

# Import statements
# For starting the Flask app
from flask import Flask
#
# For rendering the HTML templates
from flask import render_template
#
# For handling the requests from the frontend and fetching the values using their names
from flask import request
# For redirecting people to certain HTML pages
from flask import redirect
# For validating user login
from flask import session
#
# The module below helps to handle user sign up and sign in
from flask_sqlalchemy import SQLAlchemy
from os import getenv # Helps to get the environmental variables
from dotenv import load_dotenv # Helps to load the environmental variables from the .env file
#
#
# Load the environmental variables from my .env file
load_dotenv()
#
#
# Storing the database URL I saved as an environmental variable (in the .env file) to a string
myDbURL = getenv('SQLALCHEMY_DATABASE_URI')
#
#
# Creating the Flask app
app = Flask(__name__)
# This part instantiates the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = myDbURL
# Getting the secret key
app.secret_key = getenv('SECRET_KEY')
# Creating the database instance
db = SQLAlchemy(app)
#
#
# Create the User instance that we use for signup
# just the way it is done in SQLAlchemy
class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
#
#
# Routes in Flask
# Examples of routes: '/signup', '/login'

@app.route('/') # Displaying the home page
def homePage():
    """
    This function renders the home page when the
    route requested is '/'
    """
    return render_template('/index.html')
#
#
@app.route('/login') # Displaying the login page
def loginPage():
    """
    This function renders the home page when the
    route requested is '/'
    """
    return render_template('/login.html')
#
#
@app.route('/signup') # Displaying the signup page
def signupPage():
    """
    This function renders the home page when the
    route requested is '/'
    """
    return render_template('/signup.html')
#
#
@app.route('/dashboard') # Displaying the signup page
def dashboardPage():
    """
    This function renders the home page when the
    route requested is '/'
    """
    return render_template('/dashboard.html')
#
#
# Handling the sign up and login functionalities
#
#
# Signup Functionality
@app.route('/signup', methods=['GET', 'POST']) # Displaying the signup page
def signUpNewUser():
    """
    Signing up a user
    """
    # Verifying if the user is signing up (hereby, sending a POST request)
    if request.method == 'POST':
        # Fetching the variables from the frontend using the `requests` module using their HTML names
        # and store their values in variables
        UserFirstName = request.form['firstname']
        UserLastName = request.form['lastname']
        UserEmail = request.form['email']
        UserPassword = request.form['password']
        # Upon successful fetching of details from the frontend, it creates a new instance of the user
        new_user = Users(firstname=UserFirstName, lastname=UserLastName, email=UserEmail, password=UserPassword)
        # Adding the instance of the new_user
        db.session.add(new_user)
        # Submit the new user to the database
        db.session.commit()
        return redirect('/login')
#
#
# Signup Functionality
@app.route('/login', methods=['GET', 'POST']) # Displaying the signup page
def logInExistingUser():
    """
    Logging the user in
    """
    # Verifying if the the user is logging in (hereby, sending a POST request)
    if request.method == 'POST':
        # Fetching the variables from the frontend using the `requests` module using their HTML names
        email = request.form['email']
        password = request.form['password']
        # Querying the database for an existing user with the entered email and password (from the frontend)
        user = Users.query.filter_by(email=email, password=password).first()
        # print(user)
        if user: # and check_password_hash(user.password, password):
            # Store the user's ID in the session
            # session['userId'] = user.userId
            # Redirect it to the 'dashboard' route
            # print(user.userId)
            return redirect('/dashboard')
        else:
            # Redirect the user to signup using the 'signup' route
            # because the user's details do not exist in our database
            return redirect('/signup')
    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True) # Runs the app in debug mode
