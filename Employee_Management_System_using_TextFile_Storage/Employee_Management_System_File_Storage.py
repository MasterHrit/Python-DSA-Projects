#Employee Management System using Permanent File Storage (Text File)
#Employee Class
class Employee:
    """ Employee Class to store the Employee Attributes
    """
    def __init__(self,ID,Name,Department,Salary) -> None:
        self.ID: int=ID
        self.Name: str=Name
        self.Department: str=Department
        self.Salary: int=Salary
#Input Employee Attributes
def InputRecord() -> Employee:
    """InputRecord Function to take Employee Parameter input and store it in Employee Class

    Returns:
        Employee: Employe Class
    """
    ID=int(input("Enter Employee ID :"))
    Name: str=input("Enter Employee Name :")
    Department: str=input("Enter Employee Department :")
    Salary=int(input("Enter Employee Salary :"))
    emp= Employee(ID,Name,Department,Salary)
    return emp

#Inserting the Employee Attributes to Text File
def InsertRecord() -> None:
    """InsertRecord Function to Insert the Employee Paramters to Text File
    """
    Emp: Employee=InputRecord()
    with open("employee_details.txt","a") as fileobject:
        outputstream: str="%d,%s,%s,%d\n"%(Emp.ID,Emp.Name,Emp.Department,Emp.Salary)
        fileobject.write(outputstream)
    print("\nRecord Entry Added to Database!")
#Display Records from the Text File
def DisplayRecords() -> None:
    """DisplayRecords Function to Display the Employee Records stored in the Text File
    """
    with open("employee_details.txt","r") as fileobject:
        data: list[str]=fileobject.readlines()
        print("%-30s%-30s%-30s%-30s"%("ID","Name","Department","Salary"))
        print("----------"*12)
        for i in data:
            entrylist: list[str]=i.split(",")
            for j in entrylist:
                if(j.endswith("\n")):
                    j: str=j[:len(j)-1]
                print("%-30s"%(j),end="")
            print()
#Search a Record from the Text File
def SearchRecord() -> None:
    pass
def UpdateRecord() -> None:
    pass
def DeleteRecord() -> None:
    pass
def main() -> None:
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