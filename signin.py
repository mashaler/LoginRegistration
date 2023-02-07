from tkinter import *
from PIL import ImageTk

# Functionality Part
def signup_page():
    login_windom.destroy()
    import signup

def hide():
    openeye.config(file='./loginsignuppage/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='./loginsignuppage/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if UsernameEntry.get() == 'Username':
        UsernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0,END)

# GUI Part
login_windom=Tk()
login_windom.geometry('990x660+50+50')
login_windom.resizable(0,0)
login_windom.title('Login Page')

bgImage = ImageTk.PhotoImage(file='./loginsignuppage/bg.jpg')

bgLabel = Label(login_windom,image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_windom,text='USER LOGIN',font=('Microsoft Yahei UI LIGHT',23,'bold'),bg='white', fg='firebrick1')
heading.place(x=605,y=120)

UsernameEntry = Entry(login_windom,width=25,font=('Microsoft Yahei UI LIGHT',11,'bold'),bd=0,fg='firebrick1')
UsernameEntry.place(x=580,y=200)
UsernameEntry.insert(0,'Username')

UsernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_windom,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry = Entry(login_windom,width=25,font=('Microsoft Yahei UI LIGHT',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_windom,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye = PhotoImage(file='./loginsignuppage/openeye.png')
eyeButton = Button(login_windom,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton = Button(login_windom,text='Forgot Password?',bd=0,bg='white',activebackground='white',
                         cursor='hand2',font=('Microsoft Yahei UI LIGHT',9,'bold'),fg='firebrick1',activeforeground='firebrick1')
forgetButton.place(x=715,y=295)

loginButton = Button(login_windom,text='Login',font=('open sans',16,'bold'),fg='white',bg='firebrick1',
activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19)
loginButton.place(x=578,y=350)

orLabel = Label(login_windom,text='---------------OR---------------',font=('open sans',16,'bold'),fg='firebrick1',
bg='white')
orLabel.place(x=583,y=400)

facebook_logo = PhotoImage(file='./loginsignuppage/facebook.png')
fbLabel = Label(login_windom,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo = PhotoImage(file='./loginsignuppage/google.png')
googleLabel = Label(login_windom,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo = PhotoImage(file='./loginsignuppage/twitter.png')
twitterLabel = Label(login_windom,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel = Label(login_windom,text='Dont have an account?',font=('open sans',9,'bold'),fg='firebrick1',
bg='white')
signupLabel.place(x=590,y=500)

newaccountButton = Button(login_windom,text='Create new one',font=('open sans',9,'bold underline'),fg='blue',bg='white',
activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

login_windom.mainloop()