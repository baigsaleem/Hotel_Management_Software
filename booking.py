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
        global w1
        w1 = int(0.8275*w)
        global h1
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
        img2 = img2.resize((int(0.053*w1), int(0.124*h1)), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(relx=0, rely=0, width=0.070*w1, height=0.124*h1)

        # =============labelframe==========
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="Booking Details", font=(
            "times new roman", int(0.015*w1), "bold"), padx=2,)
        labelFrameLeftSide.place(relx=0.0044, rely=0.124, width=0.332*w1, height=0.866*h1)
        labelFrameLeftSide.update()
        w2, h2 = labelFrameLeftSide.winfo_width(), labelFrameLeftSide.winfo_height()
        # 375 420

        # =========labels and entries========
        # Customer Id
        lbl_cust_id = Label(labelFrameLeftSide, text="Customer ID", font=(
            "arial", int(0.0092*w1), "bold"))
        lbl_cust_id.place(relx=0, rely=0.013)

        entry_id = ttk.Entry(labelFrameLeftSide, width=int(0.0168*w1), textvariable=self.var_id, font=(
            "arial", int(0.0092*w1)))
        entry_id.place(relx=0.31, rely=0.013)

        # FetchData Button
        btnFetch = Button(labelFrameLeftSide, text="Fetch", command=self.Fetch_Id, font=(
            "arial", int(0.0088*w1), "bold"), bg="black", fg='gold', width=int(0.008*w1))
        btnFetch.place(relx=0.78, rely=0.01)

        # Booking No
        lbl_booking_no = Label(labelFrameLeftSide, text="Booking No.", font=(
            "arial", int(0.0092*w1), "bold"))
        lbl_booking_no.place(relx=0, rely=0.095)

        entry_book_no = ttk.Entry(labelFrameLeftSide, width=10, textvariable=self.var_book_no, font=(
            "arial", int(0.0092*w1)),state="readonly")
        entry_book_no.place(relx=0.31, rely=0.095)

        # Customer Name
        lbl_cust_name = Label(labelFrameLeftSide, text="Customer Name", font=(
            "arial", int(0.0092*w1), "bold"))
        lbl_cust_name.place(relx=0, rely=0.18)

        entry_name = ttk.Entry(labelFrameLeftSide, width=int(0.025*w1), textvariable=self.var_name, font=(
            "arial", int(0.0092*w1)),state="readonly")
        entry_name.place(relx=0.31, rely=0.18)

        # Check-in date
        check_in_date = Label(labelFrameLeftSide, text="Check-In",
                              font=("arial", int(0.0092*w1), "bold"))
        check_in_date.place(relx=0, rely=0.265)

        txtcheck_in_date = DateEntry(labelFrameLeftSide, width=int(0.009*w1), background='darkblue', textvariable=self.var_checkin,
                                     date_pattern='dd/mm/yyyy', font=("arial", int(0.0088*w1)), foreground='white', borderwidth=2)
        txtcheck_in_date.place(relx=0.18, rely=0.265)

        # txtcheck_in_date = ttk.Entry(
        #     labelFrameLeftSide, width=30, textvariable=self.var_checkin, font=("arial", 12))
        # txtcheck_in_date.grid(row=1, column=1)

        # Check-out date
        check_out_date = Label(labelFrameLeftSide, text="Check-Out",
                               font=("arial", int(0.0092*w1), "bold"))
        check_out_date.place(relx=0.50, rely=0.265)

        txtcheck_out_date = DateEntry(labelFrameLeftSide, width=int(0.009*w1), background='darkblue', textvariable=self.var_checkout,
                                      date_pattern='dd/mm/yyyy', font=("arial", int(0.0088*w1)), foreground='white', borderwidth=2)
        txtcheck_out_date.place(relx=0.71, rely=0.265)

        # # txtcheck_out_date = ttk.Entry(
        # #     labelFrameLeftSide, width=30, textvariable=self.var_checkout, font=("arial", 12))
        # # txtcheck_out_date.grid(row=2, column=1)

        # Room type
        label_Roomtype = Label(labelFrameLeftSide, text="Room Type",
                               font=("arial", int(0.0092*w1), "bold"))
        label_Roomtype.place(relx=0, rely=0.35)

        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        roomtypes = my_cursor.fetchall()

        combo_Roomtype = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_roomtype, font=(
            "arial", int(0.0088*w1), "bold"), width=int(0.009*w1), state="readonly")
        combo_Roomtype["value"] = roomtypes
        combo_Roomtype.current(0)
        combo_Roomtype.place(relx=0.22, rely=0.35)

        # Available Room
        lblAvailableRoom = Label(labelFrameLeftSide, text="Room No.",
                                 font=("arial", int(0.0092*w1), "bold"))
        lblAvailableRoom.place(relx=0.50, rely=0.35)

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
            "arial", int(0.0088*w1), "bold"), width=int(0.0053*w1), state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.place(relx=0.71, rely=0.35)

        # Room Charges
        lblRoomPrice = Label(labelFrameLeftSide, text="Room Charges",
                                 font=("arial", int(0.0092*w1), "bold"))
        lblRoomPrice.place(relx=0, rely=0.435)

        combo_Search = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_room_price, font=(
            "arial", int(0.0088*w1), "bold"), width=int(0.007*w1), state="readonly")
        combo_Search["value"] = ("2000","2500","3000","3500","4000","4500","5000","5500","6000","6500","7000","7500","8000","8500","9000","9500","10000")
        combo_Search.current(0)
        combo_Search.place(relx=0.28, rely=0.435)

        # Meal Charges
        lblMeal = Label(labelFrameLeftSide, text="Meal Charges",
                        font=("arial", int(0.0092*w1), "bold"))
        lblMeal.place(relx=0.50, rely=0.435)

        txtMeal = ttk.Entry(
            labelFrameLeftSide, width=int(0.01*w1), textvariable=self.var_meal, font=("arial", int(0.0088*w1),"bold"))
        txtMeal.place(relx=0.76, rely=0.435)

        # Other
        lblOther = Label(labelFrameLeftSide, text="Other Charges",
                        font=("arial", int(0.0092*w1), "bold"))
        lblOther.place(relx=0,rely=0.52)

        txtOther = ttk.Entry(
            labelFrameLeftSide, width=int(0.0115*w1), textvariable=self.var_othercharge, font=("arial", int(0.0088*w1),"bold"))
        txtOther.place(relx=0.27,rely=0.52)

        # separator
        separator = ttk.Separator(labelFrameLeftSide, orient='horizontal')
        separator.place(relx=0, rely=0.595, width=0.98*w2, height=0.010*h2)

        # Room Charge
        lblNoOfDays = Label(labelFrameLeftSide, text="Room Price",
                            font=("arial", int(0.0092*w1), "bold"))
        lblNoOfDays.place(relx=0, rely=0.610)

        txtNoOfDays = ttk.Entry(
            labelFrameLeftSide, width=int(0.012*w1), textvariable=self.var_roomcharge, font=("arial", int(0.0088*w1),"bold"),state="readonly")
        txtNoOfDays.place(relx=0.25, rely=0.610)

        # Days
        lblSubTotal = Label(labelFrameLeftSide, text="Days Stayed",
                            font=("arial", int(0.0092*w1), "bold"))
        lblSubTotal.place(relx=0.55, rely=0.610)

        txtSubTotal = ttk.Entry(
            labelFrameLeftSide, width=int(0.0088*w1), textvariable=self.var_noofdays, font=("arial", int(0.0088*w1),"bold"),state="readonly")
        txtSubTotal.place(relx=0.79, rely=0.610)

        # Total Cost
        lblTotalCost = Label(labelFrameLeftSide, text="Total Price",
                             font=("arial", int(0.0092*w1), "bold"))
        lblTotalCost.place(relx=0, rely=0.695)

        txtTotalCost = ttk.Entry(
            labelFrameLeftSide, width=int(0.014*w1), textvariable=self.var_total, font=("arial", int(0.0088*w1),"bold"),state="readonly")
        txtTotalCost.place(relx=0.25, rely=0.695)

        # =========bill & total button===============
        btnCalc = Button(labelFrameLeftSide, text="Calculate", command=self.total, font=(
            "arial", int(0.0088*w1), "bold"), bg="black", fg='gold', width=int(0.01*w1))
        btnCalc.place(relx=0.01, rely=0.77)

        btnBill = Button(labelFrameLeftSide, text="Generate Bill", command=self.Bill, font=(
            "arial", int(0.0088*w1), "bold"), bg="black", fg='gold', width=int(0.015*w1))
        btnBill.place(relx=0.30, rely=0.77)

         # separator
        separator = ttk.Separator(labelFrameLeftSide, orient='horizontal')
        separator.place(relx=0, rely=0.85, width=0.98*w2, height=0.010*h2)

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

        # =============right side image====================
        img3 = Image.open(
            r"images/room2.jpg")
        img3 = img3.resize((int(0.248*w1), int(0.371*h1)), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(relx=0.734, rely=0.134, width=0.248*w1, height=0.371*h1)

        # ==========table frame search system=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search", font=(
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
        combo_Search["value"] = ("BookID","CNIC_Passport","Room")
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
                showDataFrame.place(relx=0.340, rely=0.134, width=0.389*w1, height=0.371*h1)
                # 440 180


                # Label Name
                lblName = Label(showDataFrame, text="Name:",
                                font=("arial", int(0.01*w1), "bold"))
                lblName.place(relx=0, rely=0)

                lbl = Label(showDataFrame, text=row,
                            font=("arial", int(0.01*w1)))
                lbl.place(relx=0.125, rely=0)

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
                                  font=("arial", int(0.01*w1), "bold"))
                lblGender.place(relx=0, rely=0.139)

                lbl2 = Label(showDataFrame, text=row,
                             font=("arial", int(0.01*w1)))
                lbl2.place(relx=0.159, rely=0.139)

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
                               font=("arial", int(0.01*w1), "bold"))
                lblAge.place(relx=0, rely=0.278)

                lbl3 = Label(showDataFrame, text=row,
                             font=("arial", int(0.01*w1)))
                lbl3.place(relx=0.09, rely=0.278)


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
                                 font=("arial", int(0.01*w1), "bold"))
                lblEmail.place(relx=0, rely=0.417)

                lbl4 = Label(showDataFrame, text=row,
                             font=("arial", int(0.01*w1)))
                lbl4.place(relx=0.125, rely=0.417)

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
                                 font=("arial", int(0.01*w1), "bold"))
                lblEmail.place(relx=0, rely=0.556)

                lbl5 = Label(showDataFrame, text=row,
                             font=("arial", int(0.01*w1)))
                lbl5.place(relx=0.273, rely=0.556)

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
                                       font=("arial", int(0.01*w1), "bold"))
                lblNationality.place(relx=0, rely=0.694)

                lbl6 = Label(showDataFrame, text=row,
                             font=("arial", int(0.01*w1)))
                lbl6.place(relx=0.227, rely=0.694)

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
                               font=("arial", int(0.01*w1), "bold"))
                lblAge.place(relx=0, rely=0.833)

                lbl3 = Label(showDataFrame, text=row,
                             font=("arial", int(0.01*w1)))
                lbl3.place(relx=0.204, rely=0.833)

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
