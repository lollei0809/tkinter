import tkinter as tk


class ClickApp(tk.Tk):
    def __init__(self):
        # Initiialised the tk.Tk app
        super().__init__()

        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.clicker_frame.pack(side=tk.LEFT)

        self.background_color_frame = BackgroundColorFrame(self)
        self.background_color_frame.pack(side=tk.LEFT)


class ButtonClicker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create a click counter
        self.clicks = 0

        # This creates the widgets
        self.title_txt = tk.Label(self, text="My clicker app")
        self.btn = tk.Button(self, text="Press me", command=self.add_click)
        self.response_txt = tk.Label(self, text="")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}

        self.title_txt.grid(row=0, column=0, **settings)
        self.btn.grid(row=1, column=0, **settings)
        self.response_txt.grid(row=2, column=0, **settings)

    def add_click(self):
        self.clicks += 1
        click_text = f"Number of clicks = {self.clicks}"
        self.response_txt.config(text=click_text)


class BackgroundColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Color choices
        self.colors = ['red', 'green', 'yellow']

        # Create a tk variable which will hold the value of the selected color
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        # Create radio buttons (list comprehension)
        self.radio_options = (tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color)
                              for color in self.colors)

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        color = self.selected_color.get()
        self.config(bg=color)
        self.master.config(bg=color)
        self.master.clicker_frame.config(bg=color)


if __name__ == '__main__':
    app = ClickApp()
    app.mainloop()
