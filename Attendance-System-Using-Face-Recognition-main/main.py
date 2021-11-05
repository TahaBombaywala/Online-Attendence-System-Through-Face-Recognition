from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import datetime
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from facerecognizer import face_recognizer
from attendance import Attendance
from developer import Developer
from help import Help
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        # First image

        img=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\plain.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)


        #Second image


        img1=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\Faces.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=150)

        # Third image

        img2=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\plain.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=150)


       # bg image
        img3=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\plain.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=150,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


 #----------------------------------time-------------------------------------------------
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        lbl.place(x=40,y=0,width=110,height=50)
        time()

        






        #student button
        img4=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\stud_button.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=200,y=300,width=220,height=40)




        #detectface button
        img5=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\fd.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.recognizer_file)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.recognizer_file,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=500,y=300,width=220,height=40)




        #Attendance button
        img6=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\Attend.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=800,y=300,width=220,height=40)




        #Help button
        img7=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\helpdesk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=1100,y=300,width=220,height=40)



        #Train button
        img8=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,command=self.train_file,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,command=self.train_file,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos button
        img9=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\stt.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Images",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=500,y=580,width=220,height=40)


        #Developer button
        img10=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\Developer.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=800,y=580,width=220,height=40)



        #Exit button
        img11=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\frimages\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.exit,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        b1_1.place(x=1100,y=580,width=220,height=40)



    def open_img(self):
       os.startfile('data')


    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition","Are you sure",parent=self.root)
        print(self.exit)
        if self.exit==True:
            
            self.root.destroy()
        else:
            return


# -----------------------function button-----------------------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_file(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def recognizer_file(self):
        self.new_window=Toplevel(self.root)
        self.app = face_recognizer(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app =Help(self.new_window)







if __name__=="__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()