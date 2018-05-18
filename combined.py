from Tkinter import *

import tkMessageBox
import csv
import sys
global a
global b
global c
c=list(range(3))
b=list(range(4))
a=list(range(1,51))
count=0
p=1
operator="booked sheats are"
#global textInput
#textInput=StringVar() 


      
csvfile = open('mycsv2.csv', 'r+')
spamreader = csv.reader(csvfile, delimiter=' ', quotechar='\n')

            
a = []
for row in spamreader:
      z = ",".join(row)
      a.append(z)
      if z=='BK':
        count=count+1


def cancel():
        top=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 15 -weight bold -slant roman"  \
            " -underline 1 -overstrike 0"

        top.geometry("600x593+650+7")
        top.title("Cancel Ticket")
        top.configure(background="#008080")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        def cancelticket():
                with open("cancel.csv","r") as csv_out4:
                      row2=list()
                      user=frstname.get()
                      paswrd=lastname.get()
                      st1=int((email.get()))-1
                      st=str(st1)
                     # print "st",st
                      
                      csv_out = open('mycsv2.csv', 'w+')
                      mywriter = csv.writer(csv_out)
                      rows = zip(a)
                      mywriter.writerows(rows)
                      csv_out.close()
                      for row1 in csv_out4:
                            if user in row1 and paswrd in row1 and st in row1:
                                  #print"row1",row1
                                  a[st1]=st1+1
                                  row2.extend(row1)
                                  #print "row2",row2
                      if"\n" in row2:
                            tkMessageBox.showinfo("Cancel","Successfully Cancelled")
                      else:
                            tkMessageBox.showwarning("Cancel","Please check details")


        Frame1 = Frame(top)
        Frame1.place(relx=0.17, rely=0.2, relheight=0.67, relwidth=0.64)
        Frame1.configure(relief=GROOVE)
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief=GROOVE)
        Frame1.configure(background="#d9d9d9")
        Frame1.configure(highlightbackground="#d9d9d9")
        Frame1.configure(highlightcolor="black")
        Frame1.configure(width=385)

        Label2 = Label(Frame1)
        Label2.place(relx=0.0, rely=0.03, height=41, width=94)
        Label2.configure(activebackground="#f9f9f9")
        Label2.configure(activeforeground="black")
        Label2.configure(background="#d9d9d9")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(foreground="#000000")
        Label2.configure(highlightbackground="#d9d9d9")
        Label2.configure(text='''Email''')
        Label2.configure(width=94)

        frstname = Entry(Frame1)
        frstname.place(relx=0.05, rely=0.1,height=30, relwidth=0.69)
        frstname.configure(background="white")
        frstname.configure(disabledforeground="#a3a3a3")
        frstname.configure(font="TkFixedFont")
        frstname.configure(foreground="#000000")
        frstname.configure(highlightbackground="#d9d9d9")
        frstname.configure(highlightcolor="black")
        frstname.configure(insertbackground="black")
        frstname.configure(selectbackground="#c4c4c4")
        frstname.configure(selectforeground="black")

        Label1_1 = Label(Frame1)
        Label1_1.place(relx=0.03, rely=0.18, height=31, width=84)
        Label1_1.configure(activebackground="#f9f9f9")
        Label1_1.configure(activeforeground="black")
        Label1_1.configure(background="#d9d9d9")
        Label1_1.configure(disabledforeground="#a3a3a3")
        Label1_1.configure(foreground="#000000")
        Label1_1.configure(highlightbackground="#d9d9d9")
        Label1_1.configure(highlightcolor="black")
        Label1_1.configure(text='''Passsword''')

        lastname = Entry(Frame1)
        lastname.place(relx=0.05, rely=0.25,height=30, relwidth=0.69)
        lastname.configure(background="white")
        lastname.configure(disabledforeground="#a3a3a3")
        lastname.configure(font="TkFixedFont")
        lastname.configure(foreground="#000000")
        lastname.configure(highlightbackground="#d9d9d9")
        lastname.configure(highlightcolor="black")
        lastname.configure(insertbackground="black")
        lastname.configure(selectbackground="#c4c4c4")
        lastname.configure(selectforeground="black")

        Label3 = Label(Frame1)
        Label3.place(relx=0.05, rely=0.33, height=31, width=74)
        Label3.configure(activebackground="#f9f9f9")
        Label3.configure(activeforeground="black")
        Label3.configure(background="#d9d9d9")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(foreground="#000000")
        Label3.configure(highlightbackground="#d9d9d9")
        Label3.configure(highlightcolor="black")
        Label3.configure(text='''Seat Number''')

        email = Entry(Frame1)
        email.place(relx=0.05, rely=0.43,height=30, relwidth=0.69)
        email.configure(background="white")
        email.configure(disabledforeground="#a3a3a3")
        email.configure(font="TkFixedFont")
        email.configure(foreground="#000000")
        email.configure(highlightbackground="#d9d9d9")
        email.configure(highlightcolor="black")
        email.configure(insertbackground="black")
        email.configure(selectbackground="#c4c4c4")
        email.configure(selectforeground="black")

        Message1 = Message(Frame1)
        Message1.place(relx=0.03, rely=0.53, relheight=0.13, relwidth=0.68)
        Message1.configure(background="#d9d9d9")
        Message1.configure(foreground="#000000")
        Message1.configure(highlightbackground="#d9d9d9")
        Message1.configure(highlightcolor="black")
        Message1.configure(text='''By clicking Cancel you agree to Booking User agreement Privacy Policy and Cookie Policy.''')
        Message1.configure(width=260)

        Buttonjoin = Button(Frame1)
        Buttonjoin.place(relx=0.05, rely=0.71, height=44, width=267)
        Buttonjoin.configure(activebackground="#d9d9d9")
        Buttonjoin.configure(activeforeground="#000000")
        Buttonjoin.configure(background="#d9d9d9")
        Buttonjoin.configure(disabledforeground="#a3a3a3")
        Buttonjoin.configure(font=font9)
        Buttonjoin.configure(foreground="#000000")
        Buttonjoin.configure(highlightbackground="#d9d9d9")
        Buttonjoin.configure(highlightcolor="#ff0000")
        Buttonjoin.configure(pady="0")
        Buttonjoin.configure(text='''Cancel Now>''')
        Buttonjoin.configure(command=cancelticket)
        top.mainloop()













