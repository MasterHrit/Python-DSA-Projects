#Movie Ticket Booking System using 1D List Storage
seat_arrangement=[]
#Initializing the seat arrangement list
for i in range(1,51):
    seat_arrangement.append(str(i))

#Display Movie Seat Arrangements
def DisplaySeats():
    for i in range(len(seat_arrangement)):
        print("%-2s"%(seat_arrangement[i]),end=" ")
        if((i+1)%10==0):
            print()

#Book the seats
def BookSeats(n):
    l1=[]
    while True:
        l1=[]
        flag=0
        seat=input("Enter the seat numbers (space separated):")
        seatnumber_list=seat.split(" ")
        for i in range(len(seatnumber_list)):
            seatnumber_list[i]=int(seatnumber_list[i])
        if(len(seatnumber_list)!=n):
            print("Wrong number of seats input! Please Try Again!")
            continue
        for i in seatnumber_list:
            if (i>50 or i<1):
                print("Wrong Input! Please Try Again!")
                flag=1
                break
            elif (seat_arrangement[i-1]=="BK"):
                print(f"Seat {i} is already booked!")
                flag=1
                break
            else:
                pass
        if(flag==0):
            for i in seatnumber_list:
                l1.append(i)
                seat_arrangement[i-1]="BK"
            break
    print("\nBelow Seats are Booked :")
    for i in l1:
        print(i,end=", ")
    print("\b\b \n")
    DisplaySeats()
while True:
    print("----------"*8)
    print("Movie Ticket Booking System")
    print("----------"*8)
    DisplaySeats()
    print()
    number_of_seats=int(input("How many seats do you want to book :"))
    BookSeats(number_of_seats)
    ch=input("\nEnter Y/y if you want to book seats again :")
    if(ch=="Y" or ch=="y"):
        pass
    else:
        break