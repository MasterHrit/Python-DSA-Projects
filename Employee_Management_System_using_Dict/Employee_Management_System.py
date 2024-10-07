#Employee Management System using Dictionary as Storage
#In the Employee Record we will maintain Employee ID, Name, Department and Salary.
employee_record={}

#Insert Employee Record
def InsertEmployeeRecord():
    id=int(input("Enter the Employee ID :"))
    name=input("Enter the Employee Name :")
    dept=input("Enter the Employee Department :")
    salary=int(input("Enter the Employee Salary :"))
    employee_record.update({id:{"Name":name.title(),"Dept":dept.title(), "Salary":salary}})
    print("\nEmployee Record Added!\n")

#Display All Employee Records
def DisplayAllRecords():
    print()
    print("----------"*12)
    print("%-30s%-30s%-30s%-30s"%("ID","Name","Department","Salary"))
    print("----------"*12)
    for i in employee_record.items():
        print("%-30d"%i[0],end="")
        for j in i[1].values():
            if(isinstance(j,int)):
                print("%-30d"%(j),end="")
            else:
                print("%-30s"%(j),end="")
        print()

#Display Particular Record from ID
def DisplaySingleRecord(empid):
    print()
    print("----------"*12)
    print("%-30s%-30s%-30s%-30s"%("ID","Name","Department","Salary"))
    print("----------"*12)
    for i in employee_record.items():
        if(i[0]==empid):
            print("%-30d"%i[0],end="")
            for j in i[1].values():
                if(isinstance(j,int)):
                    print("%-30d"%(j),end="")
                else:
                    print("%-30s"%(j),end="")
            print()

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
    searchid=int(input("Enter the Employee ID to Update from the Record :"))
    flag=0
    for i in employee_record.items():
        if(i[0]==searchid):
            print("\nOld Record Value :")
            DisplaySingleRecord(searchid)
            name=input("\nEnter the New Employee Name :")
            dept=input("Enter the New Employee Department :")
            salary=int(input("Enter the New Employee Salary :"))
            employee_record.update({searchid:{"Name":name.title(),"Dept":dept.title(), "Salary":salary}})
            print(f"\nEmployee Record for ID {searchid} is Updated!\n")
            flag=1
    if(flag==0):
        print(f"\nThe Employee ID {searchid} is not found!")

#Delete Employee Record
def DeleteEmployeeRecord():
    searchid=int(input("Enter the Employee ID to Delete from the Record :"))
    if(searchid in employee_record.keys()):
        print("\nBelow Employee Record will be Deleted from the Record :")
        DisplaySingleRecord(searchid)
        popvalue=employee_record.pop(searchid)
        print(f"\nEmployee ID {searchid} has been Deleted from the Record Successfully!")
    else:
        print(f"\nThe Employee ID {searchid} is not found!")

while True:
    print()
    print("----------"*12)
    print("Employee Management System")
    print("----------"*12)
    print("1. Insert Employee Record")
    print("2. Display all Employee Records")
    print("3. Search Employee Records")
    print("4. Update Employee Records")
    print("5. Delete Employee Records")
    print("6. Exit")
    print()
    choice=int(input("Enter your choice :"))
    print()
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