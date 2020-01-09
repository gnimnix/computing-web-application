# ./app.py

# This file is to handle flask operations

from flask import Flask, render_template, url_for, request, redirect
import sqlite3

webapp = Flask(__name__)

@webapp.route('/')
def index():
    pass
