import tkinter as tk
from rock_paper_scissors import PlayerObject, Player, HumanPlayer, ComputerPlayer, Game1



class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
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
        rounds=self.menu_frame.rounds_entry.get()
        current_round = 0
        self.game_frame.rounds.configure(text = "{}/{} rounds".format(current_round,rounds))

    def back_to_menu(self):
        self.game_frame.grid_forget()
        self.menu_frame.grid()


class Menu(tk.Frame):
    def __init__(self, game_app):
        super().__init__()

        self.settings = {'padx': 10, 'pady': 10}
        self.game_app = game_app

        self.rps_btn = tk.Button(self, text="rock paper scissors", command=self.rps_selected)
        self.rpsls_btn = tk.Button(self, text="rock paper scissors lizard spock", command=self.rpsls_selected)

        self.num_rounds = tk.StringVar()
        self.rounds_entry = tk.Entry(self, width=25, textvariable=self.num_rounds)

        self.player1_name = tk.StringVar()
        self.player1_name_entry = tk.Entry(self, width=25, textvariable=self.player1_name)

        self.player2_name = tk.StringVar()
        self.player2_name_entry = tk.Entry(self, width=25, textvariable=self.player2_name)

        self.player1_name_data=self.player2_name_entry.get()
        self.player2_name_data=self.player2_name_entry.get()

        self.human_player1_btn = tk.Button(self, text="Human", command=self.human_player1)
        self.computer_player1_btn = tk.Button(self, text="Computer", command=self.computer_player1)

        self.human_player2_btn = tk.Button(self, text="Human", command=self.human_player2)
        self.computer_player2_btn = tk.Button(self, text="Computer", command=self.computer_player2)

        self.play_btn = tk.Button(self, text="PLAY!", command=self.game_app.play)
        self.play_btn.config(bg="green")

        text = ["game type", "number of rounds:", "player 1", "player 2"]
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
        self.human_player1_btn.grid(row=2, column=1, **self.settings)
        self.computer_player1_btn.grid(row=2, column=2, **self.settings)
        self.human_player2_btn.grid(row=3, column=1, **self.settings)
        self.computer_player2_btn.grid(row=3, column=2, **self.settings)
        self.play_btn.grid(row=4, column=1, **self.settings)

    def rpsls_selected(self):
        self.game_app.game_frame.lizard1_btn.grid(row=2, column=3, **self.settings)
        self.game_app.game_frame.spock1_btn.grid(row=2, column=4, **self.settings)
        self.game_app.game_frame.lizard2_btn.grid(row=3, column=3, **self.settings)
        self.game_app.game_frame.spock2_btn.grid(row=3, column=4, **self.settings)

    def rps_selected(self):
        self.game_app.game_frame.lizard1_btn.grid_remove()
        self.game_app.game_frame.spock1_btn.grid_remove()
        self.game_app.game_frame.lizard2_btn.grid_remove()
        self.game_app.game_frame.spock2_btn.grid_remove()

    def human_player1(self):
        self.player1_name_entry.grid(row=2, column=4, **self.settings)
    def computer_player1(self):
        self.player1_name_entry.grid_forget()

    def human_player2(self):
        self.player2_name_entry.grid(row=3, column=4, **self.settings)
    def computer_player2(self):
        self.player2_name_entry.grid_forget()


class Game(tk.Frame):
    def __init__(self, game_app):
        super().__init__()
        self.game_app = game_app
        self.settings = {'padx': 10, 'pady': 10}

        self.player1_score=0
        self.player2_score=0

        self.score = tk.Label(self, text=f"{self.player1_score}  :  {self.player2_score}")
        self.score.configure(font=("Calibri", 16))

        self.rounds = tk.Label(self, text=f"enter number of rounds on menu page")
        self.rounds.configure(font=("Calibri", 16))

        self.back_btn = tk.Button(self, text="back to menu", command=self.game_app.back_to_menu)
        self.back_btn.config(bg="green")

        self.rock1_btn = tk.Button(self, text="rock")
        self.rock1_btn.config(bg="grey")

        self.paper1_btn = tk.Button(self, text="paper")
        self.paper1_btn.config(bg="white")

        self.scissors1_btn = tk.Button(self, text="scissors")
        self.scissors1_btn.config(bg="red")

        self.lizard1_btn = tk.Button(self, text="lizard")
        self.lizard1_btn.config(bg="green")

        self.spock1_btn = tk.Button(self, text="spock")
        self.spock1_btn.config(bg="gold")

        self.rock2_btn = tk.Button(self, text="rock")
        self.rock2_btn.config(bg="grey")

        self.paper2_btn = tk.Button(self, text="paper")
        self.paper2_btn.config(bg="white")

        self.scissors2_btn = tk.Button(self, text="scissors")
        self.scissors2_btn.config(bg="red")

        self.lizard2_btn = tk.Button(self, text="lizard")
        self.lizard2_btn.config(bg="green")

        self.spock2_btn = tk.Button(self, text="spock")
        self.spock2_btn.config(bg="gold")

        self.place_game_widgets()

    def place_game_widgets(self):
        self.rounds.grid(row=0,column=1,**self.settings)
        self.score.grid(row=1, column=2, **self.settings)
        self.rock1_btn.grid(row=2, column=0, **self.settings)
        self.paper1_btn.grid(row=2, column=1, **self.settings)
        self.scissors1_btn.grid(row=2, column=2, **self.settings)

        self.rock2_btn.grid(row=3, column=0, **self.settings)
        self.paper2_btn.grid(row=3, column=1, **self.settings)
        self.scissors2_btn.grid(row=3, column=2, **self.settings)

        self.back_btn.grid(row=4, column=0, **self.settings)


if __name__ == '__main__':
    app = GameApp()
    app.mainloop()
