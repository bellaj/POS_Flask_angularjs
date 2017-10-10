#!/usr/bin/env python
from flask import Flask, jsonify, send_from_directory, request
app = Flask(__name__)


@app.route('/api/v1/get_names')
def get_names():
    names = {'names':
             [
                 'fred',
                 'john',
                 'paul',
                 'greg'
             ]}
    return jsonify(names)

@app.route('/api/v1/get_people')
def get_people():
    people = {"people": [
        {'name': 'fred', 'age': 10},
        {'name': 'john', 'age': 20},
        {'name': 'paul', 'age': 30},
        {'name': 'greg', 'age': 40},
    ]}
    return jsonify(people)


@app.route('/api/v1/get_time')
def get_time():
    import time
    return jsonify({'time': time.time()})

@app.route('/files/style.css', methods=['GET', 'POST'])
def test():
	return send_from_directory("files", "style.css")
	#return render_template('./files/style.css')
	
@app.route('/files/app.js', methods=['GET', 'POST'])
def test2():
	return send_from_directory("files", "app.js")
	#return render_template('./files/style.css')

@app.route('/')
def index():
    return send_from_directory(".", "index.html")
	
@app.route('/customers', methods=['GET', 'POST'])
def customers():
	total = request.args.get('total')
	return jsonify({'total': total})
	#return send_from_directory("templates","customers.html")
	


if __name__ == '__main__':
    app.debug = True
    app.run(port=1234)
