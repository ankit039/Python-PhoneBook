from Tkinter import *
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
       ifname='N/A'
    if imname=='':
       imname='N/A'
    if ilname=='':
       ilname='N/A'
    if icname=='':
       icname='N/A'
    if iadd=='':
       iadd='N/A'
    if icity=='':
       icity='N/A'
    if ipincode=='':
       ipincode='N/A'
    if iurl=='':
       iurl='N/A'
    if ibdate=='':
       ibdate='N/A'
    if iptype==1:
       iptype='Office'
    elif iptype==2:
       iptype='Home'
    elif iptype==3:
       iptype='Mobile'
    else:
       iptype='N/A'
    if iphone=='':
       iphone='N/A'
    if ietype==1:
       ietype='Office'
    elif ietype==2:
       ietype='Personal'
    else:
       ietype='N/A'
    if iemail=='':
       iemail='N/A'
    #print ifname,imname,ilname,icname,iadd,icity,ipincode,iurl,ibdate,iptype,iphone,ietype,iemail
    #database corner
    import sqlite3
    con=sqlite3.Connection('phonebook')
    cur=con.cursor()
    cur1=con.cursor()
    cur1.execute('select max(cid) from user')
    maxcid=[i[0] for i in cur1.fetchall()]
    newcid=(maxcid[0])+1
    print newcid
    cur.execute('create table if not exists user_ph(cid integer,phonetype varchar(10),pno varchar(10),primary key(cid,pno))')
    cur.execute('create table if not exists user_email(cid integer,emailtype varchar(10),email varchar(40),primary key(cid,email))')
    cur.execute('create table if not exists user(cid integer primary key AUTOINCREMENT,fname varchar(20),mname varchar(20),lname varchar(20),company varchar(20),addr varchar(40),city varchar(15),pin number(6),url fname varchar(30),bdate varchar(10),CONSTRAINT fk1 foreign key (cid) references user_ph(cid),CONSTRAINT fk2 foreign key (cid) references user_email(cid))')
    #cur.execute('alter table user add constraints fk1 foreign key(cid) references user_ph(cid)')
    #cur.execute('alter table user add constraint fk2 foreign key(cid) references user_email(cid)')
    insertuser_ph=[(newcid,iptype,iphone)]
    insertuser_email=[(newcid,ietype,iemail)]
    insertuser=[(ifname,imname,ilname,icname,iadd,icity,ipincode,iurl,ibdate)]
    cur.execute('insert into user_ph(cid,phonetype,pno) values(?,?,?)',insertuser_ph[0])
    cur.execute('insert into user_email(cid,emailtype,email) values(?,?,?)',insertuser_email[0])
    cur.execute('insert into user(fname,mname,lname,company,addr,city,pin,url,bdate) values(?,?,?,?,?,?,?,?,?)',insertuser[0])
    print "\n"
    print "The Data after entry is: "
    cur.execute('select phonetype,pno from user_ph')
    fetchuserphone=cur.fetchall()
    print fetchuserphone
    cur.execute('select * from user_email')
    fetchuseremail=cur.fetchall()
    print fetchuseremail
    cur.execute('select * from user')
    fetchuser=cur.fetchall()
    print fetchuser
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
'''
        cur4.execute("select cid from user where fname like '%?%'",searchname[0])
        cur1.execute('select * from user_ph where cid=?',cur4.fetchall())
        cur2.execute('select * from user_email where cid=?',cur4.fetchall())
        cur3.execute("select * from user where fname like '%?%'",searchname[0])

        print cur1.fetchall()
        print cur2.fetchall()
        print cur3.fetchall()

'''
def show():
    root2=Tk()
    root2.title("TilHandA")
    root2.wm_iconbitmap('hashtag.ico')
    root2.geometry("600x650")
    Label(root2,text='Search Section',font='Arial 20',fg='blue').grid(sticky="W",row=0,column=0)
    Label(root2,text='Enter Name to search- ').grid(sticky="W",row=1,column=0)
    search=Entry(root2)
    search.grid(sticky="W",row=2,column=0)
    lb2=Listbox(root2,height='36',width='100').grid(row=4,column=0)
    def shown():
        new=search.get()
        import sqlite3
        con=sqlite3.Connection('phonebook')
        cur=con.cursor()
        c=[(new)]
        cur.execute("select fname,mname,lname,company,addr,city,pin,url,bdate from user where cid=?",c[0])
        list1=cur.fetchall()
        cur.execute("select phonetype,pno from user_ph where cid=?",c[0])
        list2=cur.fetchall()
        cur.execute("select emailtype,email from user_email where cid=?",c[0])
        list3=cur.fetchall()
        lb1=Listbox(root2,height='36',width='100',font='Arial 15')
        if list1==[]:
            text="Sorry no record found!"
            lb1.insert(1,text)
            lb1.grid(row=4,column=0)
        else:
            text0="First name:  "+str(list1[0][0])+"\n\n"
            text1="Middle name:  "+str(list1[0][1])+"\n\n"
            text2="Last name:  "+str(list1[0][2])+"\n\n"
            text3="Company name:  "+str(list1[0][3])+"\n\n"
            text4="Address:  "+str(list1[0][4])+"\n\n"
            text5="City:  "+str(list1[0][5])+"\n\n"
            text6="Pincode:  "+str(list1[0][6])+"\n\n"
            text7="Website url:  "+str(list1[0][7])+"\n\n"
            text8="Birthdate:  "+str(list1[0][8])+"\n\n"
            text9="Phone Type:  "+str(list2[0][0])+"\n\n"
            text10="Phone Number:  "+str(list2[0][1])+"\n\n"
            text11="Email type:  "+str(list3[0][0])+"\n\n"
            text12="Birthdate:  "+str(list3[0][1])+"\n\n"
            lb1.insert(1,text0)
            lb1.insert(2,text1)
            lb1.insert(3,text2)
            lb1.insert(4,text3)
            lb1.insert(5,text4)
            lb1.insert(6,text5)
            lb1.insert(7,text6)
            lb1.insert(8,text7)
            lb1.insert(9,text8)
            lb1.insert(10,text9)
            lb1.insert(11,text10)
            lb1.insert(12,text11)
            lb1.insert(13,text12)
            lb1.grid(row=4,column=0)
        con.close()
    Button(root2,text='Show',command=shown).grid(sticky="W",row=3,column=0)

def editinfo():
     print "no"

def close(e=1):
     root.destroy()

Button(root,text='Insert',command=insertinfo).grid(row=16,column=0)
Button(root,text='Show User',command=show).grid(row=16,column=1)
Button(root,text='Close',command=close).grid(sticky="W",row=16,column=2)
Button(root,text='Edit',command=editinfo).grid(sticky="W",row=16,column=3)

root.mainloop()
