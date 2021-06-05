import random
from tkinter import *
from tkinter import messagebox, ttk
from reserve_card import Reserve_Card

import mysql.connector
import sqlite3
from PIL import Image, ImageTk
from datetime import datetime
from tkcalendar import DateEntry


class Reservation:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation")
        # self.root.geometry("1130x485+225+180")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # w,h=1000,600
        w1 = int(0.8275*w)
        h1 = int(0.632*h)
        x = int(0.165*w)
        y = int(0.235*h)
        self.root.geometry("%dx%d+%d+%d" % (w1, h1, x, y))
        # 1130 485

         # =========variables============
        self.var_id = StringVar()

        self.var_reserve_no = StringVar()
        x = random.randint(1000, 99999)
        self.var_reserve_no.set(str(x))

        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_arrival = StringVar()
        self.var_departure = StringVar()
        self.var_roomtype = StringVar()
        self.var_room = StringVar()
        self.var_persons = StringVar()
        self.var_payment = StringVar()
        self.var_days = StringVar()
        self.var_extraBeds = StringVar()

        # ===========title=============
        lbl_title = Label(self.root, text="Room Reservation", font=(
            "arial", int(0.0177*w1), "bold"), bg="grey", fg="gold", bd=2, relief=RIDGE)
        lbl_title.place(relx=0, rely=0, width=w1, height=0.124*h1)

        # ========logo==============
        img2 = Image.open(
            r"images/logo.png")
        img2 = img2.resize((int(0.053*w1), int(0.124*h1)), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(relx=0, rely=0, width=0.070*w1, height=0.124*h1)

        # =============labelframe==========
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="Reservation Details", font=(
            "arial", int(0.015*w1), "bold"), padx=2,)
        labelFrameLeftSide.place(relx=0.0044, rely=0.124, width=0.332*w1, height=0.866*h1)
        labelFrameLeftSide.update()
        w2, h2 = labelFrameLeftSide.winfo_width(), labelFrameLeftSide.winfo_height()
        # 375 420

         # =========labels and entries========
        # Customer Id
        lbl_cust_id = Label(labelFrameLeftSide, text="Customer ID", font=(
            "arial", int(0.0098*w1), "bold"))
        lbl_cust_id.place(relx=0, rely=0.013)

        entry_id = ttk.Entry(labelFrameLeftSide, width=int(0.019*w1), textvariable=self.var_id, font=(
            "arial", int(0.0098*w1)))
        entry_id.place(relx=0.27, rely=0.013)

        # FetchData Button
        btnFetch = Button(labelFrameLeftSide, text="Fetch", command=self.Fetch_Id, font=(
            "arial", int(0.0088*w1), "bold"), bg="black", fg='gold', width=int(0.009*w1))
        btnFetch.place(relx=0.774, rely=0.011)

        # Reservation No
        lbl_booking_id = Label(labelFrameLeftSide, text="Reservation No", font=(
            "arial", int(0.0097*w1), "bold"))
        lbl_booking_id.place(relx=0, rely=0.095)

        entry_book_id = ttk.Entry(labelFrameLeftSide, width=int(0.0062*w1), textvariable=self.var_reserve_no, font=(
            "arial", int(0.0098*w1)),state="readonly")
        entry_book_id.place(relx=0.30, rely=0.095)

        # Customer Name
        lbl_cust_id = Label(labelFrameLeftSide, text="Customer Name", font=(
            "arial", int(0.0098*w1), "bold"))
        lbl_cust_id.place(relx=0, rely=0.177)

        entry_id = ttk.Entry(labelFrameLeftSide, width=int(0.025*w1), textvariable=self.var_name, font=(
            "arial", int(0.0098*w1)),state="readonly")
        entry_id.place(relx=0.35, rely=0.177)

        # Customer Contact
        lbl_cust_id = Label(labelFrameLeftSide, text="Contact", font=(
            "arial", int(0.0097*w1), "bold"))
        lbl_cust_id.place(relx=0.48, rely=0.095)

        entry_id = ttk.Entry(labelFrameLeftSide, width=int(0.0133*w1), textvariable=self.var_contact, font=(
            "arial", int(0.0098*w1)),state="readonly")
        entry_id.place(relx=0.64, rely=0.095)

        # Arrival Date
        arrival_date = Label(labelFrameLeftSide, text="Arrival Date",
                              font=("arial", int(0.0098*w1), "bold"))
        arrival_date.place(relx=0, rely=0.259)

        txtarrival_date = DateEntry(labelFrameLeftSide, width=int(0.0133*w1), background='darkblue', textvariable=self.var_arrival,
                                     date_pattern='dd/mm/yyyy', font=("arial", int(0.0098*w1)), foreground='white', borderwidth=2)
        txtarrival_date.place(relx=0.35, rely=0.259)

        # Departure Date
        departure_date = Label(labelFrameLeftSide, text="Departure Date",
                               font=("arial", int(0.0098*w1), "bold"))
        departure_date.place(relx=0, rely=0.341)

        txtdeparture_date = DateEntry(labelFrameLeftSide, width=int(0.0133*w1), background='darkblue', textvariable=self.var_departure,
                                      date_pattern='dd/mm/yyyy', font=("arial", int(0.0098*w1)), foreground='white', borderwidth=2)
        txtdeparture_date.place(relx=0.35, rely=0.341)

        # Room type
        label_Roomtype = Label(labelFrameLeftSide, text="Room Type",
                               font=("arial", int(0.0098*w1), "bold"))
        label_Roomtype.place(relx=0, rely=0.418)

        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        roomtypes = my_cursor.fetchall()

        combo_Roomtype = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_roomtype, font=(
            "arial", int(0.0088*w1), "bold"), width=int(0.0088*w1), state="readonly")
        combo_Roomtype["value"] = roomtypes
        combo_Roomtype.current(0)
        combo_Roomtype.place(relx=0.25, rely=0.423)

        # Room
        lblRoom = Label(labelFrameLeftSide, text="Room",
                                 font=("arial", int(0.0098*w1), "bold"))
        lblRoom.place(relx=0.575, rely=0.418)

        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_room, font=(
            "arial", int(0.0088*w1), "bold"), width=int(0.0088*w1), state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.place(relx=0.715, rely=0.423)

        # Number of Persons
        lblPersons = Label(labelFrameLeftSide, text="No. of Persons",
                        font=("arial", int(0.0098*w1), "bold"))
        lblPersons.place(relx=0, rely=0.5)

        txtPersons = ttk.Entry(
            labelFrameLeftSide, width=int(0.01*w1), textvariable=self.var_persons, font=("arial", int(0.0098*w1)))
        txtPersons.place(relx=0.31, rely=0.505)

        # Mode of Payment
        lblPayment = Label(labelFrameLeftSide, text="Payment Mode",
                            font=("arial", int(0.0098*w1), "bold"))
        lblPayment.place(relx=0, rely=0.582)

        combo_Payment = ttk.Combobox(
            labelFrameLeftSide, width=int(0.01*w1), textvariable=self.var_payment, font=("arial", int(0.0098*w1)),state="readonly")
        combo_Payment["value"]=("Cash","CreditCard")
        combo_Payment.current(0)
        combo_Payment.place(relx=0.31, rely=0.587)

        # No of Days
        lblNoOfDays = Label(labelFrameLeftSide, text="No of Days",
                            font=("arial", int(0.0098*w1), "bold"))
        lblNoOfDays.place(relx=0, rely=0.664)

        entryNoOfDays = ttk.Entry(
            labelFrameLeftSide, width=int(0.0062*w1), textvariable=self.var_days, font=("arial", int(0.0098*w1)), state="readonly")
        entryNoOfDays.place(relx=0.25, rely=0.669)


        # Extra Beds
        lblExtraBeds = Label(labelFrameLeftSide, text="Extra Beds",
                             font=("arial", int(0.0098*w1), "bold"))
        lblExtraBeds.place(relx=0.499, rely=0.664)

        txtExtraBeds = ttk.Entry(
            labelFrameLeftSide, width=int(0.0088*w1), textvariable=self.var_extraBeds, font=("arial", int(0.0098*w1)))
        txtExtraBeds.place(relx=0.75, rely=0.669)


        # =============buttons==============
        btn_frame = LabelFrame(labelFrameLeftSide, bd=2, relief=RIDGE)
        btn_frame.place(relx=0, rely=0.86, width=0.96*w2, height=0.12*h2)
        # 360 30

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", int(0.0095*w1), "bold"), bg="black", fg='gold', width=int(0.008*w1), height=int(0.006*h2))
        btnAdd.place(relx=0, rely=0)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", int(0.0095*w1), "bold"), bg="black", fg='gold', width=int(0.008*w1), height=int(0.006*h2))
        btnUpdate.place(relx=0.25, rely=0)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_booking, font=(
            "arial", int(0.0095*w1), "bold"), bg="black", fg='gold', width=int(0.008*w1), height=int(0.006*h2))
        btnDelete.place(relx=0.50, rely=0)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", int(0.0095*w1), "bold"), bg="black", fg='gold', width=int(0.008*w1), height=int(0.006*h2))
        btnReset.place(relx=0.75, rely=0)

        # ==========table frame search system=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Reservation Details & Search", font=(
            "times new roman", int(0.015*w1), "bold"))
        table_Frame.place(relx=0.34, rely=0.515, width=0.655*w1, height=0.474*h1)
        table_Frame.update()
        w3, h3 = table_Frame.winfo_width(), table_Frame.winfo_height()
        # 740 230

        lbl_SearchBar = Label(table_Frame, text="Search By:", font=(
            "arial", int(0.0097*w1), "bold"), bg='red', fg='white')
        lbl_SearchBar.place(relx=0.005, rely=0.02)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(table_Frame, textvariable=self.search_var, font=(
            "arial", int(0.0097*w1), "bold"), width=int(0.0133*w1), state="readonly")
        combo_Search["value"] = ("CNIC_Passport","ReserveID","Room")
        combo_Search.current(0)
        combo_Search.place(relx=0.115, rely=0.02)

        self.search_text = StringVar()
        txt_Search = ttk.Entry(
            table_Frame, width=int(0.0265*w1), textvariable=self.search_text, font=("arial", int(0.0097*w1)))
        txt_Search.place(relx=0.3, rely=0.02)

        btnSearch = Button(table_Frame, text="Search", command=self.search, font=(
            "arial", int(0.0097*w1), "bold"), bg="green", fg='white', width=int(0.0088*w1))
        btnSearch.place(relx=0.60, rely=0)

        btnShowAll = Button(table_Frame, text="Show All", command=self.fetch_data, font=(
            "arial", int(0.0097*w1), "bold"), bg="green", fg='white', width=int(0.0088*w1))
        btnShowAll.place(relx=0.72, rely=0)

        # ===============show booking table==============
        details_table = LabelFrame(table_Frame, bd=2, relief=RIDGE)
        details_table.place(relx=0, rely=0.16, width=0.99*w3, height=0.74*h3)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Reservation_Table = ttk.Treeview(details_table, column=("ReservationNo","CNIC_Passport", "Name","Contact","ArrivalDate", "DepartureDate", "RoomType", "Room",
                                                              "Persons", "Payment","Days","ExtraBeds"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Reservation_Table.xview)
        scroll_y.config(command=self.Reservation_Table.yview)

        self.Reservation_Table.heading("ReservationNo", text="ReservationNo")
        self.Reservation_Table.heading("CNIC_Passport", text="CNIC/Passport")
        self.Reservation_Table.heading("Name", text="Name")
        self.Reservation_Table.heading("Contact", text="Contact")
        self.Reservation_Table.heading("ArrivalDate", text="Arrival Date")
        self.Reservation_Table.heading("DepartureDate", text="Departure Date")
        self.Reservation_Table.heading("RoomType", text="Room Type")
        self.Reservation_Table.heading("Room", text="Room No")
        self.Reservation_Table.heading("Persons", text="Persons")
        self.Reservation_Table.heading("Payment", text="Payment")
        self.Reservation_Table.heading("Days", text="Days")
        self.Reservation_Table.heading("ExtraBeds", text="ExtraBeds")

        self.Reservation_Table["show"] = "headings"

        self.Reservation_Table.column("ReservationNo", width=90)
        self.Reservation_Table.column("CNIC_Passport", width=100)
        self.Reservation_Table.column("Name", width=150)
        self.Reservation_Table.column("Contact", width=150)
        self.Reservation_Table.column("ArrivalDate", width=100)
        self.Reservation_Table.column("DepartureDate", width=100)
        self.Reservation_Table.column("RoomType", width=70)
        self.Reservation_Table.column("Room", width=70)
        self.Reservation_Table.column("Persons", width=70)
        self.Reservation_Table.column("Payment", width=50)
        self.Reservation_Table.column("Days", width=50)
        self.Reservation_Table.column("ExtraBeds", width=70)
        self.Reservation_Table.pack(fill=BOTH, expand=1)

        self.Reservation_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ============Add Reservation Data===========
    def add_data(self):
        if self.var_id.get() == "" or self.var_arrival.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into reservation values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                    self.var_reserve_no.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_contact.get(),
                    self.var_arrival.get(),
                    self.var_departure.get(),
                    self.var_roomtype.get(),
                    self.var_room.get(),
                    self.var_persons.get(),
                    self.var_payment.get(),
                    self.var_days.get(),
                    self.var_extraBeds.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Room Reserved", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

     # ===========fetch data=================
    def fetch_data(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from reservation")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Reservation_Table.delete(
                *self.Reservation_Table.get_children())
            for i in rows:
                self.Reservation_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =============Get data to the table==========
    def get_cursor(self, event=""):
        cursor_row = self.Reservation_Table.focus()
        content = self.Reservation_Table.item(cursor_row)
        row = content["values"]

        self.var_reserve_no.set(row[0])
        self.var_id.set(row[1])
        self.var_name.set(row[2])
        self.var_contact.set(row[3])
        self.var_arrival.set(row[4])
        self.var_departure.set(row[5])
        self.var_roomtype.set(row[6])
        self.var_room.set(row[7])
        self.var_persons.set(row[8])
        self.var_payment.set(row[9])
        self.var_days.set(row[10])
        self.var_extraBeds.set(row[11])

    # ============update data===============
    def update(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please enter CNIC/Passport No.", self.root)
        else:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            my_cursor.execute("update reservation set CNIC_Passport=?,Name=?,Contact=?,ArrivalDate=?,DepartureDate=?,RoomType=?,Room=?,Persons=?,Payment=%s,Days=?,ExtraBeds=? where ReservationNo=?", (

                self.var_id.get(),
                self.var_name.get(),
                self.var_contact.get(),
                self.var_arrival.get(),
                self.var_roomtype.get(),
                self.var_departure.get(),
                self.var_room.get(),
                self.var_persons.get(),
                self.var_payment.get(),
                self.var_days.get(),
                self.var_extraBeds.get(),
                self.var_reserve_no.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Reservation details has been updated successfully", parent=self.root)

    # ==============delete================
    def delete_booking(self):
        delete_booking = messagebox.askyesno(
            "Hotel Management Software", "Do you want to delete this reservation?", parent=self.root)
        if delete_booking > 0:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = "delete from reservation where ReservationNo=?"
            value = (self.var_reserve_no.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_booking:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # ===============Reset=================
    def reset(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.var_arrival.set(""),
        self.var_departure.set(""),
        self.var_roomtype.set(""),
        self.var_room.set(""),
        self.var_persons.set(""),
        self.var_payment.set(""),
        self.var_days.set(""),
        self.var_extraBeds.set("")
        x = random.randint(1000, 99999)
        self.var_reserve_no.set(str(x))

     # ===========Fetch Reservation Card=============
    def Fetch_Id(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Please enter CNIC/Passport No.", parent=self.root)
        else:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = ("select Name from customer where CNIC_Passport=?")
            value = (self.var_id.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            self.var_name.set(row)

            query1 = ("select Mobile from customer where CNIC_Passport=?")
            value = (self.var_id.get(),)
            my_cursor.execute(query1, value)
            row = my_cursor.fetchone()
            row = ''.join(row)
            self.var_contact.set(row)

            if row == None:
                messagebox.showerror(
                    "Error", "This number is not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=385, y=65, width=730, height=185)

                # Label Name
                lblName = Label(showDataFrame, text="Name:",
                                font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row,
                            font=("arial", 12))
                lbl.place(x=55, y=0)

                # Label Gender
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where CNIC_Passport=?")
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataFrame, text="Gender:",
                                  font=("arial", 12, "bold"))
                lblGender.place(x=0, y=25)

                lbl2 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl2.place(x=70, y=25)

                # Label Age
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Age from customer where CNIC_Passport=?")
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAge = Label(showDataFrame, text="Age:",
                               font=("arial", 12, "bold"))
                lblAge.place(x=0, y=50)

                lbl3 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl3.place(x=40, y=50)


                # Label Email
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Email from customer where CNIC_Passport=?")
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataFrame, text="Email:",
                                 font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=75)

                lbl4 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl4.place(x=55, y=75)

                # Label CNIC/Passport No.
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select CNIC_Passport from customer where CNIC_Passport=?")
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataFrame, text="CNIC/Passport:",
                                 font=("arial", 11, "bold"))
                lblEmail.place(x=0, y=100)

                lbl5 = Label(showDataFrame, text=row,
                             font=("arial", 11))
                lbl5.place(x=120, y=100)

                # Label Nationality
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where CNIC_Passport=?")
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataFrame, text="Nationality:",
                                       font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=125)

                lbl6 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl6.place(x=100, y=125)

                # Label Contact
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Mobile from customer where CNIC_Passport=?")
                value = (self.var_id.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAge = Label(showDataFrame, text="Mobile No:",
                               font=("arial", 12, "bold"))
                lblAge.place(x=0, y=150)

                lbl3 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl3.place(x=90, y=150)

                # Arrival Date
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select ArrivalDate from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblArrival = Label(showDataFrame, text="Arrival Date:",
                               font=("arial", 12, "bold"))
                lblArrival.place(x=270, y=25)

                lbl5 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl5.place(x=370, y=25)

                # Departure Date
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select DepartureDate from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblDeparture = Label(showDataFrame, text="Departure Date:",
                               font=("arial", 12, "bold"))
                lblDeparture.place(x=270, y=50)

                lbl5 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl5.place(x=400, y=50)

                # No of days calculate
                inDate = self.var_arrival.get()
                outDate = self.var_departure.get()
                inDate = datetime.strptime(inDate, "%d/%m/%Y")
                outDate = datetime.strptime(outDate, "%d/%m/%Y")
                self.var_days.set(abs(outDate-inDate).days)

                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Days from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNoOfDays = Label(showDataFrame, text="No of Days:",
                               font=("arial", 12, "bold"))
                lblNoOfDays.place(x=270, y=0)

                lbl4 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl4.place(x=370, y=0)

                # Room Type
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select RoomType from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblRoomType = Label(showDataFrame, text="Room Type:",
                               font=("arial", 12, "bold"))
                lblRoomType.place(x=270, y=75)

                lbl6 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl6.place(x=370, y=75)

                # Room 
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Room from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblRoomType = Label(showDataFrame, text="Room:",
                               font=("arial", 12, "bold"))
                lblRoomType.place(x=270, y=100)

                lbl7 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl7.place(x=330, y=100)

                # No of Persons
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Persons from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblPersons = Label(showDataFrame, text="No of Persons:",
                               font=("arial", 12, "bold"))
                lblPersons.place(x=270, y=125)

                lbl8 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl8.place(x=390, y=125)

                # Payment Method
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select Payment from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblPayment = Label(showDataFrame, text="Payment Method:",
                               font=("arial", 12, "bold"))
                lblPayment.place(x=270, y=150)

                lbl9 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl9.place(x=410, y=150)

                # Extra Beds
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                query = ("select ExtraBeds from reservation where ReservationNo=?")
                value = (self.var_reserve_no.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblExtraBeds = Label(showDataFrame, text="Extra Beds:",
                               font=("arial", 12, "bold"))
                lblExtraBeds.place(x=520, y=0)

                lbl10 = Label(showDataFrame, text=row,
                             font=("arial", 12))
                lbl10.place(x=620, y=0)

                # FetchData Button
                btnFetch = Button(showDataFrame, text="Generate Card", command=self.Reserve_card_prin, font=(
                    "arial", 10, "bold"), bg="black", fg='gold', width=12)
                btnFetch.place(x=600, y=145)


    # ==========Search System==========
    def search(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from reservation where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Reservation_Table.delete(
                *self.Reservation_Table.get_children())
            for i in rows:
                self.Reservation_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #============Bill Window=============
    def Reserve_card_prin(self):
        self.new_window = Toplevel(self.root)
        self.app = Reserve_Card(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Reservation(root)
    root.mainloop()
