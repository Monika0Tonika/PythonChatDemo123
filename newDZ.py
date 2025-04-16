from tkinter import *
import random
from PIL import Image, ImageTk

player_score = 0
computer_score = 0

# Define functions
def outcome(user_choice):
    global player_score, computer_score
    outcomes = ["elephant", "mouse", "cat"]
    computer_choice = random.choice(outcomes)
    label_computer_choice.config(text=f"Computer: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "elephant" and computer_choice == "cat") or \
         (user_choice == "cat" and computer_choice == "mouse") or \
         (user_choice == "mouse" and computer_choice == "elephant"):
        result = "You win!"
        player_score += 1
        label_player_score.config(text=f"Player: {player_score}")
    else:
        result = "You lose!"
        computer_score += 1
        label_computer_score.config(text=f"Computer: {computer_score}")

    label_result.config(text=result)

    if player_score == 10 or computer_score == 10:
        winner = "You won the game!" if player_score == 10 else "Computer won the game!"
        label_result.config(text=winner, fg="blue")

        elephant_button.config(state=DISABLED)
        cat_button.config(state=DISABLED)
        mouse_button.config(state=DISABLED)

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    label_player_score.config(text="Player: 0")
    label_computer_score.config(text="Computer: 0")
    label_result.config(text="")
    label_computer_choice.config(text="Computer: ")

    elephant_button.config(state=NORMAL)
    cat_button.config(state=NORMAL)
    mouse_button.config(state=NORMAL)


# GUI
root = Tk()
root.title("Elaphant, Cat, Mouse")
root.geometry("500x400")
root.configure(background="beige")
root.iconbitmap("heart_icon.ico")

# Labels
label1 = Label(root, text="Welcome to the fun game of Elephant, Cat, Mouse!", bg="beige", font="Calibri 15")
label1.pack()

label3 = Label(root, text="Choose your fighter:", bg="beige", font="Calibri 13")
label3.pack(pady=10)

# Images
elephant_image = ImageTk.PhotoImage(Image.open("Elephant.png"))
cat_image = ImageTk.PhotoImage(Image.open("Cat.png"))
mouse_image = ImageTk.PhotoImage(Image.open("Mouse.png"))

# Buttons
elephant_button = Button(root, image=elephant_image, bg="beige", padx=50, pady=50, command=lambda:outcome("elephant"))
elephant_button.place(x=30, y=85)

cat_button = Button(root, image=cat_image, bg="beige", padx=65, pady=50, command=lambda:outcome("cat"))
cat_button.place(x=200, y=85)

mouse_button = Button(root, image=mouse_image, bg="beige", padx=52.5, pady=50, command=lambda:outcome("mouse"))
mouse_button.place(x=365, y=85)

# Labels to show computer choice and result
label_computer_choice = Label(root, text="Computer: ", bg="beige", font="Calibri 13")
label_computer_choice.place(x=180, y=250)

label_result = Label(root, text="", bg="beige", font="Calibri 15", fg="red")
label_result.place(x=200, y=280)

# Labels to show the scores
label_player_score = Label(root, text="Player: 0", bg="beige", font="Calibri 15")
label_player_score.place(x=0, rely=1.0, anchor='sw')

label_computer_score = Label(root, text="Computer: 0", bg="beige", font="Calibri 15")
label_computer_score.place(relx=1.0, rely=1.0, anchor='se')

play_again_button = Button(root, text="Play Again", bg="beige", font="Calibri 12", command=reset_game)
play_again_button.place(relx=0.5, rely=1.0, anchor='s', y=-10)

root.mainloop()