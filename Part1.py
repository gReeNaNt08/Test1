month=input("Enter the month in numeric form: \n")
day=input("Enter the day of the month: \n")
year=input("Enter the year in two digit format: \n")

no_error=True

if int(month)<1 or int(month)>12 or not(month.isdigit()):
    no_error=False
    print("Error:Invalid Month Input")
    
if  not(day.isdigit()) or int(day)<1 or int(day)>31:
    no_error=False
    print("Error:Invalid Day Input")   
if (len(year)!=2) or not(year.isdigit()):
    no_error=False
    print("Error:Invalid Year Input")  

if no_error:

    print("Success: Congratulations! you entered the correct date")
    print(f"The date is: \t{month}/{day}/{year}")


