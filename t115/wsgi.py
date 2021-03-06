#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Run:
        $ gunicorn --bind 0.0.0.0:6000 --workers 4 --worker-class gevent \
                --threads 4 wsgi:app
    Test:
        $ for i in $(seq 1 10000); do curl http://localhost:6000/echo/$i & \
                ; done
"""

import logging

from flask import Flask

from server import Server


def init_app():
    logging.basicConfig(
            format='%(asctime)s:%(levelname)-8s:%(threadName)-12s:%(message)s')
    logging.getLogger().setLevel('DEBUG')

    s = Server()

    app = Flask(__name__)
    app.add_url_rule('/ping', 'ping', s.ping)
    app.add_url_rule('/hello', 'hello', s.hello)
    app.add_url_rule('/content', 'content', s.content)
    app.add_url_rule('/error', 'error', s.error)
    app.add_url_rule('/echo/<string>', 'echo', s.echo)
    app.add_url_rule('/echo_post/', 'echo_post', s.echo_post, methods=['POST'])

    return app


app = init_app()
