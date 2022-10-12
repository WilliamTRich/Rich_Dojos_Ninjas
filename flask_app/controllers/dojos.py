from flask_app import app
from flask import render_template, redirect, url_for, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojo', methods=['GET', 'POST'])
def dojo():
    if request.method == 'POST':
        data = {
            'name': request.form['name']
        }
        Dojo.save(data)
        return redirect('/dojo')
    else:
        return render_template('dojos.html', dojos=Dojo.get_all())

@app.route('/dojo/<dojoID>')
def single_dojo(dojoID):
    data = {'id' : dojoID}
    dojo = Dojo.get_one(data)
    ninjas = Ninja.get_all(data)
    return render_template('single_dojo.html', dojo=dojo, ninjas=ninjas)