def mainwindow():
       
        top3=Tk()
        
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI} -size 17 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 15 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"

        top3.geometry("1221x682+76+11")
        top3.title("BOOK YOUR MOVIE")
        top3.configure(background="#d9d9d9")



        Frame2 = Frame(top3)
        Frame2.place(relx=0.03, rely=0.16, relheight=0.73, relwidth=0.92)
        Frame2.configure(relief=GROOVE)
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief=GROOVE)
        Frame2.configure(background="#8080ff")
        Frame2.configure(highlightcolor="#408080")
        Frame2.configure(width=1125)

        Button2 = Button(Frame2)
        Button2.place(relx=0.23, rely=0.38, height=94, width=557)
        Button2.configure(activebackground="#d9d9d9")
        Button2.configure(activeforeground="#000000")
        Button2.configure(background="#d9d9d9")
        Button2.configure(disabledforeground="#a3a3a3")
        Button2.configure(font=font12)
        Button2.configure(foreground="#ff0000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="#ffff80")
        Button2.configure(pady="0")
        Button2.configure(text='''BOOKING''')
        Button2.configure(width=557)
        Button2.configure(command=logIN)
        Button3 = Button(Frame2)
        Button3.place(relx=0.23, rely=0.60, height=94, width=557)
        Button3.configure(activebackground="#d9d9d9")
        Button3.configure(activeforeground="#000000")
        Button3.configure(background="#d9d9d9")
        Button3.configure(disabledforeground="#a3a3a3")
        Button3.configure(font=font12)
        Button3.configure(foreground="#ff0000")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(highlightcolor="#ffff80")
        Button3.configure(pady="0")
        Button3.configure(text='''CANCEL YOUR TICKET''')
        Button3.configure(width=557)
        Button3.configure(command=cancel)

        Message1 = Message(top3)
        Message1.place(relx=0.05, rely=0.89, relheight=0.09, relwidth=1.0)
        Message1.configure(background="#d9d9d9")
        Message1.configure(font=font9)
        Message1.configure(foreground="#000000")
        Message1.configure(highlightbackground="#d9d9d9")
        Message1.configure(highlightcolor="black")
        Message1.configure(text='''Copyright @ Book your seat All Rights Reserved | Contact Us: +91 90000 00000''')
        Message1.configure(width=1220)

        Message2 = Message(top3)
        Message2.place(relx=0.04, rely=0.01, relheight=0.14, relwidth=0.88)
        Message2.configure(background="#d9d9d9")
        Message2.configure(font=font11)
        Message2.configure(foreground="#000000")
        Message2.configure(highlightbackground="#d9d9d9")
        Message2.configure(highlightcolor="black")
        Message2.configure(text='''BOOK YOUR MOVIE''')
        Message2.configure(width=1070)

        
        Button1_1 = Button(top3)
        Button1_1.place(relx=0.77, rely=0.01, height=44, width=127)
        Button1_1.configure(activebackground="#d9d9d9")
        Button1_1.configure(activeforeground="#000000")
        Button1_1.configure(background="#d9d9d9")
        Button1_1.configure(disabledforeground="#a3a3a3")
        Button1_1.configure(foreground="#000000")
        Button1_1.configure(highlightbackground="#d9d9d9")
        Button1_1.configure(highlightcolor="#eb0214")
        Button1_1.configure(pady="0")
        Button1_1.configure(text='''SIGN UP''')
        Button1_1.configure(width=127)
        Button1_1.configure(command=signup)

        Button1_1_1 = Button(top3)
        Button1_1_1.place(relx=0.88, rely=0.01, height=44, width=127)
        Button1_1_1.configure(activebackground="#d9d9d9")
        Button1_1_1.configure(activeforeground="#000000")
        Button1_1_1.configure(background="#d9d9d9")
        Button1_1_1.configure(disabledforeground="#a3a3a3")
        Button1_1_1.configure(foreground="#000000")
        Button1_1_1.configure(highlightbackground="#d9d9d9")
        Button1_1_1.configure(highlightcolor="#000000")
        Button1_1_1.configure(pady="0")
        Button1_1_1.configure(text='''LOG IN''')
        Button1_1_1.configure(command=logIN)
        top3.mainloop()




def logIN():
        top1 = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 19 -weight bold -slant roman"  \
            " -underline 1 -overstrike 0"

        top1.geometry("800x593+650+7")
        top1.title("Log IN")
        top1.configure(background="#008080")
        
        Frame1 = Frame(top1)
        Frame1.place(relx=0.17, rely=0.08, relheight=0.8, relwidth=0.64)
        Frame1.configure(relief=GROOVE)
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief=GROOVE)
        Frame1.configure(background="#d9d9d9")
        Frame1.configure(width=385)

        def LogInUser():
                with open("signup.csv","r") as csv_out:
                      row1=list()
                      email=entry1.get()
                      paswrd=entry2.get()
                      
                     
        
                      for row in csv_out:
                            if email in row and paswrd in row:
                                 
                                 c[0]=entry1.get()
                                 c[1]=entry2.get()
                                 #print "c",c[0],c[1]
                                 row1.extend(row)
                      #print "row1",row1
                                 
                  
                      if "\n" in row1 :
                           #tkMessageBox.showinfo("Log In","Log In Successful")
                           booking()

                      else:
                           tkMessageBox.showwarning("Log In","User Name or Password is incorrect")

            

        Message1 = Message( Frame1)
        Message1.place(relx=0.28, rely=0.07, relheight=0.12, relwidth=0.39)
        Message1.configure(background="#d9d9d9")
        Message1.configure(font=font9)
        Message1.configure(foreground="#000000")
        Message1.configure(highlightbackground="#d9d9d9")
        Message1.configure(highlightcolor="black")
        Message1.configure(text='''LOG IN''')
        Message1.configure(width=232)

        txtUser = Label( Frame1)
        txtUser.place(relx=0.1, rely=0.27, height=41, width=120)
        txtUser.configure(activebackground="#004080")
        txtUser.configure(activeforeground="white")
        txtUser.configure(background="#d9d9d9")
        txtUser.configure(disabledforeground="#a3a3a3")
        txtUser.configure(font=font12)
        txtUser.configure(foreground="#000000")
        txtUser.configure(text='''USER NAME''')
        txtUser.configure(width=120)

        txtpaswrd = Label( Frame1)
        txtpaswrd.place(relx=0.1, rely=0.44, height=41, width=120)
        txtpaswrd.configure(activebackground="#f9f9f9")
        txtpaswrd.configure(activeforeground="black")
        txtpaswrd.configure(background="#d9d9d9")
        txtpaswrd.configure(disabledforeground="#a3a3a3")
        txtpaswrd.configure(font=font12)
        txtpaswrd.configure(foreground="#000000")
        txtpaswrd.configure(highlightbackground="#d9d9d9")
        txtpaswrd.configure(highlightcolor="black")
        txtpaswrd.configure(text='''PASSWORD''')

        entry1 = Entry( Frame1)
        entry1.place(relx=0.38, rely=0.27,height=40, relwidth=0.32)
        entry1.configure(background="white")
        entry1.configure(disabledforeground="#a3a3a3")
        entry1.configure(font="TkFixedFont")
        entry1.configure(foreground="#000000")
        entry1.configure(insertbackground="black")
        entry1.configure(width=194)

        entry2 = Entry( Frame1)
        entry2.place(relx=0.38, rely=0.44,height=40, relwidth=0.32)
        entry2.configure(background="white")
        entry2.configure(disabledforeground="#a3a3a3")
        entry2.configure(font="TkFixedFont")
        entry2.configure(foreground="#000000")
        entry2.configure(highlightbackground="#d9d9d9")
        entry2.configure(highlightcolor="black")
        entry2.configure(insertbackground="black")
        entry2.configure(selectbackground="#c4c4c4")
        entry2.configure(selectforeground="black")
        

        btnlog = Button( Frame1)
        btnlog.place(relx=0.12, rely=0.67, height=44, width=357)
        btnlog.configure(activebackground="#e1031e")
        btnlog.configure(activeforeground="white")
        btnlog.configure(activeforeground="#e1031e")
        btnlog.configure(background="#d9d9d9")
        btnlog.configure(disabledforeground="#a3a3a3")
        btnlog.configure(font=font12)
        btnlog.configure(foreground="#000000")
        btnlog.configure(highlightbackground="#d9d9d9")
        btnlog.configure(highlightcolor="#cd0532")
        btnlog.configure(pady="0")
        btnlog.configure(text='''GO>''')
        btnlog.configure(width=357)
        btnlog.configure(command=LogInUser)

        Button3 = Button( Frame1)
        Button3.place(relx=0.12, rely=0.78, height=44, width=357)
        Button3.configure(activebackground="#d9d9d9")
        Button3.configure(activeforeground="#000000")
        Button3.configure(background="#d9d9d9")
        Button3.configure(disabledforeground="#a3a3a3")
        Button3.configure(font=font12)
        Button3.configure(foreground="#000000")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(highlightcolor="black")
        Button3.configure(pady="0")
        Button3.configure(text='''or SIGN UP''')
        Button3.configure(width=357)
        Button3.configure(command=signup)
        
        menubar = Menu( Frame1,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top1.configure(menu =menubar)
        top1.mainloop()




def signup():
        top = Tk()
        
        def details():
            b[0]=frstname.get()
            b[1]=lastname.get()
            b[2]=email.get()
            
            b[3]=paswrd.get()
            print b[0],b[1],b[2]
            
            csv_out1 = open('signup.csv', 'ab')
            mywriter = csv.writer(csv_out1)
            mywriter.writerow([b[0],b[1],b[2],b[3]])
            csv_out1.close()
            
            
            
       
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 15 -weight bold -slant roman"  \
            " -underline 1 -overstrike 0"

        top.geometry("600x593+650+7")
        top.title("Sign Up")
        top.configure(background="#008080")



        Frame1 = Frame(top)
        Frame1.place(relx=0.17, rely=0.08, relheight=0.8, relwidth=0.64)
        Frame1.configure(relief=GROOVE)
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief=GROOVE)
        Frame1.configure(background="#d9d9d9")
        Frame1.configure(width=385)

        Label2 = Label(Frame1)
        Label2.place(relx=0.03, rely=0.02, height=41, width=84)
        Label2.configure(background="#d9d9d9")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(foreground="#000000")
        Label2.configure(text='''First Name''')
        Label2.configure(width=84)

        frstname = Entry(Frame1)
        frstname.place(relx=0.05, rely=0.08,height=30, relwidth=0.69)
        frstname.configure(background="white")
        frstname.configure(disabledforeground="#a3a3a3")
        frstname.configure(font="TkFixedFont")
        frstname.configure(foreground="#000000")
        frstname.configure(insertbackground="black")
        frstname.configure(width=264)

        Label1 = Label(Frame1)
        Label1.place(relx=0.03, rely=0.15, height=31, width=84)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(foreground="#000000")
        Label1.configure(text='''Last Name''')
        Label1.configure(width=84)

        lastname = Entry(Frame1)
        lastname.place(relx=0.05, rely=0.21,height=30, relwidth=0.69)
        lastname.configure(background="white")
        lastname.configure(disabledforeground="#a3a3a3")
        lastname.configure(font="TkFixedFont")
        lastname.configure(foreground="#000000")
        lastname.configure(insertbackground="black")
        lastname.configure(width=264)

        Label3 = Label(Frame1)
        Label3.place(relx=0.0, rely=0.27, height=31, width=74)
        Label3.configure(background="#d9d9d9")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(foreground="#000000")
        Label3.configure(text='''Email''')
        Label3.configure(width=74)

        email = Entry(Frame1)
        email.place(relx=0.05, rely=0.34,height=30, relwidth=0.69)
        email.configure(background="white")
        email.configure(disabledforeground="#a3a3a3")
        email.configure(font="TkFixedFont")
        email.configure(foreground="#000000")
        email.configure(insertbackground="black")
        email.configure(width=264)

        Label4 = Label(Frame1)
        Label4.place(relx=0.03, rely=0.42, height=21, width=76)
        Label4.configure(background="#d9d9d9")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(foreground="#000000")
        Label4.configure(text='''Password''')
        Label4.configure(width=76)

        paswrd = Entry(Frame1)
        paswrd.place(relx=0.05, rely=0.48,height=30, relwidth=0.69)
        paswrd.configure(background="white")
        paswrd.configure(disabledforeground="#a3a3a3")
        paswrd.configure(font="TkFixedFont")
        paswrd.configure(foreground="#000000")
        paswrd.configure(insertbackground="black")
        paswrd.configure(width=264)

        Message1 = Message(Frame1)
        Message1.place(relx=0.05, rely=0.57, relheight=0.07, relwidth=0.68)
        Message1.configure(background="#d9d9d9")
        Message1.configure(foreground="#000000")
        Message1.configure(highlightbackground="#d9d9d9")
        Message1.configure(highlightcolor="black")
        Message1.configure(text='''By clicking Join Now you agree to Booking User agreement Privacy Policy and Cookie Policy.''')
        Message1.configure(width=260)

        Buttonjoin = Button(Frame1)
        Buttonjoin.place(relx=0.05, rely=0.67, height=44, width=267)
        Buttonjoin.configure(activebackground="#d9d9d9")
        Buttonjoin.configure(activeforeground="#000000")
        Buttonjoin.configure(background="#d9d9d9")
        Buttonjoin.configure(disabledforeground="#a3a3a3")
        Buttonjoin.configure(font=font9)
        Buttonjoin.configure(foreground="#000000")
        Buttonjoin.configure(highlightbackground="#d9d9d9")
        Buttonjoin.configure(highlightcolor="#ff0000")
        Buttonjoin.configure(pady="0")
        Buttonjoin.configure(text='''Join Now>''')
        Buttonjoin.configure(width=267)
        
        Buttonjoin.configure(command=details)
        Buttonjoin = Button(Frame1)
        Buttonjoin.place(relx=0.05, rely=0.77, height=44, width=267)
        Buttonjoin.configure(activebackground="#d9d9d9")
        Buttonjoin.configure(activeforeground="#000000")
        Buttonjoin.configure(background="#d9d9d9")
        Buttonjoin.configure(disabledforeground="#a3a3a3")
        Buttonjoin.configure(font=font9)
        Buttonjoin.configure(foreground="#000000")
        Buttonjoin.configure(highlightbackground="#d9d9d9")
        Buttonjoin.configure(highlightcolor="#ff0000")
        Buttonjoin.configure(pady="0")
        Buttonjoin.configure(text='''SIGN IN>''')
        Buttonjoin.configure(width=267)
        
        
        Buttonjoin.configure(command=logIN)
        
        top.mainloop()



      

