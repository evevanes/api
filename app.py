#!flask/Source/python

from flask import Flask, jsonify, request
from config import Config


config = Config()
cursor = config.get_cursor()
app = Flask('app')

@app.route('/')
def index():
	return 'Hello world'

@app.errorhandler(404)
def page_not_found(error):
  result = {
    "statusCode": "404",
    "status": "failed",
    "message": "Not found"
  }
  return jsonify(result)

@app.route('/user', methods=['GET'])
def getUsers():
  
  cursor.execute("SELECT * FROM user")
  user_data = cursor.fetchall()

  result = {
    "result": user_data
  }



  return jsonify(result)


@app.route('/register', methods=['POST'])
def registerUser():
  result = request.get_json()

  # Get data from the request object
  name = result['name']
  email = result['email']
  password = result['password']

  # Insert data to table
  query = "INSERT INTO user  VALUES (%s,%s,%s,%s, NOW())"
  values = (3, name, email, password)
  cursor.execute(query, values)

  return jsonify(result)
  

if __name__== '__main__':
	app.run(debug=True)