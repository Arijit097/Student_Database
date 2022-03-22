#[FRONTEND]

from tkinter import*
import tkinter.messagebox

import BackEnd

class Student:
    def __init__(self, root):
        self.root= root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        STUDENT_ID = StringVar()
        FIRST_NAME = StringVar()
        LAST_NAME= StringVar()
        DATE_OF_BIRTH= StringVar()
        AGE= StringVar()
        GENDER = StringVar()
        ADDRESS = StringVar()
        MOBILE_NO = StringVar()

        #============================================== FUNCTIONS =================================

        def Exit():
            Exit = tkinter.messagebox.askyesno("Student Database Management System","CONFIRM IF YOU WANT TO EXIT")
            if Exit < 0:
                root.destroy()
                return

        def ClearData():
            self.txtSTUDENT_ID.delete(0, END)
            self.txtFIRST_NAME.delete(0, END)
            self.txtLAST_NAME.delete(0, END)
            self.txtDATE_OF_BIRTH.delete(0, END)
            self.txtAGE.delete(0, END)
            self.txtGENDER.delete(0, END)
            self.txtADDRESS.delete(0, END)
            self.txtMOBILE_NO.delete(0, END)

        def AddData():
            if(len(STUDENT_ID.get())!=0):
                BackEnd.addstdRec(STUDENT_ID.get(),FIRST_NAME.get() , LAST_NAME.get() , DATE_OF_BIRTH.get() , AGE.get() ,GENDER.get() , ADDRESS.get() ,MOBILE_NO.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(STUDENT_ID.get(),FIRST_NAME.get() , LAST_NAME.get() , DATE_OF_BIRTH.get() , AGE.get() ,GENDER.get() , ADDRESS.get() ,MOBILE_NO.get()))


        def DisplayData():
            studentlist.delete(0,END)
            for row in BackEnd.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd= studentlist.get(searchStd)

            self.txtSTUDENT_ID.delete(0, END)
            self.txtSTUDENT_ID.insert(END,sd[1])
            self.txtFIRST_NAME.delete(0, END)
            self.txtFIRST_NAME.insert(END,sd[2])
            self.txtLAST_NAME.delete(0, END)
            self.txtLAST_NAME.insert(END,sd[3])
            self.txtDATE_OF_BIRTH.delete(0, END)
            self.txtDATE_OF_BIRTH.insert(END,sd[4])
            self.txtAGE.delete(0, END)
            self.txtAGE.insert(END,sd[5])
            self.txtGENDER.delete(0, END)
            self.txtGENDER.insert(END,sd[6])
            self.txtADDRESS.delete(0, END)
            self.txtADDRESS.insert(END,sd[7])
            self.txtMOBILE_NO.delete(0, END)
            self.txtMOBILE_NO.insert(END,sd[8])

        def DeleteData():
            if(len(STUDENT_ID.get())!=0):
                BackEnd.deleteRec(sd[0])
                ClearData()
                DisplayData()

        def SearchData():
            studentlist.delete(0,END)
            for row in BackEnd.searchData(STUDENT_ID.get(),FIRST_NAME.get() , LAST_NAME.get() , DATE_OF_BIRTH.get() , AGE.get() ,GENDER.get() , ADDRESS.get() ,MOBILE_NO.get()):
                studentlist.insert(END,row,str(""))


        def UpdateData():
            if(len(STUDENT_ID.get())!=0):
                BackEnd.deleteRec(sd[0])
            if(len(STUDENT_ID.get())!=0):
                BackEnd.addstdRec(STUDENT_ID.get(),FIRST_NAME.get() , LAST_NAME.get() , DATE_OF_BIRTH.get() , AGE.get() ,GENDER.get() , ADDRESS.get() ,MOBILE_NO.get())
                studentlist.delete(0,END)
                studentlist.insert(END(STUDENT_ID.get(),FIRST_NAME.get() , LAST_NAME.get() , DATE_OF_BIRTH.get() , AGE.get() ,GENDER.get() , ADDRESS.get() ,MOBILE_NO.get()))







        #================================================== FRAMES =================================

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=1, padx=20,pady=4, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit =Label(TitFrame, font=('arial', 35, 'bold'), text="Student Database Management System", bg="Ghost white")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width= 1350, heigh= 70, padx=18,pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20,pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height= 600, padx=20, bg="Ghost White", relief=RIDGE, font=('arial', 30, 'bold'), text="Student Information\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31,pady=3, bg="Ghost White", relief=RIDGE,font=('arial', 20, 'bold'), text="Student Details\n" )
        DataFrameRIGHT.pack(side=RIGHT)

                #================================================== LABELS AND ENTRY WIDGET =================================


        self.lblSTUDENT_ID =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="STUDENT ID:", padx=2,pady=2,  bg="Ghost white")
        self.lblSTUDENT_ID.grid(row=0, column=0, sticky=W)
        self.txtSTUDENT_ID =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=STUDENT_ID, width=30)
        self.txtSTUDENT_ID.grid(row=0, column=1)

        self.lblFIRST_NAME =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="FIRST NAME:", padx=2,pady=2,  bg="Ghost white")
        self.lblFIRST_NAME.grid(row=1, column=0, sticky=W)
        self.txtFIRST_NAME =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=FIRST_NAME, width=30)
        self.txtFIRST_NAME.grid(row=1, column=1)

        self.lblLAST_NAME =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="LAST NAME:", padx=2,pady=2,  bg="Ghost white")
        self.lblLAST_NAME.grid(row=2, column=0, sticky=W)
        self.txtLAST_NAME =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=LAST_NAME, width=30)
        self.txtLAST_NAME.grid(row=2, column=1)

        self.lblDATE_OF_BIRTH =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="DATE OF BIRTH:", padx=2,pady=2,  bg="Ghost white")
        self.lblDATE_OF_BIRTH.grid(row=3, column=0, sticky=W)
        self.txtDATE_OF_BIRTH =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DATE_OF_BIRTH, width=30)
        self.txtDATE_OF_BIRTH.grid(row=3, column=1)

        self.lblAGE =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="AGE:", padx=2,pady=2,  bg="Ghost white")
        self.lblAGE.grid(row=4, column=0, sticky=W)
        self.txtAGE =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=AGE, width=30)
        self.txtAGE.grid(row=4, column=1)

        self.lblGENDER =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="GENDER:", padx=2,pady=2,  bg="Ghost white")
        self.lblGENDER.grid(row=5, column=0, sticky=W)
        self.txtGENDER =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=GENDER, width=30)
        self.txtGENDER.grid(row=5, column=1)

        self.lblADDRESS =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="ADDRESS:", padx=2,pady=2,  bg="Ghost white")
        self.lblADDRESS.grid(row=6, column=0, sticky=W)
        self.txtADDRESS=Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=ADDRESS, width=30)
        self.txtADDRESS.grid(row=6, column=1)

        self.lblMOBILE_NO  =Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="MOBILE Number:", padx=2,pady=2,  bg="Ghost white")
        self.lblMOBILE_NO .grid(row=7, column=0, sticky=W)
        self.txtMOBILE_NO  =Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=MOBILE_NO , width=30)
        self.txtMOBILE_NO .grid(row=7, column=1)


         #================================================== LISTBOX AND SCROLLBAR WIDGET ==================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=2, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width= 32, height=16, font=('arial', 12, 'bold'), yscrollcomman= scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command= studentlist.yview)


         #================================================== BUTTON WIDGET =================================

        self.btnAddData= Button(ButtonFrame, text=" Add New", font=('arial', 12, 'bold'), height=1, width=10,bd=3, command=AddData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData= Button(ButtonFrame, text=" Display", font=('arial', 12, 'bold'), height=1, width=10,bd=3, command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData= Button(ButtonFrame, text=" Clear", font=('arial', 12, 'bold'), height=1, width=10,bd=3, command=ClearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData= Button(ButtonFrame, text=" Delete", font=('arial', 12, 'bold'), height=1, width=10,bd=3, command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData= Button(ButtonFrame, text=" Search", font=('arial', 12, 'bold'), height=1, width=10,bd=3,comman=SearchData)
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData= Button(ButtonFrame, text=" Update", font=('arial', 12, 'bold'), height=1, width=10,bd=3, command=UpdateData)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExit= Button(ButtonFrame, text=" Exit", font=('arial', 12, 'bold'), height=1, width=10,bd=3, command=Exit)
        self.btnExit.grid(row=0,column=6)


if __name__ == '__main__':
    root= Tk()
    application = Student(root)
    root.mainloop()


