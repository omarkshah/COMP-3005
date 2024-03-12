import psycopg2 #importing library

#Connecting to the server
conn = psycopg2.connect(database="StudentDBApp",
                        user="postgres",
                        password="postgres",
                        port="5432")
cur = conn.cursor()

#Gets all the students in the students table
def getAllStudents():
    #executing the command
    cur.execute('SELECT * FROM students;')
    rows = cur.fetchall() #from the execution result getting all the tuples
    conn.commit()
    for row in rows: #printing
        print(row)

#adds a the parameter into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    #executing and commiting the command
    cur.execute("INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()

#updates an email with respect to the given params
def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()

#deletes the student in the param from the students table
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()

#the user interface
    # a constant loop asking for input and calling the relevant function
x = -1
while(x != '0'):
    print("Enter input ")
    x = input()

    if(x == "1"):
        getAllStudents()
    elif(x == "2"):
        first_name = input("Enter first name ")
        last_name = input("Enter last name ")
        email  = input("Enter email ")
        enrollmentDate = input("Enter enrollment date")
        addStudent(first_name, last_name, email, enrollmentDate)
    elif(x == "3"):
        student_id = input("Enter student id ")
        new_email = input("Enter new email ")
        updateStudentEmail(student_id, new_email)
    elif(x == "4"):
        student_id = input("Enter student id ")
        deleteStudent(student_id)
cur.close()
conn.close()
