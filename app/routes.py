from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Student

main = Blueprint('main', __name__)

@main.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_student = Student(
            name=request.form['name'],
            email=request.form['email'],
            course=request.form['course']
        )
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.course = request.form['course']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', student=student)

@main.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('main.index'))