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

# Insert to DB
def insertMSSV(fb_id, MSSV):
    myCursor = myDB.cursor()
    sql = "INSERT INTO Users(fb_id, username) VALUES (%s, %s)"
    val = (fb_id, MSSV)
    myCursor.execute(sql, val)
    myDB.commit()

insertMSSV('123', '1824801030067')