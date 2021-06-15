from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
import sqlite3
from datetime import datetime
import tempfile
import os

class Bill:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        w1 = int(0.535*w)
        h1 = int(0.652*h)
        x = int(0.22*w)
        y = int(0.156*h)
        self.root.geometry("%dx%d+%d+%d" % (w1, h1, x, y))
        # 730 500

        #============variables==========
        self.var_book_no=StringVar()

        # ===========enter cnic/passport===========
        frame_id = LabelFrame(self.root, bd=2, relief=RIDGE)
        frame_id.place(relx=0.233, rely=0, width=0.548*w1, height=0.074*h1)
        # 400 37

        # Booking Id
        lbl_cust_id = Label(frame_id, text="Booking No", font=(
            "arial", int(0.016*w1), "bold"))
        lbl_cust_id.place(relx=0, rely=0.15)

        entry_id = ttk.Entry(frame_id, width=int(0.035*w1), textvariable=self.var_book_no, font=(
            "arial", int(0.015*w1)))
        entry_id.place(relx=0.23, rely=0.16)

        # FetchBill Button
        btnFetch = Button(frame_id, text="Print Bill", command=self.gen_bill, font=(
            "arial", int(0.015*w1), "bold"), bg="black", fg='gold', width=int(0.016*w1))
        btnFetch.place(relx=0.74, rely=0.09)


    def gen_bill(self):
        if self.var_book_no.get() == "":
            messagebox.showerror("Error", "Please enter customer Booking No.", parent=self.root)
        else:
            #============textarea Frame==============
            frame_billArea = Frame(self.root,relief=GROOVE,bd=5)
            frame_billArea.place(x=0,y=40,width=730,height=460)
            scrol_y=Scrollbar(frame_billArea,orient=VERTICAL)
            scrol_y.pack(side=RIGHT,fill=Y)
            textarea=Text(frame_billArea,font='arial 15',yscrollcommand=scrol_y.set)
            textarea.pack(fill=BOTH)
            scrol_y.config(command=textarea.yview)
            
            textarea.delete(1.0,END)

            # ===========title=============
            # bill_title = Label(textarea, text="Reciept", font=(
            #     "times new roman", 20, "bold","underline"), bd=0, relief=RIDGE, bg="white")
            # bill_title.place(x=0, y=30, width=460, height=40)

            # ===========Hotel Name and Adress=============
            textarea.insert(END,'\n\tHotel Management Hotel & Resort\n')
            textarea.insert(END,'\tNear Attabad Lake, on Main Karakorum Highway\n')
            textarea.insert(END,'\tP.O & Village Gulmit Gojal, District Hunza\n')
            textarea.insert(END,'\tZip Code:15100\t\tContact:0345-1111111\n')

            textarea.insert(END,'\n\n\t\t\tRECIEPT\n\n\n')

            # # ============logo=============
            # img = Image.open(r"/Hotel_Management_Software/images/logo.png")
            # img = img.resize((80, 80), Image.ANTIALIAS)
            # self.photoimg = ImageTk.PhotoImage(img)

            # lblimg = Label(textarea, image=self.photoimg, bd=0, relief=RIDGE,bg="white")
            # lblimg.place(x=0, y=0, width=100, height=100)

            # ============Booking ID============
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select BookingNo from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            textarea.insert(END,f'Booking No:{row}')

            # #=============date==============
            # curr_date = Label(textarea, text=f"Date: {datetime.now():%b %d, %Y}",font=("arial", 10, "bold"), padx=2, pady=6,bg="white")
            # curr_date.place(x=340,y=65)

            # line = Label(textarea,text="===================================================================", font=("times new roman",10,"bold"),bg="white")
            # line.place(x=5,y=90)
            textarea.insert(END,f'\t\t\t\tDate:{datetime.now():%b %d, %Y}\n\n')

            #label name
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Name from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            # lblName = Label(textarea, text="Name:",font=("arial", 11, "bold"),bg="White")
            # lblName.place(x=15, y=110)
            # lbl = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl.place(x=65, y=110)
            textarea.insert(END,f'Name:{row}')


            # Label CNIC_Passport
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select CNIC_Passport from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lblGender = Label(textarea, text="Gender:",font=("arial", 11, "bold"),bg="white")
            # lblGender.place(x=260, y=110)
            # lbl2 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl2.place(x=320, y=110)
            textarea.insert(END,f'\tCNIC/Passport:{row}\n')

            # # Label Age
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            # my_cursor = conn.cursor()
            # query = ("select Age from customer where CNIC_Passport=%s")
            # value = (self.var_id.get(),)
            # my_cursor.execute(query, value)
            # row = my_cursor.fetchone()
            # row = ''.join(row)

            # # lblAge = Label(textarea, text="Age:",font=("arial", 11, "bold"),bg="white")
            # # lblAge.place(x=390, y=110)
            # # lbl5 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # # lbl5.place(x=425, y=110)
            # textarea.insert(END,f'\tAge:{row}\n')

            # # Label Mobile
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            # my_cursor = conn.cursor()
            # query = ("select Mobile from customer where CNIC_Passport=%s")
            # value = (self.var_id.get(),)
            # my_cursor.execute(query, value)
            # row = my_cursor.fetchone()
            # row = ''.join(row)

            # # lblMobile = Label(textarea, text="Mobile No:",font=("arial", 11, "bold"),bg="white")
            # # lblMobile.place(x=15, y=135)
            # # lbl3 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # # lbl3.place(x=95, y=135)
            # textarea.insert(END,f'Mobile:{row}')

            # # Label Email
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            # my_cursor = conn.cursor()
            # query = ("select Email from customer where CNIC_Passport=%s")
            # value = (self.var_id.get(),)
            # my_cursor.execute(query, value)
            # row = my_cursor.fetchone()
            # row = ''.join(row)

            # # lblEmail = Label(textarea, text="Email:",font=("arial", 11, "bold"),bg="white")
            # # lblEmail.place(x=230, y=135)
            # # lbl4 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # # lbl4.place(x=280, y=135)
            # textarea.insert(END,f'\tEmail:{row}\n')

            # Label CheckInDate
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select CheckInDate from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_checkIn = Label(textarea, text="Check-In:",font=("arial", 11, "bold"),bg="white")
            # lbl_checkIn.place(x=15, y=160)
            # lbl6 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl6.place(x=90, y=160)
            textarea.insert(END,f'Check-In:{row}')

            # Label CheckOutDate
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select CheckOutDate from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_checkOut = Label(textarea, text="Check-Out:",font=("arial", 11, "bold"),bg="white")
            # lbl_checkOut.place(x=190, y=160)
            # lbl7 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl7.place(x=275, y=160)
            textarea.insert(END,f'\t\tCheck-Out:{row}\n')

            # Label Days
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Days from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_Days = Label(textarea, text="Days:",font=("arial", 11, "bold"),bg="white")
            # lbl_Days.place(x=380, y=160)
            # lbl8 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl8.place(x=425, y=160)
            textarea.insert(END,f'No of Days:{row}\n')

            # line = Label(textarea,text="===================================================================", font=("times new roman",10,"bold"),bg="white")
            # line.place(x=5,y=180)
            textarea.insert(END,f'=================================================================\n\n')

            # Label RoomCharge
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select RoomCharge from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_RoomCharge = Label(textarea, text="Room Charges -----------------------------------------------",font=("arial", 11),bg="white")
            # lbl_RoomCharge.place(x=15, y=210)
            # lbl9 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl9.place(x=360, y=210)
            textarea.insert(END,f'Room Charges: ---------------------------------------- {row}\n')

            # Label MealCharge
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Meal from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_MealCharge = Label(textarea, text="Meal Charges -----------------------------------------------",font=("arial", 11),bg="white")
            # lbl_MealCharge.place(x=15, y=230)
            # lbl10 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl10.place(x=360, y=230)
            textarea.insert(END,f'Meal Charges: ---------------------------------------- {row}\n')

            # Label OtherCharge
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select OtherCharge from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_OtherCharge = Label(textarea, text="Other Charges -----------------------------------------------",font=("arial", 11),bg="white")
            # lbl_OtherCharge.place(x=15, y=250)
            # lbl11 = Label(textarea, text=row,font=("arial", 11),bg="white")
            # lbl11.place(x=360, y=250)
            textarea.insert(END,f'Other Charges: --------------------------------------- {row}\n\n')

            # line = Label(textarea,text="===================================================================", font=("times new roman",10,"bold"),bg="white")
            # line.place(x=5,y=280)
            textarea.insert(END,f'=================================================================\n')
            
            # Label TotalCharge
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Total from booking where BookingNo=?")
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)

            # lbl_TotalCharge = Label(textarea, text="Total ----------------------------------------------------------",font=("arial", 11,"bold"),bg="white")
            # lbl_TotalCharge.place(x=15, y=300)
            # lbl11 = Label(textarea, text=row,font=("arial", 11,"bold"),bg="white")
            # lbl11.place(x=360, y=300)
            textarea.insert(END,f'Total: ----------------------------------------------- {row}\n')

            # line = Label(textarea,text="===================================================================", font=("times new roman",10,"bold"),bg="white")
            # line.place(x=5,y=320)
            textarea.insert(END,f'=================================================================\n\n\n')

            # signature and seal
            # line1 = Label(textarea,text="_______________________", font=("arial", 11),bg="white")
            # line1.place(x=10,y=370)
            # text1 = Label(textarea,text="Signature & Seal",font=("arial", 11),bg="white")
            # text1.place(x=35,y=390)
            textarea.insert(END,f'________________\n')
            textarea.insert(END,f'Signature & Seal')


            # print the bill
            q=textarea.get('1.0','end-1c')
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,'Print')


if __name__ == "__main__":
    root = Tk()
    obj = Bill(root)
    root.mainloop()