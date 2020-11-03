import os

app_dir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(app_dir, '..')


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### Flask-Mail configurations #####
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'infooveriq@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(app_dir, 'app.db')


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(app_dir, 'app.db')


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
                              'mysql+pymysql://root:pass@localhost/flask_app_db'


def config_creator():
    try:
        if os.environ['ENV'] == 'PROD':
            config = ProductionConfig()
        elif os.environ['ENV'] == 'TEST':
            config = TestingConfig()
        else:
            config = DevelopementConfig()
    except Exception as e:
        print(e)
        os.environ['ENV'] = 'DEV'
        config = DevelopementConfig()
    return config
