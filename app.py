from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

#creates Flask application by initializing the 'app' object
app = Flask(__name__)

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://errick@localhost/students'


# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)


#represents student table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

#student data
students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

#lists students over the age of 20
@app.route('/old_students', methods=['GET'])
def old_students():
    old_students = []
    for student in students:
        student_dict = {}
        if student['age'] > 20:
            student_dict['id'] = student['id']
            student_dict['first_name'] = student['first_name']
            student_dict['last_name'] = student['last_name']
            student_dict['age'] = student['age']
            student_dict['grade'] = student['grade']
            old_students.append(student)
    return jsonify(old_students)

#lists students under 21
@app.route('/young_students', methods=['GET'])
def young_students():
    young_students = []
    for student in students:
        student_dict = {}
        if student['age'] < 21:
            student_dict['id'] = student['id']
            student_dict['first_name'] = student['first_name']
            student_dict['last_name'] = student['last_name']
            student_dict['age'] = student['age']
            student_dict['grade'] = student['grade']
            young_students.append(student_dict)
    return jsonify(young_students)


#lists students under 21 and got an 'A'
@app.route('/advance_students', methods=['GET'])
def advance_students():
    advance_students = []
    for student in students:
        student_dict = {}
        if student['age'] < 21 and student['grade'] == 'A':
            student_dict['id'] = student['id']
            student_dict['first_name'] = student['first_name']
            student_dict['last_name'] = student['last_name']
            student_dict['age'] = student['age']
            student_dict['grade'] = student['grade']
            advance_students.append(student_dict)
    return jsonify(advance_students)

#lists students first name and last name
@app.route('/student_names', methods=['GET'])
def student_names():
    student_names = []
    for student in students:
        names_dict = {}
        names_dict['first_name'] = student['first_name']
        names_dict['last_name'] = student['last_name']
        student_names.append(names_dict)
    return jsonify(student_names)


#lists students first name, last name, and age
@app.route('/student_ages', methods=['GET'])
def student_ages():
    student_ages = []
    for student in students:
        student_dict = {}
        student_dict['age'] = student['age']
        student_dict['first_name'] = student['first_name']
        student_dict['last_name'] = student['last_name']
        student_ages.append(student_dict)
    return jsonify(student_ages)

@app.route('/student', methods=['GET'])
def get_student():
    students = Student.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade}
        for student in students
    ]
    return jsonify(student_list)
    

#runs the flask application
app.run(debug=True)



