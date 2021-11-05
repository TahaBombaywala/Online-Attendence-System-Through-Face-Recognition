from tkinter import *
from tkinter import ttk
import cv2
from time import strftime
import datetime
from datetime import datetime

from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image
import os
import numpy as np
import mysql.connector
class face_recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")



        title_lbl=Label(self.root,text="FACE RECOGNIZATION",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)


# first image
        img_top=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\trainimages\images11.jpg")
        img_top=img_top.resize((700,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=10,y=55,width=700,height=700)
        b1_1=Button(self.root,text="Face Recognization",command=self.face_recognition,cursor="hand2",font=("times new roman",18,"bold"),bg="lightgray",fg="red")
        b1_1.place(x=1000,y=400,width=220,height=60)

 #---------------------------mark attendance-----------------------------------------------
    def mark_attendance(self,i,r,n,d):
       
        with open("khan.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            print(len(myDataList))
            print(i,r,n,d)
            for line in myDataList:
                print(myDataList)
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list)) and ((r not in name_list)) and  ((r not in name_list)) and  ((d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dstring},{d1},Present")




        # -------------------------------face recognition--------------------------

    def  face_recognition(self):
        try:

            face_cascade = cv2.CascadeClassifier(r"C:\Users\Noushad\Documents\project\minorprojectvs\haarcascade_frontalface_default.xml")
            cif=cv2.face.LBPHFaceRecognizer_create()
            cif.read("classifier.xml")

            video_capture = cv2.VideoCapture(0)
            while True:
                ret , img = video_capture.read()
                gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features = face_cascade.detectMultiScale(gray_image)
                coordinates = []
                

                for x,y,w,h in features:
                     
                    
                    cv2.rectangle(img[x,y],[x+w,y+h],(0,255,0),3)
                    
                    id , predict = cif.predict(gray_image[y:y+h,x:x+w])
                    confidence = int((100*(1-predict/300)))
                    print("this is id",id)

                    conn = mysql.connector.connect(host="localhost",user="root",password='root',database="face_reccognizer")
                    my_cursor=conn.cursor()
                    print("sdfjkldflkdsjf",my_cursor)
                    my_cursor.execute("select Name from student where Student_id="+str(id))
                    n=my_cursor.fetchone()
                    print("thhis is n",n)
                    n="+".join(n)

                    my_cursor.execute("select Roll from student where Student_id="+str(id))
                    r=my_cursor.fetchone()
                    r="+".join(r)
               

                    my_cursor.execute("select Dep from student where Student_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)
                    print("i se phle")

                    my_cursor.execute("select student_id from student where Student_id="+str(id))
                    i=my_cursor.fetchone()
                    i="+".join(i)
                    print("i k bad")


                        
                
                
                    if confidence>80:
                        cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)
                        self.mark_attendance(i,r,n,d)

                    else:
                            cv2.putText(img,"unknow image",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)

                    coordinates=[x,y,w,h]



                #coord = draw_boundary(img,face_cascade,1.1,10,(255,255,0),"Face",cif)
                
                #img=recognize(img,cif,face_cascade)
                cv2.imshow("Welcome to face recognize",img)
                k =  cv2.waitKey(30) & 0xFF
                if k == 27:
                    break
                    
            video_capture.release()
            cv2.destroyAllWindows()
        except Exception as e:
            messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)  
            











if __name__ == "__main__":
    root = Tk()
    obj= face_recognizer(root)
    root.mainloop()
