#!/usr/bin/env python3
import connexion
import logging


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='definitions/')
app.add_api('openapi.yaml')#, strict_validation=True)
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app


if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
