from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
import sqlite3
from datetime import datetime
import tempfile
import os

class Reserve_Card:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation Card")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        w1 = int(0.535*w)
        h1 = int(0.652*h)
        x = int(0.22*w)
        y = int(0.156*h)
        self.root.geometry("%dx%d+%d+%d" % (w1, h1, x, y))
        # 730 500

        #============variables==========
        self.var_reserve_no=StringVar()

        # ===========enter reservation no===========
        frame_id = LabelFrame(self.root, bd=2, relief=RIDGE)
        frame_id.place(relx=0.233, rely=0, width=0.548*w1, height=0.074*h1)
        # 400 37

        # Reservation No
        lbl_reserve_no = Label(frame_id, text="Reservation No", font=(
            "arial", int(0.016*w1), "bold"))
        lbl_reserve_no.place(relx=0, rely=0.15)

        entry_reserve_id = ttk.Entry(frame_id, width=int(0.033*w1), textvariable=self.var_reserve_no, font=(
            "arial", int(0.015*w1)))
        entry_reserve_id.place(relx=0.30, rely=0.16)

        # FetchBill Button
        btnFetch = Button(frame_id, text="Print Card", command=self.gen_card, font=(
            "arial", int(0.015*w1), "bold"), bg="black", fg='gold', width=int(0.015*w1))
        btnFetch.place(relx=0.77, rely=0.09)


    def gen_card(self):
        if self.var_reserve_no.get() == "":
            messagebox.showerror("Error", "Please enter customer's Reservation No", parent=self.root)
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
            textarea.insert(END,'\n\t\t\tRESERVATION CARD\n\n\n')

            #=============Reservation ID==============
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select ReservationNo from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'Reservation No:{row}')

            # #=============date==============
            textarea.insert(END,f'\t\t\tDate:{datetime.now():%b %d, %Y}\n\n')

            # line Break
            textarea.insert(END,f'============================================================\n\n')

            #label name
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Name from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'Name:{row}')

            #label contact
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Contact from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'\t\tContact:{row}\n\n')


            # # Label Gender
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            # my_cursor = conn.cursor()
            # query = ("select Gender from customer where CNIC_Passport=%s")
            # value = (self.var_id.get(),)
            # my_cursor.execute(query, value)
            # row = my_cursor.fetchone()
            # row = ''.join(row)
            # textarea.insert(END,f'\t\tGender:{row}')

            # # Label Age
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            # my_cursor = conn.cursor()
            # query = ("select Age from customer where CNIC_Passport=%s")
            # value = (self.var_id.get(),)
            # my_cursor.execute(query, value)
            # row = my_cursor.fetchone()
            # row = ''.join(row)
            # textarea.insert(END,f'\tAge:{row}\n\n')

            # # Label Mobile
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            # my_cursor = conn.cursor()
            # query = ("select Mobile from customer where CNIC_Passport=%s")
            # value = (self.var_id.get(),)
            # my_cursor.execute(query, value)
            # row = my_cursor.fetchone()
            # row = ''.join(row)
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
            # textarea.insert(END,f'\tEmail:{row}\n\n')

            # Label Arrival Date
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select ArrivalDate from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'Arrival Date:{row}')

            # Label DepartureDate
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select DepartureDate from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'\t\tDeparture Date:{row}\n\n')

            # Label Days
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Days from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'No of Days:{row}')

            # Room Type
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select RoomType from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'\t\tRoom Type:{row}')

            # Room No
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Room from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'\tRoom No:{row}\n\n')

            # No of Persons
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Persons from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'No of Persons:{row}')

            # Payment
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Payment from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'\t\tPayment:{row}')

            # Extra Beds
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                     database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select ExtraBeds from reservation where ReservationNo=?")
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            textarea.insert(END,f'\t\tExtraBeds:{row}\n')

            # line Break
            textarea.insert(END,f'============================================================\n\n')

            # print the bill
            q=textarea.get('1.0','end-1c')
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,'Print')


if __name__ == "__main__":
    root = Tk()
    obj = Reserve_Card(root)
    root.mainloop()