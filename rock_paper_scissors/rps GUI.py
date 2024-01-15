import tkinter as tk
from rock_paper_scissors import PlayerObject


class RPS(tk.Tk):

    def __init__(self):
        super().__init__()

        self.settings = {'padx': 10, 'pady': 10}
        self.title("Rock paper scissors")

        self.rps_btn = tk.Button(self, text="rock paper scissors", command = self.rps_selected)
        self.rpsls_btn = tk.Button(self, text="rock paper scissors lizard spock", command=self.rpsls_selected)

        self.num_rounds = tk.StringVar()
        self.rounds_entry = tk.Entry(width=25, textvariable=self.num_rounds)

        self.opponent_name = tk.StringVar()
        self.name_entry = tk.Entry(width=25, textvariable=self.opponent_name)

        self.human_opponent_btn = tk.Button(self, text="Human", command=self.human_opponent)
        self.computer_opponent_btn = tk.Button(self, text="computer", command=self.computer_opponent)
        self.name_label = tk.Label(self, text="opponent name:")

        self.rock_btn = tk.Button(self, text="ROCK")
        self.rock_btn.config(bg="grey")

        self.paper_btn = tk.Button(self, text="PAPER")
        self.paper_btn.config(bg="white")

        self.scissors_btn = tk.Button(self, text="SCISSORS")
        self.scissors_btn.config(bg="red")

        self.lizard_btn = tk.Button(self, text="LIZARD")
        self.lizard_btn.config(bg="green")

        self.spock_btn = tk.Button(self, text="SPOCK")
        self.spock_btn.config(bg="gold")

        text = ["   game type    ", "number of rounds", "    opponent    ",]
        x = 0
        for item in text:
            self.response_txt = tk.Label(self, text=item)
            self.response_txt.configure(font=("Calibri", 12))
            self.response_txt.grid(row=x, column=0, sticky="W", **self.settings)
            x += 1

        self.place_widgets()

    def place_widgets(self):
        global settings
        self.rps_btn.grid(row=0, column=1, **self.settings)
        self.rpsls_btn.grid(row=0, column=2, **self.settings)
        self.rounds_entry.grid(row=1, column=1, **self.settings)
        self.human_opponent_btn.grid(row=2, column=1, **self.settings)
        self.computer_opponent_btn.grid(row=2, column=2, **self.settings)
        self.rock_btn.grid(row=5, column=0, **self.settings)
        self.paper_btn.grid(row=5, column=1, **self.settings)
        self.scissors_btn.grid(row=5, column=2, **self.settings)

    def rpsls_selected(self):
        self.lizard_btn.grid(row=5, column=3, **self.settings)
        self.spock_btn.grid(row=5, column=4, **self.settings)

    def rps_selected(self):
        self.lizard_btn.grid_remove()
        self.spock_btn.grid_remove()

    def human_opponent(self):
        self.name_label.grid(row=2, column=3, **self.settings)
        self.name_entry.grid(row=2, column=4, **self.settings)

    def computer_opponent(self):
        self.name_label.grid_forget()
        self.name_entry.grid_forget()

if __name__ == '__main__':
    app = RPS()
    app.mainloop()
