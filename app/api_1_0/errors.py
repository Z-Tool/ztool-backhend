#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify
from app.exceptions import ValidationError
from . import api_1_0


def bad_request(message):
    return jsonify({'error': 'bad request', 'message': message}), 400


def unauthorized(message):
    return jsonify({'error': 'unauthorized', 'message': message}), 401


@api_1_0.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
