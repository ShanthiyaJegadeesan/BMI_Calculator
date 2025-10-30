import tkinter as tk

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
    text="Weight",
    bg="light yellow",
    font=("Derby",15)
    )
#weight_label.pack(padx=10,pady=10)

weight_entry=tk.Entry(grid_frame,width=15)
#weight_entry.pack(padx=10)

height_label=tk.Label(
    grid_frame,
    text="Height",
    bg="light yellow",
    font=("Derby",15)
    )
#height_label.pack(padx=10,pady=10)

height_entry=tk.Entry(grid_frame,width=15)
#height_entry.pack(padx=10,pady=10)

grid_frame.pack(pady=10)
weight_label.grid(row=0,column=0,padx=10,pady=5)
weight_entry.grid(row=1,column=0,padx=10,pady=5)
height_label.grid(row=0,column=1,padx=10,pady=5)
height_entry.grid(row=1,column=1,padx=10,pady=5)

calculate_button=tk.Button(
    window,
    text="Calculate",
    bg="red",
    font=("derby",15)
    )
calculate_button.pack(padx=50)

calculate_entry=tk.Entry()
calculate_entry.pack(padx=5,pady=5)












window.mainloop()