from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

val = ""
A = 0
operator = ""

mydb = sql.connect(host = "localhost", user = "root", passwd = "SqlDhwaj195", database = "dhwaj")
cursor = mydb.cursor()
cursor.execute("create table if not exists Cal_Login(Username varchar(20) NOT NULL,Password int NOT NULL,PRIMARY KEY (Username))")

def Exit():
    Exit = messagebox.askyesno("Conformation","Confirm to Exit")
    if Exit > 0:
        mainwindow.destroy()
        return

def Reset():
    InputU.set("")
    InputP.set("")
    return
    
def signup():
    username = str(InputU.get())
    password = str(InputP.get())

    cursor.execute("SELECT * FROM Cal_Login WHERE username = '%s'"% (username,))
    row = cursor.fetchone()
    mydb.commit()

    if username == "":
        messagebox.showerror('Information', "Please Enter Username")  
        InputU.set("")  
        return  

    if password == "":
        messagebox.showerror('Information', "Please Enter Password")  
        InputP.set("")
        return

    
    if row == None:
        password = int(InputP.get())
        query = "insert into Cal_Login values(%s,%s)"          
        args = (username,password)                   
        cursor.execute(query,args)                  
        mydb.commit()
        messagebox.showinfo("SignUp Successful","You have been successfully registered in our database.")
        return
    
    
    else:
        messagebox.showerror("Information","Username already exists.SignUp with different username.")
    


def login():
    username = str(InputU.get())
    password = str(InputP.get())
    if username == "":
        messagebox.showerror('Information', "Please Enter Username")  
        InputU.set("")  
        return  
    if password == "":
        messagebox.showerror('Information', "Please Enter Password")  
        InputP.set("")
        return

    password = int(InputP.get())
    cursor.execute("select * from Cal_Login where username = '%s' and password = %s" %(username, password))
    rud = cursor.fetchall()
    mydb.commit()
        
    if rud :
        messagebox.showinfo('Information', "Login Successfully")
        exe()
            
    else :
        messagebox.showerror('Information', "Login failed,Invalid Username or Password.Try again!!!")

def delete():
    username = str(InputU.get())
    password = int(InputP.get())
    if username == "":
        messagebox.showerror('Information', "Please Enter Username")  
        InputU.set("")  
        return  
    if password == "":
        messagebox.showerror('Information', "Please Enter Password")  
        InputP.set("")
        return

    cursor.execute("select * from Cal_Login where username = '%s' and password = %s" %(username, password))
    rud = cursor.fetchall()
    mydb.commit()
        
    if rud :
        cursor.execute("delete from Cal_Login where username = '%s' and password = %s" %(username, password))
        messagebox.showinfo('Information', "Record deleted")    
        mydb.commit()
        return
    else :
        messagebox.showerror("Information","Record does not exist")

