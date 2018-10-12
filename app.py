#!flask/Source/python
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, jsonify

def mysql_conn():
    try:
      connection = mysql.connector.connect(
      host = 'localhost',
      user = 'root',
      password = 'evawanjiku',
      database = 'todo_list')

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
     
    return connection

app = Flask('app')

@app.route('/')
def index():
	return 'Hello world'

@app.route('/user', methods=['GET'])
def getUsers():
  conn = mysql_conn()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM user")
  result = cursor.fetchall()



  return jsonify(result)
  

if __name__== '__main__':
	app.run(debug=True)