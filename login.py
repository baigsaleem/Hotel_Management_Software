from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagmentSystem
import sqlite3


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


# ===========Login==============
class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        # self.root.geometry("1366x768+0+0")
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w, h))
        #1366 768

        self.bg = ImageTk.PhotoImage(
            file=r"images\login.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(relx=0, rely=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=w*0.249, height=h*0.586)
        frame.update()
        w1, h1 = frame.winfo_width(), frame.winfo_height()
        #340 450

        img1 = Image.open(
            r"images\LoginIcon.png")
        img1 = img1.resize((int(w1*0.295), int(h1*0.223)), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame,image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(relx=0.37, rely=0.04, width=w1*0.295, height=h1*0.223)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", int(w1*0.060), "bold"), fg="white", bg="black")
        get_str.place(relx=0.295, rely=0.267)

        # label
        username = Label(frame, text="Username", font=(
            "times new roman", int(w1*0.045), "bold"), fg="white", bg="black")
        username.place(relx=0.162, rely=0.367)

        self.txtuser = ttk.Entry(frame, font=("times new roman", int(w1*0.045), "bold"))
        self.txtuser.place(relx=0.103, rely=0.434, width=int(w*0.200))

        # password
        password = Label(frame, text="Password", font=(
            "times new roman", int(w1*0.045), "bold"), fg="white", bg="black")
        password.place(relx=0.162, rely=0.500)

        self.txtpass = ttk.Entry(frame, font=("times new roman", int(w1*0.045), "bold"), show="*")
        self.txtpass.place(relx=0.103, rely=0.567, width=int(w*0.200))

        # ============Icon Images===========
        img2 = Image.open(
            r"images\LoginIcon.png")
        img2 = img2.resize((int(w1*0.060), int(h1*0.045)), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(frame,image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(relx=0.1, rely=0.38, width=int(w1*0.060), height=int(h1*0.045))

        img3 = Image.open(
            r"images\PassIcon.png")
        img3 = img3.resize((int(w1*0.060), int(h1*0.045)), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(frame,image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(relx=0.1, rely=0.51, width=int(w1*0.060), height=int(h1*0.045))

        # ========loginbutton===============
        loginbtn = Button(frame, text="Login", command=self.login, font=(
            "times new roman", int(w1*0.045), "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(relx=0.323, rely=0.667, width=int(w1*0.323), height=int(h1*0.078))

        # ===========registrationbutton=======
        regbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "times new roman", int(w1*0.035), "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        regbtn.place(relx=0.047, rely=0.778, width=int(w1*0.470))

        # ==========forgot password============
        forgotPassbtn = Button(frame, text="Forgot Password", command=self.forgot_password_window, font=(
            "times new roman", int(w1*0.035), "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotPassbtn.place(relx=0.030, rely=0.834, width=int(w1*0.470))

        # ============Developer label===========
        developer = Label(frame, text="Software developed by Saleem Baig, CEO NrewSoft...", font=(
            "times new roman", int(w1*0.024)), fg="white", bg="black")
        developer.place(relx=0.132, rely=0.955)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field required")
        else:
            # conn = mysql.connector.connect(
            #     host="localhost", user="root", password="Admin@123", database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=? and password=?", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagmentSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    # ========reset password===========
    def reset_pass(self):
        if self.combo_security_Q.get() == "":
            messagebox.showerror(
                "Error", "Select the Security Question", parent=self.root2)
        elif self.answer_entry.get() == "":
            messagebox.showerror(
                "Error", "Enter the Security Question Answer", parent=self.root2)
        elif self.new_password_entry.get() == "":
            messagebox.showerror(
                "Error", "Enter the new Password", parent=self.root2)
        else:
            # conn = mysql.connector.connect(
            #     host="localhost", user="root", password="Admin@123", database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = (
                "select * from register where email=? and securityQ=? and securityA=?")
            value = (self.txtuser.get(), self.combo_security_Q.get(),
                     self.answer_entry.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Please enter the correct Answer", parent=self.root2)
            else:
                query = ("update register set password=? where email=?")
                value = (self.new_password_entry.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Your password has been reset, Please login with the new password", parent=self.root2)
                self.root2.destroy()

    # ================forgot password window==============

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please enter the email to reset password")
        else:
            # conn = mysql.connector.connect(
            #     host="localhost", user="root", password="Admin@123", database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select * from register where email=?")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter valid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                # self.root2.geometry("350x450+550+180")
                w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
                w2 = 0.256*w
                h2 = 0.586*h
                x2 = 0.402*w
                y2 = 0.234*h
                self.root2.geometry("%dx%d+%d+%d" % (w2, h2, x2, y2))

                l = Label(self.root2, text="Forgot Password", font=(
                    "times new roman", int(0.057*w2), "bold"), fg="red", bg="white")
                l.place(relx=0, rely=0.023, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=(
                    "times new roman", int(0.034*w2), "bold"))
                security_Q.place(relx=0.143, rely=0.178)
                self.combo_security_Q = ttk.Combobox(self.root2, font=(
                    "times new roman", int(0.043*w2), "bold"), state='readonly')
                self.combo_security_Q["values"] = (
                    "Select", "Your Birth Place", "Your First School", "Your pet name")
                self.combo_security_Q.place(relx=0.143, rely=0.245, width=0.714*w2)
                self.combo_security_Q.current(0)

                answer = Label(self.root2, text="Security Answer", font=(
                    "times new roman", int(0.043*w2), "bold"))
                answer.place(relx=0.143, rely=0.334)
                self.answer_entry = ttk.Entry(
                    self.root2, font=("times new roman", int(0.043*w2), "bold"))
                self.answer_entry.place(relx=0.143, rely=0.4, width=0.714*w2)

                new_password = Label(self.root2, text="New Password", font=(
                    "times new roman", int(0.043*w2), "bold"))
                new_password.place(relx=0.143, rely=0.489)
                self.new_password_entry = ttk.Entry(
                    self.root2, font=("times new roman", int(0.043*w2), "bold"),show="*")
                self.new_password_entry.place(relx=0.143, rely=0.556, width=0.714*w2)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=(
                    "times new roman", int(0.043*w2), "bold"), fg="white", bg="green", width=int(0.028*w2))
                btn.place(relx=0.286, rely=0.645)


# ================Register==================
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        # self.root.geometry("1000x600+230+100")
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        w3 = 0.732*w
        h3 = 0.781*h
        x3 = 0.168*w
        y3 = 0.130*h
        self.root.geometry("%dx%d+%d+%d" % (w3, h3,x3,y3))

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background image
        self.bg = ImageTk.PhotoImage(
            file=r"images\register.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(relx=0, rely=0, relwidth=1, relheight=1)

        # left side image
        self.bg1 = ImageTk.PhotoImage(
            file=r"images\register1.jpg")
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(relx=0.04, rely=0.084, width=0.38*w3, height=0.834*h3)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(relx=0.42, rely=0.084, width=0.54*w3, height=0.834*h3)
        # (540,500)

        # ============register form==================
        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", int(0.02*w3), "bold"), fg="darkgreen", bg="white")
        register_lbl.place(relx=0.037, rely=0.04)
        # label and entries
        # row1
        fname = Label(frame, text="First Name", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        fname.place(relx=0.037, rely=0.2)
        self.txt_fname = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", int(0.015*w3), "bold"))
        self.txt_fname.place(relx=0.037, rely=0.25, width=0.2*w3)

        lname = Label(frame, text="Last Name", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        lname.place(relx=0.518, rely=0.2)
        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", int(0.015*w3), "bold"))
        self.txt_lname.place(relx=0.518, rely=0.25, width=0.2*w3)

        # row2
        contact = Label(frame, text="Contact No.", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        contact.place(relx=0.037, rely=0.34)
        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", int(0.015*w3), "bold"))
        self.txt_contact.place(relx=0.037, rely=0.39, width=0.2*w3)

        email = Label(frame, text="Email", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        email.place(relx=0.518, rely=0.34)
        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", int(0.015*w3), "bold"))
        self.txt_email.place(relx=0.518, rely=0.39, width=0.23*w3)

        # row3
        security_Q = Label(frame, text="Select Security Question", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        security_Q.place(relx=0.037, rely=0.48)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=(
            "times new roman", int(0.015*3), "bold"), state='readonly')
        self.combo_security_Q["values"] = (
            "Select", "Your Birth Place", "Your First School", "Your pet name")
        self.combo_security_Q.place(relx=0.037, rely=0.53, width=0.20*w3)
        self.combo_security_Q.current(0)

        answer = Label(frame, text="Security Answer", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        answer.place(relx=0.518, rely=0.48)
        self.answer_entry = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", int(0.015*w3), "bold"))
        self.answer_entry.place(relx=0.518, rely=0.53, width=0.20*w3)

        # row4
        password = Label(frame, text="Password", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        password.place(relx=0.037, rely=0.62)
        self.password_entry = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", int(0.015*w3), "bold"),show="*")
        self.password_entry.place(relx=0.037, rely=0.67, width=0.20*w3)

        con_pass = Label(frame, text="Confirm Password", font=(
            "times new roman", int(0.015*w3), "bold"), bg="white")
        con_pass.place(relx=0.518, rely=0.62)
        self.con_pass_entry = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", int(0.015*w3), "bold"),show="*")
        self.con_pass_entry.place(relx=0.518, rely=0.67, width=0.20*w3)

        # ===============checkbox==========
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, text="I Agree to the Terms & Conditions", variable=self.var_check, font=(
            "times new roman", int(0.012*w3), "bold"), onvalue=1, offvalue=0)
        checkbtn.place(relx=0.037, rely=0.74)

        # ==========buttons==========
        img_reg = Image.open(
            r"images\register-now.png")
        img_reg = img_reg.resize((int(0.2*w3), int(0.1*h3)), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img_reg)
        b1 = Button(frame, image=self.photoimage, command=self.register_data,
                    borderwidth=0, cursor="hand2")
        b1.place(relx=0.037, rely=0.82, width=0.20*w3)

        img_log = Image.open(
            r"images\login-now.png")
        img_log = img_log.resize((int(0.2*w3), int(0.1*h3)), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img_log)
        b1 = Button(frame, image=self.photoimage1, command=self.return_login,
                    borderwidth=0, cursor="hand2")
        b1.place(relx=0.518, rely=0.82, width=0.20*w3)

    # ========= function declaration=============
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                'Error', 'Please agree to the terms & conditions')
        else:
            # conn = mysql.connector.connect(
            #     host="localhost", user="root", password="Admin@123", database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select * from register where email=?")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(?,?,?,?,?,?,?)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
