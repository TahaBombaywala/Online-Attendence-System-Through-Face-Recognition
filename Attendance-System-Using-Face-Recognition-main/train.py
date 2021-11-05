from tkinter import *
from tkinter import ttk
import cv2

from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image
import os
import numpy as np
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")



        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\trainimages\images1.jpg")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=10,y=55,width=1530,height=325)

        # button

        b1=Button(self.root,text="TRAIN DATA", cursor="hand2",command=self.train_classifier,font=("times new roman",20,'bold'),bg="LIGHTGRAY",fg="red")
        b1.place(x=0,y=340,width=1530,height=60)

        
        img_bootom=Image.open(r"C:\Users\Noushad\Documents\project\minorprojectvs\trainimages\images10.jpg")
        img_bootom=img_bootom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bootom=ImageTk.PhotoImage(img_bootom)

        f_lbl = Label(self.root,image=self.photoimg_bootom)
        f_lbl.place(x=10,y=400,width=1530,height=325)



    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        faces = []
        ids =[]
        
        for images in path:
            
            
            img=Image.open(images).convert('L')         #grayscale image 

            imagenp = np.array(img,'uint8')
            
            #C:\Users\Noushad\Desktop\minorprojectvs\taha\user1.1.jpg
          
            id=int(os.path.split(images)[1].split('.')[1])
           
        
            ids.append(id)
            faces.append(imagenp)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids) 


#   train the classifier

        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainind Dataset completed",parent=self.root)









if __name__ == "__main__":
    root = Tk()
    obj= Train(root)
    root.mainloop()
