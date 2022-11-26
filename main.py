import json
from flask import Flask, jsonify, request
import sqlite3

conn = sqlite3.connect('STM1.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT UNIQUE);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
   taskid INTEGER PRIMARY KEY AUTOINCREMENT,
   username TEXT,
   title TEXT UNIQUE,
   description TEXT,
   done BOOLEAN,
   FOREIGN KEY(username) REFERENCES users(userid));
""")
conn.commit()
conn.close()



app = Flask(__name__)

#add users
@app.route('/todo/api/v1.0/adduser', methods=['POST', 'GET'])
def add_user():
    if 'username' in request.args:
        try:
            conn = sqlite3.connect('STM1.db')
            cur = conn.cursor()
            username = request.args['username']
            cur.execute(f"""INSERT INTO users(username) 
            VALUES('{username}');""")
            conn.commit()
            cur.execute(f"SELECT userid FROM users WHERE username='{username}'")
            userid = cur.fetchone()
            conn.close()
        except sqlite3.IntegrityError:
            return 'This username is already in use!'
        else:
            return f"User {username} has created with id {userid[0]}!"
    else:
        return "Invalid arguments"

#get users list
@app.route('/todo/api/v1.0/get_users', methods=['GET'])
def get_user_list():
    conn = sqlite3.connect('STM1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    conn.close()
    return jsonify(result)


    #print (request.method)

#add task
@app.route('/todo/api/v1.0/add_task', methods=['POST', 'GET'])    
def add_task():
    if 'username' in request.args and 'title' in request.args and 'description' in request.args and 'done' in request.args:
        try:
            task = (request.args['username'], request.args['title'], request.args['description'], request.args['done'])
            conn = sqlite3.connect('STM1.db')
            cur = conn.cursor()
            cur.execute(f"""INSERT INTO tasks(username, title, description, done) 
                VALUES('{username}', '{title}', '{description}', '{done}');""")
            conn.commit()
            conn.close()
        except Exception:
            return print(Exception)
            
        else:
            return "Tasks added!"
    else:
        return "Invalid argument"




if __name__ == '__main__':
    app.run(debug=True)