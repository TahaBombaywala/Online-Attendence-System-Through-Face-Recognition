from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")


        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\plain.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="lightblue")
        main_frame.place(x=700,y=0,width=900,height=300)
        

        # img 1
        img_top1=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\plain.jpg")
        img_top1=img_top1.resize((250,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=0,width=250,height=200)

        
        # info
        dev_label=Label(main_frame,text="This is Nupur Banwadikar, IT",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=240)




        # img 2
        img_top2=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img_top2=img_top2.resize((250,200),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=270,y=0,width=250,height=200)

        #label_2=Label(main_frame,text="NOUSHAD KHAN",font=("times new roman",12,"bold"),bg="white")
        #label_2.grid(row=1,column=2,padx=110,sticky=W)

        # info2
        dev_label_1=Label(main_frame,text="This is Noushad Khan, IT",font=("times new roman",12,"bold"),bg="white")
        dev_label_1.place(x=280,y=240)


        # img 3
        img_top3=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img_top3=img_top3.resize((250,200),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=545,y=0,width=250,height=200)

        #label_3=Label(main_frame,text="TAHA BOMBAYWALA",font=("times new roman",12,"bold"),bg="white")
        #label_3.grid(row=1,column=7,padx=10,sticky=W)

        # info3
        
        dev_label_2=Label(main_frame,text="This is Taha Bombaywala, IT",font=("times new roman",12,"bold"),bg="white")
        dev_label_2.place(x=570,y=240)











if __name__ == "__main__":
    root = Tk()
    obj= Developer(root)
    root.mainloop()
