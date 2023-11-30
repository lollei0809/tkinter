from tkinter import ttk
import tkinter as tk
from temp_convert_func import temperature_converter


class temp_converter(tk.Tk):

    def __init__(self):
        super().__init__()

        self.settings = {'padx': 10, 'pady': 10}
        self.title("temp converter")

        self.convert_btn = tk.Button(self, text="convert", command=lambda: self.convert_clicked(self.temp_in.get(), self.unit_dropdown.get(), self.unit_dropdown2.get()))
        self.convert_btn.config(bg="red")

        self.result_label = tk.Label(self, text='⊙▂⊙')

        self.temp_in = tk.StringVar()
        self.temp_entry = tk.Entry(width=25, textvariable=self.temp_in)

        self.unit_dropdown = ttk.Combobox(values=["Kelvin", "Celsius", "Fahrenheit", "Rankine"], )
        self.unit_dropdown["state"] = "readonly"

        self.unit_dropdown2 = ttk.Combobox(values=["Kelvin", "Celsius", "Fahrenheit", "Rankine"])
        self.unit_dropdown2["state"] = "readonly"



        text = ["convert from", "temp", "convert to", "result"]
        x = 1
        for item in text:
            self.response_txt = tk.Label(self, text=item)
            self.response_txt.configure(font=("Broadway", 12, 'italic'))
            self.response_txt.grid(row=x, column=0, sticky="W", **self.settings)
            x += 1

        self.place_widgets()

    def place_widgets(self):
        global settings
        self.unit_dropdown.grid(row=1, column=1, sticky="W", **self.settings)
        self.temp_entry.grid(row=2, column=1, columnspan=2, **self.settings)
        self.unit_dropdown2.grid(row=3, column=1, sticky="W", **self.settings)
        self.result_label.grid(row=4, column=1, sticky="W", **self.settings)
        self.convert_btn.grid(row=5, column=0, **self.settings)

    def convert_clicked(self, Ptemp, Punit_from, Punit_to):
        new = temperature_converter(Ptemp, Punit_from, Punit_to)
        self.result_label.config(text=new)



if __name__ == '__main__':
    app = temp_converter()
    app.mainloop()
    app.geometry('1000x1000')
    app.resizable(1,1)
