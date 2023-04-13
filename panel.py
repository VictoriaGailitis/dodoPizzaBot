from app import app, db
import wtforms
from dodoBotDB import OnboardingCheck, CourierTest, PizzamakerTest, ManagerTest, AdminTest
from flask import Flask, render_template, request, flash, get_flashed_messages, session, redirect, url_for, abort, g
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

class AddRecord(FlaskForm):
    id_field = HiddenField()
    question = StringField('Вопрос', [InputRequired()])
    answer = StringField('Правильный ответ', [InputRequired()])
    submit = SubmitField('Добавить/изменить вопрос')


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())

@app.route('/edit_courier/<data>', methods=['GET','POST'])
def edit_courier(data):
    form1 = AddRecord()
    if form1.validate_on_submit():
        courier = CourierTest.query.filter(CourierTest.id == data).first()
        courier.question = request.form['question']
        courier.answer = request.form['answer']
        db.session.commit()
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                               data2=db.session.query(CourierTest).all(),
                               data3=db.session.query(PizzamakerTest).all(),
                               data4=db.session.query(ManagerTest).all(),
                               data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_courier.html', form1=form1)

@app.route('/add_record_courier', methods=['GET', 'POST'])
def add_record_courier():
    form1 = AddRecord()
    if form1.validate_on_submit():
        question = request.form['question']
        answer = request.form['answer']
        record = CourierTest(question=question, answer=answer)
        db.session.add(record)
        db.session.commit()
        message = f"Вопрос был добавлен."
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_courier.html', form1=form1)

@app.route('/delete_record_courier/<data>', methods=['GET', 'POST'])
def delete_record_courier(data):
    me = CourierTest.query.filter_by(id=data).first()
    db.session.delete(me)
    db.session.commit()
    return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())

@app.route('/edit_pizzamaker/<data>', methods=['GET','POST'])
def edit_pizzamaker(data):
    form1 = AddRecord()
    if form1.validate_on_submit():
        pizzamaker = PizzamakerTest.query.filter(PizzamakerTest.id == data).first()
        pizzamaker.question = request.form['question']
        pizzamaker.answer = request.form['answer']
        db.session.commit()
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                               data2=db.session.query(CourierTest).all(),
                               data3=db.session.query(PizzamakerTest).all(),
                               data4=db.session.query(ManagerTest).all(),
                               data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_pizzamaker.html', form1=form1)

@app.route('/add_record_pizzamaker', methods=['GET', 'POST'])
def add_record_pizzamaker():
    form1 = AddRecord()
    if form1.validate_on_submit():
        question = request.form['question']
        answer = request.form['answer']
        record = PizzamakerTest(question=question, answer=answer)
        db.session.add(record)
        db.session.commit()
        message = f"Вопрос был добавлен."
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_pizzamaker.html', form1=form1)

@app.route('/delete_record_pizzamaker/<data>', methods=['GET', 'POST'])
def delete_record_pizzamaker(data):
    me = PizzamakerTest.query.filter_by(id=data).first()
    db.session.delete(me)
    db.session.commit()
    return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())

@app.route('/edit_manager/<data>', methods=['GET','POST'])
def edit_manager(data):
    form1 = AddRecord()
    if form1.validate_on_submit():
        manager = ManagerTest.query.filter(ManagerTest.id == data).first()
        manager.question = request.form['question']
        manager.answer = request.form['answer']
        db.session.commit()
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                               data2=db.session.query(CourierTest).all(),
                               data3=db.session.query(PizzamakerTest).all(),
                               data4=db.session.query(ManagerTest).all(),
                               data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_manager.html', form1=form1)

@app.route('/add_record_manager', methods=['GET', 'POST'])
def add_record_manager():
    form1 = AddRecord()
    if form1.validate_on_submit():
        question = request.form['question']
        answer = request.form['answer']
        record = ManagerTest(question=question, answer=answer)
        db.session.add(record)
        db.session.commit()
        message = f"Вопрос был добавлен."
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_manager.html', form1=form1)

@app.route('/delete_record_manager/<data>', methods=['GET', 'POST'])
def delete_record_manager(data):
    me = ManagerTest.query.filter_by(id=data).first()
    db.session.delete(me)
    db.session.commit()
    return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())

@app.route('/edit_admin/<data>', methods=['GET','POST'])
def edit_admin(data):
    form1 = AddRecord()
    if form1.validate_on_submit():
        admin = AdminTest.query.filter(AdminTest.id == data).first()
        admin.question = request.form['question']
        admin.answer = request.form['answer']
        db.session.commit()
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                               data2=db.session.query(CourierTest).all(),
                               data3=db.session.query(PizzamakerTest).all(),
                               data4=db.session.query(ManagerTest).all(),
                               data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_admin.html', form1=form1)

@app.route('/add_record_admin', methods=['GET', 'POST'])
def add_record_admin():
    form1 = AddRecord()
    if form1.validate_on_submit():
        question = request.form['question']
        answer = request.form['answer']
        record = AdminTest(question=question, answer=answer)
        db.session.add(record)
        db.session.commit()
        message = f"Вопрос был добавлен."
        return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record_admin.html', form1=form1)

@app.route('/delete_record_admin/<data>', methods=['GET', 'POST'])
def delete_record_admin(data):
    me = AdminTest.query.filter_by(id=data).first()
    db.session.delete(me)
    db.session.commit()
    return render_template('index.html', data=db.session.query(OnboardingCheck).all(),
                           data2=db.session.query(CourierTest).all(),
                           data3=db.session.query(PizzamakerTest).all(),
                           data4=db.session.query(ManagerTest).all(),
                           data5=db.session.query(AdminTest).all())