import os
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


# Configure the database connection
from dotenv import dotenv_values
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    # Load the environment variables from .env file
    env = dotenv_values('.env')

    # Configure the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    return app

    # postgres://employee_db_bxwj_user:NmnlPOfwrr2L0dTPGRjDzgpqX05WGTOU@dpg-cjnelrmqdesc739pic00-a.oregon-postgres.render.com/employee_db_bxwj

# Define a Trainer model
class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

    def __init__(self, name, age, specialty):
        self.name = name
        self.age = age
        self.specialty = specialty

# Define a route to handle the POST request for storing trainer data
@app.route('/trainers')
def trainers():
    trainers=Trainer.query.all()
    return render_template('trainers.html', trainers=trainers)

@app.route('/trainers/add', methods=['GET', 'POST'])
def add_trainers():
    if request.method=='POST':
        name = request.form.get('name')
        age = request.form.get('age')
        speciality = request.form.get('speciality')
        trainer = Trainer(name,age,speciality)
        db.session.add(trainer)
        db.session.commit()
        return redirect('/trainers')
    return render_template('add_trainer.html')



if __name__ == '__main__':
    app.run(debug=True, port=5003)
