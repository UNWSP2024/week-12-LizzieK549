'''Joe's Automotive performs the following routine maintenance service:

Oil Change - $30.00
Lube Job - $20.00
Radiator Flush - $40.00
Transmission Fluid - $100.00
Inspection - $35.00
Muffler replacement - $200.00
Tire Rotation - $20.00
Write a GUI with check buttons that allows the user to select any or all of these services.
 When the user clicks a button, the total charges should be displayed.'''

import tkinter
import tkinter as tk
import tkinter.messagebox
from winreg import FlushKey


class JoesAutomotive:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        self.main_window.geometry("400x300")

        #creating variables
        self.OilChange = tk.IntVar()
        self.LubeJob = tk.IntVar()
        self.RadiatorFlush = tk.IntVar()
        self.TransmissionFluid = tk.IntVar()
        self.Inspection = tk.IntVar()
        self.MufflerReplacement = tk.IntVar()
        self.TireRotation = tk.IntVar()

        #need to use checkbuttons
        self.create_checkbutton("Oil Change - $30.00", self.OilChange)
        self.create_checkbutton("Lube Job - $20.00", self.LubeJob)
        self.create_checkbutton("Radiator Flush= $40.00", self.RadiatorFlush)
        self.create_checkbutton("Transmission Fluid= $100.00", self.TransmissionFluid)
        self.create_checkbutton("Inspection= $35.00", self.Inspection)
        self.create_checkbutton("Muffler Replacement= $200.00", self.MufflerReplacement)
        self.create_checkbutton("Tire Rotation= $20.00", self.TireRotation)




        # Cost calculator:
        self.COST_button = tkinter.Button(self.main_window, text="Calculate", command=self.calculateTotal)
        self.COST_button.pack()

        # quit:
        self.quit_button = tkinter.Button(self.main_window, text="All Done (Exit)", command=self.main_window.destroy)
        self.quit_button.pack()

        tkinter.mainloop()

    def create_checkbutton(self, text, variable):
        cb = tk.Checkbutton(self.main_window, text=text, variable=variable)

        cb.pack(anchor='w')

    def calculateTotal(self):
        #Using if statements to add prices to the total
        total = 0
        if self.OilChange.get() == 1:
            total += 30
        if self.LubeJob.get() == 1:
            total += 20
        if self.RadiatorFlush.get() == 1:
            total += 40
        if self.TransmissionFluid.get() == 1:
            total += 100
        if self.Inspection.get() == 1:
            total += 35
        if self.MufflerReplacement.get() == 1:
            total += 200
        if self.TireRotation.get() == 1:
            total += 20

        tkinter.messagebox.showinfo("Total charges: $ ", str(total))

if __name__ == '__main__':
    JoesAutomotive()