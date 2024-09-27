
import sqlite3
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
       self.root=root
       self.root.title("Student Result Management Sytem")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="white")
       #==========icons========

       self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

       #==========title========

       title=Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)       
       #==========menu==========

       M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
       M_Frame.place(x=10,y=70,width=1340,height=80)
        
       #==========Buttons===========

       btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
       btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
       btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
       btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
       btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=900,y=5,width=200,height=40)

       #==========content============

       self.bg_img=Image.open("images/bg.png")
       self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
       self.bg_img=ImageTk.PhotoImage(self.bg_img)
       
       self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

       #=============update_details=============

       self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
       self.lbl_course.place(x=400,y=530,width=300,height=100)

       self.lbl_student=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
       self.lbl_student.place(x=710,y=530,width=300,height=100)

       self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
       self.lbl_result.place(x=1020,y=530,width=300,height=100)      
       
       
        #=============Variable=============
       self.update_details()
    
    def update_details(self):
      con=sqlite3.connect(database="rms.db")
      cur=con.cursor()
      try:
          cur.execute("select * from course")
          cr=cur.fetchall()
          self.lbl_course.config(text=f"Total Courses[{str(len(cr))}]")
          
          cur.execute("select * from student")
          cr=cur.fetchall()
          self.lbl_student.config(text=f"Total Students[{str(len(cr))}]")

          cur.execute("select * from result")
          cr=cur.fetchall()
          self.lbl_result.config(text=f"Total Results[{str(len(cr))}]")

          self.lbl_course.after(200,self.update_details)

          
      except Exception as ex:
         messagebox.showerror("Error",f"Error due to {str(ex)}")

   
   
   
    def add_course(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=CourseClass(self.new_win)

    def add_student(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=studentClass(self.new_win)
   
    def add_result(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=resultClass(self.new_win)
   
    def add_report(self):
       self.new_win=Toplevel(self.root)
       self.new_obj=reportClass(self.new_win)

    def exit_(self):
       op=messagebox.askyesno("Confirm","Do you really want to Exit")
       if op==True:
          self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
