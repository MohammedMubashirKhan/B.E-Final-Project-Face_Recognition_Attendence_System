import csv
import datetime
import pickle
import pandas as pd
import os

class MarkAttendence:
    def __init__(self):
        pass



    def saveAttendenceFile(self, attendenceFilePath,studentDetails):

        row = [studentDetails["UIN"],studentDetails["name"]]
        for i in range(1,32):
            row.append("-")
        with open(attendenceFilePath, 'a+') as csvFile:
            writer = csv.writer(csvFile)
            # Entry of the row in csv file
            writer.writerow(row)
        csvFile.close()

        # ------------------- Creating Header in attendence file------------
        df = pd.read_csv(attendenceFilePath)
        # adding header
        headerList = ['UIN', 'Name']
        for i in range(1,32):
            if i < 10:
                headerList.append("0"+str(i))
            else:
                headerList.append(str(i))


        # converting data frame to csv
        df.to_csv(attendenceFilePath, header=headerList, index=False)


    def markAbsent(self,attendenceFilePath):
        # Get the current date to mark present on date
        currentDate = datetime.date.today()
        currentDate = str(currentDate)
        tem = currentDate.split('-')
        day = int(tem[2])

        # reading the csv file
        df = pd.read_csv(attendenceFilePath)

        # Getting the line Number in an attendence file where the UIN is present 
        with open("attendence.csv", 'r') as file_obj:
            reader_obj = csv.reader(file_obj)
            count_line = -1
            for row in reader_obj:
                count_line += 1
                print(row)
                print(count_line)
                try:
                    if len(row) > 25 and row[day+1] == "-":
                        print(row[day+1])   
                        # print("Breaking of count_line",count_line) 
                        # reading the csv file
                        df = pd.read_csv(attendenceFilePath)

                        # updating the column value/data
                        # count_line-2 because line number start from 0 and heared line is excluded
                        df.loc[count_line-1, str(day)] = "Absent"

                        # writing into the file
                        df.to_csv(attendenceFilePath, index=False)
                except:
                    pass                        



        pass

    def markAttendence(self, attendenceFilePath, UIN_name):
        # Spliting UIN from UIN_name
        print(UIN_name)
        UIN = UIN_name.split("_")[0]
        # Get the current date to mark present on date
        currentDate = datetime.date.today()
        currentDate = str(currentDate)
        tem = currentDate.split('-')
        day = tem[2]

        # Getting the line Number in an attendence file where the UIN is present 
        with open("attendence.csv", 'r') as file_obj:
            reader_obj = csv.reader(file_obj)
            count_line = -1
            for row in reader_obj:
                count_line += 1
                print(row)
                if row[0] == UIN:
                    print("Breaking of count_line",count_line) 
                    # reading the csv file
                    df = pd.read_csv(attendenceFilePath)

                    # updating the column value/data
                    # count_line-1 because line number start from 0 and heared line is excluded
                    df.loc[count_line-1, str(day)] = "Present"

                    # writing into the file
                    df.to_csv(attendenceFilePath, index=False)
                    break

        # print("Count Line is ", count_line)
        

        


if __name__ =="__main__":

    obj = MarkAttendence()
    # obj.saveAttendenceFile("attendence.csv", {"year":"Year",
    #                             "branch":"COMPS",
    #                             "UIN":"111",
    #                             "name":"Mubashir",
    #                             "gender":"Male",
    #                             "camNumber":0,
    #                             "studentFolderPath":"studentFolderPath", 
    #                             "isRegistered":False
    #                             })
    # obj.markAttendence(attendenceFilePath="attendence.csv", UIN_name="171_MMK")
    # obj.markAbsent(attendenceFilePath="attendence.csv")

        

