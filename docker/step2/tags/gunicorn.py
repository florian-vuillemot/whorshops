"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()

if gunicorn_folder := environ.get("GUNICORN_FOLDER"):
    accesslog = f'{gunicorn_folder}/gunicorn.log'
    errorlog = f'{gunicorn_folder}/gunicorn.error.log'
else:
    print('No log file')

capture_output = True
log_level = 'debug'
