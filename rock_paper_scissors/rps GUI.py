import tkinter as tk
from tkinter import ttk
from rock_paper_scissors import PlayerObject, Player, HumanPlayer, ComputerPlayer, Game1


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Game1 = Game1()
        self.settings = {'padx': 10, 'pady': 10}
        self.title("rock paper scissors")
        self.menu_frame = Menu(self)
        self.game_frame = Game(self)

        self.pack_frames()

    def pack_frames(self):
        self.menu_frame.grid()

    def play(self):
        self.menu_frame.grid_forget()
        self.game_frame.grid()
        rounds = int(self.menu_frame.rounds_entry.get())
        self.Game1.set_max_rounds(rounds)
        self.game_frame.rounds.configure(text="{}/{} rounds".format(self.Game1.current_round, self.Game1.max_rounds))

    def back_to_menu(self):
        self.game_frame.grid_forget()
        self.menu_frame.grid()


class Menu(tk.Frame):
    def __init__(self, game_app):
        super().__init__()

        self.settings = {'padx': 10, 'pady': 10}
        self.game_app = game_app

        self.num_rounds = tk.StringVar()
        self.rounds_entry = tk.Entry(self, width=25, textvariable=self.num_rounds)

        self.player1_name = tk.StringVar()
        self.player1_name_entry = tk.Entry(self, width=25, textvariable=self.player1_name)

        self.player2_name = tk.StringVar()
        self.player2_name_entry = tk.Entry(self, width=25, textvariable=self.player2_name)

        self.player1_name_data = self.player2_name_entry.get()
        self.player2_name_data = self.player2_name_entry.get()

        self.human_player1_btn = tk.Button(self, text="Human", command=self.human_player1)
        self.computer_player1_btn = tk.Button(self, text="Computer", command=self.computer_player1)

        self.human_player2_btn = tk.Button(self, text="Human", command=self.human_player2)
        self.computer_player2_btn = tk.Button(self, text="Computer", command=self.computer_player2)

        self.go_to_game_btn = tk.Button(self, text="go to game", command=self.game_app.play)
        self.go_to_game_btn.config(bg="green")

        text = ["number of rounds:", "player 1", "player 2"]
        x = 0
        for item in text:
            self.response_txt = tk.Label(self, text=item)
            self.response_txt.configure(font=("Calibri", 12))
            self.response_txt.grid(row=x, column=0, sticky="W", **self.settings)
            x += 1

        self.place_widgets()

    def place_widgets(self):
        global settings
        self.rounds_entry.grid(row=0, column=1, **self.settings)
        self.human_player1_btn.grid(row=1, column=1, **self.settings)
        self.computer_player1_btn.grid(row=1, column=2, **self.settings)
        self.human_player2_btn.grid(row=2, column=1, **self.settings)
        self.computer_player2_btn.grid(row=2, column=2, **self.settings)
        self.go_to_game_btn.grid(row=3, column=1, **self.settings)

    def human_player1(self):
        self.player1_name_entry.grid(row=1, column=4, **self.settings)
        self.game_app.Game1.add_human_player(self.player1_name_entry.get())

    def computer_player1(self):
        self.player1_name_entry.grid_forget()
        self.game_app.game_frame.player1_options.grid_remove()
        self.game_app.game_frame.player1_options_label.grid_remove()
        self.game_app.Game1.add_computer_player()

    def human_player2(self):
        self.player2_name_entry.grid(row=2, column=4, **self.settings)
        self.game_app.Game1.add_human_player(self.player2_name_entry.get())

    def computer_player2(self):
        self.player2_name_entry.grid_forget()
        self.game_app.game_frame.player2_options.grid_remove()
        self.game_app.game_frame.player2_options_label.grid_remove()
        self.game_app.Game1.add_computer_player()


class Game(tk.Frame):
    def __init__(self, game_app):
        super().__init__()
        self.choice1 = None
        self.choice2 = None
        self.game_app = game_app
        self.settings = {'padx': 10, 'pady': 10}

        self.player1_score = 0
        self.player2_score = 0

        self.score = tk.Label(self, text=f"{self.player1_score}  :  {self.player2_score}")
        self.score.configure(font=("Calibri", 16))

        self.rounds = tk.Label(self, text=f"rounds:?")
        self.rounds.configure(font=("Calibri", 16))

        self.back_btn = tk.Button(self, text="back to menu", command=self.game_app.back_to_menu)

        self.player1_options = ttk.Combobox(self, values=["rock", "paper", "scissors"])
        self.player1_options["state"] = "readonly"
        self.player2_options = ttk.Combobox(self, values=["rock", "paper", "scissors"])
        self.player2_options["state"] = "readonly"

        self.player1_options_label = tk.Label(self, text="{} object".format(self.game_app.Game1.players[0].name))
        self.player2_options_label = tk.Label(self, text="{} object".format(self.game_app.Game1.players[1].name))

        self.play_game_button = tk.Button(self, text="PLAY", command=self.play_game)
        self.play_game_button.config(bg="green")

        self.results_label = tk.Label(self, text="{}".format(self.game_app.Game1.find_winner()))
        self.place_game_widgets()

    def place_game_widgets(self):
        self.rounds.grid(row=3, column=0, **self.settings)
        self.score.grid(row=4, column=0, **self.settings)
        self.player1_options_label.grid(row=1, column=0, **self.settings)
        self.player2_options_label.grid(row=2, column=0, **self.settings)
        self.player1_options.grid(row=1, column=1, **self.settings)
        self.player2_options.grid(row=2, column=1, **self.settings)
        self.back_btn.grid(row=6, column=0, **self.settings)
        self.results_label.grid(row=5, column=0, **self.settings)
        self.play_game_button.grid(row=6, column=1, **self.settings)

    def play_game(self):
        self.choice1 = self.player1_options.get
        self.choice2 = self.player2_options.get
        self.game_app.Game1.players[0].choose_object(self.choice1)
        self.game_app.Game1.players[1].choose_object(self.choice2)


if __name__ == '__main__':
    app = GameApp()
    app.mainloop()
