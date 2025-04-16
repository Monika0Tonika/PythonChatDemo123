from tkinter import *
import random
from PIL import Image, ImageTk

# Images
elephant_image = ImageTk.PhotoImage(Image.open("Elephant.png"))
cat_image = ImageTk.PhotoImage(Image.open("Cat.png"))
mouse_image = ImageTk.PhotoImage(Image.open("Mouse.png"))

# Dictionary for easy access
images = {
    "elephant": elephant_image,
    "cat": cat_image,
    "mouse": mouse_image
}

# Define function
def outcome(user_choice):
    outcomes = ["elephant", "mouse", "cat"]
    computer_choice = random.choice(outcomes)
    computer_image_label.config(image=images[computer_choice])
    computer_image_label.image = images[computer_choice]

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "elephant" and computer_choice == "cat") or \
         (user_choice == "cat" and computer_choice == "mouse") or\
         (user_choice == "mouse" and computer_choice == "elephan"):
        result = "You win!"
    else:
        result = "You lose!"

    label_result.config(text=result)

# GUI
root = Tk()
root.title("Elaphant, Cat, Mouse")
root.geometry("500x500")


# Labels
label1 = Label(root, text="Welcome to the fun game of Elaphant, Cat, Mouse!", font="Calibri 15")
label1.pack()

label3 = Label(root, text="Choose your fighter:", font="Calibri 13")
label3.pack(pady=10)


# Buttons
elephant_button = Button(root, image=elephant_image, padx=50, pady=50, command=lambda:outcome("elephant"))
elephant_button.place(x=30, y=85)

cat_button = Button(root, image=cat_image, padx=65, pady=50, command=lambda:outcome("cat"))
cat_button.place(x=200, y=85)

mouse_button = Button(root, image=mouse_image, padx=52.5, pady=50, command=lambda:outcome("mouse"))
mouse_button.place(x=365, y=85)

# Show computer's choice
computer_label = Label(root, text="Computer chose:", font="Calibri 13")
computer_label.pack(pady=10)

computer_image_label = Label(root)
computer_image_label.pack()

# Result label
result_label = Label(root, text="", font="Calibri 15", fg="blue")
result_label.pack(pady=20)

root.mainloop()