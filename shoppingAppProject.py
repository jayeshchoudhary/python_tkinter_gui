from Tkinter import *
from PIL import ImageTk, Image
import os
import MySQLdb

global items
items = ['iphone X', 'Casio Watch', 'Sony Headpone', 'Laptop Bag']

def mainPage():
    global appm
    appm = Tk()
    appm.title("Shopping App")
    w=850
    h=550
    ws = appm.winfo_screenwidth()
    hs = appm.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appm.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # appm.geometry('850x550')
    # appm['bg'] = '#97e5db'

    welcomeLabel = Label(appm, text='Welcome To \n Shopping Cart App', font='Times 36 bold')
    welcomeLabel.pack(pady=(80,50))

    loginButton = Button(appm, text="Login", command=login, width=14, font="Times 16")
    loginButton.pack(pady=10)

    registerButton = Button(appm, text="Register", command=register, width=14, font="Times 16")
    registerButton.pack(pady=10)

    appm.mainloop()

def login():
    try:
        appr.destroy()
    except:
        appm.destroy()
    
    global appl
    appl = Tk()
    w=850
    h=550
    ws = appl.winfo_screenwidth()
    hs = appl.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appl.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # appl.geometry('850x550')
    appl.title("Login")

    loginPg = Label(appl, text="Login Page", font="Times 32 bold")
    loginPg.pack(pady=(100,60))

    info = Frame(height=150, width=300)
    info.pack()

    usernameLabel = Label(info, text="Username  : ", font="Times 15")
    usernameLabel.grid(column=0, row=0)

    passwordLabel = Label(info, text="Password  : ", font="Times 15")
    passwordLabel.grid(column=0, row=1)

    usernameEntry = Entry(info)
    usernameEntry.grid(column=1, row=0)

    passwordEntry = Entry(info,show='*')
    passwordEntry.grid(column=1, row=1)

    loginButton = Button(appl, text="Login", command=lambda: [loginUser(usernameEntry.get(), passwordEntry.get())], width=10, font="Times 14")
    loginButton.pack(pady=20)

    appl.mainloop()

def loginUser(eusername, epassword):
    print eusername, epassword
    db = MySQLdb.connect("localhost","root","jayesh@@","test")
    cursor = db.cursor()
    sql = "select * from user where username = '%s'"%(eusername)
    # try:
    print 'Successfully loged in'
    cursor.execute(sql)
    val = cursor.fetchall()
    db.commit()
    try:
        if(str(val[0][2])==str(eusername)):
            if(str(val[0][3])==str(epassword)):
                app = Tk()
                w=300
                h=200
                ws = app.winfo_screenwidth()
                hs = app.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                app.geometry('%dx%d+%d+%d' % (w, h, x, y))
                # app.geometry('300x200')
                app.title("User Loged in")

                tlabel = Label(app, text="Loged in Successfully", font="Times 16 bold")
                tlabel.pack(pady=10)

                tButton = Button(app, text="OK", command=lambda:[app.destroy(), shoppingCart(eusername, epassword)], width=10, font="Times 12")
                tButton.pack(pady=10)

                app.mainloop()
                # shoppingCart(eusername, epassword)
                print 'Successfully loged in'
            else:
                app = Tk()
                w=300
                h=180
                ws = app.winfo_screenwidth()
                hs = app.winfo_screenheight()
                # calculate position x, y
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                app.geometry('%dx%d+%d+%d' % (w, h, x, y))
                # app.geometry('300x300')
                app.title("Wrong Password")

                tlabel = Label(app, text="Wrong Password", font="Times 16 bold")
                tlabel.pack(pady=10)

                tButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
                tButton.pack(pady=10)

                app.mainloop()
                print 'wrong password'
        else:
            app = Tk()
            w=300
            h=300
            ws = app.winfo_screenwidth()
            hs = app.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            app.geometry('%dx%d+%d+%d' % (w, h, x, y))
            # app.geometry('300x300')
            app.title("Error")

            tlabel = Label(app, text="Something Went Wrong \n Check Login Details \n or \n Register", font="Times 16 bold")
            tlabel.pack(pady=10)

            tButton = Button(app, text="Login", command=lambda:[app.destroy()], width=10, font="Times 12")
            tButton.pack(pady=10)

            t2Button = Button(app, text="Register", command=lambda:[app.destroy(), register()], width=10, font="Times 12")
            t2Button.pack(pady=10)

            app.mainloop()
            print 'something went wrong'

    except:
        app = Tk()
        w=300
        h=300
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # app.geometry('300x300')
        app.title("yooo")

        tlabel = Label(app, text="Something Went Wrong \n Check Login Details \n or \n Register", font="Times 16 bold")
        tlabel.pack(pady=10)

        tButton = Button(app, text="Login", command=lambda:[app.destroy()], width=10, font="Times 12")
        tButton.pack(pady=10)

        t2Button = Button(app, text="Register", command=lambda:[app.destroy(), register()], width=10, font="Times 12")
        t2Button.pack(pady=10)

        app.mainloop()
        print 'Something Went Wrong'



