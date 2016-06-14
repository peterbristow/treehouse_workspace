import json

from flask import (Flask, render_template, redirect,
                   url_for, request, make_response, flash)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'vbasd7r6345k13451978&tf*^fghj63I'


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))  # json.loads converts json string to a dict
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    # import pdb; pdb.set_trace() ### Debugger
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()  # get data from cookie
    data.update(dict(request.form.items()))  # update data if anything has changed
    response.set_cookie('character', json.dumps(data))  # json.dumps creates a json.string
    return response


app.run(debug=True, host='127.0.0.1', port=8000)
