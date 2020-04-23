from flask import Flask
import os
app = Flask(__name__)

@app.route('/')

def hello_world():
	var = "Flash Dockerized"
	mod_var = "This is a new addition"
	print(var)
	return mod_var

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
