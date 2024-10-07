#Employee Management System using Dictionary as Storage
employee_record={}

#Insert Employee Record
def InsertEmployeeRecord():
    

#Display All Employee Records
def DisplayAllRecords():
    pass

#Search Employee Records
def SearchEmployeeRecord():
    pass

#Update Employee Record
def UpdateEmployeeRecord():
    pass

#Delete Employee Record
def DeleteEmployeeRecord():
    pass

while True:
    print("---------------------------------------")
    print("Employee Management System")
    print("---------------------------------------")
    print("1. Insert Employee Record")
    print("2. Display all Employee Records")
    print("3. Search Employee Records")
    print("4. Update Employee Records")
    print("5. Delete Employee Records")
    print("6. Exit")
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