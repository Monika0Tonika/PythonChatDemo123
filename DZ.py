from tkinter import *
import random
from PIL import Image, ImageTk

# Define function
def outcome(user_choice):
    outcomes = ["elephant", "mouse", "cat"]
    computer_choice = random.choice(outcomes)
    label_computer_choice.config(text=f"Computer: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "elephant" and computer_choice == "cat") or \
         (user_choice == "cat" and computer_choice == "mouse") or \
         (user_choice == "mouse" and computer_choice == "elephant"):
        result = "You win!"
    else:
        result = "You lose!"

    label_result.config(text=result)

# GUI
root = Tk()
root.title("Elaphant, Cat, Mouse")
root.geometry("500x400")


# Labels 
label1 = Label(root, text="Welcome to the fun game of Elaphant, Cat, Mouse!", font="Calibri 15")
label1.pack()

label3 = Label(root, text="Choose your fighter:", font="Calibri 13")
label3.pack(pady=10)

# Images
elephant_image = ImageTk.PhotoImage(Image.open("Elephant.png"))
cat_image = ImageTk.PhotoImage(Image.open("Cat.png"))
mouse_image = ImageTk.PhotoImage(Image.open("Mouse.png"))

# Buttons
elephant_button = Button(root, image=elephant_image, padx=50, pady=50, command=lambda:outcome("elephant"))
elephant_button.place(x=30, y=85)

cat_button = Button(root, image=cat_image, padx=65, pady=50, command=lambda:outcome("cat"))
cat_button.place(x=200, y=85)

mouse_button = Button(root, image=mouse_image, padx=52.5, pady=50, command=lambda:outcome("mouse"))
mouse_button.place(x=365, y=85)

# Labels to show computer choice and result
label_computer_choice = Label(root, text="Computer: ", font="Calibri 13")
label_computer_choice.place(x=180, y=250)

label_result = Label(root, text="", font="Calibri 15", fg="blue")
label_result.place(x=200, y=280)

# Labels to show the scores
label_player_score = Label(root, text="Player: 0", font="Calibri 15")
label_player_score.place(x=0, rely=1.0, anchor='sw')

label_computer_score = Label(root, text="Computer: 0", font="Calibri 15")
label_computer_score.place(relx=1.0, rely=1.0, anchor='se')

root.mainloop()