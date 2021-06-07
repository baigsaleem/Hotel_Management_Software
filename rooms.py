import random
from tkinter import *
from tkinter import messagebox, ttk
from time import strftime
from datetime import datetime

import mysql.connector
import sqlite3
from PIL import Image, ImageTk


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Rooms Info")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # w,h=1000,600
        w1 = int(0.8275*w)
        h1 = int(0.632*h)
        x = int(0.165*w)
        y = int(0.235*h)
        self.root.geometry("%dx%d+%d+%d" % (w1, h1, x, y))
        # 1130 485

        # ===========title=============
        lbl_title = Label(self.root, text="Room Booking Details", font=(
            "times new roman", int(0.0177*w1), "bold"), bg="grey", fg="gold", bd=2, relief=RIDGE)
        lbl_title.place(relx=0, rely=0, width=w1, height=0.124*h1)

        # ========logo==============
        img2 = Image.open(
            r"images/logo.png")
        img2 = img2.resize((int(0.053*w1), int(0.124*h1)), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(relx=0, rely=0, width=0.070*w1, height=0.124*h1)

        # =============labelframe==========
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=(
            "times new roman", int(0.015*w1), "bold"))
        labelFrameLeftSide.place(relx=0.0044, rely=0.124, width=0.389*w1, height=0.866*h1)
        labelFrameLeftSide.update()
        w2, h2 = labelFrameLeftSide.winfo_width(), labelFrameLeftSide.winfo_height()
        # 440 420

        # Floor
        lbl_floor = Label(labelFrameLeftSide, text="Floor", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_floor.place(relx=0.04, rely=0)

        self.var_floor = StringVar()
        entry_floor = ttk.Entry(labelFrameLeftSide, width=int(0.016*w1), textvariable=self.var_floor, font=(
            "arial", int(0.0106*w1)))
        entry_floor.place(relx=0.25, rely=0)

        # Room No
        lbl_RoomNo = Label(labelFrameLeftSide, text="Room No.", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_RoomNo.place(relx=0.04, rely=0.09)

        self.var_roomNo = StringVar()
        entry_RoomNo = ttk.Entry(labelFrameLeftSide, width=int(0.016*w1), textvariable=self.var_roomNo, font=(
            "arial", int(0.0106*w1)))
        entry_RoomNo.place(relx=0.25, rely=0.09)

        # Room Type
        lbl_RoomType = Label(labelFrameLeftSide, text="Room Type", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_RoomType.place(relx=0.04, rely=0.18)

        self.var_RoomType = StringVar()
        entry_RoomType = ttk.Entry(labelFrameLeftSide, width=int(0.016*w1), textvariable=self.var_RoomType, font=(
            "arial", int(0.0106*w1)))
        entry_RoomType.place(relx=0.25, rely=0.18)

        # No of Beds
        lbl_NoOfBeds = Label(labelFrameLeftSide, text="No. of Beds", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_NoOfBeds.place(relx=0.04, rely=0.27)

        self.var_NoOfBeds = StringVar()
        entry_NoOfBeds = ttk.Entry(labelFrameLeftSide, width=int(0.016*w1), textvariable=self.var_NoOfBeds, font=(
            "arial", int(0.0106*w1)))
        entry_NoOfBeds.place(relx=0.25, rely=0.27)


        # =============buttons==============
        btn_frame = LabelFrame(labelFrameLeftSide, bd=2, relief=RIDGE)
        btn_frame.place(relx=0, rely=0.40, width=int(0.99*w2), height=int(0.095*h2))
        # 380 39

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.009*w1))
        btnAdd.place(relx=0, rely=0.05)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.009*w1))
        btnUpdate.place(relx=0.25, rely=0.05)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_room_detail, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.009*w1))
        btnDelete.place(relx=0.50, rely=0.05)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.009*w1))
        btnReset.place(relx=0.75, rely=0.05)

        # ==========table for room details=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=(
            "times new roman", int(0.015*w1), "bold"))
        table_Frame.place(relx=0.416, rely=0.124, width=int(0.575*w1), height=int(0.866*h1))

        scroll_x = ttk.Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_Frame, orient=VERTICAL)
        self.Room_Table = ttk.Treeview(table_Frame, column=(
            "floor", "roomNo", "roomType","noOfBeds"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("floor", text="Floor")
        self.Room_Table.heading("roomNo", text="RoomNo")
        self.Room_Table.heading("roomType", text="RoomType")
        self.Room_Table.heading("noOfBeds", text="NoOfBeds")

        self.Room_Table["show"] = "headings"

        self.Room_Table.column("floor", width=150)
        self.Room_Table.column("roomNo", width=100)
        self.Room_Table.column("roomType", width=100)
        self.Room_Table.column("noOfBeds", width=100)

        self.Room_Table.pack(fill=BOTH, expand=1)
        self.Room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ============Add Room Data===========
    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(?,?,?,?)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_RoomType.get(),
                    self.var_NoOfBeds.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "New Room Added Sucessfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    # ===========fetch data=================

    def fetch_data(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(
                *self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===========get cursor================
    def get_cursor(self, event=""):
        cursor_row = self.Room_Table.focus()
        content = self.Room_Table.item(cursor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])
        self.var_NoOfBeds.set(row[3])

    # ============update data===============
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter mobile no.", self.root)
        else:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=?, RoomType=?, NoOfBeds=? where RoomNo=?", (

                self.var_floor.get(),
                self.var_RoomType.get(),
                self.var_NoOfBeds.get(),
                self.var_roomNo.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Room details has been updated successfully", parent=self.root)

    # ==============delete================
    def delete_room_detail(self):
        delete_room_detail = messagebox.askyesno(
            "Hotel Management Software", "Do you want to delete this?", parent=self.root)
        if delete_room_detail > 0:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = "delete from details where RoomNo=?"
            value = (self.var_roomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_room_detail:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # ===============Reset=================
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set(""),
        self.var_NoOfBeds.set(""),


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
