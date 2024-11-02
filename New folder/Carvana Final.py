from tkinter import *

window = Tk()
window.title("Carvana")

welcome_text = Label(window, text = """
    Welcome To Carvana
    Glad To See You Here
                     """)
welcome_text.config(font = ("Arial", 14))
welcome_text.pack()

output_text = Text(window, height=15, width=50, font=("Arial", 12))
output_text.pack(pady= 10)

def read_file(file_name):
    with open(file_name) as file:
        content = file.read()
        output_text.insert(END, content)

def read_ferrari():
    read_file("ferrari.txt")

def read_dodge():
    read_file("dodge.txt")

def read_chrysler():
    read_file("chrysler.txt")

def read_chevrolet():
    read_file("chevrolet.txt")

def read_bentley():
    read_file("bentley.txt")

def read_cadillac():
    read_file("cadillac.txt")

def read_ford():
    read_file("ford.txt")

def read_bmw():
    read_file("bmw.txt")

def read_audi():
    read_file("audi.txt")

# Create buttons for each car
ferrari = Button(window, text="Ferrari", command=read_ferrari, font=("Arial", 20, "bold"), bg = "#b8ffeb")
dodge = Button(window, text="Dodge", command=read_dodge, font=("Arial", 20, "bold"), bg = "#b8ffeb")
bmw = Button(window, text="BMW", command=read_bmw, font=("Arial", 20, "bold"), bg = "#b8ffeb")
ford = Button(window, text="Ford", command=read_ford, font=("Arial", 20, "bold"), bg = "#b8ffeb")
bentley = Button(window, text="Bentley", command=read_bentley, font=("Arial", 20, "bold"), bg = "#b8ffeb")
cadillac = Button(window, text="Cadillac", command=read_cadillac, font=("Arial", 20, "bold"), bg = "#b8ffeb")
audi = Button(window, text="Audi", command=read_audi, font=("Arial", 20, "bold"), bg = "#b8ffeb")
chrysler = Button(window, text="Chrysler", command=read_chrysler, font=("Arial", 20, "bold"), bg = "#b8ffeb")
chevrolet = Button(window, text="Chevrolet", command=read_chevrolet, font=("Arial", 20, "bold"), bg = "#b8ffeb")

# Pack buttons into the window
ferrari.pack(pady= 5)
dodge.pack(pady= 5)
bmw.pack(pady= 5)
ford.pack(pady= 5)
bentley.pack(pady= 5)
cadillac.pack(pady=5)
audi.pack(pady= 5)
chrysler.pack(pady= 5)
chevrolet.pack(pady= 5)

window.mainloop()
