from tkinter import*  
from tkinter import messagebox
from PIL import Image,ImageTk 
import pymysql     

class Register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")

    # *********Background Image*********
        self.bg=ImageTk.PhotoImage(file="images/b1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

    # *****************Left Image********
        self.left=ImageTk.PhotoImage(file="images/a3.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=400)

    # **********Register Frame********
        Frame1=Frame(self.root,bg="purple2")
        Frame1.place(x=480,y=100,width=700,height=400)

        title=Label(Frame1,text="SIGNUP  FORM",font=("showcard gothic",28,"bold"),bg="purple2",fg="black").place(x=100,y=30)

        username=Label(Frame1,text="Username",font=("kristen itc",15,"bold"),bg="purple2",fg="black").place(x=100,y=100)
        self.txt_username=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_username.place(x=100,y=130,width=250)

        email=Label(Frame1,text="Email",font=("kristen itc",15,"bold"),bg="purple2",fg="black").place(x=370,y=100)
        self.txt_email=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=130,width=250)

        password=Label(Frame1,text="Password",font=("kristen itc",15,"bold"),bg="purple2",fg="black").place(x=100,y=180)
        self.txt_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_password.place(x=100,y=210,width=250)

        con_password=Label(Frame1,text="Confirm Password",font=("kristen itc",15,"bold"),bg="purple2",fg="black").place(x=370,y=180)
        self.txt_con_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_con_password.place(x=370,y=210,width=250)

        self.var_check=IntVar()
        check=Checkbutton(Frame1,text="I Agree the terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,bg="purple2", font=("kristen itc",12)).place(x=100,y=250)

        self.btn=Button(Frame1,text="Register Here",font=("showcard gothic",15,"bold"),bg="pink",bd=0,cursor="hand2",command=self.register).place(x=200,y=300,width="250")
       
        left_btn=Button(self.root,text="Sign in",command=self.login_window, font=("castellar",15,"bold"),bg="gold",bd=0,cursor="hand2").place(x=150,y=400,width="250")


    

    # *********working with database*******
    
    def login_window(self):
        self.root.destroy()
        import try1
    
    def clear(self):
        self.txt_username.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_con_password.delete(0,END)
        
    
    
    def register(self):
        if self.txt_username.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_con_password.get()=="": 
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_con_password.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="signupp")
                cur=con.cursor()
                cur.execute("select * from admin where email=%s", self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Email Error occurred","User Already Exists with this email, please try with another email",parent=self.root)
                else:
                    cur.execute("insert into admin (username, email, password) values(%s,%s,%s)",
                            (self.txt_username.get(),
                             self.txt_email.get(),
                             self.txt_password.get()
                             ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.root.destroy()
                    import try1
                    self.clear()


            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



root=Tk()
obj=Register_window(root)
root.mainloop()
