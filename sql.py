#import
import mysql.connector
mydb = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'student'
)

#cursor
mycursor = mydb.cursor()

#creating table
table = 'CREATE TABLE StudentInfo(student_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, first_name LONGTEXT NOT NULL, last_name LONGTEXT NOT NULL, date_of_birth LONGTEXT NOT NULL, amount_due LONGTEXT NOT NULL)'

mycursor.execute(table)

