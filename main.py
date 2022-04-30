import tkinter as tk
from tkinter import Toplevel, ttk
import GetStudentDetails.Get_Student_Details as Get_Student_Details 
import RealTimeDatabase
from markAttedence import MarkAttendence
from register_student import Register_student
from save_encoding import Save_Encoding
realTimeDatabase = RealTimeDatabase.RealTimeDatabase(pathToFirebaseAdminFile="second-hand-book-exchang-1cf57-firebase-adminsdk-ae2w6-5e934cc6a2.json")
get_student_details = Get_Student_Details.GetStudentDetails(realTimeDatabase=realTimeDatabase)

def register_student():
    # new_window = Toplevel(window)
    # open register stdent form 
    Register_student(realTimeDatabase=realTimeDatabase)

def recognize_face():
    markAttendence_obj = MarkAttendence()
    Save_Encoding.recognize_face()
    markAttendence_obj.markAbsent(attendenceFilePath="attendence.csv")


if __name__ == "__main__":


        window = tk.Tk()
        window.geometry("1080x720")
        window.title("Main Window")
        window.configure(background ='white', width=1000, height=800)
        window.grid_rowconfigure(0, weight = 1)
        window.grid_columnconfigure(0, weight = 1)
        message = tk.Label(
            window, text ="Face-Recognition-System",
            bg ="green", fg = "white", width = 50,
            height = 3, font = ('times', 30, 'bold'))
        message.place(x = 200, y = 20)

        

        # -------------- Register Button-------------
        Register = tk.Button(window, text ="Register Student",
                                command=register_student,fg ="white", bg ="green", 
                                width = 20, height = 3, activebackground = "Red", 
                                font =('times', 15, ' bold ')
                            )
        Register.place(x = 300, y = 500)


        # -------------- Recognize Button-------------
        Recognize = tk.Button(window, text ="Recognize Student",
                                command=recognize_face,fg ="white", bg ="green", 
                                width = 20, height = 3, activebackground = "Red", 
                                font =('times', 15, ' bold ')
                            )
        Recognize.place(x = 550, y = 500)

        
        
        # --------------- Quit Button--------------
        quit_bt = tk.Button(window, text ="Quit",
                                command = window.destroy, fg ="white", bg ="green", 
                                width = 20, height = 3, activebackground = "Red", 
                                font =('times', 15, ' bold ')
                            )
        quit_bt.place(x = 800, y = 500)

        window.mainloop()