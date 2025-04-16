from tkinter import *
from tkinter import messagebox
import random


words=["leopard", "koala", "moose", "parrot", "penguin", "giraffe", "zebra", "donkey", "crow"]
word_choice=random.choice(words)

root = Tk()
root.title("Hangman")
root.geometry("500x500")

label1=Label(root, text="Hangman", font="calibri, 20")
label1.pack()

label1=Label(root, text="Guess the word", font="calibri, 12")
label1.pack()

root.mainloop()