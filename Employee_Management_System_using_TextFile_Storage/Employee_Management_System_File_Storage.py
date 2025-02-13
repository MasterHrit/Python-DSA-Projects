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
def InputRecord(id: int=-1) -> Employee:
    """InputRecord Function to take Employee Parameter input and store it in Employee Class

    Returns:
        Employee: Employe Class
    """
    if(id==-1):
        ID=int(input("Enter Employee ID :"))
    else:
        ID: int=id
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
    """SearchRecord Function to search particular Employee ID in the Record
    """
    searchid: int=int(input("Enter the Employee ID to search :"))
    with open("employee_details.txt","r") as fileobject:
        flag=0
        data: list[str]=fileobject.readlines()
        count=0
        for i in data:
            entrylist: list[str]=i.split(",")
            if(searchid==int(entrylist[0])):
                if(count==0):
                    print("%-30s%-30s%-30s%-30s"%("ID","Name","Department","Salary"))
                    print("----------"*12)
                    count+=1
                flag=1
                for j in entrylist:
                    if(j.endswith("\n")):
                        j: str=j[:len(j)-1]
                    print("%-30s"%(j),end="")
                print()
        if(flag==0):
            print(f"\nID {searchid} not found!")

def UpdateRecord() -> None:
    """UpdateRecord Function to Update a particular Employee Record based on Employee ID
    """
    searchid=int(input("Enter the Employee ID to update :"))
    data: list[str]=[]
    with open("employee_details.txt","r+") as fileobject:
        index: int=-1
        data=fileobject.readlines()
        for i in data:
            wordlist: list[str]=i.split(",")
            if(int(wordlist[0])==searchid):
                index=data.index(i)
        if(index==-1):
            print("No such element found!")
        else:
            data.pop(index)
    with open("employee_details.txt","w+") as fileobject:
        for i in data:
            fileobject.write(i)
    with open("employee_details.txt","a+") as fileobject:
        print("Enter the new values for the Employee ")
        Emp: Employee=InputRecord(searchid)
        outputstream: str="%d,%s,%s,%d\n"%(Emp.ID,Emp.Name,Emp.Department,Emp.Salary)
        fileobject.write(outputstream)
        print("\nRecord Entry Updated in the Database!")

def DeleteRecord() -> None:
    """DeleteRecord Function to Delete the Employee Record based on the Employee ID
    """
    searchid=int(input("Enter the Employee ID to delete :"))
    data: list[str]=[]
    with open("employee_details.txt","r+") as fileobject:
        index: int=-1
        data=fileobject.readlines()
        for i in data:
            wordlist: list[str]=i.split(",")
            if(int(wordlist[0])==searchid):
                index=data.index(i)
        if(index==-1):
            print("No such element found!")
        else:
            data.pop(index)
            print(f"\nThe Record with ID {searchid} is deleted Successfully!")
    with open("employee_details.txt","w+") as fileobject:
        for i in data:
            fileobject.write(i)

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