def booking():
        top=Tk()
        
       # global operator

        global textInput
        textInput=StringVar() 
        textInput.set(operator)
          
       
        def nosheets():
           global j,k
           k =Entry1.get()
           j=int(k)
           print j,type(j)
           return j
        def bookingt(sheet1):
          global count,p,textInput
          global operator
          
         
          sheet=sheet1
          c[2]=sheet1
          print "c sheats",c[2]
          #print "c is",c
          #print"in csv",c[2]
          csv_out2 = open('cancel.csv', 'ab')
          mywriter1 = csv.writer(csv_out2)
          mywriter1.writerow([c[0],c[1],c[2]])
          csv_out2.close()

          j=nosheets()
          operator=operator +str( sheet1)
          print operator
          textInput.set(operator)
          print textInput
          
          if p>j:
                
                tkMessageBox.showwarning("Booking","U can book only given no of seats") 
          while p<=j:
                bookings=[]
                if sheet > 50:
                    tkMessageBox.showinfo("Booking","INVALID SEAT Number please enter valid sheet")
                elif a[sheet] == 'BK':
                         tkMessageBox.showinfo("Booking","SEAT IS ALREADY BOOKED ,SEE AVAILABLE SHEETS AND BOOK\n")
                         p=p-1
                         break
                  
                else:
                      a[sheet] = 'BK'
                      count = count + 1
                      csv_out = open('mycsv2.csv', 'w+')
                      mywriter = csv.writer(csv_out)
                      rows = zip(a)
                      mywriter.writerows(rows)
                      csv_out.close()
                      bookings.append(sheet)
                      p=p+1
                     # with open("cinema.csv","a") as csfile:
                             #  writer=csv.writer(csfile)
                              # writer.writerow(bookings)
                      break

        
                
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 13 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 19 -weight bold -slant roman"  \
            " -underline 1 -overstrike 0"
       
        top.geometry("600x450+753+130")
        top.title("Booking")
        top.configure(background="#80ffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
         #txtDisplay=Entry(top,font=('arial',20,'bold'),textvariable=textInput,bd=30,insertwidth=4,justify='right')
       # txtDisplay.grid(columnspan=4,pady=300)
        

               



        Message1 = Message(top)
        Message1.place(relx=0.08, rely=0.2, relheight=0.07, relwidth=0.42)
        Message1.configure(background="#80ffff")
        Message1.configure(font=font9)
        Message1.configure(foreground="#004080")
        Message1.configure(highlightbackground="#004080")
        Message1.configure(highlightcolor="#004080")
        Message1.configure(text='''SEATS     CHART''')
        Message1.configure(width=250)

        menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = menubar)
        Label1 = Label(top)
        Label1.place(relx=0.07, rely=0.04, height=29, width=143)
        Label1.configure(activebackground="#f9f9f9")
        Label1.configure(activeforeground="black")
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font10)
        Label1.configure(foreground="#000000")
        Label1.configure(highlightbackground="#d9d9d9")
        Label1.configure(highlightcolor="black")
        Label1.configure(text='''How many seats?''')
        Entry1 = Entry(top)
        Entry1.place(relx=0.33, rely=0.04,height=30, relwidth=0.07)
        Entry1.configure(background="white")
        Entry1.configure(disabledforeground="#a3a3a3")
        Entry1.configure(font="TkFixedFont")
        Entry1.configure(foreground="#000000")
        Entry1.configure(highlightbackground="#d9d9d9")
        Entry1.configure(highlightcolor="black")
        Entry1.configure(insertbackground="black")
        Entry1.configure(selectbackground="#c4c4c4")
        Entry1.configure(selectforeground="black")
        Button0 = Button(top)
        Button0.place(relx=0.42, rely=0.04, height=34, width=57)
        Button0.configure(activebackground="#d9d9d9")
        Button0.configure(activeforeground="#000000")
        Button0.configure(background="#d9d9d9")
        Button0.configure(disabledforeground="#a3a3a3")
        Button0.configure(foreground="#000000")
        Button0.configure(highlightbackground="#d9d9d9")
        Button0.configure(highlightcolor="black")
        Button0.configure(pady="0")
        Button0.configure(text='''CONFIRM''')
        Button0.configure(width=57)
        Button0.configure(command=nosheets)
        Button1 = Button(top)
        Button1.place(relx=0.07, rely=0.27, height=24, width=27)
        Button1.configure(activebackground="#d9d9d9")
        Button1.configure(activeforeground="#000000")
        Button1.configure(background="#d9d9d9")
        Button1.configure(disabledforeground="#a3a3a3")
        Button1.configure(foreground="#000000")
        Button1.configure(highlightbackground="#d9d9d9")
        Button1.configure(highlightcolor="black")
        Button1.configure(pady="0")
        Button1.configure(text=a[0])
        Button1.configure(command=lambda:bookingt(0))

        Button2 = Button(top)
        Button2.place(relx=0.12, rely=0.27, height=24, width=27)
        Button2.configure(activebackground="#d9d9d9")
        Button2.configure(activeforeground="#000000")
        Button2.configure(background="#d9d9d9")
        Button2.configure(disabledforeground="#a3a3a3")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text=a[1])
        Button2.configure(command=lambda:bookingt(1))

        Button3 = Button(top)
        Button3.place(relx=0.17, rely=0.27, height=24, width=27)
        Button3.configure(activebackground="#d9d9d9")
        Button3.configure(activeforeground="#000000")
        Button3.configure(background="#d9d9d9")
        Button3.configure(disabledforeground="#a3a3a3")
        Button3.configure(foreground="#000000")
        Button3.configure(highlightbackground="#d9d9d9")
        Button3.configure(highlightcolor="black")
        Button3.configure(pady="0")
        Button3.configure(text=a[2])
        Button3.configure(command=lambda:bookingt(2))

        Button4 = Button(top)
        Button4.place(relx=0.22, rely=0.27, height=24, width=27)
        Button4.configure(activebackground="#d9d9d9")
        Button4.configure(activeforeground="#000000")
        Button4.configure(background="#d9d9d9")
        Button4.configure(disabledforeground="#a3a3a3")
        Button4.configure(foreground="#000000")
        Button4.configure(highlightbackground="#d9d9d9")
        Button4.configure(highlightcolor="black")
        Button4.configure(pady="0")
        Button4.configure(text=a[3])
        Button4.configure(command=lambda:bookingt(3))

        Button5 = Button(top)
        Button5.place(relx=0.27, rely=0.27, height=24, width=27)
        Button5.configure(activebackground="#d9d9d9")
        Button5.configure(activeforeground="#000000")
        Button5.configure(background="#d9d9d9")
        Button5.configure(disabledforeground="#a3a3a3")
        Button5.configure(foreground="#000000")
        Button5.configure(highlightbackground="#d9d9d9")
        Button5.configure(highlightcolor="black")
        Button5.configure(pady="0")
        Button5.configure(text=a[4])
        Button5.configure(command=lambda:bookingt(4))

        Button6 = Button(top)
        Button6.place(relx=0.32, rely=0.27, height=24, width=27)
        Button6.configure(activebackground="#d9d9d9")
        Button6.configure(activeforeground="#000000")
        Button6.configure(background="#d9d9d9")
        Button6.configure(disabledforeground="#a3a3a3")
        Button6.configure(foreground="#000000")
        Button6.configure(highlightbackground="#d9d9d9")
        Button6.configure(highlightcolor="black")
        Button6.configure(pady="0")
        Button6.configure(text=a[5])
        Button6.configure(command=lambda:bookingt(5))

        Button8 = Button(top)
        Button8.place(relx=0.42, rely=0.27, height=24, width=27)
        Button8.configure(activebackground="#d9d9d9")
        Button8.configure(activeforeground="#000000")
        Button8.configure(background="#d9d9d9")
        Button8.configure(disabledforeground="#a3a3a3")
        Button8.configure(foreground="#000000")
        Button8.configure(highlightbackground="#d9d9d9")
        Button8.configure(highlightcolor="black")
        Button8.configure(pady="0")
        Button8.configure(text=a[7])
        Button8.configure(command=lambda:bookingt(7))

        Button9 = Button(top)
        Button9.place(relx=0.47, rely=0.27, height=24, width=27)
        Button9.configure(activebackground="#d9d9d9")
        Button9.configure(activeforeground="#000000")
        Button9.configure(background="#d9d9d9")
        Button9.configure(disabledforeground="#a3a3a3")
        Button9.configure(foreground="#000000")
        Button9.configure(highlightbackground="#d9d9d9")
        Button9.configure(highlightcolor="black")
        Button9.configure(pady="0")
        Button9.configure(text=a[8])
        Button9.configure(command=lambda:bookingt(8))

        Button10 = Button(top)
        Button10.place(relx=0.52, rely=0.27, height=24, width=23)
        Button10.configure(activebackground="#d9d9d9")
        Button10.configure(activeforeground="#000000")
        Button10.configure(background="#d9d9d9")
        Button10.configure(disabledforeground="#a3a3a3")
        Button10.configure(foreground="#000000")
        Button10.configure(highlightbackground="#d9d9d9")
        Button10.configure(highlightcolor="black")
        Button10.configure(pady="0")
        Button10.configure(text=a[9])
        Button10.configure(command=lambda:bookingt(9))

        Button11 = Button(top)
        Button11.place(relx=0.07, rely=0.33, height=24, width=23)
        Button11.configure(activebackground="#d9d9d9")
        Button11.configure(activeforeground="#000000")
        Button11.configure(background="#d9d9d9")
        Button11.configure(disabledforeground="#a3a3a3")
        Button11.configure(foreground="#000000")
        Button11.configure(highlightbackground="#d9d9d9")
        Button11.configure(highlightcolor="black")
        Button11.configure(pady="0")
        Button11.configure(text=a[10])
        Button11.configure(command=lambda:bookingt(10))

        Button12 = Button(top)
        Button12.place(relx=0.12, rely=0.33, height=24, width=23)
        Button12.configure(activebackground="#d9d9d9")
        Button12.configure(activeforeground="#000000")
        Button12.configure(background="#d9d9d9")
        Button12.configure(disabledforeground="#a3a3a3")
        Button12.configure(foreground="#000000")
        Button12.configure(highlightbackground="#d9d9d9")
        Button12.configure(highlightcolor="black")
        Button12.configure(pady="0")
        Button12.configure(text=a[11])
        Button12.configure(command=lambda:bookingt(11))

        Button13 = Button(top)
        Button13.place(relx=0.17, rely=0.33, height=24, width=23)
        Button13.configure(activebackground="#d9d9d9")
        Button13.configure(activeforeground="#000000")
        Button13.configure(background="#d9d9d9")
        Button13.configure(disabledforeground="#a3a3a3")
        Button13.configure(foreground="#000000")
        Button13.configure(highlightbackground="#d9d9d9")
        Button13.configure(highlightcolor="black")
        Button13.configure(pady="0")
        Button13.configure(text=a[12])
        Button13.configure(command=lambda:bookingt(12))

        Btn14 = Button(top)
        Btn14.place(relx=0.22, rely=0.33, height=24, width=23)
        Btn14.configure(activebackground="#d9d9d9")
        Btn14.configure(activeforeground="#000000")
        Btn14.configure(background="#d9d9d9")
        Btn14.configure(disabledforeground="#a3a3a3")
        Btn14.configure(foreground="#000000")
        Btn14.configure(highlightbackground="#d9d9d9")
        Btn14.configure(highlightcolor="black")
        Btn14.configure(pady="0")
        Btn14.configure(text=a[13])
        Btn14.configure(command=lambda:bookingt(13)) 

        Button16 = Button(top)
        Button16.place(relx=0.32, rely=0.33, height=24, width=23)
        Button16.configure(activebackground="#d9d9d9")
        Button16.configure(activeforeground="#000000")
        Button16.configure(background="#d9d9d9")
        Button16.configure(disabledforeground="#a3a3a3")
        Button16.configure(foreground="#000000")
        Button16.configure(highlightbackground="#d9d9d9")
        Button16.configure(highlightcolor="black")
        Button16.configure(pady="0")
        Button16.configure(text=a[15])
        Button16.configure(command=lambda:bookingt(15))


        Btn18 = Button(top)
        Btn18.place(relx=0.42, rely=0.33, height=24, width=23)
        Btn18.configure(activebackground="#d9d9d9")
        Btn18.configure(activeforeground="#000000")
        Btn18.configure(background="#d9d9d9")
        Btn18.configure(disabledforeground="#a3a3a3")
        Btn18.configure(foreground="#000000")
        Btn18.configure(highlightbackground="#d9d9d9")
        Btn18.configure(highlightcolor="black")
        Btn18.configure(pady="0")
        Btn18.configure(text=a[17])
        Btn18.configure(command=lambda:bookingt(17))


        Btn19 = Button(top)
        Btn19.place(relx=0.47, rely=0.33, height=24, width=23)
        Btn19.configure(activebackground="#d9d9d9")
        Btn19.configure(activeforeground="#000000")
        Btn19.configure(background="#d9d9d9")
        Btn19.configure(disabledforeground="#a3a3a3")
        Btn19.configure(foreground="#000000")
        Btn19.configure(highlightbackground="#d9d9d9")
        Btn19.configure(highlightcolor="black")
        Btn19.configure(pady="0")
        Btn19.configure(text=a[18])
        Btn19.configure(command=lambda:bookingt(18))

        

        Btn20 = Button(top)
        Btn20.place(relx=0.52, rely=0.33, height=24, width=23)
        Btn20.configure(activebackground="#d9d9d9")
        Btn20.configure(activeforeground="#000000")
        Btn20.configure(background="#d9d9d9")
        Btn20.configure(disabledforeground="#a3a3a3")
        Btn20.configure(foreground="#000000")
        Btn20.configure(highlightbackground="#d9d9d9")
        Btn20.configure(highlightcolor="black")
        Btn20.configure(pady="0")
        Btn20.configure(text=a[19])
        Btn20.configure(command=lambda:bookingt(19))

        Btn15 = Button(top)
        Btn15.place(relx=0.27, rely=0.33, height=24, width=23)
        Btn15.configure(activebackground="#d9d9d9")
        Btn15.configure(activeforeground="#000000")
        Btn15.configure(background="#d9d9d9")
        Btn15.configure(disabledforeground="#a3a3a3")
        Btn15.configure(foreground="#000000")
        Btn15.configure(highlightbackground="#d9d9d9")
        Btn15.configure(highlightcolor="black")
        Btn15.configure(pady="0")
        Btn15.configure(text=a[14])
        Btn15.configure(command=lambda:bookingt(14))


        Btn17 = Button(top)
        Btn17.place(relx=0.37, rely=0.33, height=24, width=23)
        Btn17.configure(activebackground="#d9d9d9")
        Btn17.configure(activeforeground="#000000")
        Btn17.configure(background="#d9d9d9")
        Btn17.configure(disabledforeground="#a3a3a3")
        Btn17.configure(foreground="#000000")
        Btn17.configure(highlightbackground="#d9d9d9")
        Btn17.configure(highlightcolor="black")
        Btn17.configure(pady="0")
        Btn17.configure(text=a[16])
        Btn17.configure(command=lambda:bookingt(16))


        btn7 = Button(top)
        btn7.place(relx=0.37, rely=0.27, height=24, width=27)
        btn7.configure(activebackground="#d9d9d9")
        btn7.configure(activeforeground="#000000")
        btn7.configure(background="#d9d9d9")
        btn7.configure(disabledforeground="#a3a3a3")
        btn7.configure(foreground="#000000")
        btn7.configure(highlightbackground="#d9d9d9")
        btn7.configure(highlightcolor="black")
        btn7.configure(pady="0")
        btn7.configure(text=a[6])
        btn7.configure(command=lambda:bookingt(6))


        Btn21 = Button(top)
        Btn21.place(relx=0.07, rely=0.4, height=24, width=27)
        Btn21.configure(activebackground="#d9d9d9")
        Btn21.configure(activeforeground="#000000")
        Btn21.configure(background="#d9d9d9")
        Btn21.configure(disabledforeground="#a3a3a3")
        Btn21.configure(foreground="#000000")
        Btn21.configure(highlightbackground="#d9d9d9")
        Btn21.configure(highlightcolor="black")
        Btn21.configure(pady="0")
        Btn21.configure(text=a[20])
        Btn21.configure(command=lambda:bookingt(20))


        Btn22 = Button(top)
        Btn22.place(relx=0.12, rely=0.4, height=24, width=27)
        Btn22.configure(activebackground="#d9d9d9")
        Btn22.configure(activeforeground="#000000")
        Btn22.configure(background="#d9d9d9")
        Btn22.configure(disabledforeground="#a3a3a3")
        Btn22.configure(foreground="#000000")
        Btn22.configure(highlightbackground="#d9d9d9")
        Btn22.configure(highlightcolor="black")
        Btn22.configure(pady="0")
        Btn22.configure(text=a[21])
        Btn22.configure(command=lambda:bookingt(21))

        Button23 = Button(top)
        Button23.place(relx=0.17, rely=0.4, height=24, width=27)
        Button23.configure(activebackground="#d9d9d9")
        Button23.configure(activeforeground="#000000")
        Button23.configure(background="#d9d9d9")
        Button23.configure(disabledforeground="#a3a3a3")
        Button23.configure(foreground="#000000")
        Button23.configure(highlightbackground="#d9d9d9")
        Button23.configure(highlightcolor="black")
        Button23.configure(pady="0")
        Button23.configure(text=a[22])
        Button23.configure(command=lambda:bookingt(22))

        Button24 = Button(top)
        Button24.place(relx=0.22, rely=0.4, height=24, width=27)
        Button24.configure(activebackground="#d9d9d9")
        Button24.configure(activeforeground="#000000")
        Button24.configure(background="#d9d9d9")
        Button24.configure(disabledforeground="#a3a3a3")
        Button24.configure(foreground="#000000")
        Button24.configure(highlightbackground="#d9d9d9")
        Button24.configure(highlightcolor="black")
        Button24.configure(pady="0")
        Button24.configure(text=a[23])
        Button24.configure(command=lambda:bookingt(23))

        Button25 = Button(top)
        Button25.place(relx=0.27, rely=0.4, height=24, width=27)
        Button25.configure(activebackground="#d9d9d9")
        Button25.configure(activeforeground="#000000")
        Button25.configure(background="#d9d9d9")
        Button25.configure(disabledforeground="#a3a3a3")
        Button25.configure(foreground="#000000")
        Button25.configure(highlightbackground="#d9d9d9")
        Button25.configure(highlightcolor="black")
        Button25.configure(pady="0")
        Button25.configure(text=a[24])
        Button25.configure(command=lambda:bookingt(24))


        Button26 = Button(top)
        Button26.place(relx=0.32, rely=0.4, height=24, width=27)
        Button26.configure(activebackground="#d9d9d9")
        Button26.configure(activeforeground="#000000")
        Button26.configure(background="#d9d9d9")
        Button26.configure(disabledforeground="#a3a3a3")
        Button26.configure(foreground="#000000")
        Button26.configure(highlightbackground="#d9d9d9")
        Button26.configure(highlightcolor="black")
        Button26.configure(pady="0")
        Button26.configure(text=a[25])
        Button26.configure(command=lambda:bookingt(25))

        Button27 = Button(top)
        Button27.place(relx=0.37, rely=0.4, height=24, width=27)
        Button27.configure(activebackground="#d9d9d9")
        Button27.configure(activeforeground="#000000")
        Button27.configure(background="#d9d9d9")
        Button27.configure(disabledforeground="#a3a3a3")
        Button27.configure(foreground="#000000")
        Button27.configure(highlightbackground="#d9d9d9")
        Button27.configure(highlightcolor="black")
        Button27.configure(pady="0")
        Button27.configure(text=a[26])
        Button27.configure(command=lambda:bookingt(26))

        Button28 = Button(top)
        Button28.place(relx=0.42, rely=0.4, height=24, width=27)
        Button28.configure(activebackground="#d9d9d9")
        Button28.configure(activeforeground="#000000")
        Button28.configure(background="#d9d9d9")
        Button28.configure(disabledforeground="#a3a3a3")
        Button28.configure(foreground="#000000")
        Button28.configure(highlightbackground="#d9d9d9")
        Button28.configure(highlightcolor="black")
        Button28.configure(pady="0")
        Button28.configure(text=a[27])
        Button28.configure(command=lambda:bookingt(27))

        Button29 = Button(top)
        Button29.place(relx=0.47, rely=0.4, height=24, width=27)
        Button29.configure(activebackground="#d9d9d9")
        Button29.configure(activeforeground="#000000")
        Button29.configure(background="#d9d9d9")
        Button29.configure(disabledforeground="#a3a3a3")
        Button29.configure(foreground="#000000")
        Button29.configure(highlightbackground="#d9d9d9")
        Button29.configure(highlightcolor="black")
        Button29.configure(pady="0")
        Button29.configure(text=a[28])
        Button29.configure(command=lambda:bookingt(28))

        Button30 = Button(top)
        Button30.place(relx=0.52, rely=0.4, height=24, width=27)
        Button30.configure(activebackground="#d9d9d9")
        Button30.configure(activeforeground="#000000")
        Button30.configure(background="#d9d9d9")
        Button30.configure(disabledforeground="#a3a3a3")
        Button30.configure(foreground="#000000")
        Button30.configure(highlightbackground="#d9d9d9")
        Button30.configure(highlightcolor="black")
        Button30.configure(pady="0")
        Button30.configure(text=a[29])
        Button30.configure(command=lambda:bookingt(29))

        Button31 = Button(top)
        Button31.place(relx=0.07, rely=0.47, height=24, width=27)
        Button31.configure(activebackground="#d9d9d9")
        Button31.configure(activeforeground="#000000")
        Button31.configure(background="#d9d9d9")
        Button31.configure(disabledforeground="#a3a3a3")
        Button31.configure(foreground="#000000")
        Button31.configure(highlightbackground="#d9d9d9")
        Button31.configure(highlightcolor="black")
        Button31.configure(pady="0")
        Button31.configure(text=a[30])
        Button31.configure(command=lambda:bookingt(30))

        Button32 = Button(top)
        Button32.place(relx=0.12, rely=0.47, height=24, width=27)
        Button32.configure(activebackground="#d9d9d9")
        Button32.configure(activeforeground="#000000")
        Button32.configure(background="#d9d9d9")
        Button32.configure(disabledforeground="#a3a3a3")
        Button32.configure(foreground="#000000")
        Button32.configure(highlightbackground="#d9d9d9")
        Button32.configure(highlightcolor="black")
        Button32.configure(pady="0")
        Button32.configure(text=a[31])
        Button32.configure(command=lambda:bookingt(31))

        Button33 = Button(top)
        Button33.place(relx=0.17, rely=0.47, height=24, width=27)
        Button33.configure(activebackground="#d9d9d9")
        Button33.configure(activeforeground="#000000")
        Button33.configure(background="#d9d9d9")
        Button33.configure(disabledforeground="#a3a3a3")
        Button33.configure(foreground="#000000")
        Button33.configure(highlightbackground="#d9d9d9")
        Button33.configure(highlightcolor="black")
        Button33.configure(pady="0")
        Button33.configure(text=a[32])
        Button33.configure(command=lambda:bookingt(32))

        Button34 = Button(top)
        Button34.place(relx=0.22, rely=0.47, height=24, width=27)
        Button34.configure(activebackground="#d9d9d9")
        Button34.configure(activeforeground="#000000")
        Button34.configure(background="#d9d9d9")
        Button34.configure(disabledforeground="#a3a3a3")
        Button34.configure(foreground="#000000")
        Button34.configure(highlightbackground="#d9d9d9")
        Button34.configure(highlightcolor="black")
        Button34.configure(pady="0")
        Button34.configure(text=a[33])
        Button34.configure(command=lambda:bookingt(33))

        Button35 = Button(top)
        Button35.place(relx=0.27, rely=0.47, height=24, width=27)
        Button35.configure(activebackground="#d9d9d9")
        Button35.configure(activeforeground="#000000")
        Button35.configure(background="#d9d9d9")
        Button35.configure(disabledforeground="#a3a3a3")
        Button35.configure(foreground="#000000")
        Button35.configure(highlightbackground="#d9d9d9")
        Button35.configure(highlightcolor="black")
        Button35.configure(pady="0")
        Button35.configure(text=a[34])
        Button35.configure(command=lambda:bookingt(34))

        Button36 = Button(top)
        Button36.place(relx=0.32, rely=0.47, height=24, width=27)
        Button36.configure(activebackground="#d9d9d9")
        Button36.configure(activeforeground="#000000")
        Button36.configure(background="#d9d9d9")
        Button36.configure(disabledforeground="#a3a3a3")
        Button36.configure(foreground="#000000")
        Button36.configure(highlightbackground="#d9d9d9")
        Button36.configure(highlightcolor="black")
        Button36.configure(pady="0")
        Button36.configure(text=a[35])
        Button36.configure(command=lambda:bookingt(35))

        Button37 = Button(top)
        Button37.place(relx=0.37, rely=0.47, height=24, width=27)
        Button37.configure(activebackground="#d9d9d9")
        Button37.configure(activeforeground="#000000")
        Button37.configure(background="#d9d9d9")
        Button37.configure(disabledforeground="#a3a3a3")
        Button37.configure(foreground="#000000")
        Button37.configure(highlightbackground="#d9d9d9")
        Button37.configure(highlightcolor="black")
        Button37.configure(pady="0")
        Button37.configure(text=a[36])
        Button37.configure(command=lambda:bookingt(36))

        Button38 = Button(top)
        Button38.place(relx=0.42, rely=0.47, height=24, width=27)
        Button38.configure(activebackground="#d9d9d9")
        Button38.configure(activeforeground="#000000")
        Button38.configure(background="#d9d9d9")
        Button38.configure(disabledforeground="#a3a3a3")
        Button38.configure(foreground="#000000")
        Button38.configure(highlightbackground="#d9d9d9")
        Button38.configure(highlightcolor="black")
        Button38.configure(pady="0")
        Button38.configure(text=a[37])
        Button38.configure(command=lambda:bookingt(37))

        Button39 = Button(top)
        Button39.place(relx=0.47, rely=0.47, height=24, width=27)
        Button39.configure(activebackground="#d9d9d9")
        Button39.configure(activeforeground="#000000")
        Button39.configure(background="#d9d9d9")
        Button39.configure(disabledforeground="#a3a3a3")
        Button39.configure(foreground="#000000")
        Button39.configure(highlightbackground="#d9d9d9")
        Button39.configure(highlightcolor="black")
        Button39.configure(pady="0")
        Button39.configure(text=a[38])
        Button39.configure(command=lambda:bookingt(38))

        Button40 = Button(top)
        Button40.place(relx=0.52, rely=0.47, height=24, width=27)
        Button40.configure(activebackground="#d9d9d9")
        Button40.configure(activeforeground="#000000")
        Button40.configure(background="#d9d9d9")
        Button40.configure(disabledforeground="#a3a3a3")
        Button40.configure(foreground="#000000")
        Button40.configure(highlightbackground="#d9d9d9")
        Button40.configure(highlightcolor="black")
        Button40.configure(pady="0")
        Button40.configure(text=a[39])
        Button40.configure(command=lambda:bookingt(39))

        Button41 = Button(top)
        Button41.place(relx=0.07, rely=0.53, height=24, width=27)
        Button41.configure(activebackground="#d9d9d9")
        Button41.configure(activeforeground="#000000")
        Button41.configure(background="#d9d9d9")
        Button41.configure(disabledforeground="#a3a3a3")
        Button41.configure(foreground="#000000")
        Button41.configure(highlightbackground="#d9d9d9")
        Button41.configure(highlightcolor="black")
        Button41.configure(pady="0")
        Button41.configure(text=a[40])
        Button41.configure(command=lambda:bookingt(40))

        Button42 = Button(top)
        Button42.place(relx=0.12, rely=0.53, height=24, width=27)
        Button42.configure(activebackground="#d9d9d9")
        Button42.configure(activeforeground="#000000")
        Button42.configure(background="#d9d9d9")
        Button42.configure(disabledforeground="#a3a3a3")
        Button42.configure(foreground="#000000")
        Button42.configure(highlightbackground="#d9d9d9")
        Button42.configure(highlightcolor="black")
        Button42.configure(pady="0")
        Button42.configure(text=a[41])
        Button42.configure(command=lambda:bookingt(41))

        Button43 = Button(top)
        Button43.place(relx=0.17, rely=0.53, height=24, width=27)
        Button43.configure(activebackground="#d9d9d9")
        Button43.configure(activeforeground="#000000")
        Button43.configure(background="#d9d9d9")
        Button43.configure(disabledforeground="#a3a3a3")
        Button43.configure(foreground="#000000")
        Button43.configure(highlightbackground="#d9d9d9")
        Button43.configure(highlightcolor="black")
        Button43.configure(pady="0")
        Button43.configure(text=a[42])
        Button43.configure(command=lambda:bookingt(42))

        Button44 = Button(top)
        Button44.place(relx=0.22, rely=0.53, height=24, width=27)
        Button44.configure(activebackground="#d9d9d9")
        Button44.configure(activeforeground="#000000")
        Button44.configure(background="#d9d9d9")
        Button44.configure(disabledforeground="#a3a3a3")
        Button44.configure(foreground="#000000")
        Button44.configure(highlightbackground="#d9d9d9")
        Button44.configure(highlightcolor="black")
        Button44.configure(pady="0")
        Button44.configure(text=a[43])
        Button44.configure(command=lambda:bookingt(43));

        Button45 = Button(top)
        Button45.place(relx=0.27, rely=0.53, height=24, width=27)
        Button45.configure(activebackground="#d9d9d9")
        Button45.configure(activeforeground="#000000")
        Button45.configure(background="#d9d9d9")
        Button45.configure(disabledforeground="#a3a3a3")
        Button45.configure(foreground="#000000")
        Button45.configure(highlightbackground="#d9d9d9")
        Button45.configure(highlightcolor="black")
        Button45.configure(pady="0")
        Button45.configure(text=a[44])
        Button45.configure(command=lambda:bookingt(44));


        Button46 = Button(top)
        Button46.place(relx=0.32, rely=0.53, height=24, width=27)
        Button46.configure(activebackground="#d9d9d9")
        Button46.configure(activeforeground="#000000")
        Button46.configure(background="#d9d9d9")
        Button46.configure(disabledforeground="#a3a3a3")
        Button46.configure(foreground="#000000")
        Button46.configure(highlightbackground="#d9d9d9")
        Button46.configure(highlightcolor="black")
        Button46.configure(pady="0")
        Button46.configure(text=a[45])
        Button46.configure(command=lambda:bookingt(45))


        Button47 = Button(top)
        Button47.place(relx=0.37, rely=0.53, height=24, width=27)
        Button47.configure(activebackground="#d9d9d9")
        Button47.configure(activeforeground="#000000")
        Button47.configure(background="#d9d9d9")
        Button47.configure(disabledforeground="#a3a3a3")
        Button47.configure(foreground="#000000")
        Button47.configure(highlightbackground="#d9d9d9")
        Button47.configure(highlightcolor="black")
        Button47.configure(pady="0")
        Button47.configure(text=a[46])
        Button47.configure(command=lambda:bookingt(46))


        Button48 = Button(top)
        Button48.place(relx=0.42, rely=0.53, height=24, width=27)
        Button48.configure(activebackground="#d9d9d9")
        Button48.configure(activeforeground="#000000")
        Button48.configure(background="#d9d9d9")
        Button48.configure(disabledforeground="#a3a3a3")
        Button48.configure(foreground="#000000")
        Button48.configure(highlightbackground="#d9d9d9")
        Button48.configure(highlightcolor="black")
        Button48.configure(pady="0")
        Button48.configure(text=a[47])
        Button48.configure(command=lambda:bookingt(47))


        Button49 = Button(top)
        Button49.place(relx=0.47, rely=0.53, height=24, width=27)
        Button49.configure(activebackground="#d9d9d9")
        Button49.configure(activeforeground="#000000")
        Button49.configure(background="#d9d9d9")
        Button49.configure(disabledforeground="#a3a3a3")
        Button49.configure(foreground="#000000")
        Button49.configure(highlightbackground="#d9d9d9")
        Button49.configure(highlightcolor="black")
        Button49.configure(pady="0")
        Button49.configure(text=a[48])
        Button49.configure(command=lambda:bookingt(48))
 

        Button50 = Button(top)
        Button50.place(relx=0.52, rely=0.53, height=24, width=27)
        Button50.configure(activebackground="#d9d9d9")
        Button50.configure(activeforeground="#000000")
        Button50.configure(background="#d9d9d9")
        Button50.configure(disabledforeground="#a3a3a3")
        Button50.configure(foreground="#000000")
        Button50.configure(highlightbackground="#d9d9d9")
        Button50.configure(highlightcolor="black")
        Button50.configure(pady="0")
        Button50.configure(text=a[49])
        Button50.configure(command=lambda:bookingt(49))
        txtDisplay=Entry(top,font=('arial',20,'bold'),textvariable=textInput,bd=30,insertwidth=4,justify='right')
        txtDisplay.grid(columnspan=4,pady=300)
        

        
        
        top.mainloop()
        

mainwindow()
#booking()
#logIN()