def register():
    try:
        appm.destroy()
    except:
        appl.destroy()
    
    global appr
    appr = Tk()
    w=850
    h=550
    ws = appr.winfo_screenwidth()
    hs = appr.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appr.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # appr.geometry('850x550')
    appr.title("Register")

    registerPg = Label(text="Register Page", font="Times 32 bold")
    registerPg.pack(pady=(100,60))

    info = Frame(height=150, width=300)
    info.pack()

    fullnameLabel = Label(info, text="Full Name  : ", font="Times 15")
    fullnameLabel.grid(column=0, row=0)

    emailLabel = Label(info, text="Email  : ", font="Times 15")
    emailLabel.grid(column=0, row=1)

    usernameLabel = Label(info, text="User name  : ", font="Times 15")
    usernameLabel.grid(column=0, row=2)

    passwordLabel = Label(info, text="Password  : ", font="Times 15")
    passwordLabel.grid(column=0, row=3)

    fullnameEntry = Entry(info)
    fullnameEntry.grid(column=1, row=0)

    emailEntry = Entry(info)
    emailEntry.grid(column=1, row=1)

    usernameEntry = Entry(info)
    usernameEntry.grid(column=1, row=2)

    passwordEntry = Entry(info, show='*')
    passwordEntry.grid(column=1, row=3)

    registerButton = Button(appr, text="Register", command=lambda:[addUser(fullnameEntry.get(), emailEntry.get(), usernameEntry.get(), passwordEntry.get())], width=10, font="Times 14")
    registerButton.pack(pady=20)

    appr.mainloop()

def addUser(name, email, username, password):

    print name, email, username, password
    db = MySQLdb.connect("localhost","root","jayesh@@","test")
    cursor = db.cursor()
    qur = "select count(*) from user where username = '%s'"%(username)
    cursor.execute(qur)
    val = cursor.fetchone()[0]
    if(val==0):
        try:
            sql = "insert into user(name, email, username, password) values ('%s','%s','%s','%s')"%(name, email, username, password)
            print 'Successfully registered'
            cursor.execute(sql)
            db.commit()

            app = Tk()
            w=300
            h=200
            ws = app.winfo_screenwidth()
            hs = app.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            app.geometry('%dx%d+%d+%d' % (w, h, x, y))
            # app.geometry('300x200')
            app.title("User Added")

            tlabel = Label(app, text="User Added Successfully \n Try To Login ", font="Times 16 bold")
            tlabel.pack(pady=10)

            tButton = Button(app, text="Login", command=lambda:[app.destroy(), login()], width=10, font="Times 12")
            tButton.pack(pady=10)

            app.mainloop()

        except:
            app = Tk()
            w=300
            h=300
            ws = app.winfo_screenwidth()
            hs = app.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            app.geometry('%dx%d+%d+%d' % (w, h, x, y))
            # app.geometry('300x300')
            app.title("Error")

            elabel = Label(app, text="Something Went Wrong \n Try Again \n ", font="Times 16 bold")
            elabel.pack(pady=10)

            eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
            eButton.pack(pady=10)

            app.mainloop()

    else:
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # app.geometry('300x300')
        app.title("Error")

        elabel = Label(app, text="Username Already Exist \n Try Again With \n Unique Username", font="Times 16 bold")
        elabel.pack(pady=10)

        eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 10")
        eButton.pack(pady=10)

        app.mainloop()


