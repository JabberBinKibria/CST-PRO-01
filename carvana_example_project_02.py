#car company list in a python list
car_companies = ["BMW", "Ford", "Audi", "Bentley", "Cadillac",
                  "Chevrolet", "Chrysler", "Dodge", "Ferrari"]

#introduction 
print("""
      Welcome to Carvana
      Thanks for choosing us""")

print("Available Cars Companiens ")

for cars in car_companies:
    print(cars)                 #getting car names from the list



#creating a function to show user which cars models are available
def main():
    while True:
        car_from_user = input("""
                        Please Select The Car
                        You Want By Typing The
                        Name Of The Car
                        Type Exit To End The Program
                        """)
        car_from_user = car_from_user.lower()


        if car_from_user == "audi":
            audi()          
        elif car_from_user == "bmw":
            bmw()         
        elif car_from_user == "ford":
            ford()
        elif car_from_user == "bentley":
            bentley()
        elif car_from_user == "cadillac":
            cadillac()
        elif car_from_user == "chevrolet":
            chevrolet()
        elif car_from_user == "Chrysler":
            chrysler()
        elif car_from_user == "dodge":
            dodge()
        elif car_from_user == "ferrari":
            ferrari()
        elif car_from_user == "exit":
            print("See you soon!!")
            break
        else:
            print("Please enter the car name correctly")






def ferrari():
    print("""
        Available cars:
        1. 2024 Ferrari Purosangue
        MSRP: From $393,350
        MPG: 11 city / 15 highway
        Horsepower: 715 hp
        Engine : 6.5 L V12
        Transmission: 8-speed automati
        Dimensions: 196″ L x 80″ W x 63″ H
        
        2. 2015 Ferrari 458 Spider
        MSRP: From $259,000 – $294,000
        MPG: 13 city / 17 highway
        Engine : 4.5 L V8
        Horsepower : 570 hp
        Transmission :7-speed automatic
        Dimensions: 178″ L x 76″ W x 48″ H

        """)  


def dodge():
    print("""
        Available cars:
        1. 2023 Dodge Challenger
        MSRP: From $32,800
        MPG: Up to 19 city / 30 highway
        Horsepower: 303 to 797 hp
        Engine : 3.6 L V6,
                 5.7 L V8,
                 6.4 L V8
        Towing capacity: 1,000 lbs
        Transmission: 8-speed automatic, 6-speed manual
                
        2. 2025 Dodge Durango
        MSRP: From $41,995
        MPG: Up to 18 city / 25 highway
        Engine : 3.6 L V6,
                 5.7 L V8,
                 6.2 L V8
        Horsepower :295 to 710 hp
        Transmission :8-speed automatic
        Towing capacity: 6,200 to 8,700 lbs

        """)  

def chrysler():
    print("""
        Available cars:
        1. 2023 Chrysler 300
        MSRP: From $36,145
        MPG: Up to 19 city / 30 highway
        Horsepower: 213 hp
        Transmission: Electric
        Dimensions: 202-209″ L x 79″ W x 68-69″ H
                
        2. 2025 Chevrolet Corvette
        MSRP: From $68,300
        MPG: Up to 16 city / 24 highway
        Engine : 3.6 L V6,
                 5.7 L V8,
                 6.4 L V8
        Horsepower :292 to 485 hp
        Transmission :8-speed automatic
        Towing capacity :1,000 lbs 

        """)

def chevrolet():
    print("""
        Available cars:
        1. 2025 Chevrolet Equinox EV
        MSRP: From $33,600
        MPG: 117 city / 99 highway
        Horsepower: 213 hp
        Transmission: Electric
        Dimensions: 202-209″ L x 79″ W x 68-69″ H
                
        2. 2025 Chevrolet Corvette
        MSRP: From $68,300
        MPG: Up to 16 city / 24 highway
        Engine : 5.5 L V8,
                6.2 L V8
        Horsepower :490 to 670 hp
        Transmission :8-speed automatic
        Dimensions : 182-185″ L x 76-80″ W x 49″ 

        """)


def bentley():
    print("""
        Available cars:
        1. 2024 Bentley Bentayga
        MSRP: From $203,200
        MPG: Up to 14 city / 21 highway
            Engine: 4.0 L V8
        Horsepower: 542 hp
        Transmission: 8-speed automatic
        Dimensions: 202-209″ L x 79″ W x 68-69″ H
                
        2. 2024 Bentley Continental GT
        MSRP: From $242,700
        MPG: Up to 14 city / 22 highway
        Engine : 4.0 L V8,
                6.0 L W12
        Horsepower :542 to 650 hp
        Transmission :8-speed automatic
        Dimensions : 191″ L x 77″ W x 55″ H

        """)


def cadillac():
    print("""
        Available cars:
        1. 2024 Cadillac Escalade
        MSRP: From $81,895
        MPG: Up to 21 city / 27 highway
        Engine: 3.0 L 6-cylinder diesel,
                6.2 L V8
        Horsepower: 277 to 682 hp
        Transmission: 10-speed automatic
        Towing capacity: 7,000 to 7,700 lbs
                
        2.2024  cadillac lyriq
        MSRP: From $57,195
        MPG: 95 city / 82 highway
        Engine : 314 mi battery-only
        Horsepower : About 220 miles in 32 minutes
        Transmission : Electric
          
        """)


def ford():
    print("""
        Available cars:
        1. 2025 Ford Mustang
        MSRP: From $31,920
        MPG: Up to 21 city / 32 highway
        Engine: 2.3 L 4-cylinder,
                5.0 L V8
        Horsepower: 315 to 500 hp
        Transmission: 10-speed automatic,
                    6-speed manual
        Dimensions: 189-190″ L x 75-76″ W x 55″ H
                
        2. 2006 Ford GT
        MSRP:From $60,950
        MPG: 13 city / 31 highway
        Engine :5.4 L V8
        Horsepower :550 hp
        Transmission :6-speed automatic
        Dimensions :183″ L x 77″ W x 44″ H

        """)

def bmw():
        print("""
            Available cars:
            1. 2025 BMW M3
            MSRP: From $76,000
            MPG: 16 city / 23 highway
            Engine: 3.0 L 6-cylinder
            Horsepower: 473 to 523 hp
            Transmission: 8-speed automatic,
                        6-speed manual
            Dimensions: 189″ L x 74″ W x 57″ H
                
            2. 2025 BMW X1
            MSRP:From $40,950
            MPG: 23 city / 31 highway
            Engine :2.0 L 4-cylinder
            Horsepower :241 to 312 hp
            Transmission :7-speed automatic
            Dimensions :177″ L x 73″ W x 65″ H
        """)

def audi():
    print("""
        Available cars:
        1. AUDI R8
        MSRP: From $158,600
        MPG: Up to 14 city / 23 highway
        Engine: 5.2 L V10
        Horsepower: 562 to 602 hp
        Transmission: 7-speed automatic
        Dimensions: 174″ L x 76″ W x 49″ H

        2. 2024 Audi RS 3
        MSRP:From $62,300
        MPG: 19 city / 29 highway
        Engine :2.5 L 5-cylinder
        Horsepower :401 hp
        Transmission :7-speed automatic
        Dimensions :179″ L x 73″ W x 56″ H
                
        """)



main()
