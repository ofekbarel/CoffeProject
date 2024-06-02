import os
from sqlalchemy.exc import IntegrityError
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from sqlalchemy import func, Text


#we can choose to run the application in localhost or k8s cluster

password = os.getenv('POSTGRES_USER')           #k8s
username = os.getenv('POSTGRES_PASSWORD')       #k8s
host = os.getenv('HOST')

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/users'             #localhost

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{host}:5432/test'       #k8s
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    recipes = db.relationship('PrivetRecipe')

    def __init__(self, email, password, name):

        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


class PrivetRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id


class PublicRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(Text)


    def __init__(self, title, description):
        self.title = title
        self.description = description


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()



#@app.route('/')
#def index():
    #return render_template('index2.html')





@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('Email already exists. Please use a different email.', 'error')
            return redirect(url_for('register'))  # Redirect back to registration page with error message
        return redirect(url_for('login'))  # Use url_for for better routing

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))  # Use url_for
        else:
            return render_template('login.html', error='Invalid user')

    return render_template('login.html')


@app.route('/dashboard')
@login_required  # Protect this route with login requirement
def dashboard():
    if current_user.is_authenticated:
        return render_template('dashboard2.html', user=current_user)
    else:
        return redirect(url_for('login'))  # Redirect to login if not logged in


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))




@app.route('/all_recipes')
def all_recipes():
    user_recipes = PublicRecipe.query.all()
    return render_template('all_recipes2.html', user_recipes=user_recipes)



@app.route('/add_public_recipe', methods=['GET', 'POST'])
@login_required  # Only logged in users can access this route
def add_public_recipe():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        new_recipe = PublicRecipe(title=title, description=description)
        db.session.add(new_recipe)
        db.session.commit()

        return redirect(url_for('dashboard'))
    return render_template('add_public_recipe2.html')


@app.route('/add_privet_recipe', methods=['GET', 'POST'])
@login_required  # Only logged in users can access this route
def add_privet_recipe():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        new_recipe = PrivetRecipe(title=title, description=description, user_id=current_user.id)
        db.session.add(new_recipe)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('add_privet_recipe2.html')


@app.route('/my_recipes')
@login_required  # Only logged in users can access this route
def my_recipes():
    if current_user.is_authenticated:
        user_recipes = PrivetRecipe.query.filter_by(user_id=current_user.id).all()
        return render_template('my_recipes2.html', user_recipes=user_recipes)
    else:
        return redirect(url_for('login'))


@app.route('/random_recipe')
def random_recipe():
    random_recipe = PublicRecipe.query.order_by(func.random()).first()
    return render_template('random_recipe2.html', random_recipe=random_recipe)


@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
@login_required  # Protect this route with login requirement
def delete_recipe(recipe_id):
    if current_user.is_authenticated:
        recipe = PrivetRecipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
    return redirect(url_for('my_recipes'))

@app.route('/gallery')
def gallery():
    images = os.listdir('static')
    return render_template('gallery.html', images=images)



if __name__ == '__main__':
    app.run(debug=True)
