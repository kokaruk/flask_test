# python -c 'import os; print(os.urandom(16))'   -  get random string
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Conf(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
