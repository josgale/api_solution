import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

cnx = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_DATABASE'),
    port=os.getenv('DB_PORT')
)

cursor = cnx.cursor()


def post_user(usr_id, name):
    add_user = "INSERT INTO users (id, user_name) VALUES (%s, %s)"
    user_data = (usr_id, name)
    cursor.execute(add_user, user_data)
    cnx.commit()


def get_all_users():
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = []
    for (usr_id, name) in cursor:
        user = {'id': usr_id, 'user_name': name}
        users.append(user)
    return users


def get_user_by_id(usr_id):
    query = "SELECT user_name FROM users WHERE id = %s"
    cursor.execute(query, (usr_id,))
    user = cursor.fetchone()
    if user:
        return {'id': usr_id, 'user_name': user[0]}
    else:
        return None
