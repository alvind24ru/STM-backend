import json
from flask import Flask, jsonify, request
from tasks import TASCKS
import sqlite3

conn = sqlite3.connect('STM1.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   email TEXT UNIQUE);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
   taskid INTEGER PRIMARY KEY AUTOINCREMENT,
   user TEXT,
   title TEXT,
   description TEXT,
   done BOOLEAN,
   FOREIGN KEY(user) REFERENCES users(userid));
""")
conn.commit()
conn.close()



app = Flask(__name__)

#add users
@app.route('/todo/api/v1.0/adduser', methods=['POST', 'GET'])
def add_user():
    if 'username' in request.args and 'email' in request.args:
        try:
            conn = sqlite3.connect('STM1.db')
            cur = conn.cursor()
            username = request.args['username']
            email = request.args['email']
            cur.execute(f"""INSERT INTO users(name, email) 
            VALUES('{username}', '{email}');""")
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            return 'mail is already available'
        else:
            return f"User {username} created"
    else:
        return "something went wrong"
        

    #print (request.method)
    
    


if __name__ == '__main__':
    app.run(debug=True)