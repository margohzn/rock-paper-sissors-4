import tkinter as tk
import random


class Single:

    def __init__(self, single_window):
        self.window = single_window
        self.window.geometry("550x600")
        self.window.title("Rock Paper Scissors, Single")
        self.window.configure(background = "white")

        self.player_score = 0 
        self.computor_score = 0 
        self.options = [("rock", 0), ("paper", 1), ("scissors", 2)]
        self.widgets()

    def widgets(self):
        title = tk.Label(self.window, text = "Rock Paper Sicorss!", bg = "white", fg = "black", font = ("Helvetica", 35), bd = 3, pady = 5, relief = tk.RIDGE).pack(pady = 10)
        self.winner_text = tk.Label(self.window, text = "", bg = "white", fg = "green", font = ("times", 20))
        self.winner_text.pack()

        #top frame
        option_frame = tk.Frame(self.window, borderwidth = 5, relief = tk.GROOVE)
        option_frame.configure(background = "#641A5D")

        choice_label = tk.Label(option_frame, text = "Your options:", bg = "#641A5D", fg = "black", font = ("times", 40)).pack()
        rock_button = tk.Button(option_frame, text = "Rock", command = lambda: self.get_player_choice(self.options[0])).pack(pady = 5)
        paper_button = tk.Button(option_frame, text = "Paper", command = lambda: self.get_player_choice(self.options[1])).pack(pady = 20)
        scissors_button = tk.Button(option_frame, text = "Scissors", command = lambda: self.get_player_choice(self.options[2])).pack(pady = 5)

        option_frame.pack(fill = tk.BOTH, expand = True, pady = 10, padx = 2)

        #bottom frame
        result_frame = tk.Frame(self.window, relief = tk.GROOVE, borderwidth = 3)
        result_frame.configure(background = "#192581")

        score_label = tk.Label(result_frame, text = "Score:", font = ("times", 40), bg = "#192581", fg = "black").pack(side = "left", anchor = tk.NW)
        self.player_choice_label = tk.Label(result_frame, text = "You selected:", fg = "black", bg = "#192581", font = ("times", 20))
        self.player_score_label = tk.Label(result_frame, text = "Player score:", fg = "black", bg = "#192581", font = ("times", 20))
        self.computor_choice_label = tk.Label(result_frame, text = "Computor choice:", bg = "#192581", fg = "black", font = ("times", 20))
        self.computor_score_label = tk.Label(result_frame, text = "Computor score:", fg = "black", bg = "#192581", font = ("times", 20))

        self.player_choice_label.place(x = 10, y = 50)
        self.player_score_label.place(x = 300, y = 50)
        self.computor_choice_label.place(x = 10, y = 100)
        self.computor_score_label.place(x = 300, y = 100)

        result_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 2)

    # Function to select computor option
    def get_computor_choice(self):
        return random.choice(self.options)

    def get_player_choice(self, player_input):
        computor_input = self.get_computor_choice()
        print(computor_input)
        print(player_input)
        self.player_choice_label.config(text="You selected: " + player_input[0])
        self.computor_choice_label.config(text="Computor selected: " + computor_input[0])
        if player_input == computor_input:
            self.tie()
        if player_input[1] == 0:
            if computor_input[1] == 1:
                self.computor_wins()
            elif computor_input[1] == 2:
                self.player_wins()
        elif player_input[1] == 1:
            if computor_input[1] == 0:
                self.player_wins()
            elif computor_input[1] == 2:
                self.computor_wins()
        elif player_input[1] == 2:
            if computor_input[1] == 0:
                self.computor_wins()
            elif computor_input[1] == 1:
                self.player_wins()

    def tie(self):
        self.winner_text.config(text="Tie")
        self.player_score_label.config(text="Player score: " + str(self.player_score))
        self.computor_score_label.config(text="Computor score: " + str(self.computor_score))

    def player_wins(self):
        self.winner_text.config(text="Player Wins!")
        self.player_score += 1
        self.player_score_label.config(text="Player score: " + str(self.player_score))
        self.computor_score_label.config(text="Computor score: " + str(self.computor_score))

    def computor_wins(self):
        self.winner_text.config(text="Computor Wins!")
        self.computor_score += 1
        self.player_score_label.config(text="Player score: " + str(self.player_score))
        self.computor_score_label.config(text="Computor score: " + str(self.computor_score))



class Menu:

    def __init__(self, menu_window):
        self.window = menu_window
        self.window.geometry("200x200")
        self.window.title("Rock Paper Scissor")
        self.creat_widgets()

    def creat_widgets(self):
        title = tk.Label(self.window, text = "Selfect mode", font = ("times", 30)).pack(pady = 20)
        single = tk.Button(self.window, text = "Single player", font = ("times", 20), command = self.single_player).pack()
        multi = tk.Button(self.window, text = "Multi Player", font = ("times", 20), command = self.multi_player).pack(pady = 20)

    def single_player(self):
        self.window.destroy()
        single_window = tk.Tk()
        Single(single_window)
        single_window.mainloop()

    def multi_player(self):
        self.window.destroy()
        multi_window = tk.Tk()
        #Multi(multi_window)
        multi_window.mainloop()

window1 = tk.Tk()
Menu(window1)
window1.mainloop()