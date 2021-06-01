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
        self.root.geometry("1120x460+237+205")

        # ===========title=============
        lbl_title = Label(self.root, text="Room Booking Details", font=(
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
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=(
            "times new roman", 17, "bold"), padx=2,)
        labelFrameLeftSide.place(x=5, y=60, width=440, height=395)

        # Floor
        lbl_floor = Label(labelFrameLeftSide, text="Floor", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()
        entry_floor = ttk.Entry(labelFrameLeftSide, width=18, textvariable=self.var_floor, font=(
            "arial", 12))
        entry_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(labelFrameLeftSide, text="Room No.", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomNo = StringVar()
        entry_RoomNo = ttk.Entry(labelFrameLeftSide, width=18, textvariable=self.var_roomNo, font=(
            "arial", 12))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(labelFrameLeftSide, text="Room Type", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_RoomType = StringVar()
        entry_RoomType = ttk.Entry(labelFrameLeftSide, width=18, textvariable=self.var_RoomType, font=(
            "arial", 12))
        entry_RoomType.grid(row=2, column=1, sticky=W)

        # No of Beds
        lbl_NoOfBeds = Label(labelFrameLeftSide, text="No. of Beds", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lbl_NoOfBeds.grid(row=3, column=0, sticky=W)

        self.var_NoOfBeds = StringVar()
        entry_NoOfBeds = ttk.Entry(labelFrameLeftSide, width=18, textvariable=self.var_NoOfBeds, font=(
            "arial", 12))
        entry_NoOfBeds.grid(row=3, column=1, sticky=W)



        # =============buttons==============
        btn_frame = LabelFrame(labelFrameLeftSide, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=150, width=380, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 12, "bold"), bg="black", fg='gold', width=8)
        btnAdd.grid(row=0, column=0, padx=2)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", 12, "bold"), bg="black", fg='gold', width=8)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_room_detail, font=(
            "arial", 12, "bold"), bg="black", fg='gold', width=8)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 12, "bold"), bg="black", fg='gold', width=8)
        btnReset.grid(row=0, column=3, padx=2)

        # ==========table for room details=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=(
            "times new roman", 17, "bold"), padx=2,)
        table_Frame.place(x=470, y=60, width=645, height=395)

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
