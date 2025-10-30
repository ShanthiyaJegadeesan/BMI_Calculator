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





    














window.mainloop()