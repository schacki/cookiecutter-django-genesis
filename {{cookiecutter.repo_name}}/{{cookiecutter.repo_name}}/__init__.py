# -*- coding: utf-8 -*-

import os, environ, logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

prepared = False
env = environ.Env()

def prepare(target=''):
    global prepared
    if prepared:
        return

    if target and not target.startswith('-'):
        target = '-' + target

    # ROOT_DIR is the the top project directory
    ROOT_DIR = environ.Path(__file__) - 2
    logger.info('ROOT_DIR is: {}'.format(ROOT_DIR))

    # ETC_DIR contains any relevant configuration data and files
    ETC_DIR = env(
        'DJANGO_ETC_DIR',
        default=str(ROOT_DIR.path('etc'))
    )
    logger.info('ETC_DIR is: {}'.format(ETC_DIR))

    # ENV_FILE_PATH is a .env file that might contain configuration data for Django that might overrid the defaults
    # specified in this settings file.
    ENV_FILE_PATH = env(
        'DJANGO_ENV_FILE_PATH',
        default=str(environ.Path(ETC_DIR).path('.{{ cookiecutter.repo_name }}{}-env'.format(target),))
    )
    logger.info('ENV_FILE_PATH is: {}'.format(ENV_FILE_PATH))

    # Read the the specified .env file to activate any of the  specified configurations.
    environ.Env.read_env(ENV_FILE_PATH)

    # VAR_DIR contains variable data like meda, static, database etc.
    try:
        VAR_DIR = env('DJANGO_VAR_DIR')
    except:
        VAR_DIR = str(ROOT_DIR.path('var'))
        os.environ.setdefault('DJANGO_VAR_DIR', VAR_DIR)
    logger.info('VAR_DIR is: {}'.format(VAR_DIR))

    try:
        DB_FILE_PATH = env('DJANGO_DB_FILE_PATH')
    except:
        DB_FILE_PATH = str(environ.Path(VAR_DIR).path('db.sqlite3'))
        os.environ.setdefault('DJANGO_DB_FILE_PATH', DB_FILE_PATH)
    logger.info('DB_FILE_PATH is: {}'.format(DB_FILE_PATH))

    try:
        STATIC_ROOT = env('DJANGO_STATIC_ROOT')
    except:
        STATIC_ROOT = str(environ.Path(VAR_DIR).path('www/static'))
        os.environ.setdefault('DJANGO_STATIC_ROOT', STATIC_ROOT)
        logger.info('STATIC_ROOT is: {}'.format(STATIC_ROOT))

    try:
        STATICFILES_DIRS = env.list('DJANGO_STATICFILES_DIRS')
    except:
        STATICFILES_DIRS = str(ROOT_DIR.path('bower_components'))
        os.environ.setdefault('DJANGO_STATICFILES_DIRS', STATICFILES_DIRS)
        logger.info('STATICFILES_DIRS is: {}'.format(STATICFILES_DIRS))

    try:
        MEDIA_ROOT = env('DJANGO_MEDIA_ROOT')
    except:
        MEDIA_ROOT = str(environ.Path(VAR_DIR).path('www/media'))
        os.environ.setdefault('DJANGO_MEDIA_ROOT', MEDIA_ROOT)
        logger.info('MEDIA_ROOT is: {}'.format(MEDIA_ROOT))

    try:
        DEBUG_LOG_FILE_PATH = env('DJANGO_DEBUG_LOG_FILE_PATH')
    except:
        DEBUG_LOG_FILE_PATH = str(environ.Path(VAR_DIR).path('log').path('{{ cookiecutter.repo_name }}-django-debug.log'))
        os.environ.setdefault('DJANGO_DEBUG_LOG_FILE_PATH', DEBUG_LOG_FILE_PATH)
        logger.info('DEBUG_LOG_FILE_PATH is: {}'.format(DEBUG_LOG_FILE_PATH))

    try:
        ERROR_LOG_FILE_PATH = env('DJANGO_ERROR_LOG_FILE_PATH')
    except:
        ERROR_LOG_FILE_PATH = str(environ.Path(VAR_DIR).path('log').path('{{ cookiecutter.repo_name }}-django-error.log'))
        os.environ.setdefault('DJANGO_ERROR_LOG_FILE_PATH', ERROR_LOG_FILE_PATH)
        logger.info('ERROR_LOG_FILE_PATH is: {}'.format(ERROR_LOG_FILE_PATH))

    prepared = True