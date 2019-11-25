from Tkinter import *
import tkMessageBox

startw=Tk()
startw.title("TilHandA")
startw.wm_iconbitmap('hashtag.ico')
startw.geometry("450x200")
Label(startw,text='Project Title: Phonebook',font='Arial 20',fg='black').grid(row=0,column=1)
Label(startw,text='Project of Python and Database',font='Arial 20',fg='black').grid(row=1,column=1)
Label(startw,text='Developed by - Ankit Raj(181B039)',font='Arial 20',fg='blue').grid(row=2,column=1)
Label(startw,text='-------------------------------',font='Arial 20',fg='black').grid(row=3,column=1)
Label(startw,text='Make a mouse move on the screen!',font='Arial 20',fg='red').grid(row=4,column=1)

def openmain(e=1):
    startw.destroy()
    root=Tk()
    root.title("TilHandA")
    root.wm_iconbitmap('hashtag.ico')
    root.geometry("600x650")
    img=PhotoImage(file='phonebook.gif')
    Label(root,image=img).grid(row=0,column=1)
    Label(root,text='Phonebook',font='Arial 20',fg='blue').grid(row=1,column=1)
    Label(root,text='First Name:             ').grid(row=2,column=0)
    fname=Entry(root)
    fname.grid(row=2,column=1)
    Label(root,text='Middle Name:        ').grid(row=3,column=0)
    mname=Entry(root)
    mname.grid(row=3,column=1)
    Label(root,text='Last Name:            ').grid(row=4,column=0)
    lname=Entry(root)
    lname.grid(row=4,column=1)
    Label(root,text='Company Name:  ').grid(row=5,column=0)
    cname=Entry(root)
    cname.grid(row=5,column=1)
    Label(root,text='Address:                ').grid(row=6,column=0)
    add=Entry(root)
    add.grid(row=6,column=1)
    Label(root,text='City:                       ').grid(row=7,column=0)
    city=Entry(root)
    city.grid(row=7,column=1)
    Label(root,text='Pincode:                ').grid(row=8,column=0)
    pincode=Entry(root)
    pincode.grid(row=8,column=1)
    Label(root,text='Website Url:          ').grid(row=9,column=0)
    url=Entry(root)
    url.grid(row=9,column=1)
    Label(root,text='Birthdate:              ').grid(row=10,column=0)
    bdate=Entry(root)
    bdate.grid(row=10,column=1)
    Label(root,text='Select Phone Type: ',font='Arial 15',fg='blue').grid(row=11,column=0)
    ptype=IntVar()
    p1=Radiobutton(root,text='Office',variable=ptype,value=1).grid(row=11,column=1)
    p2=Radiobutton(root,text='Home    ',variable=ptype,value=2).grid(sticky="W",row=11,column=2)
    p3=Radiobutton(root,text='Mobile',variable=ptype,value=3).grid(sticky="W",row=11,column=3)
    Label(root,text='Phone Number:     ').grid(row=12,column=0)
    phone=Entry(root)
    phone.grid(row=12,column=1)
    Label(root,text='Select Email Type: ',font='Arial 15',fg='blue').grid(row=13,column=0)
    etype=IntVar()
    e1=Radiobutton(root,text='Office',variable=etype,value=1).grid(row=13,column=1)
    e2=Radiobutton(root,text='Personal',variable=etype,value=2).grid(sticky="W",row=13,column=2)
    Label(root,text='Email Id:                 ').grid(row=14,column=0)
    email=Entry(root)
    email.grid(row=14,column=1)
    def insertinfo():
       tkMessageBox.showinfo("Inserted","Congrats! you have instested a plate into stack :)")
       #getting user data
       ifname=fname.get()
       imname=mname.get()
       ilname=lname.get()
       icname=cname.get()
       iadd=add.get()
       icity=city.get()
       ipincode=pincode.get()
       iurl=url.get()
       ibdate=bdate.get()
       iptype=ptype.get()
       iphone=phone.get()
       ietype=etype.get()
       iemail=email.get()
       #checking empty feild
       if ifname=='':
          ifname=' '
       if imname=='':
          imname=' '
       if ilname=='':
          ilname=' '
       if icname=='':
          icname=' '
       if iadd=='':
          iadd=' '
       if icity=='':
          icity=' '
       if ipincode=='':
          ipincode=' '
       if iurl=='':
          iurl=' '
       if ibdate=='':
          ibdate=' '
       if iptype==1:
          iptype='Office'
       elif iptype==2:
          iptype='Home'
       elif iptype==3:
          iptype='Mobile'
       else:
          iptype=' '
       if iphone=='':
          iphone=' '
       if ietype==1:
          ietype='Office'
       elif ietype==2:
          ietype='Personal'
       else:
          ietype=' '
       if iemail=='':
          iemail=' '
       #database corner
       import sqlite3
       con=sqlite3.Connection('phonebooknew')
       cur=con.cursor()
       cur1=con.cursor()
       cur.execute('create table if not exists user(cid integer primary key AUTOINCREMENT,fname varchar(20),mname varchar(20),lname varchar(20),company varchar(20),addr varchar(40),city varchar(15),pin number(6),url fname varchar(30),bdate varchar(10),phonetype varchar(10),pno varchar(10),emailtype varchar(10),email varchar(40))')
       insertuser=[(ifname,imname,ilname,icname,iadd,icity,ipincode,iurl,ibdate,iptype,iphone,ietype,iemail)]
       cur.execute('insert into user(fname,mname,lname,company,addr,city,pin,url,bdate,phonetype,pno,emailtype,email) values(?,?,?,?,?,?,?,?,?,?,?,?,?)',insertuser[0])
       cur.execute('select * from user')
       fetchuser=cur.fetchall()
       con.commit()
       con.close()
       #delete as they enter once
       fname.delete(0,END)
       mname.delete(0,END)
       lname.delete(0,END)
       cname.delete(0,END)
       add.delete(0,END)
       city.delete(0,END)
       pincode.delete(0,END)
       url.delete(0,END)
       phone.delete(0,END)
       email.delete(0,END)
       bdate.delete(0,END)
    Label(root,text=' ').grid(row=15,column=0)
    Button(root,text='Insert',command=insertinfo).grid(row=16,column=0)
    Button(root,text='Show User',command=tempshow).grid(row=16,column=1)
    Button(root,text='Close',command=close).grid(sticky="W",row=16,column=2)
    root.mainloop()


