from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, UserMixin, login_user, login_required,logout_user, current_user
from config import Config
# from forms import RegistrationForm, UserLoginForm
from models import User, db, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb013ce0c676dfde280ba245'
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(use_id))

@app.route('/')
def index():
    return render_template('home.html', title='Home')


@app.route("/profile")
@login_required
def home():
    user = User.query.filter_by(username='Dedrick').first()
    login_user(user)
    return render_template()

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title= 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Login', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'




if __name__ == '__main__':
    app.run(debug=True)
