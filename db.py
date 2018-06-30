import MySQLdb
from namegenerator import RandomName
from table_python import Table_python
import random

# Open database connection
def database():
    # Create a db connection
    db = MySQLdb.connect("localhost","root","","hometogo_db" )
    user = Table_python("Billy Omallah", "jishinde1234", "Administrator")
    print(updateTable(db, 13, user))
    disconnectDatabase(db)

# Populate database records
def populateDatabase(number_of_records, db):
    for user in range(0, number_of_records):
        # generated variables
        uname = generateRandomUsername()
        pd = generateRandomPassword()
        role = generateRandomRole()
        new_user = Table_python(uname, pd, role)
        insertData(db, new_user)

# Generate random userrole
def generateRandomRole():
    #create a tuple of 4 userroles - Administrator, SuperAdmin, Guest and Viewer
    user_role = ('Administrator', 'Superadministrator', 'Guest', 'Viewer')
    index_value = random.randint(0, 3)
    return user_role[index_value]

# Generate random username
def generateRandomUsername():
    random_name = RandomName()
    generated_word = random_name.generate_word(random.randint(0, 6))
    return generated_word

# Generate random password
def generateRandomPassword():
    initial_words = RandomName()
    passwordNumbers = random.randint(1000, 9999)
    generated_password = initial_words.generate_word(random.randint(0, 6)) + str(passwordNumbers)
    return generated_password

# View all records
def viewDatabaseRecords(db_connection):
    cursor = db_connection.cursor()
    query = "SELECT * FROM table_python"
    cursor.execute(query)
    data = cursor.fetchall()
    for row in range(0, len(data)):
        print(f"Username: {data[row][1]} | Userrole: {data[row][4]} | Time of Sign up: {data[row][3]}")

# Perform a db delete
def deleteTable(db_connection):
    cursor = db_connection.cursor()
    query = "DELETE table_python"
    cursor.execute(query)
    message = cursor.fetchone()
    return message;

# Perform a db insert
def insertData(db_connection, user):
    # capture all required variables from the class
    username = user.getUsername()
    password = user.getPassword()
    userrole = user.getUserrole()

    query = "INSERT INTO table_python(tbl_name, tbl_password, tbl_timestamp, tbl_user_role) VALUES('{}', '{}', CURRENT_TIMESTAMP ,'{}')".format(username, password, userrole)
    print(query)
    cursor = db_connection.cursor()
    cursor.execute(str(query))
    db_connection.commit()
    message = cursor.fetchall()
    return message


def updateTable(db_connection, row_id, user):
    cursor = db_connection.cursor()
    query = "UPDATE table_python SET tbl_name ='{}', tbl_password ='{}', tbl_user_role ='{}' WHERE tbl_python_id ='{}'".format(user.getUsername(), user.getPassword(), user.getUserrole(), row_id)
    cursor.execute(query)
    db_connection.commit()
    message = cursor.fetchone();
    return message;

def checkTableDetails(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DESCRIBE table_python")
    # grab one raw with fetchone and one row with fetch all...
    message = cursor.fetchall()
    return message

def createTable(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS table_python(tbl_python_id INT NOT NULL PRIMARY KEY, tbl_name VARCHAR(30) NOT NULL,tbl_password VARCHAR(40) NOT NULL, tbl_timestamp TIMESTAMP, tbl_user_role VARCHAR(30))")
    message = cursor.fetchone()
    return message

# Check if database is live
def testDatabase(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT VERSION()")
    print("Database test completed successfully")
    message = cursor.fetchone()
    print(f"MySQL Database version is {message}")

# Disconnect database
def disconnectDatabase(db_connection):
    db_connection.close()
    print("Database disconnected successfully")


if __name__ == '__main__':
    database()


