from flask import Flask

app = Flask(__name__)


# TODO - move this into a class

@app.route('/api/user/login/')
def login():
	return 'Hello World, I am the Users Service, I will "handle" users :D !'


@app.route('/api/user/create/')
def create():
	return 'Hello World, I am the Users Service, I will "handle" users :D !'


@app.route('/api/user/update/')
def update():
	return 'Hello World, I am the Users Service, I will "handle" users :D !'


@app.route('/api/user/delete/')
def delete():
	return 'Hello World, I am the Users Service, I will "handle" users :D !'


if __name__ == '__main__':
	app.run(host="127.0.0.1", port=8080, debug=True)
