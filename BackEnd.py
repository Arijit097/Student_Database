import sqlite3
#backend
import cur


def studentData():
    con = sqlite3.connect("student.db")
    cur.execute("CREATE TABLE IF NOT EXISTS student(ID INTEGER PRIMARY KEY, STUDENT_ID text, FIRST_NAME text, LAST_NAME text, DATE_OF_BIRTH text, AGE text,GENDER text, ADDRESS text,MOBILE_NO text )")
    con.commit()
    con.close()



def addstdRec(STUDENT_ID , FIRST_NAME , LAST_NAME , DATE_OF_BIRTH , AGE ,GENDER , ADDRESS ,MOBILE_NO ):
    con = sqlite3.connect("student.db")
    cur = con.cursor('*')
    cur.execute("INSERT INTO student VALUES(NULL, ?,?,?,?,?,?,?,?)",STUDENT_ID , FIRST_NAME , LAST_NAME , DATE_OF_BIRTH , AGE ,GENDER , ADDRESS ,MOBILE_NO)
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor('*')
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    con.close()
    return row

def deleteRec():
    con=sqlite3.connect("student.db")
    cur= con.cursor('*')
    cur.execute("DELETE FROM FROM student WHERE id=?",(id,))
    con.commit()
    con.close()

def searchData(STUDENT_ID="" , FIRST_NAME="" , LAST_NAME="" , DATE_OF_BIRTH="" , AGE="" ,GENDER="" , ADDRESS="" ,MOBILE_NO=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE STUDENT_ID=? OR FIRST_NAME=? OR LAST_NAME=? OR DATE_OF_BIRTH=? OR AGE= ? OR GENDER=? OR ADDRESS=? OR MOBILE_NO=?", (STUDENT_ID , FIRST_NAME , LAST_NAME , DATE_OF_BIRTH , AGE ,GENDER , ADDRESS ,MOBILE_NO))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,STUDENT_ID="" , FIRST_NAME="" , LAST_NAME="" , DATE_OF_BIRTH="" , AGE="" ,GENDER="" , ADDRESS="", MOBILE_NO=""):
    con= sqlite3.connect("student.db")
    cur.execute("UPDATE student SET STUDENT_ID=? OR FIRST_NAME=? OR LAST_NAME=? OR DATE_OF_BIRTH=? OR AGE= ? OR GENDER=? OR ADDRESS=? OR MOBILE_NO=?, WHERE id=?",\
                (STUDENT_ID , FIRST_NAME , LAST_NAME , DATE_OF_BIRTH , AGE ,GENDER , ADDRESS ,MOBILE_NO, id))
    con.commit()
    con.close()

