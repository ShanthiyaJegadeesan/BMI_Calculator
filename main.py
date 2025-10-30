import tkinter as tk
from tkinter import messagebox
def bmi():
    try:

        weight=float(weight_entry.get())
        height=float(height_entry.get())
        if height<=0 or weight<=0:
            messagebox.showerror("Invalid Input","Height and Weight must be greater than 0")
    except ValueError:
        messagebox.showerror("Input Error","Please input valid number for height and weight")


    bmi_calculation= weight/(height**2)
    print(f"{bmi_calculation:.2f}")
    calculate_entry.delete(0,tk.END)
    if bmi_calculation<18.5:
        calculate_entry.config(fg="blue",bg="light blue")
        calculate_entry.insert(0,f"{bmi_calculation:.2f} --> Underweight")
    elif 18.5<= bmi_calculation <=24.9:
        calculate_entry.config(fg="green",bg="light green")
        calculate_entry.insert(0,f"{bmi_calculation:.2f} --> Normal")
    elif 25<= bmi_calculation <=29.9:
        calculate_entry.config(fg="orange",bg="light yellow")
        calculate_entry.insert(0,f"{bmi_calculation:.2f} --> Overweight")
    else:
        calculate_entry.config(fg="red",bg="light pink")
        calculate_entry.insert(0,f"{bmi_calculation:.2f} --> Obese")
    
    
def clear_field():
    height_entry.delete(0,tk.END)
    weight_entry.delete(0,tk.END)
    calculate_entry.delete(0,tk.END)

    

window=tk.Tk()
window.title("BMI Calculator")
window.config(bg="light blue")
window.minsize(400,400)

grid_frame=tk.Frame(
    window,
    bg="light blue",
)

weight_label=tk.Label(
    grid_frame,
    text="Weight(kg)",
    bg="light yellow",
    font=("Derby",15)
    )


weight_entry=tk.Entry(grid_frame,width=15)


height_label=tk.Label(
    grid_frame,
    text="Height(m)",
    bg="light yellow",
    font=("Derby",15)
    )


height_entry=tk.Entry(grid_frame,width=15)


grid_frame.pack(pady=10)
weight_label.grid(row=0,column=0,padx=10,pady=5)
weight_entry.grid(row=1,column=0,padx=10,pady=5)
height_label.grid(row=0,column=1,padx=10,pady=5)
height_entry.grid(row=1,column=1,padx=10,pady=5)

calculate_button=tk.Button(
    window,
    text="Calculate",
    bg="red",
    font=("derby",15),
    command=bmi
    )
calculate_button.pack(padx=5)

calculate_entry=tk.Entry()
calculate_entry.pack(padx=5,pady=5)



clear_button=tk.Button(text="clear",bg="grey",font=("ariel",15),command=clear_field)
clear_button.pack(padx=5,pady=5)

    














window.mainloop()