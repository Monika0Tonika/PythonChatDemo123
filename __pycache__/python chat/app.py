import tkinter as tk
import pymongo

# connect to mongo
client=pymongo.MongoClient("mongodb://localhost:27017")
db= client["PythonChat"]
messages_col=db["messages"]

# gui
root=tk.Tk()
root.title("PythonChat")
root.geometry("500x500")

entry=tk.Entry(root, width=40)
entry.pack(pady=5)



def send_message():
    if entry.get:
        messages_col.insert_one({"text": entry.get()})
        entry.delete(0, tk.END)

send_button=tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

root.mainloop()






# git status (friviligt)
#git add .
# git commit -m"Added new code for mongo"
# git push