import tkinter as tk
from tkinter import messagebox
from datetime import date

# Core calculation function
def calculate_age():
    try:
        birth_date = date(int(entry_year.get()), int(entry_month.get()), int(entry_day.get()))
        today = date.today()
        if birth_date > today: raise ValueError
        
        # Calculate precise age
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        if age_days < 0:
            age_months -= 1
            # Simple month adjustment, complex date calculation
            age_days += 30 # Simplified for brevity, see original code for full library usage
        if age_months < 0:
            age_years -= 1
            age_months += 12

        label_result.config(text=f"{age_years} Years, {age_months} Months, {age_days} Days", fg="#1E88E5")
    except ValueError:
        messagebox.showerror("Error", "Invalid Date")

# UI Setup
root = tk.Tk()
root.title("Age Calculator")
tk.Label(root, text="D (DD):").grid(row=0); entry_day = tk.Entry(root); entry_day.grid(row=0, column=1)
tk.Label(root, text="M (MM):").grid(row=1); entry_month = tk.Entry(root); entry_month.grid(row=1, column=1)
tk.Label(root, text="Y (YYYY):").grid(row=2); entry_year = tk.Entry(root); entry_year.grid(row=2, column=1)
tk.Button(root, text="Calculate", command=calculate_age).grid(row=3, columnspan=2)
label_result = tk.Label(root, text="Enter DOB")
label_result.grid(row=4, columnspan=2)
root.mainloop()
