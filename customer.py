import random
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
import sqlite3
from PIL import Image, ImageTk


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        # self.root.geometry("1130x485+225+180")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # w,h=1000,600
        w1 = int(0.8275*w)
        h1 = int(0.632*h)
        x = int(0.165*w)
        y = int(0.235*h)
        self.root.geometry("%dx%d+%d+%d" % (w1, h1, x, y))

        # =============variables============
        self.var_ref = StringVar()
        x = random.randint(1000, 99999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_cust_age = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_cnic = StringVar()
        self.var_nationality = StringVar()

        # ===========title=============
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=(
            "arial", int(0.0177*w1), "bold"), bg="grey", fg="gold", bd=2, relief=RIDGE)
        lbl_title.place(relx=0, rely=0, width=w1, height=0.123*h1)

        # ========logo==============
        img2 = Image.open(
            r"images\logo.png")
        img2 = img2.resize((int(0.053*w1), int(0.124*h1)), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=2, relief=RIDGE)
        lblimg.place(relx=0, rely=0, width=0.070*w1, height=0.124*h1)

        # =============labelframe==========
        labelFrameLeftSide = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=(
            "arial", int(0.015*w1), "bold"), padx=2,)
        labelFrameLeftSide.place(relx=0.0044, rely=0.124, width=0.389*w1, height=0.866*h1)
        labelFrameLeftSide.update()
        w2, h2 = labelFrameLeftSide.winfo_width(), labelFrameLeftSide.winfo_height()
        # 440 420

        # =========labels and entries========
        # Ref no.
        lbl_cust_ref = Label(labelFrameLeftSide, text="Customer Ref No.", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_cust_ref.place(relx=0, rely=0.019)

        entry_ref = ttk.Entry(labelFrameLeftSide, width=int(0.0101*w1), textvariable=self.var_ref, font=(
            "arial", int(0.0106*w1)), state="readonly")
        entry_ref.place(relx=0.35, rely=0.019)

        # customer name
        cust_name = Label(labelFrameLeftSide, text="Full Name",
                          font=("arial", int(0.0106*w1), "bold"))
        cust_name.place(relx=0, rely=0.1)

        txt_cust_name = ttk.Entry(
            labelFrameLeftSide, width=int(0.027*w1), textvariable=self.var_cust_name, font=("arial",int(0.0106*w1)))
        txt_cust_name.place(relx=0.35, rely=0.1)

        # customer age
        cust_age = Label(labelFrameLeftSide, text="Customer Age",
                         font=("arial", int(0.0106*w1), "bold"))
        cust_age.place(relx=0, rely=0.184)

        txt_cust_age = ttk.Entry(
            labelFrameLeftSide, width=int(0.01*w1), textvariable=self.var_cust_age, font=("arial", int(0.0106*w1)))
        txt_cust_age.place(relx=0.35, rely=0.184)

        # gender combo box
        lbl_gender = Label(labelFrameLeftSide, text="Customer Gender",
                           font=("arial", int(0.0106*w1), "bold"))
        lbl_gender.place(relx=0, rely=0.266)

        combo_gender = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_gender, font=(
            "arial", int(0.0106*w1), "bold"), width=int(0.01*w1), state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.place(relx=0.35, rely=0.266)

        # Mobile No.
        lbl_cellNo = Label(labelFrameLeftSide, text="Mobile No.", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_cellNo.place(relx=0, rely=0.35)

        txt_cellNo = ttk.Entry(labelFrameLeftSide, width=int(0.027*w1),
                               textvariable=self.var_mobile, font=("arial", int(0.0106*w1)))
        txt_cellNo.place(relx=0.35, rely=0.35)

        # Email Address
        lbl_email = Label(labelFrameLeftSide, text="Email Address",
                          font=("arial", int(0.0106*w1), "bold"))
        lbl_email.place(relx=0, rely=0.434)

        txt_email = ttk.Entry(labelFrameLeftSide, width=int(0.027*w1),
                              textvariable=self.var_email, font=("arial", int(0.0106*w1)))
        txt_email.place(relx=0.35, rely=0.434)

        # ID
        lbl_id = Label(labelFrameLeftSide, text="CNIC/Passport No.",
                       font=("arial", int(0.0106*w1), "bold"))
        lbl_id.place(relx=0, rely=0.516)

        txt_id = ttk.Entry(labelFrameLeftSide, width=int(0.027*w1),
                           textvariable=self.var_cnic, font=("arial", int(0.0106*w1)))
        txt_id.place(relx=0.35, rely=0.516)

        # Nationality
        lbl_nationality = Label(labelFrameLeftSide, text="Nationality", font=(
            "arial", int(0.0106*w1), "bold"))
        lbl_nationality.place(relx=0, rely=0.60)

        combo_nationality = ttk.Combobox(labelFrameLeftSide, textvariable=self.var_nationality, font=(
            "arial", int(0.0106*w1), "bold"), width=int(0.017*w1), state="readonly")
        combo_nationality["value"] = ('Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan',
                                      'Antiguans', 'Argentinean', 'Armenian', 'Australian', 'Austrian', 'Azerbaijani', 'Bahamian', 'Bahraini',
                                      'Bangladeshi', 'Barbadian', 'Barbudans', 'Batswana', 'Belarusian', 'Belgian', 'Belizean', 'Beninese',
                                      'Bhutanese', 'Bolivian', 'Bosnian', 'Brazilian', 'British', 'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese',
                                      'Burundian', 'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian', 'Chilean',
                                      'Chinese', 'Colombian', 'Comoran',  'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech',
                                      'Danish', 'Djibouti', 'Dominican', 'Dutch', 'Dutchman', 'Dutchwoman', 'East Timorese', 'Ecuadorean', 'Egyptian',
                                      'Emirian', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino', 'Finnish', 'French',
                                      'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinea-Bissauan',
                                      'Guinean', 'Guyanese', 'Haitian', 'Herzegovinian', 'Honduran', 'Hungarian', 'I-Kiribati', 'Icelander', 'Indian',
                                      'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Ivorian', 'Jamaican', 'Japanese', 'Jordanian',
                                      'Kazakhstani', 'Kenyan', 'Kittian and Nevisian', 'Kuwaiti', 'Kyrgyz', 'Laotian', 'Latvian', 'Lebanese', 'Liberian',
                                      'Libyan', 'Liechtensteiner', 'Lithuanian', 'Luxembourger', 'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivan',
                                      'Malian', 'Maltese', 'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan', 'Monacan', 'Mongolian',
                                      'Moroccan', 'Mosotho', 'Motswana', 'Mozambican', 'Namibian', 'Nauruan', 'Nepalese', 'Netherlander', 'New Zealander', 'Ni-Vanuatu',
                                      'Nicaraguan', 'Nigerian', 'Nigerien', 'North Korean', 'Northern Irish', 'Norwegian', 'Omani', 'Pakistani', 'Palauan', 'Panamanian',
                                      'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian', 'Rwandan', 'Saint Lucian',
                                      'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi', 'Scottish', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean',
                                      'Singaporean', 'Slovakian', 'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan',
                                      'Sudanese', 'Surinamer', 'Swazi', 'Swedish', 'Swiss', 'Syrian', 'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan',
                                      'Trinidadian or Tobagonian', 'Tunisian', 'Turkish', 'Tuvaluan', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbekistani', 'Venezuelan',
                                      'Vietnamese', 'Welsh', 'Yemenite', 'Zambian', 'Zimbabwean')
        combo_nationality.current(139)
        combo_nationality.place(relx=0.35, rely=0.60)

        # =============buttons==============
        btn_frame = LabelFrame(labelFrameLeftSide, bd=2, relief=RIDGE)
        btn_frame.place(relx=0.01, rely=0.880, width=0.95*w2, height=0.095*h2)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.023*w2))
        btnAdd.place(relx=0, rely=0.05)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.023*w2))
        btnUpdate.place(relx=0.25, rely=0.05)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_cust, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.023*w2))
        btnDelete.place(relx=0.50, rely=0.05)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", int(0.0106*w1), "bold"), bg="black", fg='gold', width=int(0.023*w2))
        btnReset.place(relx=0.75, rely=0.05)

        # ==========table frame search system=============
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search", font=(
            "arial", int(0.015*w1), "bold"), padx=2)
        table_Frame.place(relx=0.399, rely=0.124, width=0.595*w1, height=0.865*h1)
        table_Frame.update()
        w3, h3 = table_Frame.winfo_width(), table_Frame.winfo_height()
        # 492 328

        lbl_SearchBar = Label(table_Frame, text="Search By:", font=(
            "arial", int(0.0097*w1), "bold"), bg='red', fg='white')
        lbl_SearchBar.place(relx=0, rely=0.01)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(table_Frame, textvariable=self.search_var, font=(
            "arial", int(0.0097*w1), "bold"), width=int(0.020*w3), state="readonly")
        combo_Search["value"] = ("Ref","CNIC_Passport")
        combo_Search.current(0)
        combo_Search.place(relx=0.13, rely=0.01)

        self.search_text = StringVar()
        txt_Search = ttk.Entry(
            table_Frame, width=int(0.044*w3), textvariable=self.search_text, font=("arial", int(0.0097*w1)))
        txt_Search.place(relx=0.31, rely=0.01)

        btnSearch = Button(table_Frame, text="Search", command=self.search, font=(
            "arial", int(0.0097*w1), "bold"), bg="green", fg='white', width=int(0.020*w3))
        btnSearch.place(relx=0.64, rely=0)

        btnShowAll = Button(table_Frame, text="Show All", command=self.fetch_data, font=(
            "arial", int(0.0097*w1), "bold"), bg="green", fg='white', width=int(0.020*w3))
        btnShowAll.place(relx=0.82, rely=0)

        # ===============show data table==============
        details_table = LabelFrame(table_Frame, bd=2, relief=RIDGE)
        details_table.place(relx=0, rely=0.1, width=0.584*w1, height=0.72*h1)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("Ref", "Name", "Age", "Gender", "Mobile",
                                                                      "Email", "CNIC_Passport", "Nationality"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref", text="Ref")
        self.Cust_Details_Table.heading("Name", text="Name")
        self.Cust_Details_Table.heading("Age", text="Age")
        self.Cust_Details_Table.heading("Gender", text="Gender")
        self.Cust_Details_Table.heading("Mobile", text="Mobile")
        self.Cust_Details_Table.heading("Email", text="Email")
        self.Cust_Details_Table.heading("CNIC_Passport", text="CNIC/Passport")
        self.Cust_Details_Table.heading("Nationality", text="Nationality")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("Ref", width=70)
        self.Cust_Details_Table.column("Name", width=200)
        self.Cust_Details_Table.column("Age", width=50)
        self.Cust_Details_Table.column("Gender", width=70)
        self.Cust_Details_Table.column("Mobile", width=150)
        self.Cust_Details_Table.column("Email", width=150)
        self.Cust_Details_Table.column("CNIC_Passport", width=150)
        self.Cust_Details_Table.column("Nationality", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_cust_name.get() == "" or self.var_cust_age.get() == "" or self.var_mobile.get() == "" or self.var_cnic.get() == "" or self.var_nationality.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
                #                                database="hotel_managment", auth_plugin='mysql_native_password')
                conn = sqlite3.connect("./Database/hotel_managment.db")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(?,?,?,?,?,?,?,?)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_cust_age.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_cnic.get(),
                    self.var_nationality.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_age.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_cnic.set(row[6]),
        self.var_nationality.set(row[7])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile no.", self.root)
        else:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name=?,Age=?,Gender=?,Mobile=?,Email=?,CNIC_Passport=?,Nationality=? where Ref=?", (

                self.var_cust_name.get(),
                self.var_cust_age.get(),
                self.var_gender.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_cnic.get(),
                self.var_nationality.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(
                "Update", "Customer details has been updated successfully", parent=self.root)

    def delete_cust(self):
        delete_cust = messagebox.askyesno(
            "Hotel Management Software", "Do you want to delete this customer?", parent=self.root)
        if delete_cust > 0:
            # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
            #                                database="hotel_managment", auth_plugin='mysql_native_password')
            conn = sqlite3.connect("./Database/hotel_managment.db")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref=?"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_cust:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_cust_age.set(""),
        # self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_cnic.set(""),
        # self.var_nationality.set("")
        x = random.randint(1000, 99999)
        self.var_ref.set(str(x))

    def search(self):
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
