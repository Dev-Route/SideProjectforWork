from datetime import datetime
import time
while True:

    print("\n\n")
    print("                                              #########################")
    print("                                              #                       #")
    print("                                              # Welcome to LaCompanie #")
    print("                                              #                       #")
    print("                                              #########################")
    offTime_str = str(input("\n\n\nPlease enter the OFFTIME (Airborne) here: "))
    offTime_obj = datetime.strptime(offTime_str, '%H:%M')
    print("You entered the following >>>>>   " + str(offTime_obj.time())+ "\n")
    flightTime_str = str(input("\n\nPlease enter the flight time here: "))
    flightTime_obj = datetime.strptime(flightTime_str,'%H:%M')
    print("You entered the following >>>>>   " + str(flightTime_obj.time())+ "\n")
    time_zero = datetime.strptime('00:00', '%H:%M')
    calculatedTime = offTime_obj - time_zero + flightTime_obj
    print(f'The estimated arrival time at Orly Airport at Paris >>>>>      {calculatedTime.time()} \n')
    time.sleep(1)
    print("Please confirm with Gabbie or Martina if you don't trust your IT guy!\n")
    time.sleep(2)
    print("Have a lovely night.\n\n\n")




