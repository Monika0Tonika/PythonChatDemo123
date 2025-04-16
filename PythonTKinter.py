import tkinter as tk

#create main window
root = tk.Tk()
root.title("Basic GUI window")
root.geometry("300x350")

#label
label=tk.Label(root, text="This is a label")
label.pack(pady=5)

#input field- enty box
entry=tk.Entry(root)
entry.pack(pady=5)

#knapp
button=tk.Button(root, text="Click me")
button.pack(pady=5)

#radio buttons
radio1=tk.Radiobutton(root, text="Option 1", value=1)
radio1.pack()

radio2=tk.Radiobutton(root, text="Option 2", value=2)
radio2.pack()

#checkbox
checkbox=tk.Checkbutton(root, text="Check me")
checkbox.pack(pady=5)

#dropdown meny
options=["Javascrpt, Python, C#"]
dropdown_var=tk.StringVar(value=options[0])

dropdown_label=tk.Label(root, text="Favo language:")
dropdown_label.pack(pady=10)

dropdown=tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()

#run the app
root.mainloop()          

