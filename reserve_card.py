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
        self.root.geometry("730x500+300+120")

        #============variables==========
        self.var_reserve_no=StringVar()

        # ===========enter reservation no===========
        frame_id = LabelFrame(self.root, bd=2, relief=RIDGE)
        frame_id.place(x=170, y=0, width=400, height=37)

        # Reservation No
        lbl_reserve_no = Label(frame_id, text="Reservation No", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_reserve_no.grid(row=0, column=0, sticky=W)

        entry_reserve_id = ttk.Entry(frame_id, width=22, textvariable=self.var_reserve_no, font=(
            "arial", 10))
        entry_reserve_id.grid(row=0, column=1, sticky=W)

        # FetchBill Button
        btnFetch = Button(frame_id, text="Print Card", command=self.gen_card, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=12)
        btnFetch.place(x=280, y=1)


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