def shoppingCart(username, password):
    print username, password
    try:
        appl.destroy()
    except:
        appc.destroy()

    global apps
    apps = Tk()
    w=700
    h=620
    ws = apps.winfo_screenwidth()
    hs = apps.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    apps.geometry('%dx%d+%d+%d' % (w, h, x, y))
    apps.geometry('700x610')
    apps.title("Shoping Cart App")

    # info1 = Frame(apps, height=150, width=500)
    # info1.pack()

    # msg = Label(info1, text='Press Add To Cart Button to add product to your cart', font='Times 12')
    # msg.pack()

    title = Label(apps, text='All Products', font='Times 30 bold')
    title.grid(padx=(100,40), pady=(10,0), column=1, row=0)

    img1 = ImageTk.PhotoImage(Image.open("iphonex.jpg"))
    panel1 = Label(apps, image = img1)
    panel1.grid(padx=(20,0), pady=10, column=0, row=1, sticky='w')

    name1 = Label(apps, text='Iphone X', font='Times 16')
    name1.grid(padx=30, column=1, row=1, sticky='w')

    cartButton = Button(apps, text='Add To Cart', command=lambda:[cartAdd(username, password, items[0])],width=10, font="Times 14")
    cartButton.grid(column=2, row=1)

    img2 = ImageTk.PhotoImage(Image.open("watch.jpg"))
    panel2 = Label(apps, image = img2)
    panel2.grid(padx=(20,0), pady=10, column=0, row=2, sticky='w')

    name2 = Label(apps, text='Casio Watch', font='Times 16')
    name2.grid(padx=30, column=1, row=2, sticky='w')

    cartButton = Button(apps, text='Add To Cart', command=lambda:[cartAdd(username, password, items[1])],width=10, font="Times 14")
    cartButton.grid(column=2, row=2)

    img3 = ImageTk.PhotoImage(Image.open("headphone.jpg"))
    panel3 = Label(apps, image = img3)
    panel3.grid(padx=(20,0), pady=10, column=0, row=3, sticky='w')

    name3 = Label(apps, text='Sony Headphone', font='Times 16')
    name3.grid(padx=30, column=1, row=3, sticky='w')

    cartButton = Button(apps, text='Add To Cart', command=lambda:[cartAdd(username, password, items[2])],width=10, font="Times 14")
    cartButton.grid(column=2, row=3)

    img4 = ImageTk.PhotoImage(Image.open("bag.jpg"))
    panel4 = Label(apps, image = img4)
    panel4.grid(padx=(20,0), pady=10, column=0, row=4, sticky='w')

    name4 = Label(apps, text='Puma Laptop Bag', font='Times 16')
    name4.grid(padx=30, column=1, row=4, sticky='w')

    cartButton = Button(apps, text='Add To Cart', command=lambda:[cartAdd(username, password, items[3])],width=10, font="Times 14")
    cartButton.grid(column=2, row=4)

    viewButton = Button(apps, text='Show Cart',command=lambda: [cartDetails(username, password)], fg='green',width=10, font="Times 14")
    viewButton.grid(padx=(50,0), column=1, row=5)    

    apps.mainloop()

def cartAdd(username, password, item):
    print username, password, item
    db = MySQLdb.connect("localhost","root","jayesh@@","test")
    cursor = db.cursor()
    sql = "insert into cart(username, password, cart) values ('%s','%s','%s')"%(username, password, item)

    try:
        print 'Successfully inserted item'
        cursor.execute(sql)
        db.commit()

        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # app.geometry('300x200')
        app.title("Product Added")

        tlabel = Label(app, text="Product Added Successfully", font="Times 16 bold")
        tlabel.pack(pady=10)

        tButton = Button(app, text="OK", command=lambda:[app.destroy()], width=10, font="Times 12")
        tButton.pack(pady=10)

        app.mainloop()

    except:
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # app.geometry('300x300')
        app.title("Error")

        elabel = Label(app, text="Something Went Wrong \n Try Again", font="Times 16 bold")
        elabel.pack(pady=10)

        eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
        eButton.pack(pady=10)

        app.mainloop()


def cartDetails(username, password):
    apps.destroy()

    global appc
    appc = Tk()
    w=850
    h=550
    ws = appc.winfo_screenwidth()
    hs = appc.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    appc.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # appc.geometry('850x550')
    appc.title("Shoping Cart App")

    # print username, password, item
    db = MySQLdb.connect("localhost","root","jayesh@@","test")
    cursor = db.cursor()
    

    try:
        print 'details'
        sql = "select * from user where username='%s' "%(username)
        cursor.execute(sql)
        details = cursor.fetchall()
        for i in details:
            print i
        elabel = Label(appc, text="User Details", font="Times 28 bold")
        elabel.pack(pady=(10,20))
        elabel = Label(appc, text="Name  -  %s"%(str(details[0][0])), font="Times 16")
        elabel.pack(pady=3)
        elabel = Label(appc, text="Email  -  %s"%(str(details[0][1])), font="Times 16")
        elabel.pack(pady=3)
        elabel = Label(appc, text="Username  -  %s"%(str(details[0][2])), font="Times 16")
        elabel.pack(pady=(3,40))



        elabel = Label(appc, text="Cart Items", font="Times 28 bold")
        elabel.pack(pady=(0,20))

        sql = "select cart from cart where username='%s' "%(username)
        cursor.execute(sql)
        aitem = cursor.fetchall()

        for row in cursor:
            elabel = Label(appc, text='%s'%(row), font="Times 16")
            elabel.pack(pady=5)

        db.commit()

        backButton = Button(appc, text='Back',command=lambda: [shoppingCart(username, password)], width=10, font="Times 14")
        backButton.pack(pady=(25,10)) 

    except:
        app = Tk()
        w=300
        h=200
        ws = app.winfo_screenwidth()
        hs = app.winfo_screenheight()
        # calculate position x, y
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        app.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # app.geometry('300x300')
        app.title("Error")

        elabel = Label(app, text="Something Went Wrong \n Try Again", font="Times 16 bold")
        elabel.pack(pady=10)

        eButton = Button(app, text="Try Again", command=lambda:[app.destroy()], width=10, font="Times 12")
        eButton.pack(pady=10)

        app.mainloop()   

    appc.mainloop()

if __name__ == '__main__':
    mainPage()
    
