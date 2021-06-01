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
        self.root.geometry("1120x460+237+205")

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
            "times new roman", 20, "bold"), bg="grey", fg="gold", bd=2, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1120, height=60)

        # ========logo==============
        img2 = Image.open(
            r"images/logo.png")
        img2 = img2.resize((60, 60), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=0, y=0, width=80, height=60)

        # =============labelframe==========
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="Reservation Details", font=(
            "times new roman", 17, "bold"), padx=2,)
        labelFrameLeftSide.place(x=5, y=60, width=380, height=390)

         # =========labels and entries========
        # Customer Id
        lbl_cust_id = Label(labelFrameLeftSide, text="Customer ID", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=0, column=0, sticky=W)

        entry_id = ttk.Entry(labelFrameLeftSide, width=20, textvariable=self.var_id, font=(
            "arial", 11))
        entry_id.grid(row=0, column=1, sticky=W)

        # FetchData Button
        btnFetch = Button(labelFrameLeftSide, text="Fetch", command=self.Fetch_Id, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=8)
        btnFetch.place(x=290, y=1)

        # Reservation No
        lbl_booking_id = Label(labelFrameLeftSide, text="Reservation No", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_booking_id.grid(row=1, column=0, sticky=W)

        entry_book_id = ttk.Entry(labelFrameLeftSide, width=7, textvariable=self.var_reserve_no, font=(
            "arial", 10),state="readonly")
        entry_book_id.grid(row=1, column=1, sticky=W)

        # Customer Name
        lbl_cust_id = Label(labelFrameLeftSide, text="Customer Name", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=2, column=0, sticky=W)

        entry_id = ttk.Entry(labelFrameLeftSide, width=30, textvariable=self.var_name, font=(
            "arial", 11),state="readonly")
        entry_id.grid(row=2, column=1, sticky=W)

        # Customer Contact
        lbl_cust_id = Label(labelFrameLeftSide, text="Contact", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_cust_id.place(x=180, y=32)

        entry_id = ttk.Entry(labelFrameLeftSide, width=15, textvariable=self.var_contact, font=(
            "arial", 11),state="readonly")
        entry_id.place(x=240, y=38)

        # Arrival Date
        arrival_date = Label(labelFrameLeftSide, text="Arrival Date",
                              font=("arial", 11, "bold"), padx=2, pady=6)
        arrival_date.grid(row=3, column=0, sticky=W)

        txtarrival_date = DateEntry(labelFrameLeftSide, width=15, background='darkblue', textvariable=self.var_arrival,
                                     date_pattern='dd/mm/yyyy', font=("arial", 11), foreground='white', borderwidth=2)
        txtarrival_date.grid(row=3, column=1, sticky=W)

        # Departure Date
        departure_date = Label(labelFrameLeftSide, text="Departure Date",
                               font=("arial", 11, "bold"), padx=2, pady=6)
        departure_date.grid(row=4, column=0, sticky=W)

        txtdeparture_date = DateEntry(labelFrameLeftSide, width=15, background='darkblue', textvariable=self.var_departure,
                                      date_pattern='dd/mm/yyyy', font=("arial", 11), foreground='white', borderwidth=2)
        txtdeparture_date.grid(row=4, column=1, sticky=W)

        # Room type
        label_Roomtype = Label(labelFrameLeftSide, text="Room Type",
                               font=("arial", 11, "bold"), padx=2, pady=6)
        label_Roomtype.grid(row=5, column=0, sticky=W)

        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        roomtypes = my_cursor.fetchall()

        combo_Roomtype = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_roomtype, font=(
            "arial", 10, "bold"), width=10, state="readonly")
        combo_Roomtype["value"] = roomtypes
        combo_Roomtype.current(0)
        combo_Roomtype.grid(row=5, column=1,sticky=W)

        # Room
        lblRoom = Label(labelFrameLeftSide, text="Room",
                                 font=("arial", 11, "bold"), padx=2, pady=6)
        lblRoom.place(x=220, y=167)

        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_room, font=(
            "arial", 10, "bold"), width=10, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.place(x=268, y=172)

        # Number of Persons
        lblPersons = Label(labelFrameLeftSide, text="No. of Persons",
                        font=("arial", 11, "bold"), padx=2, pady=6)
        lblPersons.grid(row=6, column=0, sticky=W)

        txtPersons = ttk.Entry(
            labelFrameLeftSide, width=20, textvariable=self.var_persons, font=("arial", 11))
        txtPersons.grid(row=6, column=1, sticky=W)

        # Mode of Payment
        lblPayment = Label(labelFrameLeftSide, text="Payment Mode",
                            font=("arial", 11, "bold"), padx=2, pady=6)
        lblPayment.grid(row=7, column=0, sticky=W)

        combo_Payment = ttk.Combobox(
            labelFrameLeftSide, width=15, textvariable=self.var_payment, font=("arial", 11),state="readonly")
        combo_Payment["value"]=("Cash","CreditCard")
        combo_Payment.current(0)
        combo_Payment.grid(row=7, column=1,sticky=W)

        # No of Days
        lblNoOfDays = Label(labelFrameLeftSide, text="No of Days",
                            font=("arial", 11, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=8, column=0, sticky=W)

        entryNoOfDays = ttk.Entry(
            labelFrameLeftSide, width=7, textvariable=self.var_days, font=("arial", 11), state="readonly")
        entryNoOfDays.grid(row=8, column=1,sticky=W)


        # Extra Beds
        lblExtraBeds = Label(labelFrameLeftSide, text="Extra Beds",
                             font=("arial", 11, "bold"), padx=2, pady=6)
        lblExtraBeds.place(x=185, y=270)

        txtExtraBeds = ttk.Entry(
            labelFrameLeftSide, width=10, textvariable=self.var_extraBeds, font=("arial", 11))
        txtExtraBeds.place(x=270, y=274)


        # =============buttons==============
        btn_frame = LabelFrame(labelFrameLeftSide, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=325, width=360, height=30)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=9)
        btnAdd.grid(row=0, column=0, padx=3)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=9)
        btnUpdate.grid(row=0, column=1, padx=3)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_booking, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=9)
        btnDelete.grid(row=0, column=2, padx=3)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=9)
        btnReset.grid(row=0, column=3, padx=3)

        # ==========table frame search system=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Reservation Details & Search", font=(
            "times new roman", 17, "bold"), padx=2,)
        table_Frame.place(x=385, y=250, width=730, height=200)

        lbl_SearchBar = Label(table_Frame, text="Search By:", font=(
            "arial", 11, "bold"), bg='red', fg='white')
        lbl_SearchBar.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(table_Frame, textvariable=self.search_var, font=(
            "arial", 11, "bold"), width=15, state="readonly")
        combo_Search["value"] = ("CNIC_Passport","ReserveID","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=3)

        self.search_text = StringVar()
        txt_Search = ttk.Entry(
            table_Frame, width=30, textvariable=self.search_text, font=("arial", 11))
        txt_Search.grid(row=0, column=2, padx=3)

        btnSearch = Button(table_Frame, text="Search", command=self.search, font=(
            "arial", 11, "bold"), bg="black", fg='gold', width=10)
        btnSearch.grid(row=0, column=3, padx=3)

        btnShowAll = Button(table_Frame, text="Show All", command=self.fetch_data, font=(
            "arial", 11, "bold"), bg="black", fg='gold', width=10)
        btnShowAll.grid(row=0, column=4, padx=3)

        # ===============show booking table==============
        details_table = LabelFrame(table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=40, width=725, height=130)

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
