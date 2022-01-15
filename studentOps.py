import student
from tkinter import *

a = student.createStudent("Baby", '123', 36, 15, 14, 11, 10)
b = student.createStudent("Shriya", '456', 90, 70, 99, 90, 100)
c = student.createStudent("Nathee", '789', 12, 37, 14, 11, 100)
d = student.createStudent("chitiki", '101', 90, 70, 90, 81, 90)
listOfStudents = [a,b,c,d]

   
def addStudent(name,usn,m1,m2,m3,m4,m5):
    student1 = student.createStudent(name,usn,int(m1),int(m2),int(m3),int(m4),int(m5))
    listOfStudents.append(student1)
    if len(listOfStudents) > 0:
        print(listOfStudents[len(listOfStudents) - 1])
        
        
def deletestud(USN):
    for student in listOfStudents:
        if student.USN==USN:
            print('Deleted Student is', student.name)
            listOfStudents.remove(student)
            print('Remaining Students')
            for stud in listOfStudents:
                print(stud.name)
            break
        else:
            print("no student with this usn exists")      
        
                
def delstud():
    root= Tk()
    name = Label(root,text = 'enter the usn of the student you want to delete:')
    name.grid()
    q = Entry(root,text = 'enter the usn of the student:')
    q.grid()
    bt3 = Button(root,text = 'submit',command = lambda: deletestud(q.get()))
    bt3.grid()
    
        

    


def createStudentWindow():
    root = Tk()
    name = Label(root,text = 'enter the name: ')
    name.grid()
    a = Entry(root,text = "enter the name of the student: ")
    a.grid()

    enterUSN = Label(root,text = 'enter the USN of the student: ')
    enterUSN.grid()
    b = Entry(root,width = 20)
    b.grid()

    m1 = Label(root,text = 'enter the marks for the first subject: ')
    m1.grid()
    c = Entry(root,width = 5)
    c.grid()
    m2 = Label(root,text = 'enter the marks for the second subject: ')
    m2.grid()
    d = Entry(root,width = 5)
    d.grid()
    m3 = Label(root,text = 'enter the marks for the third subject: ')
    m3.grid()
    e = Entry(root,width = 5)
    e.grid()
    m4 = Label(root,text = 'enter the marks for the fourth subject: ')
    m4.grid()
    f = Entry(root,width = 5)
    f.grid()
    m5 = Label(root,text = 'enter the marks for the fifth subject: ')
    m5.grid()
    g = Entry(root,width = 5)
    g.grid()
    bt2 = Button(root,text = 'Create Student', command = lambda: addStudent(a.get(),b.get(),c.get(),d.get(),e.get(),f.get(),g.get()))
    bt2.grid()



def getaverage():
    if len(listOfStudents) == 0:
        print('No students')
    else:
        average_of_students = 0
        for students in listOfStudents:
            print(students.name,"'s" " average is ", students.average())
            average_of_students += students.average()
        print('Average of all Students is ', average_of_students/len(listOfStudents))
        print('Test')



def searchBasedUSN(USN):
    student_found = False
    for student in listOfStudents:
        if student.USN == USN:
            print("the student is ",student.name)
            student_found = True
            break
    if student_found == False:
        print("sudent not found")      
        
        
        
def searchBasedUSNwindow():
    root = Tk()
    USNlabel = Label(root,text = "enter the USN of the student you want to check: ")
    USNlabel.grid()
    k = Entry(root,text = "enter the usn:")
    k.grid()
    bt4 = Button(root,text = 'submit',command = lambda : searchBasedUSN(k.get()))
    bt4.grid()


def studentcheck(USN):
    for students in listOfStudents:
        if students.USN == USN:
            if students.m1<35:
                print("name : ",students.name)
                print("USN : ", students.USN)
                print("subject 1 : FAIL ")
            else :
                print("name : ",students.name)
                print("USN : ", students.USN)
                print("subject 1 : PASS ")
            if students.m2<35:
                print("subject 2 : FAIL")
            else :
                print("subject 2 : PASS")
            if students.m3<35:
                print("subject 3 : FAIL")
            else :
                print("subject 3 : PASS")
            if students.m4<35:
                print("subject 4 : FAIL")
            else :
                print("subject 4 : PASS")
            if students.m5<35:
                print("subject 5 : FAIL")
            else :
                print("subject 5 : PASS")
            


def studentcheckwindow():
    root = Tk()
    studchecklabel = Label(root,text = "to check the porformance of the student")
    studchecklabel.grid()
    f= Entry(root,text = "enter the student's usn you want to check for")
    f.grid()
    bt5 = Button(root,text = "submit",command = lambda : studentcheck(f.get()))
    bt5.grid()
    
    
def studentpassed():
    for students in listOfStudents:
        if students.m1>35 and students.m2>35 and students.m3>35 and students.m4>35 and students.m5>35 :
            print(students.name, " passed all the 5 subjects . ")    



def student_failed_atleastone():
    for students in listOfStudents:
        if students.m1<35 or students.m2<35 or students.m3<35 or students.m4<35 or students.m5<35 :
            print(students.name, " failed in atleast one subject.")
    
    

    

root = Tk()
CreateStudentLabel = Button(root,text = 'create a student: ', fg = 'blue',bg = 'black',command = createStudentWindow)
CreateStudentLabel.grid(row=0, column=1, padx=10, pady=10)


DeleteStudrntLabel = Button(root,text = 'delete a student: ',fg = 'blue',bg = 'black',command = delstud)
DeleteStudrntLabel.grid(row=10, column=1, padx=10, pady=10)


AverageMarkaLabel = Button(root,text = 'average marks of all students: ',fg = 'blue',bg = 'black',command = getaverage)
AverageMarkaLabel.grid(row=20, column=1, padx=10, pady=10)


searchBasedusn = Button(root,text = "search based on USN",fg = 'blue',bg = 'black',command = searchBasedUSNwindow)
searchBasedusn.grid(row=30, column=1, padx=10, pady=10)


studcheck = Button(root,text = "check the performance of the student",fg = 'blue',bg = 'black',command = studentcheckwindow)
studcheck.grid(row=40, column=1, padx=10, pady=10)


studpassed = Button(root,text = "check for the students who passed all the subjects",fg = 'blue',bg = 'black', command = studentpassed)
studpassed.grid(row=50, column=1, padx=10, pady=10)


stud_failed_atleastone = Button(root,text = "check for the students who failed in atleast one subject",fg = 'blue',bg = 'black',command = student_failed_atleastone)
stud_failed_atleastone.grid(row=60, column=1, padx=10, pady=10)



root.mainloop()
