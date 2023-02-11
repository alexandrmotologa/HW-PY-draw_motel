from os import system

# DATA
cost_room_single_per_day = 30
cost_room_double_per_day = 50

system("cls")
#personal data prompt
print("\nPERSONAL DATA\n-------------------")
client_f_name = input("Your fullname: ")
client_m_phone = input("Your mobile phone: ")

# booking data prompt
room_type = input("\nROOM TYPE\n\
------------------\n\
1.Single room (" + str(cost_room_single_per_day) + " per day)\n\
1.Single room (" + str(cost_room_double_per_day) + " per day)\n\
x.Cancel \n> ")

if room_type == "x":
    print("Thank you, we are sorry you didn't choose our services! ")
else:
    room_period = int(input("\nPERIOD (days): "))
    # calculations
    if room_type == "1":
        cost_total = cost_room_single_per_day * room_period
    elif room_type == "2":
        cost_total = cost_room_double_per_day * room_period
        
    print("The rent for",room_period,"days will cost", cost_total)