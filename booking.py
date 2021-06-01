import random
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
from tkcalendar import DateEntry
from bill import Bill

import mysql.connector
import sqlite3
from PIL import Image, ImageTk


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking")
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
        
        self.var_book_no = StringVar()
        x = random.randint(1000, 99999)
        self.var_book_no.set(str(x))
        
        self.var_name = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_room_price = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_roomcharge = StringVar()
        self.var_othercharge = StringVar()
        self.var_total = StringVar()

        # ===========title=============
        lbl_title = Label(self.root, text="Room Booking", font=(
            "times new roman", int(0.017*w1), "bold"), bg="grey", fg="gold", bd=2, relief=RIDGE)
        lbl_title.place(relx=0, rely=0, width=w1, height=0.124*h1)

        # ========logo==============
        img2 = Image.open(
            r"images/logo.png")
        img2 = img2.resize((60, 60), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(x=0, y=0, width=80, height=60)

        # =============labelframe==========
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="Booking Details", font=(
            "times new roman", 17, "bold"), padx=2,)
        labelFrameLeftSide.place(x=5, y=60, width=370, height=390)

        # =========labels and entries========
        # Customer Id
        lbl_cust_id = Label(labelFrameLeftSide, text="Customer ID", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=0, column=0, sticky=W)

        entry_id = ttk.Entry(labelFrameLeftSide, width=19, textvariable=self.var_id, font=(
            "arial", 11))
        entry_id.grid(row=0, column=1, sticky=W)

        # FetchData Button
        btnFetch = Button(labelFrameLeftSide, text="Fetch", command=self.Fetch_Id, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=8)
        btnFetch.place(x=280, y=1)

        # Booking No
        lbl_booking_no = Label(labelFrameLeftSide, text="Booking No.", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_booking_no.grid(row=1, column=0, sticky=W)

        entry_book_no = ttk.Entry(labelFrameLeftSide, width=10, textvariable=self.var_book_no, font=(
            "arial", 11),state="readonly")
        entry_book_no.grid(row=1, column=1, sticky=W)

        # Customer Name
        lbl_cust_name = Label(labelFrameLeftSide, text="Customer Name", font=(
            "times new roman", 11, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=2, column=0, sticky=W)

        entry_name = ttk.Entry(labelFrameLeftSide, width=29, textvariable=self.var_name, font=(
            "arial", 11),state="readonly")
        entry_name.grid(row=2, column=1, sticky=W)

        # Check-in date
        check_in_date = Label(labelFrameLeftSide, text="Check-In",
                              font=("arial", 10, "bold"), padx=2, pady=6)
        check_in_date.grid(row=3, column=0, sticky=W)

        txtcheck_in_date = DateEntry(labelFrameLeftSide, width=12, background='darkblue', textvariable=self.var_checkin,
                                     date_pattern='dd/mm/yyyy', font=("arial", 10), foreground='white', borderwidth=2)
        txtcheck_in_date.grid(row=3, column=1, sticky=W)

        # txtcheck_in_date = ttk.Entry(
        #     labelFrameLeftSide, width=30, textvariable=self.var_checkin, font=("arial", 12))
        # txtcheck_in_date.grid(row=1, column=1)

        # Check-out date
        check_out_date = Label(labelFrameLeftSide, text="Check-Out",
                               font=("arial", 10, "bold"), padx=2, pady=6)
        check_out_date.grid(row=4, column=0, sticky=W)

        txtcheck_out_date = DateEntry(labelFrameLeftSide, width=12, background='darkblue', textvariable=self.var_checkout,
                                      date_pattern='dd/mm/yyyy', font=("arial", 10), foreground='white', borderwidth=2)
        txtcheck_out_date.grid(row=4, column=1, sticky=W)

        # txtcheck_out_date = ttk.Entry(
        #     labelFrameLeftSide, width=30, textvariable=self.var_checkout, font=("arial", 12))
        # txtcheck_out_date.grid(row=2, column=1)

        # Room type
        label_Roomtype = Label(labelFrameLeftSide, text="Room Type",
                               font=("arial", 10, "bold"), padx=2, pady=6)
        label_Roomtype.grid(row=5, column=0, sticky=W)

        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        roomtypes = my_cursor.fetchall()

        combo_Roomtype = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_roomtype, font=(
            "arial", 10, "bold"), width=12, state="readonly")
        combo_Roomtype["value"] = roomtypes
        combo_Roomtype.current(0)
        combo_Roomtype.grid(row=5, column=1, sticky=W)

        # Available Room
        lblAvailableRoom = Label(labelFrameLeftSide, text="Room",
                                 font=("arial", 10, "bold"), padx=2, pady=6)
        lblAvailableRoom.place(x=225, y=130)

        # txtAvailableRoom = ttk.Entry(
        #     labelFrameLeftSide, width=30, textvariable=self.var_roomavailable, font=("arial", 12))
        # txtAvailableRoom.grid(row=4, column=1)
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_roomavailable, font=(
            "arial", 10, "bold"), width=6, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.place(x=273, y=136)

        # Room Price
        lblRoomPrice = Label(labelFrameLeftSide, text="Price",
                                 font=("arial", 10, "bold"), padx=2, pady=6)
        lblRoomPrice.place(x=225, y=163)

        combo_Search = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_room_price, font=(
            "arial", 10, "bold"), width=9, state="readonly")
        combo_Search["value"] = ("2000","2500","3000","3500","4000","4500","5000","5500","6000","6500","7000","7500","8000","8500","9000","9500","10000")
        combo_Search.current(0)
        combo_Search.place(x=270, y=168)

        # Meal
        lblMeal = Label(labelFrameLeftSide, text="Meal Price",
                        font=("arial", 10, "bold"), padx=2, pady=6)
        lblMeal.grid(row=6, column=0, sticky=W)

        txtMeal = ttk.Entry(
            labelFrameLeftSide, width=13, textvariable=self.var_meal, font=("arial", 10))
        txtMeal.grid(row=6, column=1, sticky=W)

        # Other
        lblOther = Label(labelFrameLeftSide, text="Other",
                        font=("arial", 10, "bold"), padx=2, pady=6)
        lblOther.place(x=215,y=196)

        txtOther = ttk.Entry(
            labelFrameLeftSide, width=13, textvariable=self.var_othercharge, font=("arial", 10))
        txtOther.place(x=260,y=200)

        # Room Charge
        lblNoOfDays = Label(labelFrameLeftSide, text="Room Charge",
                            font=("arial", 10, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=7, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(
            labelFrameLeftSide, width=16, textvariable=self.var_roomcharge, font=("arial", 10),state="readonly")
        txtNoOfDays.grid(row=7, column=1,sticky=W)

        # Days
        lblSubTotal = Label(labelFrameLeftSide, text="Days",
                            font=("arial", 10, "bold"), padx=2, pady=6)
        lblSubTotal.place(x=235, y=227)

        txtSubTotal = ttk.Entry(
            labelFrameLeftSide, width=10, textvariable=self.var_noofdays, font=("arial", 10),state="readonly")
        txtSubTotal.place(x=280, y=232)

        # Total Cost
        lblTotalCost = Label(labelFrameLeftSide, text="Total Cost",
                             font=("arial", 10, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=8, column=0, sticky=W)

        txtTotalCost = ttk.Entry(
            labelFrameLeftSide, width=16, textvariable=self.var_total, font=("arial", 10),state="readonly")
        txtTotalCost.grid(row=8, column=1,sticky=W)

        # =========bill & total button===============
        btnCalc = Button(labelFrameLeftSide, text="Calculate", command=self.total, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=12)
        btnCalc.grid(row=10, column=0, padx=2, sticky=W)

        btnBill = Button(labelFrameLeftSide, text="Generate Bill", command=self.Bill, font=(
            "arial", 10, "bold"), bg="black", fg='gold', width=12)
        btnBill.grid(row=10, column=1, padx=2, sticky=W)

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

        # =============right side image====================
        img3 = Image.open(
            r"images/room2.jpg")
        img3 = img3.resize((280, 180), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=830, y=65, width=280, height=180)

        # ==========table frame search system=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search", font=(
            "times new roman", 17, "bold"), padx=2,)
        table_Frame.place(x=385, y=250, width=730, height=200)

        lbl_SearchBar = Label(table_Frame, text="Search By:", font=(
            "arial", 11, "bold"), bg='red', fg='white')
        lbl_SearchBar.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(table_Frame, textvariable=self.search_var, font=(
            "arial", 11, "bold"), width=15, state="readonly")
        combo_Search["value"] = ("CNIC_Passport","BookID","Room")
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

        self.Room_Table = ttk.Treeview(details_table, column=("BookingNo","CNIC_Passport","Name", "CheckInDate", "CheckOutDate", "RoomType", "Room","RoomPrice",
                                                              "Meal", "Days","RoomCharge","OtherCharge","Total"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("BookingNo", text="BookingNo")
        self.Room_Table.heading("CNIC_Passport", text="CNIC/Passport")
        self.Room_Table.heading("Name", text="Name")
        self.Room_Table.heading("CheckInDate", text="Check-In")
        self.Room_Table.heading("CheckOutDate", text="Check-Out")
        self.Room_Table.heading("RoomType", text="Room Type")
        self.Room_Table.heading("Room", text="Room No")
        self.Room_Table.heading("RoomPrice", text="Room Price")
        self.Room_Table.heading("Meal", text="Meal")
        self.Room_Table.heading("Days", text="Days")
        self.Room_Table.heading("RoomCharge", text="RoomCharge")
        self.Room_Table.heading("OtherCharge", text="OtherCharge")
        self.Room_Table.heading("Total", text="Total")


        self.Room_Table["show"] = "headings"

        self.Room_Table.column("BookingNo", width=70)
        self.Room_Table.column("CNIC_Passport", width=100)
        self.Room_Table.column("Name", width=150)
        self.Room_Table.column("CheckInDate", width=80)
        self.Room_Table.column("CheckOutDate", width=80)
        self.Room_Table.column("RoomType", width=70)
        self.Room_Table.column("Room", width=70)
        self.Room_Table.column("RoomPrice", width=70)
        self.Room_Table.column("Meal", width=50)
        self.Room_Table.column("Days", width=50)
        self.Room_Table.column("RoomCharge", width=100)
        self.Room_Table.column("OtherCharge", width=100)
        self.Room_Table.column("Total", width=100)
        self.Room_Table.pack(fill=BOTH, expand=1)

        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ============Add Booking Data===========
    def add_data(self):
        if self.var_id.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into booking values(?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                    self.var_book_no.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_room_price.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_roomcharge.get(),
                    self.var_othercharge.get(),
                    self.var_total.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    # ===========fetch data=================
    def fetch_data(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from booking")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(
                *self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # =============Get data to the table==========
    def get_cursor(self, event=""):
        cursor_row = self.Room_Table.focus()
        content = self.Room_Table.item(cursor_row)
        row = content["values"]

        self.var_book_no.set(row[0])
        self.var_id.set(row[1])
        self.var_name.set(row[2])
        self.var_checkin.set(row[3])
        self.var_checkout.set(row[4])
        self.var_roomtype.set(row[5])
        self.var_roomavailable.set(row[6])
        self.var_room_price.set(row[7])
        self.var_meal.set(row[8])
        self.var_noofdays.set(row[9])
        self.var_roomcharge.set(row[10])
        self.var_othercharge.set(row[11])
        self.var_total.set(row[12])

    # ============update data===============
    def update(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please enter CNIC/Passport No.", self.root)
        else:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            my_cursor.execute("update booking set CNIC_Passport=?,Name=?,CheckInDate=?,CheckOutDate=?,RoomType=?,Room=?,RoomPrice=?,Meal=?,Days=?,RoomCharge=?,OtherCharge=?,Total=? where BookingNo=?", (

                self.var_id.get(),
                self.var_name.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_room_price.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_roomcharge.get(),
                self.var_othercharge.get(),
                self.var_total.get(),
                self.var_book_no.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Booking details has been updated successfully", parent=self.root)

    # ==============delete================
    def delete_booking(self):
        delete_booking = messagebox.askyesno(
            "Hotel Management Software", "Do you want to delete this booking?", parent=self.root)
        if delete_booking > 0:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = "delete from booking where BookingNo=?"
            value = (self.var_book_no.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_booking:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # ===============Reset=================
    def reset(self):
        #self.var_book_id.set(""),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_room_price.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_roomcharge.set(""),
        self.var_othercharge.set(""),
        self.var_total.set("")
        x = random.randint(1000, 99999)
        self.var_book_no.set(str(x))

    # ===========All data fetch=============
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

            if row == None:
                messagebox.showerror(
                    "Error", "This number is not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=385, y=65, width=440, height=180)

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

                # Label Nationaluty
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

    # ==========Search System==========
    def search(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from booking where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(
                *self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ==========Billing================
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        meal_price = int(self.var_meal.get())
        days = int(self.var_noofdays.get())
        other = int(self.var_othercharge.get())
        rent = int(self.var_room_price.get())
        room_rent = float(rent*days)
        total = float(room_rent+meal_price+other)
        self.var_roomcharge.set(str(room_rent))
        self.var_total.set(str(total))
        self.var_meal.set(str(meal_price))
        self.var_othercharge.set(str(other))

        # if (self.var_roomtype.get() == "Luxury"):
        #     rent = float(8000)
        #     room_rent = float(rent*days)
        #     total = float(room_rent+meal_price+other)
        #     self.var_roomcharge.set(str(room_rent))
        #     self.var_total.set(str(total))
        #     self.var_meal.set(str(meal_price))
        #     self.var_othercharge.set(str(other))
        # elif (self.var_roomtype.get() == "Deluxe"):
        #     rent = float(6000)
        #     room_rent = float(rent*days)
        #     total = float(room_rent+meal_price+other)
        #     self.var_roomcharge.set(str(room_rent))
        #     self.var_total.set(str(total))
        #     self.var_meal.set(str(meal_price))
        #     self.var_othercharge.set(str(other))
        # elif (self.var_roomtype.get() == "Economy"):
        #     rent = float(4000)
        #     room_rent = float(rent*days)
        #     total = float(room_rent+meal_price+other)
        #     self.var_roomcharge.set(str(room_rent))
        #     self.var_total.set(str(total))
        #     self.var_meal.set(str(meal_price))
        #     self.var_othercharge.set(str(other))

    
    #============Bill Window=============
    def Bill(self):
        self.new_window = Toplevel(self.root)
        self.app = Bill(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
