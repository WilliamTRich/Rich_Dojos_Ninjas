from flask_app import app
from flask import render_template, redirect, url_for, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninja', methods=['POST', 'GET'])
def ninja():
    if request.method == 'POST':
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'dojos_id' : request.form['dojo'],
            'age' : request.form['age']
        }
        Ninja.save(data)
        return redirect('/dojo/{}'.format(data['dojos_id']))
    else:
        return render_template('new_ninja.html', dojos=Dojo.get_all())