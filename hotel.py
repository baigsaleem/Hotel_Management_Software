from tkinter import*
from PIL import Image, ImageTk
from customer import Cust_Win
from booking import RoomBooking
from rooms import DetailsRoom
from reservation import Reservation
from report import Report
from time import strftime
from datetime import datetime


class HotelManagmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("WEZTEL")
        # self.root.geometry("1365x700+0+0")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        # w,h=1000,600
        root.geometry("%dx%d+0+0" % (w, h))
        # 1366, 768

        # ========cover==============
        img1 = Image.open(
            r"images\cover.jpg")
        img1 = img1.resize((int(w*0.908), int(h*0.156)), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(relx=0.16, rely=0, width=0.84*w, height=0.165*h)

        # ========logo==============
        img2 = Image.open(
            r"images\logo.png")
        img2 = img2.resize((int(w*0.073), int(h*0.130)), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(relx=0, rely=0, width=0.172*w, height=0.165*h)

        # ==========title Frame========
        title_frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        title_frame.place(relx=0, rely=0.156, width=w, height=0.065*h)

        # ===========title=============
        lbl_title = Label(title_frame, text="WEZTEL", font=(
            "arial", int(0.013*w), "bold"), bg="black", fg="gold")
        lbl_title.place(relx=0.44, rely=0.09)

        # ===========time=============
        def time():
            string = strftime("%H:%M:%S %p")
            lbl_time.config(text=string)
            lbl_time.after(1000, time)
        
        lbl_time = Label(title_frame, font=(
            "arial", int(0.011*w), "bold"), bg="black", fg="gold")
        lbl_time.place(relx=0.039, rely=0.13)
        time()

        # ===========Date=============
        lbl_date = Label(title_frame, text=f"{datetime.now():%a, %b %d %Y}",font=(
            "arial", int(0.011*w), "bold"), bg="black", fg="gold")
        lbl_date.place(relx=0.86, rely=0.13)

        # ==============mainframe=======
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(relx=0, rely=0.220, width=w, height=0.730*h)
        main_frame.update()
        w1, h1 = main_frame.winfo_width(), main_frame.winfo_height()
        # 1366, 500

        # ==============menu============
        lbl_menu = Label(main_frame, text="MENU", font=(
            "arial", int(0.014*w), "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(relx=0, rely=0, width=0.168*w1)

        # ==============button frame=======
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(relx=0, rely=0.07, width=0.168*w1, height=0.46*h1)
        btn_frame.update()
        w2, h2 = btn_frame.winfo_width(), btn_frame.winfo_height()
        # 151 180

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, font=(
            "arial", int(0.01*w), "bold"), bg="grey", fg="gold", bd=1, cursor="hand2")
        cust_btn.place(relx=0, rely=0,width=int(w2*0.970), height=int(h2*0.16))

        booking_btn = Button(btn_frame, text="BOOKING", command=self.booking_details, font=(
            "arial", int(0.01*w), "bold"), bg="grey", fg="gold", bd=1, cursor="hand2")
        booking_btn.place(relx=0, rely=0.167,width=int(w2*0.970), height=int(h2*0.16))

        reservation_btn = Button(btn_frame, text="RESERVATION", command=self.room_reservation, font=(
            "arial", int(0.01*w), "bold"), bg="grey", fg="gold", bd=1, cursor="hand2")
        reservation_btn.place(relx=0, rely=0.334,width=int(w2*0.970), height=int(h2*0.16))

        details_btn = Button(btn_frame, text="ROOMS", command=self.room_details, font=(
            "arial", int(0.01*w), "bold"), bg="grey", fg="gold", bd=1, cursor="hand2")
        details_btn.place(relx=0, rely=0.502,width=int(w2*0.970), height=int(h2*0.16))

        report_btn = Button(btn_frame, text="REPORT", command=self.report, font=(
            "arial", int(0.01*w), "bold"), bg="grey", fg="gold", bd=1, cursor="hand2")
        report_btn.place(relx=0, rely=0.668,width=int(w2*0.970), height=int(h2*0.16))

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout,font=(
            "arial", int(0.01*w), "bold"), bg="grey", fg="gold", bd=1, cursor="hand2")
        logout_btn.place(relx=0, rely=0.834,width=int(w2*0.970), height=int(h2*0.16))

        # ===========right side image==============
        img3 = Image.open(
            r"images\front.jpg")
        img3 = img3.resize((w1, h1), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(relx=0.168, rely=0, width=0.830*w1, height=0.94*h1)

        # ============down images==============
        img4 = Image.open(
            r"images\room1.jpg")
        img4 = img4.resize((int(0.168*w1), int(0.27*h1)), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(relx=0, rely=0.53, width=0.168*w1, height=0.230*h1)

        img5 = Image.open(
            r"images\restaurant.jpg")
        img5 = img5.resize((int(0.168*w1), int(0.27*h1)), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(relx=0, rely=0.73, width=0.168*w1, height=0.230*h1)

        # ===========footer===============
        lbl_footer = Label(self.root, text="Software developed by Saleem Baig, CEO NrewSoft... Copyright 2021", font=(
            "arial", int(0.008*w)), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_footer.place(relx=0, rely=0.95, width=w, height=0.052*h)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def booking_details(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def room_reservation(self):
        self.new_window = Toplevel(self.root)
        self.app = Reservation(self.new_window)

    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagmentSystem(root)
    root.mainloop()
