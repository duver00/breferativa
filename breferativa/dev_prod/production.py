import environ
from breferativa.dev_prod.development import DATABASES, SECRET_KEY
env = environ.Env()
environ.Env.read_env()
ALLOWED_HOSTS = ['127.0.0.0.1','intranet.onrm.minem.cu']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',

]