def exe():
    window = Toplevel(mainwindow)
    window.resizable(0,0)
    window.geometry("307x250+300+200")
    window.configure(bg = "#c0ded9")


    Mainframe = Frame(window,bd = 10)
    Mainframe.grid()

    RecieptButton_F = LabelFrame(Mainframe,bd = 10, width = 551, height = 80,
                                         font = ('Helvetica',12,'bold'), relief = RIDGE)
    RecieptButton_F.pack(side = TOP)

    #=====Exit=======

    def Exit():
        Exit = messagebox.askyesno("Conformation","Confirm to Exit")
        if Exit > 0:
            window.destroy()
            return

    #=====file1=======

    def Whole():
        
        root = Toplevel(window)
        root.resizable(0,0)
        root.geometry("598x400+300+200")
        root.configure(bg = "")

        Baseframe = Frame(root,bd = 10)
        Baseframe.grid()

        TopF = Frame(Baseframe, bd = 10, width = 100,relief = RIDGE)
        TopF.pack(side = TOP)

        TitleLabel = Label(TopF, font = ('Edo SZ',18,'bold'),text = "Permutation\n&\nCombination", width = 39, height = 3,
                          justify = CENTER,bg = "light blue")
        TitleLabel.grid(padx = 2)

        Inputframe = LabelFrame(Baseframe, bd = 10, width = 551, height = 200,
                                font = ('Helvetica',12,'bold'), relief = RIDGE)
        Inputframe.pack(side = TOP)

        Buttonframe = LabelFrame(Baseframe, bd = 10, width = 551, height = 200,
                                font = ('Helvetica',12,'bold'), relief = RIDGE)
        Buttonframe.pack(side = TOP)

        TopN = Frame(Baseframe, bd = 10, width = 100,relief = RIDGE)
        TopN.pack(side = BOTTOM)

        lblName = Label(TopN, font = ('Edo SZ',15,'bold'),text = "Programmed By- Dhwaj Agarwal", width = 49, height = 1,
                                     justify = RIGHT, bg = "light blue")
        lblName.grid(padx = 4)

        InputN = StringVar()
        InputN.set("Please enter the value of 'n' here")
        InputR = StringVar()
        InputR.set("Please enter the value of 'r' here")
        Answer = StringVar()
        Answer.set("Your answer will be displayed here")

        lblInputN = Label(Inputframe, font = ('Edo SZ',15,'bold'),text = "Input N",bd = 7)
        lblInputN.grid(row = 0, column = 0, sticky = W)
        txtInputN = Entry(Inputframe, font = ('Edo SZ',13,'bold'), bd = 7, textvariable = InputN, width = 44)
        txtInputN.grid(row = 0, column = 1)

        lblInputR = Label(Inputframe, font = ('Edo SZ',15,'bold'),text = "Input R",bd = 7)
        lblInputR.grid(row = 1, column = 0, sticky = W)
        txtInputR = Entry(Inputframe, font = ('Edo SZ',13,'bold'), bd = 7, textvariable = InputR, width = 44)
        txtInputR.grid(row = 1, column = 1)
                
        lblAnswer = Label(Inputframe, font = ('Edo SZ',15,'bold'),text = "Answer",bd = 7)
        lblAnswer.grid(row = 2, column = 0, sticky = W)
        lblAnswer = Entry(Inputframe, font = ('Edo SZ',13,'bold'), bd = 7, textvariable = Answer, width = 44,state = DISABLED)
        lblAnswer.grid(row = 2, column = 1)

        def Reset():
            InputN.set("")
            InputR.set("")
            Answer.set("")
            return

        def iExit():
            iExit = messagebox.askyesno("Conformation","Confirm to Exit")
            if iExit > 0:
                root.destroy()
                return

        def P():
            Item1 = (InputN.get())
            Item2 = (InputR.get())
            if (Item1.isdigit() and Item2.isdigit()):
                Item1 = int(Item1)
                Item2 = int(Item2)
                if Item1<=0:
                    messagebox.showerror('Error',"Value of R cannot be less than or equal to '0'")
                    InputN.set('')
                elif Item2==0:
                    Answer.set(1)
                else:
                    f1 = 1
                    f2 = 1
                    i1 = 1
                    i2 = 1
                    while i1 <= Item1 :
                        f1 = f1*i1
                        i1 = i1+1
                    N1 = f1
                    while i2 <= (Item1-Item2) :
                        f2 = f2*i2
                        i2 = i2+1
                    N2 = f2
                    Answer.set(N1/N2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                elif Item2 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputN.set("")

        def C():
            Item1 = (InputN.get())
            Item2 = (InputR.get())
            if (Item1.isdigit() and Item2.isdigit()):
                Item1 = int(Item1)
                Item2 = int(Item2)
                if Item1<=0:
                    messagebox.showerror('Error',"Value of R cannot be less than or equal to '0'")
                    InputN.set('')
                elif Item2==0:
                    Answer.set(1)
                elif Item1==Item2:
                    Answer.set(1)
                else:
                    f3 = 1
                    f4 = 1
                    f5 = 1
                    i3 = 1
                    i4 = 1 
                    i5 = 1
                    while i3 <= Item1 :
                        f3 = f3*i3
                        i3 = i3+1
                    N3 = f3
                    while i4<= (Item1-Item2) :
                        f4 = f4*i4
                        i4 = i4+1
                    N4 = f4
                    while i5<=Item2 :
                        f5 = f5*i5
                        i5 = i5+1
                    N5 = f5
                    Answer.set(N3/(N4*N5))
                    
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                elif Item2 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputN.set("")
                    

        #buttons
        btnP = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 9,
                      command = P,text = 'Permutation', bg = 'light blue').grid(row = 0, column = 0, pady = 12)

        btnC = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 9,
                      command = C,text = 'Combination', bg = 'light blue').grid(row = 0, column = 1, pady = 12)

        btnReset = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                          command = Reset, text = 'Reset', bg = 'light blue').grid(row = 0, column = 2, pady = 12)
                
        btnExit = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                         command = iExit,text = 'Exit', bg = 'light blue').grid(row = 0, column = 3, pady = 12)

        root.mainloop()

    #=====file2=======

    def Num():
        root = Toplevel(window)
        root.resizable(0,0)
        root.title("Number System convertor")
        root.geometry("598x505+300+200")
        root.configure(bg = "#c0ded9")
                
                #=================================================Frames=============================================================================

        Mainframe = Frame(root,bd = 10)
        Mainframe.grid()
                
        Tops = Frame(Mainframe,bd = 10, width = 100,relief = RIDGE)
        Tops.pack(side = TOP)
                
        lblInfo = Label(Tops, font = ('Edo SZ',18,'bold'),text = "Number System Convertor", width = 39, height = 1,
                                     justify = CENTER,bg = "#c0ded9")
        lblInfo.grid(padx = 2)
                
               
        MembersName_F = LabelFrame(Mainframe, bd = 10, width = 551, height = 200,
                                           font = ('Helvetica',12,'bold'), relief = RIDGE)
        MembersName_F.pack(side = TOP)
               
        RecieptButton_F = LabelFrame(Mainframe,bd = 10, width = 551, height = 80,
                                            font = ('Helvetica',12,'bold'), relief = RIDGE)
        RecieptButton_F.pack(side = TOP)

        Tops1 = Frame(Mainframe,bd = 10, width = 100,relief = RIDGE)
        Tops1.pack(side = TOP)
                
        lblName = Label(Tops1, font = ('Edo SZ',15,'bold'),text = "Programmed By- Dhwaj Agarwal", width = 49, height = 1,
                                     justify = RIGHT, bg = "#c0ded9")
        lblName.grid(padx = 4)
                
                #=================================================Variables=============================================================================

        InputVar = StringVar()
        InputVar.set("Please enter the value here")
        Answer = StringVar()
        Answer.set("Your answer will be displayed here")
                
                #=================================================Label Entry========================================================================

        lblInputVar = Label(MembersName_F, font = ('Edo SZ',15,'bold'),text = "Input",bd = 7)
        lblInputVar.grid(row = 0, column = 0, sticky = W)
        txtInputVar = Entry(MembersName_F, font = ('Edo SZ',13,'bold'), bd = 7, textvariable = InputVar, width = 44)
        txtInputVar.grid(row = 0, column = 1)
                
        lblAnswer = Label(MembersName_F, font = ('Edo SZ',15,'bold'),text = "Answer",bd = 7)
        lblAnswer.grid(row = 1, column = 0, sticky = W)
        lblAnswer = Entry(MembersName_F, font = ('Edo SZ',13,'bold'), bd = 7, textvariable = Answer, width = 44,state = DISABLED)
        lblAnswer.grid(row = 1, column = 1)

                #==================================================Functions======================================================================

        def Reset():
            InputVar.set("")
            Answer.set("")
            return

        def iExit():
            iExit = messagebox.askyesno("Conformation","Confirm to Exit")
            if iExit > 0:
                root.destroy()
                return
        #1    
        def dec_to_bin():
            Item1 = (InputVar.get())
            if (Item1.isdigit()):
                Item2 = bin(int(Item1))
                Item2 = Item2[2:]
                Answer.set(Item2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #2
        def bin_to_dec():
            Item1 = (InputVar.get())
            set1 = set(Item1)
            if Item1.isdigit():
                    Item2 = int(Item1,2)
                    Answer.set(Item2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #3
        def dec_to_oct():
            Item1 = (InputVar.get())
            if (Item1.isdigit()):
                Item2 = oct(int(Item1))
                Item2 = Item2[2:]
                Answer.set(Item2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")

        #4        
        def oct_to_dec():
            Item1 = (InputVar.get())
            Item1= Item1.upper()
            if (Item1.isdigit()):
                Item2 = int(Item1,8)
                Answer.set(Item2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #5
        def dec_to_hex():
            Item1 = (InputVar.get())
            if (Item1.isdigit()):
                Item2 = hex(int(Item1))
                Item2 = Item2.upper()
                Item2 = Item2[2:]
                Answer.set(Item2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #6
        def hex_to_dec():
            Item1 = (InputVar.get())
            Item1= Item1.upper()
            if (Item1.isalnum()):
                Item2 = int(Item1,16)
                Answer.set(Item2)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter Alpha-Numerical value")
                    InputVar.set("")

        #7
        def bin_to_oct():
            Item1 = (InputVar.get())
            if Item1.isdigit():
                Item2 = int(Item1,2)
                Item3= oct(Item2)
                Item3 = Item3[2:]
                Answer.set(Item3)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")

        #8
        def oct_to_bin():
            Item1 = (InputVar.get())
            if Item1.isdigit():
                Item2 = int(Item1,8)
                Item3= bin(Item2)
                Item3 = Item3[2:]
                Answer.set(Item3)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #9
        def bin_to_hex():
            Item1 = (InputVar.get())
            if Item1.isdigit():
                Item2 = int(Item1,2)
                Item3= hex(Item2)
                Item3 = Item3[2:]
                Item3 = Item3.upper()
                Answer.set(Item3)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #10
        def hex_to_bin():
            Item1 = (InputVar.get())
            if Item1.isalnum():
                Item2 = int(Item1,16)
                Item3= bin(Item2)
                Item3 = Item3[2:]
                Item3 = Item3.upper()
                Answer.set(Item3)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #11
        def oct_to_hex():
            Item1 = (InputVar.get())
            if Item1.isdigit():
                Item2 = int(Item1,8)
                Item3= hex(Item2)
                Item3 = Item3[2:]
                Item3 = Item3.upper()
                Answer.set(Item3)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
        #12
        def hex_to_oct():
            Item1 = (InputVar.get())
            if Item1.isalnum():
                Item2 = int(Item1,16)
                Item3= oct(Item2)
                Item3 = Item3[2:]
                Item3 = Item3.upper()
                Answer.set(Item3)
            else:
                if Item1 == "":
                    messagebox.showinfo("Error","The field is empty\nEnter a value to perform calculation")
                else:
                    messagebox.showerror("Error","The value entered is Invalid!!\nPlease enter integral value")
                    InputVar.set("")
                
                #==================================================Buttons===========================================================================
                
        btnDecToBin = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = dec_to_bin, relief = RIDGE, text = 'Dec to Bin', bg = 'orange').grid(row = 2, column = 0, pady = 12)
        btnBinToDec = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = bin_to_dec, relief = RIDGE, text = 'Bin to Dec', bg = 'yellow').grid(row = 2, column = 1, pady = 12)

        btnOctToDec = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = oct_to_dec, relief = RIDGE, text = 'Oct to Dec', bg = '#00ffff').grid(row = 2, column = 2, pady = 12)

        btnHexToDec = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = hex_to_dec, relief = RIDGE, text = 'Hex to Dec', bg = 'dodgerblue').grid(row = 2, column = 3, pady = 12)
                
        btnDecToOct = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = dec_to_oct, relief = RIDGE, text = 'Dec to Oct', bg = 'orange').grid(row = 3, column = 0, pady = 12)
                
        btnBinToOct = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = bin_to_oct, relief = RIDGE, text = 'Bin to Oct', bg = 'yellow').grid(row = 3, column = 1, pady = 12)

        btnOctToBin = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = oct_to_bin, relief = RIDGE,text = 'Oct to Bin', bg = '#00ffff').grid(row = 3, column = 2, pady = 12)

        btnHexToBin = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = hex_to_bin, relief = RIDGE, text = 'Hex to Bin', bg = 'dodgerblue').grid(row = 3, column = 3, pady = 12)
                
        btnDecToHex = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = dec_to_hex, relief = RIDGE, text = 'Dec to Hex', bg = 'orange').grid(row = 4, column = 0, pady = 12)
                
        btnBinToHex = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = bin_to_hex, relief = RIDGE, text = 'Bin to Hex', bg = 'yellow').grid(row = 4, column = 1, pady = 12)
                
        btnOctToHex = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = oct_to_hex, relief = RIDGE, text = 'Oct to Hex', bg = '#00ffff').grid(row = 4, column = 2, pady = 12)
                
        btnHexToOct = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                             command = hex_to_oct, relief = RIDGE, text = 'Hex to Oct', bg = 'dodgerblue').grid(row = 4, column = 3, pady = 12)
                
        btnReset = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                          command = Reset, relief = RIDGE, text = 'Reset', bg = 'lightgreen').grid(row = 5, column = 1, pady = 12)
                
        btnExit = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,
                         command = iExit, relief = RIDGE,text = 'Exit', bg = 'firebrick1').grid(row = 5, column = 2, pady = 12)

    #====file3======
                
    

    def cal():
        
        def btn_1_isclicked():
            global val
            val = val + "1"
            data.set(val)
            
        def btn_2_isclicked():
            global val
            val = val + "2"
            data.set(val)

        def btn_3_isclicked():
            global val
            val = val + "3"
            data.set(val)

        def btn_4_isclicked():
            global val
            val = val + "4"
            data.set(val)

        def btn_5_isclicked():
            global val
            val = val + "5"
            data.set(val)

        def btn_6_isclicked():
            global val
            val = val + "6"
            data.set(val)

        def btn_7_isclicked():
            global val
            val = val + "7"
            data.set(val)

        def btn_8_isclicked():
            global val
            val = val + "8"
            data.set(val)

        def btn_9_isclicked():
            global val
            val = val + "9"
            data.set(val)

        def btn_0_isclicked():
            global val
            val = val + "0"
            data.set(val)

        def btn_plus_clicked():
            global A
            global operator
            global val
            A = int(val)
            operator = "+"
            val = val + "+"
            data.set(val)

        def btn_minus_clicked():
            global A
            global operator
            global val
            A = int(val)
            operator = "-"
            val = val + "-"
            data.set(val)

        def btn_multiply_clicked():
            global A
            global operator
            global val
            A = int(val)
            operator = "*"
            val = val + "*"
            data.set(val)

        def btn_division_clicked():
            global A
            global operator
            global val
            A = int(val)
            operator = "/"
            val = val + "/"
            data.set(val)

        def c_pressed():
            global A
            global operator
            global val
            val = ""
            A = 0
            operator = "C"
            data.set(val)

        def result():
            global A
            global operator
            global val
            val2 = val
            
            if operator == "+":
                x = int((val2.split("+")[1]))
                C = A + x
                data.set(C)
                val = str(C)
                
            elif operator == "-":
                x = int((val2.split("-")[1]))
                C = A - x
                data.set(C)
                val = str(C)
                
            elif operator == "*":
                x = int((val2.split("*")[1]))
                C = A * x
                data.set(C)
                val = str(C)
                
            elif operator == "/":
                x = int((val2.split("/")[1]))
                if x == 0:
                    messagebox.showerror("Error","Division by 0 Not allowed!")
                    A = ""
                    val = ""
                    data.set(val)
                else:
                    C = A / x
                    data.set(C)
                    val = str(C)

        root = Toplevel(window)
        root.geometry("250x400+300+300")
        root.resizable(0,0)
        root.title("calculator")

        data = StringVar()
        lbl = Label(
            root,
            text = "Label",
            anchor = SE,
            font = ("Verdana", 20),
            textvariable = data,
            background = "#ffffff",
            fg = "#000000",
        )
        lbl.pack(expand = True,fill = "both",)

        btnrow1 = Frame(root,bg="#000000")
        btnrow1.pack(expand = True,fill = "both",)

        btnrow2 = Frame(root)
        btnrow2.pack(expand = True,fill = "both",)

        btnrow3 = Frame(root)
        btnrow3.pack(expand = True,fill = "both",)

        btnrow4 = Frame(root)
        btnrow4.pack(expand = True,fill = "both",)

        btn1 = Button(
            btnrow1,
            text = "1",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_1_isclicked,
        )
        btn1.pack(side = LEFT, expand = True, fill = "both",)

        btn2 = Button(
            btnrow1,
            text = "2",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_2_isclicked,
        )
        btn2.pack(side = LEFT, expand = True, fill = "both",)

        btn3 = Button(
            btnrow1,
            text = "3",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_3_isclicked,
        )
        btn3.pack(side = LEFT, expand = True, fill = "both",)

        btnplus = Button(
            btnrow1,
            text = "+",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_plus_clicked,
        )
        btnplus.pack(side = LEFT, expand = True, fill = "both",)

        btn4 = Button(
            btnrow2,
            text = "4",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_4_isclicked,
        )
        btn4.pack(side = LEFT, expand = True, fill = "both",)

        btn5 = Button(
            btnrow2,
            text = "5",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_5_isclicked,
        )
        btn5.pack(side = LEFT, expand = True, fill = "both",)

        btn6 = Button(
            btnrow2,
            text = "6",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_6_isclicked,
        )
        btn6.pack(side = LEFT, expand = True, fill = "both",)

        btnminus = Button(
            btnrow2,
            text = "-",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_minus_clicked,
        )
        btnminus.pack(side = LEFT, expand = True, fill = "both",)

        btn7 = Button(
            btnrow3,
            text = "7",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_7_isclicked,
        )
        btn7.pack(side = LEFT, expand = True, fill = "both",)

        btn8 = Button(
            btnrow3,
            text = "8",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_8_isclicked,
        )
        btn8.pack(side = LEFT, expand = True, fill = "both",)

        btn9 = Button(
            btnrow3,
            text = "9",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_9_isclicked,
        )
        btn9.pack(side = LEFT, expand = True, fill = "both",)

        btnmultiply = Button(
            btnrow3,
            text = "*",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_multiply_clicked,
        )
        btnmultiply.pack(side = LEFT, expand = True, fill = "both",)    

        btnclear = Button(
            btnrow4,
            text = "C",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = c_pressed,
        )
        btnclear.pack(side = LEFT, expand = True, fill = "both",)

        btn0 = Button(
            btnrow4,
            text = "0",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_0_isclicked,
        )
        btn0.pack(side = LEFT, expand = True, fill = "both",)

        btnequal = Button(
            btnrow4,
            text = "=",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = result,
        )
        btnequal.pack(side = LEFT, expand = True, fill = "both",)

        btndivision = Button(
            btnrow4,
            text = "/",
            font = ("Verdana", 22),
            relief = GROOVE,
            border = 0,
            command = btn_division_clicked,
        )
        btndivision.pack(side = LEFT, expand = True, fill = "both",)

        root.mainloop()


    #=====
    btnPandC = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,height = 3,
                      command = Whole, relief = RIDGE, text = 'Permutation\n&\n Combination', bg = 'firebrick1').grid(row = 0, column = 0, pady = 12)
    btnNum = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,height = 3,
                    command = Num, relief = RIDGE, text = 'Number\nSystem\nConvertor', bg = 'yellow').grid(row = 0, column = 1, pady = 12)
    btnCal = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,height = 3,
                    command = cal, relief = RIDGE, text = 'Integer\nCalculator', bg = 'light blue').grid(row = 1, column = 0, pady = 12)
    btnExit = Button(RecieptButton_F, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 8,height = 3,
                     command = Exit, relief = RIDGE, text = 'Exit', bg = 'orange').grid(row = 1, column = 1, pady = 12)

    window.mainloop()
    return


