import datetime
from app import app
from flask import Flask, render_template, request
import utils
import json


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.form.get('table_name'):
        columns = utils.get_table_columns(request.form['table_name'])
    else:
        columns = []
    return render_template(
         'index.html',
         title="Main Page",
         user="Super Tester",
         tables=utils.get_tables(),
         form_data=request.form,
         columns=columns,
    )

@app.route('/tables/<table_name>/columns')
def get_columns(table_name):
    table_columns = utils.get_table_columns(table_name)
    return json.dumps(table_columns)
