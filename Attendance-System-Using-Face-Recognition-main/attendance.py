from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog
mydata = []

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")




        #-------------text variable-------------------
        self.var_attend_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar() 
        self.var_atten_attendance = StringVar()

          # First image

        img=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)


        #Second image


        img1=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\Faces.png")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # bg image
        img3=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\Faces.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        # bg_img = Label(self.root,image=self.photoimg3)
        # bg_img.place(x=0,y=150,width=1530,height=710)


        title_lbl=Label(self.root,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=180,width=1530,height=45)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10,y=220,width=1500,height=700)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)



        img_left=Image.open(r"C:\Users\Noushad\Desktop\minorprojectvs\face_recognition system\frimages\plain.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        Left_inside_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        Left_inside_frame.place(x=5,y=160,width=720,height=240)


        # ------------labels and entry-----------------------
  #---------------attendance id ------------------------------
        attendanceId_label=Label(Left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_attend_id,width=20,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #-----------------------ROll-------------------
        rolllabel=Label(Left_inside_frame,text="Roll",font=("times new roman",12,"bold"),bg="white")
        rolllabel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #------------------Name-----------------------------------------
        namelabel=Label(Left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        namelabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #---------------------------------Department ----------------------------------
        deplabel=Label(Left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        deplabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_dep=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #----------------------------date--------------------

        datelabel=Label(Left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        datelabel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_date=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=1,column=3,padx=10,pady=5,sticky=W)




        #-------------------Attendance status-----------
        attendancelabel=Label(Left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        

        self.atten_status=ttk.Combobox(Left_inside_frame,font=("times new roman",12,"bold"),textvariable=self.var_atten_attendance,state="read only",width=18)
        self.atten_status["values"]=("Status","Absent","Present")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=2,pady=5,sticky=W)



        #- ------------------time ---------------------------
        timeabel=Label(Left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        timeabel.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        time_date=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_date.grid(row=3,column=3,padx=10,pady=5,sticky=W)


   #------------------buttons frame--------------------

        btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        import_btn = Button(btn_frame,text="Import csv",width=19,command=self.importcsv,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export csv",width=19,command=self.exportcsv,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",width=19,command=self.resetdata,font=("times new roman",12,"bold"),bg="light blue",fg="blue")
        reset_btn.grid(row=0,column=3)








#-------------------------------right label frame---------------------------------------------

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=680,height=520)


#-------------------scroll bar table------------------------------------
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"] ="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
     

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)


        
        #-----------------------fetch data-------------------
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #-----------------import csv file

    def importcsv(self):
        
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file"," *.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)


        
    #-------------export data -----------------

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file"," *.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Complete","Data has Exported to "+os.path.basename(fln)+"succesfully")
        except  Exception as e:
                messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

        
    def getcursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6]) 

    def resetdata(self):
        self.var_attend_id.set("")
        
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")








        

       



if __name__ == "__main__":
    root = Tk()
    obj= Attendance(root)
    root.mainloop()
