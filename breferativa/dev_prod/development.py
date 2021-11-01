import environ

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'debug_toolbar',

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(env('NAME')),
        'USER': str(env('USER')),
        'PASSWORD': str(env('PASSWORD')),
        'HOST': str(env('HOST')),
        'DATABASE_PORT': str(env('DATABASE_PORT')),

    }
}