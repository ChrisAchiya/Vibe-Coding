import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        name = name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a student's name.")
            return
        
        marks = []
        for i in range(3):
            mark_str = mark_entries[i].get().strip()
            if not mark_str:
                messagebox.showerror("Error", f"Please enter mark for subject {i+1}.")
                return
            mark = float(mark_str)
            marks.append(mark)
        
        average = sum(marks) / 3
        
        if average >= 75:
            grade = 'A'
        elif average >= 60:
            grade = 'B'
        elif average >= 40:
            grade = 'C'
        else:
            grade = 'Fail'
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "------------------------------\n")
        result_text.insert(tk.END, f"Name : {name}\n")
        result_text.insert(tk.END, f"Average: {average:.1f}\n")
        result_text.insert(tk.END, f"Grade : {grade}\n")
        result_text.insert(tk.END, "------------------------------\n")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for marks.")

def clear_fields():
    name_entry.delete(0, tk.END)
    for entry in mark_entries:
        entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# Create main window
root = tk.Tk()
root.title("Student Grade Calculator")

# Name input
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Marks inputs
mark_entries = []
for i in range(3):
    tk.Label(root, text=f"Mark for Subject {i+1}:").grid(row=i+1, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    mark_entries.append(entry)

# Buttons
calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=4, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=1, padx=10, pady=10)

# Result display
tk.Label(root, text="Result:").grid(row=5, column=0, padx=10, pady=5, sticky="ne")
result_text = tk.Text(root, height=6, width=30)
result_text.grid(row=5, column=1, padx=10, pady=5)

# Run the GUI
root.mainloop()