mainwindow = Tk()
mainwindow.resizable(0,0)
mainwindow.geometry("566x370+300+200")
mainwindow.configure(bg = "#c0ded9")

Baseframe = Frame(mainwindow,bd = 10)
Baseframe.grid()

TopF = Frame(Baseframe, bd = 10, width = 100,relief = RIDGE)
TopF.pack(side = TOP)
TitleLabel = Label(TopF, font = ('Edo SZ',16,'bold'),text = "Multipurpose Calculator\nLogin Window", width = 43, height = 3,
                   justify = CENTER,bg = "light blue")
TitleLabel.grid(padx = 2)

Inputframe = LabelFrame(Baseframe, bd = 10, width = 551, height = 200,
                        font = ('Helvetica',12,'bold'), relief = RIDGE)
Inputframe.pack(side = TOP)

Buttonframe = LabelFrame(Baseframe, bd = 10, width = 551, height = 200,
                         font = ('Helvetica',12,'bold'), relief = RIDGE)
Buttonframe.pack(side = TOP)

Nameframe = LabelFrame(Baseframe, bd = 10, width = 551, height = 200,
                       font = ('Helvetica',12,'bold'), relief = RIDGE)
Nameframe.pack(side = TOP)
NameLabel = Label(Nameframe, font = ('Edo SZ',16,'bold'),text = "Progrmmed By-\nDhwaj Agarwal", width = 43, height = 2,
                   justify = CENTER,bg = "#c0ded9")
