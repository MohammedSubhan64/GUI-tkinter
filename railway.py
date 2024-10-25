import tkinter as tk
from tkinter import messagebox

def submit_reservation():
    # Collecting input data
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    source = source_var.get()
    destination = destination_var.get()
    travel_date = entry_date.get()
    train_number = entry_train_number.get()
    berth = berth_var.get()

    # Simple validation
    if all([name, age, gender, source, destination, travel_date, train_number, berth]):
        messagebox.showinfo("Reservation Successful", 
                            f"Name: {name}\nAge: {age}\nGender: {gender}\n"
                            f"Source: {source}\nDestination: {destination}\n"
                            f"Travel Date: {travel_date}\nTrain Number: {train_number}\n"
                            f"Berth: {berth}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

# Create the main window
root = tk.Tk()
root.title("Railway Reservation System")

# form
tk.Label(root, text="Name:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root,font=("Arial", 12), bg="#e6f2ff",  relief="groove")
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(root,font=("Arial", 12), bg="#e6f2ff",  relief="groove",show="*")
entry_age.grid(row=1, column=1, padx=10, pady=10)

gender_list=["Male","Female"]
tk.Label(root, text="Gender:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=2, column=0, padx=10, pady=10)
gender_var = tk.StringVar(value="Male")
# tk.Radiobutton(root, text="Male", variable=gender_var, value="Male",font=("Arial", 12), fg="#333333",  bg="#f7f7f7", selectcolor="#e6f2ff", activebackground="#d4edda").grid(row=2, column=1, padx=5, pady=5, sticky="w")
# tk.Radiobutton(root, text="Female", variable=gender_var, value="Female",font=("Arial", 12), fg="#333333",  bg="#f7f7f7", selectcolor="#e6f2ff", activebackground="#d4edda").grid(row=2, column=2, padx=5, pady=5, sticky="w")
from tkinter import ttk
combo=ttk.Combobox(root,values=gender_list,font=("Arial", 12, "bold"))
combo.set('Select a Gender') 
combo.grid(row=2, column=1, padx=10, pady=10)
# Journey Details
tk.Label(root, text="Source:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=3, column=0, padx=10, pady=10)
source_var = tk.StringVar(value="Hyderabad")
source_dropdown = tk.OptionMenu(root, source_var, "Hyderabad", "Mumbai", "Goa")
source_dropdown.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Destination:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=4, column=0, padx=10, pady=10)
destination_var = tk.StringVar(value="Mumbai")
destination_dropdown = tk.OptionMenu(root, destination_var, "Hyderabad", "Mumbai", "Goa")
destination_dropdown.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Travel Date (YYYY-MM-DD):",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=5, column=0, padx=10, pady=10)
entry_date = tk.Entry(root,font=("Arial", 12), bg="#e6f2ff",  relief="groove")
entry_date.grid(row=5, column=1, padx=10, pady=10)

# Train Information
tk.Label(root, text="Train Number:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=6, column=0, padx=10, pady=10)
entry_train_number = tk.Entry(root,font=("Arial", 12), bg="#e6f2ff",  relief="groove")
entry_train_number.grid(row=6, column=1, padx=10, pady=10)

# Berth Options
tk.Label(root, text="Select Berth Type:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=7, column=0, padx=10, pady=10)
berth_var = tk.StringVar(value="Sleeper")

berth_options = [
    ("Sleeper", "lightblue"),
    ("AC", "lightgreen"),
    ("General", "lightpink"),
    ("Tatkal", "lightcoral"),
    ("Waiting", "lightgrey")
]

for i, (option, color) in enumerate(berth_options):
    rb = tk.Radiobutton(root, text=option, variable=berth_var, value=option, bg=color)
    rb.grid(row=7, column=i + 1, padx=5, pady=5)

# Submit button
btn_submit = tk.Button(root, text="Submit Reservation", command=submit_reservation,font=("Arial", 12), bg="#28a745",  fg="white", activebackground="#218838",  relief="raised")
btn_submit.grid(row=8, columnspan=6, pady=20)

# Run the application
root.mainloop()
