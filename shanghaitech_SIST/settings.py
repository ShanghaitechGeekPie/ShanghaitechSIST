"""
Django settings for shanghaitech_SIST project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kak^%w2j_h4#gqydh#j469z)vpafa*%=)gii7m&ny4l+6l#w-0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["sist.geekpie.org"]

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cms',  # django CMS itself
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.

    'djangocms_text_ckeditor',
    'djangocms_picture',
    'djangocms_file',
    'djangocms_timerange',
    'djangocms_plaintext',
    # 'gunicorn',
    'shanghaitech_SIST',

    'django.contrib.admin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'shanghaitech_SIST.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.core.context_processors.i18n',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

CMS_TEMPLATES = (
    ('article.html', 'Article'),
    ('seminars.html', 'Seminars'),
    ('people.html', 'People'),
    ('list.html', 'List'),
    ('list_news.html', 'News List'),
    ('list_seminars.html', 'Seminars List'),
    ('list_people.html', 'People List'),
    ('list_overview.html', 'Overview List'),
    ('list_overview_people.html', 'Overview_people List'),
    ('home.html', 'Home'),
)

MIGRATION_MODULES = {
    # Add also the following modules if you're using these plugins:
    # 'djangocms_file': 'djangocms_file.migrations_django',
    # 'djangocms_flash': 'djangocms_flash.migrations_django',
    # 'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    # 'djangocms_inherit': 'djangocms_inherit.migrations_django',
    # 'djangocms_link': 'djangocms_link.migrations_django',
    # 'djangocms_picture': 'djangocms_picture.migrations_django',
    # 'djangocms_snippet': 'djangocms_snippet.migrations_django',
    # 'djangocms_teaser': 'djangocms_teaser.migrations_django',
    # 'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations',
}

WSGI_APPLICATION = 'shanghaitech_SIST.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sist_db',
#         'USER': 'root',
#         'PASSWORD': 'jinlei',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sist_db',
        'USER': 'sist_db',
        'PASSWORD': 'nhuHwBvXCPMSNcUW',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('zh', '中文'),
]

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_dev"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# CKEditor Configuration

TEXT_SAVE_IMAGE_FUNCTION = None

CMS_CACHE_DURATIONS = {
    'content': 1,
    'menus': 1,
    'permissions': 1,
}

CMS_PLACEHOLDER_CONF = {
    'article.html article_content': {
        'name' : 'article_content',
        'plugins': ['TextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'TextPlugin',
                'values':{
                    'body':'<p>Enter your Content</p>'
                }
            },
        ]
    },
    'seminars.html seminars_speaker': {
        'name' : 'seminars_speaker',
        'plugins': ['PlainTextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'PlainTextPlugin',
                'values':{
                    'body':'Enter your Name'
                }
            },
        ]
    },
    'seminars.html seminars_timerange': {
        'name' : 'seminars_timerange',
        'plugins': ['TimeRangePlugin'],
        'default_plugins':[
            {
                'plugin_type':'TimeRangePlugin',
                'values':{
                    'starttime':'2013-9-30 0:0:0',
                    'endtime':'2013-9-30 0:0:0'
                }
            },
        ]
    },
    'seminars.html seminars_location': {
        'name' : 'seminars_location',
        'plugins': ['PlainTextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'PlainTextPlugin',
                'values':{
                    'body':'Enter your Location'
                }
            },
        ]
    },
    'seminars.html seminars_content': {
        'name' : 'seminars_content',
        'plugins': ['TextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'TextPlugin',
                'values':{
                    'body':'<p>Enter your Content</p>'
                }
            },
        ]
    },
    'people.html people_photo': {
        'name' : 'people_photo',
        'plugins': ['PicturePlugin'],
        'default_plugins':[
            {
                'plugin_type':'PicturePlugin',
                'values':{
                    'image':'/static/image/people_none.jpg'
                }
            },
        ]
    },
    'people.html people_profile': {
        'name' : 'people_profile',
        'plugins': ['TextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'TextPlugin',
                'values':{
                    'body':'''
                    <p><strong>Title: </strong>Title here<br/></p>
                    <p><strong>PHD: </strong>PHD here<br/></p>
                    <p><strong>Tel: </strong>Tel here<br/></p>
                    <p><strong>Email: </strong>Email here<br/></p>
                    <p><strong>Office: </strong>Office here<br/></p>
                    <p><strong>Homepage: </strong>Homepage here<br/></p>
                    '''
                }
            },
        ]
    },
    'people.html people_name': {
        'name' : 'people_name',
        'plugins': ['TextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'TextPlugin',
                'values':{
                    'body':'<p>Dean Cher Wang / 王雪红 院长</p>'
                }
            },
        ]
    },
    'people.html people_brefintro': {
        'name' : 'people_brefintro',
        'plugins': ['TextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'TextPlugin',
                'values':{
                    'body':'<p>Enter your bref introduction. This content will show on list page.</p>'
                }
            },
        ]
    },
    'people.html people_content': {
        'name' : 'people_content',
        'plugins': ['TextPlugin'],
        'default_plugins':[
            {
                'plugin_type':'TextPlugin',
                'values':{
                    'body':'<p>Enter your Content</p>'
                }
            },
        ]
    },
}
