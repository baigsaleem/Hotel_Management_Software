from tkinter import *
import xlsxwriter
import mysql.connector
import sqlite3


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Report")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # w,h=1000,600
        w1 = int(0.22*w)
        h1 = int(0.39*h)
        x = int(0.22*w)
        y = int(0.267*h)
        self.root.geometry("%dx%d+%d+%d" % (w1, h1, x, y))
        # 300 300

        # ===========title=============
        bill_title = Label(self.root, text="Reports", font=(
            "times new roman", int(0.067*w1), "bold","underline"), bd=0, relief=RIDGE, bg="grey")
        bill_title.place(relx=0, rely=0, width=w1, height=int(0.134*h1))

    
        # Customer table Button
        btnFetch = Button(self.root, text="Export Customer Table", command=self.export("customer"), font=(
            "arial", int(0.034*w1), "bold"), bg="black", fg='gold', width=int(0.067*w1))
        btnFetch.place(relx=0.234, rely=0.167)

        # Booking table Button
        btnFetch = Button(self.root, text="Export Booking Table", command=self.export("booking"), font=(
            "arial", int(0.034*w1), "bold"), bg="black", fg='gold', width=int(0.067*w1))
        btnFetch.place(relx=0.234, rely=0.334)

        # Reservation table Button
        btnFetch = Button(self.root, text="Export Reservation Table", command=self.export("reservation"), font=(
            "arial", int(0.034*w1), "bold"), bg="black", fg='gold', width=int(0.067*w1))
        btnFetch.place(relx=0.234, rely=0.5)

        # ===========Message=============
        bill_title = Label(self.root, text="Please check the root folder for the report table \nin Excel file format", font=(
            "times new roman", int(0.04*w1)), bd=0, relief=RIDGE)
        bill_title.place(relx=0.017, rely=0.667)


    def export(self,table_name):
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(table_name + '.xlsx')
        worksheet = workbook.add_worksheet('MENU')

        # Create style for cells
        header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
        body_cell_format = workbook.add_format({'border': True})

        # header, rows = fetch_table_data(table_name)

        # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
        # conn = mysql.connector.connect(host="localhost", user="root", password="Admin@123",
        #                                         database="hotel_managment", auth_plugin='mysql_native_password')
        conn = sqlite3.connect("./Database/hotel_managment.db")
        my_cursor = conn.cursor()
        my_cursor.execute('select * from ' + table_name)

        header = [row[0] for row in my_cursor.description]

        rows = my_cursor.fetchall()

        row_index = 0
        column_index = 0

        for column_name in header:
            worksheet.write(row_index, column_index, column_name, header_cell_format)
            column_index += 1

        row_index += 1
        for row in rows:
            column_index = 0
            for column in row:
                worksheet.write(row_index, column_index, column, body_cell_format)
                column_index += 1
            row_index += 1

        # Closing workbook
        workbook.close()


if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()