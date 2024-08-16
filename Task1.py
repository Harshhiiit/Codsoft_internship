import tkinter as tk
from random import choice
from PIL import Image, ImageTk

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("400x400")
        self.window.configure(bg='#f0f0f0')  # Set background color

        self.user_score = 0
        self.computer_score = 0

        self.rock_image = ImageTk.PhotoImage(Image.open("stone.png").resize((100, 100)))
        self.paper_image = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
        self.scissors_image = ImageTk.PhotoImage(Image.open("sizer.png").resize((100, 100)))

        self.create_widgets()
    
    def create_widgets(self):
        title_label = tk.Label(self.window, text="Rock, Paper, Scissors", font=("Arial", 24, "bold"), bg='#f0f0f0')
        title_label.pack(pady=10)

        self.user_frame = tk.Frame(self.window, bg='#f0f0f0')
        self.user_frame.pack(pady=10)

        self.user_label = tk.Label(self.user_frame, text="User", font=("Arial", 18), bg='#f0f0f0')
        self.user_label.pack()

        self.user_image_label = tk.Label(self.user_frame, image="")
        self.user_image_label.pack()

        self.computer_frame = tk.Frame(self.window, bg='#f0f0f0')
        self.computer_frame.pack(pady=10)

        self.computer_label = tk.Label(self.computer_frame, text="Computer", font=("Arial", 18), bg='#f0f0f0')
        self.computer_label.pack()

        self.computer_image_label = tk.Label(self.computer_frame, image="")
        self.computer_image_label.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 18, "bold"), bg='#f0f0f0')
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.window, text="Score - User: 0, Computer: 0", font=("Arial", 16), bg='#f0f0f0')
        self.score_label.pack(pady=10)

        button_frame = tk.Frame(self.window, bg='#f0f0f0')
        button_frame.pack(pady=10)

        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("rock"), width=10)
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("paper"), width=10)
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("scissors"), width=10)
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.reset_button = tk.Button(self.window, text="Play Again", command=self.reset_game, bg='#4682B4', fg='#FFFFFF', font=("Arial", 12, "bold"))
        self.reset_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "Tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "User wins!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.display_choices(user_choice, computer_choice)
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - User: {self.user_score}, Computer: {self.computer_score}")

    def display_choices(self, user_choice, computer_choice):
        if user_choice == "rock":
            self.user_image_label.config(image=self.rock_image)
        elif user_choice == "paper":
            self.user_image_label.config(image=self.paper_image)
        else:
            self.user_image_label.config(image=self.scissors_image)

        if computer_choice == "rock":
            self.computer_image_label.config(image=self.rock_image)
        elif computer_choice == "paper":
            self.computer_image_label.config(image=self.paper_image)
        else:
            self.computer_image_label.config(image=self.scissors_image)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="Score - User: 0, Computer: 0")
        self.user_image_label.config(image="")
        self.computer_image_label.config(image="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