NameLabel.grid(padx = 2)

InputU = StringVar()
InputU.set("Enter your Username [Limit 20 characters]")
InputP = IntVar()
InputP.set("Enter your Password [Integer combination only]")

lblInputU = Label(Inputframe, font = ('Edo SZ',16,'bold'),text = "Username",bd = 7)
lblInputU.grid(row = 0, column = 0, sticky = W)
txtInputU = Entry(Inputframe, font = ('Constantia',13,'bold'), bd = 7, textvariable = InputU, width = 39)
txtInputU.grid(row = 0, column = 1)

lblInputP = Label(Inputframe, font = ('Edo SZ',16,'bold'),text = "Password",bd = 7)
lblInputP.grid(row = 1, column = 0, sticky = W)
txtInputP = Entry(Inputframe, font = ('Constantia',13,'bold'), bd = 7, textvariable = InputP, width = 39)
txtInputP.grid(row = 1, column = 1)

#buttons
btn_Login = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 5,
                   command = login,text = 'Login', bg = 'dodgerblue').grid(row = 0, column = 0, pady = 12)

btn_Signup = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 5,
                    command = signup,text = 'SignUp', bg = 'dodgerblue').grid(row = 0, column = 1, pady = 12)

btn_Delete = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 5,
                    command = delete,text = 'Delete', bg = 'dodgerblue').grid(row = 0, column = 2, pady = 12)

btnReset = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 5,
                  command = Reset, text = 'Reset', bg = 'dodgerblue').grid(row = 0, column = 3, pady = 12)
            
btnExit = Button(Buttonframe, padx = 18, font = ('Edo SZ',13,'bold'), bd = 7, width = 5,
                 command = Exit,text = 'Exit', bg = 'dodgerblue').grid(row = 0, column = 4, pady = 12)
        
mainwindow.mainloop()