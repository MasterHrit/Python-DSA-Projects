#Employee Management System using Dictionary as Storage
#In the Employee Record we will maintain Employee ID, Name, Department and Salary.
employee_record={}

#Insert Employee Record
def InsertEmployeeRecord():
    id=int(input("Enter the Employee ID :"))
    name=input("Enter the Employee Name :")
    dept=input("Enter the Employee Department :")
    salary=int(input("Enter the Employee Salary :"))
    employee_record.update({id:{"Name":name,"Dept":dept, "Salary":salary}})
    print("\nEmployee Record Added!\n")

#Display All Employee Records
def DisplayAllRecords():
    print()
    print("----------"*8)
    print("%-20s%-20s%-20s%-20s"%("ID","Name","Department","Salary"))
    print("----------"*8)
    for i in employee_record.items():
        print("%-20d"%i[0],end="")
        for j in i[1].values():
            if(isinstance(j,int)):
                print("%-20d"%(j),end="")
            else:
                print("%-20s"%(j),end="")
        print()

#Display Particular Record from ID
def DisplaySingleRecord(empid):
    print()
    print("----------"*8)
    print("%-20s%-20s%-20s%-20s"%("ID","Name","Department","Salary"))
    print("----------"*8)
    for i in employee_record.items():
        if(i[0]==empid):
            print("%-20d"%i[0],end="")
            for j in i[1].values():
                if(isinstance(j,int)):
                    print("%-20d"%(j),end="")
                else:
                    print("%-20s"%(j),end="")

#Search Employee Records
def SearchEmployeeRecord():
    searchid=int(input("Enter the Employee ID to Search in the Record :"))
    flag=0
    for i in employee_record.items():
        if(i[0]==searchid):
            print(f"\nEmployee ID {searchid} Found in the Record!")
            DisplaySingleRecord(searchid)
            flag=1
    if(flag==0):
        print(f"\nThe Employee ID {searchid} is not found!")

#Update Employee Record
def UpdateEmployeeRecord():
    pass

#Delete Employee Record
def DeleteEmployeeRecord():
    pass

while True:
    print()
    print("----------"*8)
    print("Employee Management System")
    print("----------"*8)
    print("1. Insert Employee Record")
    print("2. Display all Employee Records")
    print("3. Search Employee Records")
    print("4. Update Employee Records")
    print("5. Delete Employee Records")
    print("6. Exit")
    print()
    choice=int(input("Enter your choice :"))
    if(choice==1):
        InsertEmployeeRecord()
    elif(choice==2):
        DisplayAllRecords()
    elif(choice==3):
        SearchEmployeeRecord()
    elif(choice==4):
        UpdateEmployeeRecord()
    elif(choice==5):
        DeleteEmployeeRecord()
    if(choice==6):
        break