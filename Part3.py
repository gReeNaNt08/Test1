from time import sleep
def convertSalary():
    validCountry=["Canada","USA","Cambodia","United Kingdom"]
    salary=float(input("Enter the salary: "))
    country=input(f"Enter the country you want to migrate to:{validCountry} ")
    convertedSal=float()
    if not(country in validCountry):
        print("Enter a valid country")
        sleep(2)
        quit()
    if country=="Canada":
        rate=56
        convertedSal=salary*rate
        average_sal=64000
        currency="CAD"
    elif country=="USA":
        rate=1.18
        convertedSal=salary*rate 
        average_sal=56516
        currency="USD"
    elif country=="UK":     
         rate=0.91
         convertedSal=salary*rate 
         average_sal=56516
         currency="Pound Sterling"
    elif country=="Cambodia":
        rate=4847.38
        convertedSal=rate*salary
        average_sal=5649856
        currency="Cambodian riel"
    else:
        print("Invalid salary") 


    if convertedSal>average_sal:
        print(f"You will be rich in {country} with a salary of {convertedSal}{currency}.")
    else:
         print(f"You will be poor in {country} with a salary of {convertedSal}{currency}.")         

convertSalary()