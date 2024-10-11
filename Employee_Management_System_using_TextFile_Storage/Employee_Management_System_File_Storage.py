#Employee Management System using Permanent File Storage (Text File)
#Employee Class
class Employee:
    def __init__(self):
        ID=None
        Name=None
        Department=None
        Salary=None
#Input Employee Attributes
def InputRecord(emp: Employee):
    emp.ID=int(input("Enter Employee ID :"))
    emp.Name=input("Enter Employee Name :")
    emp.Department=input("Enter Employee Department :")
    emp.Salary=int(input("Enter Employee Salary :"))
#Inserting the Employee Attributes to Text File
def InsertRecord():
    Emp=Employee()
    InputRecord(Emp)
    with open("employee_details.txt","a") as fileobject:
        outputstream="%d,%s,%s,%d\n"%(Emp.ID,Emp.Name,Emp.Department,Emp.Salary)
        fileobject.write(outputstream)
    print("\nRecord Entry Added to Database!")
#Display Records from the Text File
def DisplayRecords():
    with open("employee_details.txt","r") as fileobject:
        data=fileobject.readlines()
        print("%-30s%-30s%-30s%-30s"%("ID","Name","Department","Salary"))
        print("----------"*12)
        for i in data:
            entrylist=i.split(",")
            for j in entrylist:
                if(j.endswith("\n")):
                    j=j[:len(j)-1]
                print("%-30s"%(j),end="")
            print()
#Search a Record from the Text File
def SearchRecord():
    pass
def UpdateRecord():
    pass
def DeleteRecord():
    pass
def main():
    while True:
        print()
        print("----------"*12)
        print("Employee Management System")
        print("----------"*12)
        print("1. Insert an Employee Record.")
        print("2. Display all Employee Records.")
        print("3. Search an Employee Record.")
        print("4. Update an Employee Record.")
        print("5. Delete an Employee Record.")
        print("6. Exit.")
        choice=int(input("\nEnter your choice :"))
        if(choice==1):
            InsertRecord()
        elif(choice==2):
            DisplayRecords()
        elif(choice==3):
            SearchRecord()
        elif(choice==4):
            UpdateRecord()
        elif(choice==5):
            DeleteRecord()
        elif(choice==6):
            break
        else:
            print("Wrong Choice! Please Try Again!")

if(__name__=="__main__"):
    main()