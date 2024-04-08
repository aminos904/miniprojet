import mysql.connector as db

def connectDB():
    return db.connect(
        host="localhost",
        user="root",
        password="",
        database="mini_project"
    )