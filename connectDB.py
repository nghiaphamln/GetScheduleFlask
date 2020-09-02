import mysql.connector


myDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='userofstudent'
)


# Get MSSV
def getMSSV(fb_id):
    myCursor = myDB.cursor()
    sql = "SELECT username FROM users WHERE fb_id = '" + fb_id + "'"
    myCursor.execute(sql)
    myResult = myCursor.fetchall()
    return myResult[0][0]
