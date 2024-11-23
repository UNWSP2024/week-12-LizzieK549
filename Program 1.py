#Program #1: MPG Calculator
#Write a GUI program that calculates a car's gas mileage.
# #The program's window should have Entry widgets that
# let the user enter the number of gallons of gas the car holds,
# and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked,
# the program should display the numbaer of miles that the car may be driven per gallon of gas.
# Use the following formula to calculate miles per gallon:  MPG = miles / gallons.

import tkinter
import tkinter.messagebox


class MPGCalculator:
    def __init__(self):
        #window with entry widget
        self.main_window = tkinter.Tk()
        self.main_window.geometry("400x300")

        #label everything
        self.Gallons_label = tkinter.Label(self.main_window, text="Number of Gallons:")
        self.Gallons_label.pack()
        self.Gallons_entry = tkinter.Entry(self.main_window)
        self.Gallons_entry.pack()

        self.miles_label = tkinter.Label(self.main_window, text="Number of Miles:")
        self.miles_label.pack()
        self.miles_entry = tkinter.Entry(self.main_window)
        self.miles_entry.pack()

        #MPG calculator:
        self.MPG_button = tkinter.Button(self.main_window, text="Calculate", command=self.calculate)
        self.MPG_button.pack()

        #quit:
        self.quit_button = tkinter.Button(self.main_window, text="All Done (Exit)", command=self.main_window.destroy)
        self.quit_button.pack()

        tkinter.mainloop()
    def calculate(self):
        try:
            gallons = float(self.Gallons_entry.get())
            miles = float(self.miles_entry.get())

            mpg = miles / gallons

            tkinter.messagebox.showinfo("MPG:", f"The mileage of your car is {mpg: .2f} miles per gallon.")
        except:
            tkinter.messagebox.showinfo("Invalid input")

if __name__ == '__main__':
    MPGCalculator()



