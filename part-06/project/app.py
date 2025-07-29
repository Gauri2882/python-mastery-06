from flask import Flask,  render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(300), nullable = False)
    image = db.Column(db.String(200), nullable = False)
    link = db.Column(db.String(200), nullable = False)

# initialize database
with app.app_context():
    db.create_all()

# home route
@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects = projects)

# projects route
@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects = projects)

# contact route
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name or not email or not message:
            flash('All fields are required!', 'error')
        else:
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('home'))
        
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)