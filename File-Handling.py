# Data_Log
Python Program for File-Handling: Data Logging is Used to add an information of Visitors visited in hospital or Reception 


Name = input("Enter a name of visitor: \n")
Phone_Number = int(input("Enter a Contact Number of Visitor: \n"))
Place_From = input("Visitor Address: \n")
Body_Temp = int(input("Enter Body Temperature in Integer: \n"))
enter = ("\n")

for data in (Name, Phone_Number, Place_From, Body_Temp, enter):
    if data == '' :
        f = open("Visitor_info.txt", "w")
        f.writelines(data + "\t")
    elif data == data:
        f = open("Visitor_info.txt", "a")
        f.writelines(str(data) + "\t")
    else:
        f = open("Visitor_info.txt", "r")
        f.read(data)
f.close()
