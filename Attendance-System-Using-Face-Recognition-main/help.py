from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\plain.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label_0=Label(f_lbl,text="HEY USERS,",font=("times new roman",14,"bold"))
        dev_label_0.place(x=50,y=50)


        dev_label_2=Label(f_lbl,text="ARE YOU FACING ANY CHALLENGES OR DO YOU HAVE ANY QUERRY WORKIN WITH OUR DESKTOP APPLICATION ??",font=("times new roman",14,"bold"))
        dev_label_2.place(x=50,y=80)

        dev_label_3=Label(f_lbl,text="IF YES , THE YOU DONT NEED TO WORRY AT ALL. YOU CAN SEND YOUR QUERRIRS ON THE BELOW MENTIONED EMAIL-ADDRESSES.",font=("times new roman",14,"bold"))
        dev_label_3.place(x=50,y=110)

        dev_label_4=Label(f_lbl,text="Email 1: nbanwadikar2000@gmail.com",font=("times new roman",14,"bold"),bg="lightblue")
        dev_label_4.place(x=50,y=200)

        dev_label_5=Label(f_lbl,text="Email 2: noushad@gmail.com",font=("times new roman",14,"bold"),bg="lightblue")
        dev_label_5.place(x=50,y=230)

        dev_label_6=Label(f_lbl,text="Email 3: Taha@gmail.com",font=("times new roman",14,"bold"),bg="lightblue")
        dev_label_6.place(x=50,y=260)













if __name__ == "__main__":
    root = Tk()
    obj= Help(root)
    root.mainloop()
