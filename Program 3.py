import tkinter as tk
import tkinter.messagebox


class LongDistanceCalls:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Long-Distance Calls Calculator")

        self.RateType = tk.StringVar()
        self.RateType.set("Daytime")

        self.Daytime_rb = tk.Radiobutton(self.main_window, text="Daytime (6:00 AM - 5:59 PM) = $0.02/min", variable=self.RateType, value="Daytime")
        self.Daytime_rb.pack(anchor='w')
        self.Evening_rb = tk.Radiobutton(self.main_window, text="Evening (6:00 PM - 11:59 PM) = $0.12/min", variable=self.RateType, value="Evening")
        self.Evening_rb.pack(anchor='w')
        self.OffPeak_rb = tk.Radiobutton(self.main_window, text="Off Peak (12:00 AM - 5:59 AM) = $0.05/min",variable=self.RateType, value="OffPeak")
        self.OffPeak_rb.pack(anchor='w')

        #entry widget
        self.minutes_label = tk.Label(self.main_window, text="Number of minutes:")
        self.minutes_label.pack()
        self.minutes_entry = tk.Entry(self.main_window)
        self.minutes_entry.pack()

        #calculate button
        self.calc_button = tk.Button(self.main_window, text="Calculate Charge", command=self.LongDistanceCalls)
        self.calc_button.pack(pady=10)

        #quit button
        self.quit_button = tk.Button(self.main_window, text="quit", command=self.main_window.destroy)
        self.quit_button.pack(pady=10)

        tk.mainloop()

    def LongDistanceCalls(self):
        try:
            minutes = float(self.minutes_entry.get())
            rate = 0

            if self.RateType.get() == "Daytime":
                rate = 0.02
            elif self.RateType.get() == "Evening":
                rate = 0.12
            elif self.RateType.get() == "OffPeak":
                rate = 0.05

            charge = minutes * rate
            tk.messagebox.showinfo("Price of Call", f"Your total charge is ${charge:.2f}")

        except ValueError:
            tk.messagebox.showerror("Invlaid Input", "Try again.")



if __name__ == '__main__':
    LongDistanceCalls()