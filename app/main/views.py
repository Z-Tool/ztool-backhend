#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template

from . import main


@main.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')
