from datetime import datetime
from base64 import b64encode, b64decode
from instafarm import app, db

def commit():
    db.session.commit()

def rollback():
    db.session.rollback()

def add(model):
    db.session.add(model)

def delete(model):
    db.session.delete(model)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    email    = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role     = db.Column(db.String(100), nullable=False)
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)

    def __init__(self, email='', password='', role=''):
        self.email = email
        self.password = password
        self.role = role
        self.create_at = datetime.now()
        self.update_at = datetime.now()
    
    def get_token(self):
        return b64encode(bytearray(self.email + ":" + self.password, 'utf-8')).decode('ascii')
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'role': self.role
        }
    
    @staticmethod
    def find_by_id(uid):
        return User.query.get(uid)
    
    @staticmethod
    def find_by_role(role):
        returnUser.query.filter_by(role=role)
    
    @staticmethod
    def find_by_email(email):
        if email is None or email == '':
            return None
        return User.query.filter_by(email=email).first()

    @staticmethod
    def find_by_token(token):
        decoded_token = b64decode(bytearray(token, "ascii")).decode('utf-8')
        tokens = decoded_token.split(":")
        email = tokens[0]
        password = tokens[1]
        return User.find_by_email_and_password(email, password)
    
    @staticmethod
    def find_by_email_and_password(email, password):
        if email is None or email == '':
            return None
        if password is None or password == '':
            return None
        return User.query.filter_by(email=email, password=password).first()
    
    @staticmethod
    def check_exist_by_email(email, me=None):
        user = User.query.filter_by(email=email).first()
        if user is None:
            return False
        if me is None:
            return True
        return me.id != user.id

