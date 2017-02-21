#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify

from . import main


@main.route('/', methods=['GET'])
def hello_world():
    return jsonify(status='success', message='welcome to jack003!')
