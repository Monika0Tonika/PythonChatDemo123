from tkinter import *
import random
from PIL import Image, ImageTk

# Main window
root = Tk()
root.title("Elephant, Cat, Mouse")
root.geometry("500x500")

# Load images
elephant_img = ImageTk.PhotoImage(Image.open("Elephant.png"))
cat_img = ImageTk.PhotoImage(Image.open("Cat.png"))
mouse_img = ImageTk.PhotoImage(Image.open("Mouse.png"))

# Dictionary for easy access
images = {
    "elephant": elephant_img,
    "cat": cat_img,
    "mouse": mouse_img
}

# Labels
Label(root, text="Welcome to Elephant, Cat, Mouse!", font="Calibri 15").pack(pady=10)
Label(root, text="Choose your fighter:", font="Calibri 13").pack()

# Buttons
Button(root, image=elephant_img, command=lambda: play("elephant")).pack(side=LEFT, padx=10, pady=10)
Button(root, image=cat_img, command=lambda: play("cat")).pack(side=LEFT, padx=10, pady=10)
Button(root, image=mouse_img, command=lambda: play("mouse")).pack(side=LEFT, padx=10, pady=10)

# Show computer's choice
computer_label = Label(root, text="Computer chose:", font="Calibri 13")
computer_label.pack(pady=10)

computer_image_label = Label(root)
computer_image_label.pack()

# Result label
result_label = Label(root, text="", font="Calibri 15", fg="blue")
result_label.pack(pady=20)

# Game logic
def play(user_choice):
    options = ["elephant", "cat", "mouse"]
    computer_choice = random.choice(options)

    # Show computer's image
    computer_image_label.config(image=images[computer_choice])
    computer_image_label.image = images[computer_choice]

    # Determine result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "elephant" and computer_choice == "cat") or \
         (user_choice == "cat" and computer_choice == "mouse") or \
         (user_choice == "mouse" and computer_choice == "elephant"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=result)

# Buttons
Button(root, image=elephant_img, command=lambda: play("elephant")).pack(side=LEFT, padx=10, pady=10)
Button(root, image=cat_img, command=lambda: play("cat")).pack(side=LEFT, padx=10, pady=10)
Button(root, image=mouse_img, command=lambda: play("mouse")).pack(side=LEFT, padx=10, pady=10)

root.mainloop()