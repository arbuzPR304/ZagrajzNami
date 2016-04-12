"""
Django settings for zzn project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'd98)s0bz(ne4pfgjv0_u$_sd*a%*7)!%j2=q9s)#s(j%r87-tt'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'                                                                             
EMAIL_HOST ='smtp.gmail.com'                                   
EMAIL_PORT = 587                                                             
EMAIL_HOST_USER = 'opole.zagraj.z.nami@gmail.com'                              
EMAIL_HOST_PASSWORD = 'opole2015abc' #This is not your gmail password.
EMAIL_USE_TLS = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    'crispy_forms',
    'multiselectfield',
    'django_cleanup',
    'sport_event',
    'profiles',
    'comments',
    'notifications',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.request",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        # "allauth.account.context_processors.account",
        # "allauth.socialaccount.context_processors.socialaccount",
    )


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID =1

ACCOUNT_AUTHENTICATION_METHOD  = "username_email"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION ="mandatory"
# SOCIALACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_SESSION_REMEMBER = False
# SOCIALACCOUNT_PROVIDERS = \
#     {'facebook':
#        {'METHOD': 'oauth2',
#         'SCOPE': ['email', 'public_profile', 'user_friends'],
#         'AUTH_PARAMS': {'auth_type': 'https'},
#         'FIELDS': [
#             'id',
#             'email',
#             'name',
#             'first_name',
#             'last_name',
#             'verified',
#             'locale',
#             'timezone',
#             'link',
#             'gender',
#             'updated_time'],
#         'EXCHANGE_TOKEN': True,
#         'VERIFIED_EMAIL': False,
#         'VERSION': 'v2.4'}}
ROOT_URLCONF = 'zzn.urls'

WSGI_APPLICATION = 'zzn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'pl_PL'

LANGUAGES = (
('pl', 'Polski'),
)

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_dirs"),
    #'/Users/jmitch/Desktop/srvup/static/static_dirs/', #on mac
    #'\Users\jmitch\Desktop\srvup\static\static_dirs\', somethingl ike this on windows
    #'/var/www/static/',
)

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media_root")


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

#crispy staff
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#Registration TAGs settings

LOGIN_REDIRECT_URL = '/dashboard'
