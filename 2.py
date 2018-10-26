def c2k():
    celcius = int(input("Enter the tempearature in Celcius\n"))
    return celcius+273

def k2c():
    kelvin = int(input("Enter the tempearature in Kelvin\n"))
    return kelvin-273
choice =0
while choice!=3:
    choice = int(input("Enter 1 to convert from Celcius to Kelvin\nEnter 2 to convert from Kelvin to Celcius\nEnter 3 to exit\n"))
    if choice == 1:
      print(c2k())
    elif choice == 2:
      print(k2c())
    elif choice == 3:
        exit()
