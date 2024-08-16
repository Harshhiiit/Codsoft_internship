import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Initialize the list of tasks
        self.tasks = []
        
        # Set background color for the main window
        self.root.configure(bg='#F0F8FF')
        
        # Define a common style for buttons
        button_style = {
            "bg": "#4682B4",
            "fg": "#FFFFFF",
            "font": ("Arial", 10, "bold"),
            "relief": tk.RAISED,
            "bd": 2
        }

        # Create the main frame with a background
        self.frame = tk.Frame(root, bg='#F0F8FF')
        self.frame.pack(pady=10)

        # Listbox to display tasks with a background and border
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE, bg='#FFFFFF', fg='#000000', font=("Arial", 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry box for adding new tasks with styling
        self.task_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        # Buttons with the defined style
        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task, **button_style)
        self.add_button.pack(pady=5)

        self.schedule_button = tk.Button(root, text="Schedule Task", width=15, command=self.schedule_task, **button_style)
        self.schedule_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", width=15, command=self.update_task, **button_style)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", width=15, command=self.delete_task, **button_style)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", width=15, command=self.clear_tasks, **button_style)
        self.clear_button.pack(pady=5)

        # Start the periodic check for alarms
        self.check_alarms()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "time": None})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def schedule_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks available to schedule. Please add a task first.")
            return

        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = selected_task_index[0]
            time_str = simpledialog.askstring("Schedule Task", "Enter time for the reminder (HH:MM in 24-hour format):")
            try:
                schedule_time = datetime.strptime(time_str, "%H:%M").time()
                self.tasks[selected_task]["time"] = schedule_time
                self.update_listbox()
            except ValueError:
                messagebox.showerror("Error", "Invalid time format. Please enter time as HH:MM in 24-hour format.")
        else:
            messagebox.showwarning("Warning", "You must select a task to schedule.")

    def check_alarms(self):
        now = datetime.now().time()
        for task in self.tasks:
            if task["time"] and now >= task["time"]:
                messagebox.showinfo("Reminder", f"Time to complete the task: {task['task']}")
                task["time"] = None  # Clear the time after reminder

        # Check again after 30 seconds
        self.root.after(30000, self.check_alarms)

    def update_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks available to update. Please add a task first.")
            return

        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = selected_task_index[0]
            new_task = simpledialog.askstring("Update Task", "Enter new task:")
            if new_task:
                self.tasks[selected_task]["task"] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks available to delete. Please add a task first.")
            return

        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = selected_task_index[0]
            del self.tasks[selected_task]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def clear_tasks(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks to clear.")
            return

        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["task"]
            if task["time"]:
                display_text += f" (Scheduled at {task['time'].strftime('%H:%M')})"
            self.task_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
