from flask_sqlalchemy import SQLAlchemy
from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=True)
    chat_id = db.Column(db.Integer, nullable=False)

class OnboardingCheck(db.Model):
    __tablename__ = 'onboarding_check'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    onboarding_type = db.Column(db.Text, nullable=False)
    result = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.Text, nullable=False)
    job_pic = db.Column(db.Text, nullable=False)
    job_text = db.Column(db.Text, nullable=False)

class PizzamakerTest(db.Model):
    __tablename__ = 'pizzamaker_test'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

class CourierTest(db.Model):
    __tablename__ = 'courier_test'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

class ManagerTest(db.Model):
    __tablename__ = 'manager_test'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

class AdminTest(db.Model):
    __tablename__ = 'admin_test'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    pizza_name = db.Column(db.Text, nullable=False)
    pizza_pic = db.Column(db.Text, nullable=False)
    pizza_text = db.Column(db.Text, nullable=False)

# class PizzaTest(db.Model):
#     __tablename__ = 'pizza_test'
#     id = db.Column(db.Integer, primary_key=True)
#     pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"))
#     question1 = db.Column(db.Text, nullable=False)
#     right_answer1 = db.Column(db.Text, nullable=False)
#     wrong_answer1 = db.Column(db.Text, nullable=False)
#     question2 = db.Column(db.Text, nullable=False)
#     right_answer2 = db.Column(db.Text, nullable=False)
#     wrong_answer2 = db.Column(db.Text, nullable=False)
#     question3 = db.Column(db.Text, nullable=False)
#     right_answer3 = db.Column(db.Text, nullable=False)
#     wrong_answer3 = db.Column(db.Text, nullable=False)

class WorkingPlace(db.Model):
    __tablename__ = 'working_place'
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.Text, nullable=False)
    place_pic = db.Column(db.Text, nullable=False)
    place_text = db.Column(db.Text, nullable=False)

if __name__ == '__main__':
    print('ok')
    # with app.app_context():
    #     db.create_all()
    #app.run()
    # db.session.add(CourierTest(question='Курьер должен:\n1) Готовить пиццу\n2) Доставлять пиццу', answer='2'))
    # db.session.add(CourierTest(question='Курьер отвозит пиццу на:\n1) Своей машине\n2) На машине компании', answer='1'))
    # db.session.add(CourierTest(question='Курьер должен быть одет в:\n1) Любую одежду\n2) Брендированную одежду', answer='2'))
    #
    # db.session.add(PizzamakerTest(question='Пиццамейкер должен:\n1) Готовить пиццу\n2) Доставлять пиццу', answer='1'))
    # db.session.add(PizzamakerTest(question='Обязан ли пиццамейкер поддерживать чистоту на рабочем месте?:\n1) Да\n2) Нет', answer='1'))
    # db.session.add(PizzamakerTest(question='Должен ли пиццамейкер прислушиваться к указаниям менеджера?:\n1) Да\n2) Нет', answer='1'))
    #
    # db.session.add(ManagerTest(question='Может ли менеджер открывать и закрывать смены сотрудникам?:\n1) Да\n2) Нет', answer='1'))
    # db.session.add(ManagerTest(question='Должен ли менеджер решать конфликты сотрудников?:\n1) Да\n2) Нет', answer='1'))
    # db.session.add(ManagerTest(question='Должен ли менеджер помогать делать пиццу пиццамейкерам при необходимости?:\n1) Да\n2) Нет', answer='1'))
    #
    # db.session.add(AdminTest(question='Должен ли управляющий развивать команду?:\n1) Да\n2) Нет', answer='1'))
    # db.session.add(AdminTest(question='Должен ли управляющий следить за показателями?:\n1) Да\n2) Нет', answer='1'))
    # db.session.add(AdminTest( question='Должен ли управляющий общаться с поставщиками?:\n1) Да\n2) Нет', answer='1'))
    #
    # db.session.commit()
    # db.session.add(Users(username='test', first_name='test',
    #                      last_name='test'))
    # db.session.commit()
    # me = Users.query.filter_by(id=1).first()
    # db.session.delete(me)
    # db.session.commit()
    # db.session.query(AdminTest).delete()
    # db.session.query(ManagerTest).delete()
    # db.session.query(PizzamakerTest).delete()
    # db.session.commit()

    #Users.__table__.drop(db.engine)