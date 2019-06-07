import os
import configparser

_basepath = os.path.dirname(os.path.dirname(__file__))

_config = configparser.ConfigParser()
_config.read(os.path.join(_basepath, 'env.ini'))

db_path = 'sqlite:///' + os.path.join(_basepath, 'instafarm.sqlite3')

db_host = ''
db_port = ''
db_name = ''
db_username = ''
db_password = ''

if 'database' in _config:
    db_host = _config['database']['db_host']
    db_port = _config['database']['db_port']
    db_name = _config['database']['db_name']
    db_username = _config['database']['db_username']
    db_password = _config['database']['db_password']

if  db_host != '' and db_port != '' and db_name != '' and \
    db_username != '' and db_password != '':
    db_path = 'postgresql://' \
            + db_username + ':' + db_password + '@' \
            + db_host + ':' + db_port + '/' + db_name

config ={
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'SECRET_KEY': "random string",
    'SQLALCHEMY_DATABASE_URI': db_path
}

