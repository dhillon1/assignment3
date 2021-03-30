#import
from flask import *
import mysql.connector

#MySQL database connector
mydb = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    database = 'student'
)

#MySQL cursor
mycursor = mydb.cursor()

app = Flask(__name__)

#app route to a demo page
@app.route('/')
def hello():
    return "Hello world!"

#this route will help us to create and read student records
@app.route('/student-record',methods= ['GET','POST'])
def info():
    # get  method for reading all students records
    if request.method == 'GET':
        mycursor.execute("Select * from StudentInfo")
        myresult = mycursor.fetchall()
        result = []
        for data in myresult:
            var1 = {
                "student_id" : int(data[0]),
                "first_name" : data[1],
                "last_name" : data[2],
                "date_of_birth" : data[3],
                "amount_due" : data[4]
            }
            result.append(var1)

        return jsonify(result)

    # post method for creating student record
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['date_of_birth']
        amount_due = request.form['amount_due']

        # storing data to sql
        sql = "INSERT INTO StudentInfo (first_name, last_name,date_of_birth,amount_due) VALUES (%s, %s,%s,%s)"
        val = (first_name,last_name,dob,amount_due)
        mycursor.execute(sql, val)
        mydb.commit()
        
        #reading  data from sql to show data to postman via restapi
        mycursor.execute("Select * from StudentInfo")
        myresult = mycursor.fetchall()
        result = []
        for data in myresult:
            var1 = {
                "student_id" : int(data[0]),
                "first_name" : data[1],
                "last_name" : data[2],
                "date_of_birth" : data[3],
                "amount_due" : data[4]
            }
            result.append(var1)

        return jsonify(result)

# thisroute will help us to read, update and delete student record by student id
@app.route('/student-record/<int:id>',methods= ['GET','PUT','DELETE'])
def update(id):

    # for getting student record by student id
    if request.method == 'GET':
        # reading  from sql
        mycursor.execute("Select * from StudentInfo where student_id = {}".format(id))
        myresult = mycursor.fetchone()
        if myresult == None:
            return "No record found. Please check student id "
        else:
            result = {
        
                "student_id" : int(myresult[0]),
                "first_name" : myresult[1],
                "last_name" : myresult[2],
                "date_of_birth" : myresult[3],
                "amount_due" : myresult[4]
            }
            return jsonify(result)

    # for updating  student record by student id
    if request.method == 'PUT':
        mycursor.execute("Select * from StudentInfo where student_id = {}".format(id))
        myresult = mycursor.fetchone()
        if myresult == None:
            return "No record found. Please check student id "
        else:
        
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            date_of_birth = request.form['date_of_birth']
            amount_due = request.form['amount_due']

            #updating student record in sql
            sql = "UPDATE StudentInfo set first_name = '"+first_name+"', last_name ='"+last_name +"' ,date_of_birth = '"+date_of_birth+"' , amount_due= '"+ amount_due+"'  where student_id = {}".format(id)
            print(sql)
            mycursor.execute(sql)
            mydb.commit()

            result = {
        
                "student_id" : int(myresult[0]),
                "first_name" : first_name,
                "last_name" : last_name,
                "date_of_birth" : date_of_birth,
                "amount_due" : amount_due
            }
            return jsonify(result)
            
    #deleting student record by student id
    if request.method == 'DELETE':
        sql = "DELETE FROM StudentInfo WHERE student_id = {}".format(id)
        mycursor.execute(sql)
        mydb.commit()
        return 'Record deleted'

if __name__ == "__main__":
    app.run(debug =  True)