import tkinter as tk
from tkinter import ttk, messagebox
root = tk.Tk()
root.geometry("500x550")
root.title("BMI Calculator")

tk.Label(root,text="Age :",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=0,column=0,padx=10,pady=10)
age=tk.StringVar()
tk.Entry(root,textvariable=age,font=("Arial", 12), bg="#e6f2ff",  relief="groove").grid(row=0,column=1,padx=10,pady=10)


tk.Label(root, text="Gender:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=10)
gender = tk.StringVar(value="Male")
# Create a Combobox with the new style
style = ttk.Style()
style.configure('TCombobox', font=("Arial", 12))  # Change font to Helvetica, spyhtonize 12

gender_list=["Male","Female"]
combo=ttk.Combobox(root,values=gender_list,style='TCombobox',font=("Arial", 12, "bold"))
combo.set('Select a Gender') 
combo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Height - cm:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=2, column=0, padx=10, pady=10)
height=tk.StringVar()
tk.Entry(root,textvariable=height,font=("Arial", 12), bg="#e6f2ff",  relief="groove").grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="weight - kg:",font=("Arial", 16, "bold"), fg="#001f3f",  bg="#f7f7f7").grid(row=3, column=0, padx=10, pady=10)
weight=tk.StringVar()
tk.Entry(root,textvariable=weight,font=("Arial", 12), bg="#e6f2ff",  relief="groove").grid(row=3, column=1, padx=10, pady=10)

def fun():
    h=height.get()
    w=weight.get()
    m=int(h)/100
    bmi=int(w)/(m*m)
    msg=f"Your BMI is {bmi:0.2f}"
    print(msg)
    messagebox.showinfo("BMI",message=msg)

# Submit button
btn_submit = tk.Button(root, text="Submit Reservation", command=fun,font=("Arial", 12), bg="#28a745",  fg="white", activebackground="#218838",  relief="raised")
btn_submit.grid(row=4, columnspan=6, pady=20)

# Define the categories, descriptions, and colors
bmi_info = [
    ("Underweight: Less than 18.5", "lightblue"),
    ("Optimum range: 18.5 to 24.9", "lightgreen"),
    ("Overweight: 25 to 29.9", "lightyellow"),
    ("Class I obesity: 30 to 34.9", "orange"),
    ("Class II obesity: 35 to 39.9", "red"),
    ("Class III obesity: More than 40", "darkred")
]
r=5
# # Create a Label for each category with styling
for info, color in bmi_info:
    label = tk.Label(root, text=info, bg=color, fg="black", font=("Arial", 15,"bold"))
    label.grid(row=r, columnspan=6, pady=5)
    r+=1
# listbox = tk.Listbox(root, height=6, width=50, font=("Arial", 15,'bold'))
# listbox.grid(row=5, column=0, padx=10, pady=10)
# # listbox.grid(row=5, columnspan=6, pady=5)
# for item, color in bmi_info:
#     listbox.insert(tk.END, item)
#     # Create a label for each item with color
#     listbox.itemconfig(tk.END, {'bg': color})

root.mainloop()
