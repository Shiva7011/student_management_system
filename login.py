from tkinter import*    #For GUI
from tkinter import ttk  
from tkinter import messagebox
from PIL import ImageTk  # for Image related work 
import os   #for file 
import webbrowser
import sys,sqlite3
from datetime import datetime

#--------

class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Form".center(420))  # title for Window 
        self.root.configure(background = "white")  # background color for window 
        self.root.geometry("1360x768+0+0")

        bg_color ="#2B547E"
        
        #-----------Storing -------image to variables-------------------
        self.user_icon=ImageTk.PhotoImage(file="images.png")
        self.pasw_icon=ImageTk.PhotoImage(file="images (1).png")

        self.email=StringVar()
        self.pasw=StringVar()
        self.email.set("Email Id(eg:a@ab.com)")
        
        F1 = Frame(self.root, bg=bg_color, bd=0)
        F1.place(x=380,y=144,width=600,height=480 )
        lbl = Label(F1,text="LOGIN As Admin ", bg=bg_color, fg="gold", font= ("times new roman",30,"bold"))
        lbl.place(x=300, y=80, anchor="center")

        btn_login = Button(F1, text="Login",relief=FLAT,command=self.login, font=("times new roman",14,"bold"),bg="#348017",foreground="#FEFCFF")
        btn_login.place(x=250, y=350, width=130, height=35, anchor="w")
        
        btn_SignUp = Button(F1, text="SignUp",command=self.signup,relief=FLAT, font=("times new roman",14,"bold"),bg="#1569C7",foreground="#FEFCFF")
        btn_SignUp.place(x=400, y=350, width=130, height=35, anchor="w")

        btn_switch = Button(F1, text="Login as Employee", relief=FLAT, command=self.login3, font=("times new roman",12,"underline"), bg=bg_color, fg="gold", cursor="hand2")
        btn_switch.place(x=300, y=415, anchor="center")

        logolbl=Label(F1, image=self.user_icon, bg=bg_color)
        logolbl.place(x=80,y=210,anchor="w")
        lbl6 = Label(F1, text = "Email Id",fg="white",bg=bg_color, font= ("times new roman",20,"bold"))
        lbl6.place(x=115,y=210,anchor="w")
        txtu = Entry(F1,bd=1,textvariable=self.email, relief = SOLID,font=("",15))
        txtu.place(x=250,y=210,width=280,height=35,anchor="w")
        

        logolbl2=Label(F1, image=self.pasw_icon, bg=bg_color)
        logolbl2.place(x=80,y=280,anchor="w")
        lbl7 = Label(F1, text = "Password",fg="white",bg=bg_color, font= ("times new roman",20,"bold"))
        lbl7.place(x=115,y=280,anchor="w")
        txtp = Entry(F1,bd=1,textvariable=self.pasw, show="*",relief = SOLID,font=("",15))
        txtp.place(x=250,y=280,width=280,height=35,anchor="w")
        
        now = datetime.now()
        self.Time1=now.strftime('%H:%M:%S')
        self.date= now.strftime("%d-%b-%Y")


    def link1(self):
        webbrowser.open_new("http://www.google.com")
    
    def link2(self):
        webbrowser.open_new("https://www.instagram.com/?hl=en")
    
    def link3(self):
        webbrowser.open_new("http://www.facebook.com")

    def link4(self):
        webbrowser.open_new("http://www.twitter.com")
    


    def login(self):
        with open("Temp.txt","w+") as file:
            file.write(self.email.get())
    
        if self.email.get()=="" or self.pasw.get()=="":
            messagebox.showerror("Error!","All field should be filled")
        if "@" not in self.email.get():
            messagebox.showwarning("Error","Email should have '@' Character")
        else:
            self.conn=sqlite3.connect("sdms.db")
            self.c=self.conn.cursor()
            self.find_user = ("SELECT * FROM admin WHERE email = ?  AND pasw = ?")
            self.c.execute(str(self.find_user),(str(self.email.get()),str(self.pasw.get())))
            results = (self.c).fetchall()
            if results:
                for i in results:
                    self.root.destroy()
                    import Home    
            else:
                messagebox.showerror("Error!","Username or Password may be wrong")
    
    def login2(self):
        self.root.destroy()
        import login
    
    def login3(self):
        self.root.destroy()
        import logine
    
    def signup(self):
        self.root.destroy()
        import signup
                
    
       
    

            
#create Window    
root = Tk()
obj = win1(root)
root.mainloop()