def tempshow():
    root2=Tk()
    root2.title("TilHandA")
    root2.wm_iconbitmap('hashtag.ico')
    root2.geometry("600x670")
    Label(root2,text='Search Section',font='Arial 20',fg='blue').grid(row=0,column=0)
    Label(root2,text='Enter Name to search- ').grid(row=1,column=0)
    search=Entry(root2)
    search.grid(row=2,column=0)
    lb2=Listbox(root2,height='30',width='100').grid(row=4,column=0)
    def shown(e=1):
        new=search.get()
        a=[1]
        b=[1]
        a[0]=['%'+str(new)+'%']
        import sqlite3
        con=sqlite3.Connection('phonebooknew')
        cur=con.cursor()
        c=[(new)]
        b[0]=a[0]*13
        cur.execute("select * from user where fname like ? or mname like ? or lname like ? or company like ? or addr like ? or city like ? or pin like ? or url like ? or bdate like ? or phonetype like ? or pno like ? or emailtype like ? or email like ? order by fname",b[0])
        list1=cur.fetchall()
        lb1=Listbox(root2,height='22',width='55',font='Arial 15',fg='blue')
        lb2=Listbox(root2,height='22',width='55',font='Arial 15',fg='black')
        if list1==[]:
            text="Sorry no record found!"
            lb1.insert(1,text)
            lb1.grid(row=4,column=0)
            lb1.delete(0,END)
        else:
           def callfun(evt):
              var=lb1.curselection()
              newvar=int(var[0])
              getid=(list1[newvar][0])
              import sqlite3
              con=sqlite3.Connection('phonebooknew')
              cur=con.cursor()
              def editinfo():
                    import sqlite3
                    con=sqlite3.Connection('phonebooknew')
                    cur=con.cursor()
                    cur.execute("select * from user where cid = {0}".format(getid))
                    list4=cur.fetchall()
                    con.close()
                    root3=Tk()
                    root3.title("TilHandA")
                    root3.wm_iconbitmap('hashtag.ico')
                    root3.geometry("520x380")
                    Label(root3,text='Edit Section',font='Arial 20',fg='blue').grid(row=1,column=1)
                    Label(root3,text='First Name:             ').grid(row=2,column=0)
                    efname=Entry(root3)
                    efname.insert(0,str(list4[0][1]))
                    efname.grid(row=2,column=1)
                    Label(root3,text='Middle Name:        ').grid(row=3,column=0)
                    emname=Entry(root3)
                    emname.insert(0,str(list4[0][2]))
                    emname.grid(row=3,column=1)
                    Label(root3,text='Last Name:            ').grid(row=4,column=0)
                    elname=Entry(root3)
                    elname.insert(0,str(list4[0][3]))
                    elname.grid(row=4,column=1)
                    Label(root3,text='Company Name:  ').grid(row=5,column=0)
                    ecname=Entry(root3)
                    ecname.insert(0,str(list4[0][4]))
                    ecname.grid(row=5,column=1)
                    Label(root3,text='Address:                ').grid(row=6,column=0)
                    eadd=Entry(root3)
                    eadd.insert(0,str(list4[0][5]))
                    eadd.grid(row=6,column=1)
                    Label(root3,text='City:                       ').grid(row=7,column=0)
                    ecity=Entry(root3)
                    ecity.insert(0,str(list4[0][6]))
                    ecity.grid(row=7,column=1)
                    Label(root3,text='Pincode:                ').grid(row=8,column=0)
                    epincode=Entry(root3)
                    epincode.insert(0,str(list4[0][7]))
                    epincode.grid(row=8,column=1)
                    Label(root3,text='Website Url:          ').grid(row=9,column=0)
                    eurl=Entry(root3)
                    eurl.insert(0,str(list4[0][8]))
                    eurl.grid(row=9,column=1)
                    Label(root3,text='Birthdate:              ').grid(row=10,column=0)
                    ebdate=Entry(root3)
                    ebdate.insert(0,str(list4[0][9]))
                    ebdate.grid(row=10,column=1)
                    Label(root3,text='Select Phone Type: ',font='Arial 15',fg='blue').grid(row=11,column=0)
                    eptype=IntVar()
                    p1=Radiobutton(root3,text='Office',variable=eptype,value=1).grid(row=11,column=1)
                    p2=Radiobutton(root3,text='Home    ',variable=eptype,value=2).grid(sticky="W",row=11,column=2)
                    p3=Radiobutton(root3,text='Mobile',variable=eptype,value=3).grid(sticky="W",row=11,column=3)
                    Label(root3,text='Phone Number:     ').grid(row=12,column=0)
                    ephone=Entry(root3)
                    ephone.insert(0,str(list4[0][11]))
                    ephone.grid(row=12,column=1)
                    Label(root3,text='Select Email Type: ',font='Arial 15',fg='blue').grid(row=13,column=0)
                    eetype=IntVar()
                    e1=Radiobutton(root3,text='Office',variable=eetype,value=1).grid(row=13,column=1)
                    e2=Radiobutton(root3,text='Personal',variable=eetype,value=2).grid(sticky="W",row=13,column=2)
                    Label(root3,text='Email Id:                 ').grid(row=14,column=0)
                    eemail=Entry(root3)
                    eemail.insert(0,str(list4[0][13]))
                    eemail.grid(row=14,column=1)
                    def insertinfo():
                       tkMessageBox.showinfo("Updated","Congrats! you have updated the stack :)")
                       #getting user data
                       eifname=efname.get()
                       eimname=emname.get()
                       eilname=elname.get()
                       eicname=ecname.get()
                       eiadd=eadd.get()
                       eicity=ecity.get()
                       eipincode=epincode.get()
                       eiurl=eurl.get()
                       eibdate=ebdate.get()
                       eiptype=eptype.get()
                       eiphone=ephone.get()
                       eietype=eetype.get()
                       eiemail=eemail.get()
                       #checking empty feild
                       if eifname=='':
                           eifname=' '
                       if eimname=='':
                           eimname=' '
                       if eilname=='':
                           eilname=' '
                       if eicname=='':
                           eicname=' '
                       if eiadd=='':
                           eiadd=' '
                       if eicity=='':
                           eicity=' '
                       if eipincode=='':
                           eipincode=' '
                       if eiurl=='':
                           eiurl=' '
                       if eibdate=='':
                           eibdate=' '
                       if eiptype==1:
                           eiptype='Office'
                       elif eiptype==2:
                           eiptype='Home'
                       elif eiptype==3:
                           eiptype='Mobile'
                       else:
                           eiptype=' '
                       if eiphone=='':
                           eiphone=' '
                       if eietype==1:
                           eietype='Office'
                       elif eietype==2:
                           eietype='Personal'
                       else:
                           eietype=' '
                       if eiemail=='':
                           eiemail=' '
                       #database corner
                       import sqlite3
                       con=sqlite3.Connection('phonebooknew')
                       cur=con.cursor()
                       cur1=con.cursor()
                       insertuser=[(eifname,eimname,eilname,eicname,eiadd,eicity,eipincode,eiurl,eibdate,eiptype,eiphone,eietype,eiemail,getid)]
                       cur.execute('update user set fname=?,mname=?,lname=?,company=?,addr=?,city=?,pin=?,url=?,bdate=?,phonetype=?,pno=?,emailtype=?,email=? where cid =?',insertuser[0])
                       cur.execute('select * from user')
                       fetchuser=cur.fetchall()
                       con.commit()
                       con.close()
                       #delete as they enter once
                       efname.delete(0,END)
                       emname.delete(0,END)
                       elname.delete(0,END)
                       ecname.delete(0,END)
                       eadd.delete(0,END)
                       ecity.delete(0,END)
                       epincode.delete(0,END)
                       eurl.delete(0,END)
                       ephone.delete(0,END)
                       eemail.delete(0,END)
                       ebdate.delete(0,END)
                    Button(root3,text='Insert',command=insertinfo).grid(row=16,column=1)
                    Label(root3,text=' ').grid(row=15,column=0)
                    root3.mainloop()
    
              def delt():
                 import sqlite3
                 con=sqlite3.Connection('phonebooknew')
                 cur=con.cursor()
                 cur.execute("delete from user where cid = {0}".format(getid))
                 tkMessageBox.showinfo("Deleted","Woosh! the data has been vanished :(")
                 cur.execute("select * from user")
                 con.commit()
                 con.close()
              cur.execute("select * from user where cid = {0}".format(getid))
              list3=cur.fetchall()
              text0="First name:  "+str(list3[0][1])+"\n\n"
              text1="Middle name:  "+str(list3[0][2])+"\n\n"
              text2="Last name:  "+str(list3[0][3])+"\n\n"
              text3="Company name:  "+str(list3[0][4])+"\n\n"
              text4="Address:  "+str(list3[0][5])+"\n\n"
              text5="City:  "+str(list3[0][6])+"\n\n"
              text6="Pincode:  "+str(list3[0][7])+"\n\n"
              text7="Website url:  "+str(list3[0][8])+"\n\n"
              text8="Birthdate:  "+str(list3[0][9])+"\n\n"
              text9="Phone Type:  "+str(list3[0][10])+"\n\n"
              text10="Phone Number:  "+str(list3[0][11])+"\n\n"
              text11="Email type:  "+str(list3[0][12])+"\n\n"
              text12="Email:  "+str(list3[0][13])+"\n\n"
              lb2.insert(1,text0)
              lb2.insert(2,text1)
              lb2.insert(3,text2)
              lb2.insert(4,text3)
              lb2.insert(5,text4)
              lb2.insert(6,text5)
              lb2.insert(7,text6)
              lb2.insert(8,text7)
              lb2.insert(9,text8)
              lb2.insert(10,text9)
              lb2.insert(11,text10)
              lb2.insert(12,text11)
              lb2.insert(13,text12)
              lb2.grid(row=4,column=0)
              Button(root2,text='Delete',command=delt).grid(row=5,column=0)        
              Button(root2,text='Edit',command=editinfo).grid(row=6,column=0)
              con.close()
           for i in list1:
                 text0=str(i[1])+"\n\n"
                 text1=str(i[2])+"\n\n"
                 text2=str(i[3])+"\n\n"
                 lb1.insert(END,text0+" "+text1+" "+text2)
                 lb1.bind('<<ListboxSelect>>',callfun)
                 lb1.grid(row=4,column=0)
        con.close()
    root2.bind('<Key>',shown)
    root2.mainloop()



def close(e=1):
   root.destroy()

startw.bind('<Motion>',openmain)
startw.mainloop()
