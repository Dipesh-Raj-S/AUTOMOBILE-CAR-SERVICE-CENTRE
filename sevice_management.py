print('''                WELCOME TO AUTOMOBILE SERVICE CENTRE
Please provide your information''')

Name= input("customer name:- ")
car_type = (int(input('''What type of car do you have?(select as per number)
          1.SUV
          2.Sedan
          3.Hatchback :- ''')))
if car_type > 3 or car_type < 0:
  print("Please enter between the given options")
  sys.exit()

SUV = 10000
Sedan = 7000
Hatchback = 5000

number_plate = int(input("Please enter last 4 digits of your number plate:-"))
if number_plate < 1000 or number_plate > 9999:
  print ("Invalid Number plate")
  sys.exit()

car_model=int(input('''Please enter your car model:- (select between given number)
            1.BMW
            2.Audi
            3.Mercedes Benz
            4.Toyota
            5.Honda
            6.Suzuki
            7.TATA
            8.Skoda
            9.Hundai
            10.Mahindra  :-     '''))
if car_model>11 or car_model<0:
    print("Please enter a valid number")
    sys.exit()

service_prices_list1 = [19500,9000,10000,0]
service_prices_list2 = [19000,8500,11000,0]
service_prices_list3 = [20000,10000,12000,0]
service_prices_list4 = [10000, 4000, 6000,0]
service_prices_list5 = [8000, 2500, 3000,0]
service_prices_list6 = [7800, 2200, 3200,0]
service_prices_list7 = [5000, 1500, 2000,0]
service_prices_list8 = [15000, 8000, 9000,0]
service_prices_list9 = [7600, 3400, 3700, 0]
service_prices_list10 = [9450, 4200, 5500, 0]

service = []
service_choice = 0
if car_model == 1:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 2:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE      -                      ₹9,000
            2.WHEEL ALIGNMENT      -                      ₹4,500
            3.CAR WASH             -                      ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 3:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE        -                    ₹8,000
            2.WHEEL ALIGNMENT        -                    ₹4,000
            3.CAR WASH               -                    ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 4:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 5:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 6:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 7:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 8:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

elif car_model == 9:
    print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

else:
  print('''Rupees charged as per the services:
            1.GENERAL SERVICE     -                       ₹10,000
            2.WHEEL ALIGNMENT     -                       ₹5,000
            3.CAR WASH            -                       ₹2,500
            Please enter a particular service only one time    :- ''')

if car_model == 1:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list1[service_choice-1])
        else:
            break
elif car_model == 2:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list2[service_choice-1])
        else:
            break

elif car_model == 3:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list3[service_choice-1])
        else:
            break

elif car_model == 4:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list4[service_choice-1])
        else:
            break

elif car_model == 5:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list5[service_choice-1])
        else:
            break

elif car_model == 6:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list6[service_choice-1])
        else:
            break

elif car_model == 7:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list7[service_choice-1])
        else:
            break

elif car_model == 8:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list8[service_choice-1])
        else:
            break

elif car_model == 9:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list9[service_choice-1])
        else:
            break

else:
  for i in range(3):
        service_choice = int(input('''Please enter the service which reqired
            1.GENERAL SERVICE
            2.WHEEL ALIGNMENT
            3.CAR WASH
            4.NO
            Please enter a particular service only one time    :- '''))
        if(service_choice != 4):
            service.append(service_prices_list10[service_choice-1])
        else:
            break

print(service)
total_sum = sum(service)

if car_type == 1:
  print("The total_amount to be paid:- ₹",total_sum + SUV)
elif car_type == 2:
  print ("The total amount to be paid:- ₹", total_sum + Sedan)
else:
  print ("The total amount to be paid:- ₹", total_sum + Hatchback)

print ("Client Name:- ", Name)
print ("Client Number plate:- ", number_plate)

if car_model == 1:
  print("Client Car Company:- BMW")
elif car_model == 2:
  print("Client Car Company:- Audi")
elif car_model == 3:
  print ("Client Car Company:- Mercedes Benz")
elif car_model == 4:
  print ("Client Car Company:- Toyota")
elif car_model == 5:
  print ("Client Car Company:- Honda")
elif car_model == 6:
  print ("Client Car Company:- Suzuki")
elif car_model == 7:
  print ("Client Car Company:- TATA")
elif car_model == 8:
  print ("Client Car Company:- Skoda")
elif car_model == 9:
  print ("Client Car Company:- Hundai")
else:
  print ("Client Car Company:- Mahindra")

#to get date of delivery
from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()

# Add 5 days to the current date
new_date = current_datetime + timedelta(days=5)

# Print the new date
print("Current date:", current_datetime.date())
print("Delivery date after service:", new_date.date())
