# importing libraries
import tkinter as tk
from tkinter import Message, Text
from tkinter import ttk
import cv2
import GetStudentDetails.Get_Student_Details as Get_Student_Details 
import RealTimeDatabase
import markAttedence
import save_encoding
# realTimeDatabase = RealTimeDatabase.RealTimeDatabase(pathToFirebaseAdminFile="second-hand-book-exchang-1cf57-firebase-adminsdk-ae2w6-5e934cc6a2.json")

class Register_student:
    def __init__(self, realTimeDatabase) -> None:
        self.realTimeDatabase = realTimeDatabase
        self.get_student_details = Get_Student_Details.GetStudentDetails(realTimeDatabase=self.realTimeDatabase)
        self.Register()


    def Register(self):
        window = tk.Tk()
        window.geometry("1080x720")
        window.title("Register Student")
        window.configure(background ='white', width=1000, height=800)
        window.grid_rowconfigure(0, weight = 1)
        window.grid_columnconfigure(0, weight = 1)
        message = tk.Label(
            window, text ="Face-Recognition-System",
            bg ="green", fg = "white", width = 50,
            height = 3, font = ('times', 30, 'bold'))
        message.place(x = 200, y = 20)

        x = 400
        y = 200
        # ------------ year label and text field-------------
        year_lbl= tk.Label(window, text = "Year",
        width = 20, height = 2, fg ="green",
        bg = "white", font = ('times', 15, ' bold ') )
        year_lbl.place(x = 400, y = 200)

        year_txt = tk.Entry(window,
        width = 20, bg ="white",
        fg ="green", font = ('times', 15, ' bold '))
        year_txt.place(x = 700, y = 215)


        # ------------ branch label and text field-------------
        branch_lbl= tk.Label(window, text = "Branch",
        width = 20, height = 2, fg ="green",
        bg = "white", font = ('times', 15, ' bold ') )
        branch_lbl.place(x = 400, y = 250)

        branch_txt = tk.Entry(window,
        width = 20, bg ="white",
        fg ="green", font = ('times', 15, ' bold '))
        branch_txt.place(x = 700, y = 265)


        # ------------ UIN label and text field-------------
        UIN_lbl= tk.Label(window, text = "UIN",
        width = 20, height = 2, fg ="green",
        bg = "white", font = ('times', 15, ' bold ') )
        UIN_lbl.place(x = 400, y = 300)

        UIN_txt = tk.Entry(window,
        width = 20, bg ="white",
        fg ="green", font = ('times', 15, ' bold '))
        UIN_txt.place(x = 700, y = 315)


        # ------------ Name label and text field-------------
        name_lbl = tk.Label(window, text ="Name",
        width = 20, fg ="green", bg ="white",
        height = 2, font =('times', 15, ' bold '))
        name_lbl.place(x = 400, y = 350)

        name_txt = tk.Entry(window, width = 20,
        bg ="white", fg ="green",
        font = ('times', 15, ' bold ') )
        name_txt.place(x = 700, y = 365)


        # ------------ Gender label and text field-------------
        gender_lbl = tk.Label(window, text ="Gender",
        width = 20, fg ="green", bg ="white",
        height = 2, font =('times', 15, ' bold '))
        gender_lbl.place(x = 400, y = 400)

        gender_combo_box = ttk.Combobox(window, values=["Male", "Female"], )
        gender_combo_box.set("Choose Gender")
        gender_combo_box.place(x = 700, y = 410)


        def register_student():
            message.config(text="Face-Recognition-System ")
            studentDetails = {"year":year_txt.get(),
                                "branch":branch_txt.get(),
                                "UIN":UIN_txt.get(),
                                "name":name_txt.get(),
                                "gender":gender_combo_box.get(),
                                "camNumber":0,
                                "studentFolderPath":"studentFolderPath", 
                                "isRegistered":False
                                }
            if studentDetails["UIN"] == "":
                print("UIN field is Empty")
                return 0
            tem = self.get_student_details.checkStudentIsPresentInDatabase(UIN=studentDetails["UIN"])
            print(tem)
            message.config(text="Face-Recognition-System " + str(tem))
            if tem["UIN"] == None:
                self.get_student_details.getStudentDetails(studentDetails=studentDetails, message=message)
                self.realTimeDatabase.addStudent(databaseReferencePath="/", studentDetails={studentDetails["UIN"]:studentDetails})
                # save_face_recognize_data(dir="GetStudentDetails/Students Encoding of Face")
                message.config(text="Face-Recognition-System " + "\nUpdating Student Encoding of Face")
                save_encoding.Save_Encoding.save_face_recognize_data(dir="GetStudentDetails/Students Encoding of Face")
                # Saving student in attendence file
                obj = markAttedence.MarkAttendence()
                obj.saveAttendenceFile(attendenceFilePath="attendence.csv",studentDetails=studentDetails)
                message.config(text="Face-Recognition-System " + "\nStudent Registration is Complete")

            else:
                # TODO:Display this message in a dialog box 
                message.config(text="Face-Recognition-System " + "\nStudent is already there in Database")
            


        # -------------- Register Button-------------
        Register = tk.Button(window, text ="Register",
                                command = register_student, fg ="white", bg ="green", 
                                width = 20, height = 3, activebackground = "Red", 
                                font =('times', 15, ' bold ')
                            )
        Register.place(x = 400, y = 500)

        # --------------- Quit Button--------------
        quit_bt = tk.Button(window, text ="Quit",
                                command = window.destroy, fg ="white", bg ="green", 
                                width = 20, height = 3, activebackground = "Red", 
                                font =('times', 15, ' bold ')
                            )
        quit_bt.place(x = 650, y = 500)

        window.mainloop()


if __name__ == "__main__":
    realTimeDatabase = RealTimeDatabase.RealTimeDatabase(pathToFirebaseAdminFile="second-hand-book-exchang-1cf57-firebase-adminsdk-ae2w6-5e934cc6a2.json")
    obj = Register_student(realTimeDatabase=realTimeDatabase)
