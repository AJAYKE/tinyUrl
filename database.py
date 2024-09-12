import mysql.connector

#mydb = mysql.connector.connect(host = 'localhost', user = 'mysql', password = 'strong_password', port = 3306, database="TINYURL")



def get_data_from_db():
    mydb = mysql.connector.connect(host = 'localhost', user = 'mysql', password = 'strong_password', port = 3306, database="TINYURL")

    mycursor = mydb.cursor()
    mycursor.execute('''select * from ranges
''')
    data = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return data

print(get_data_from_db())