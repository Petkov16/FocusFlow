import tkinter as tk
from tkinter import messagebox

class TimeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Management App")
        self.root.geometry("400x500")
        self.root.configure(bg="#F7F7F7")

        # Task list
        self.tasks = []

        # Task list UI
        self.task_label = tk.Label(root, text="Your Tasks", font=("Helvetica", 16, "bold"), bg="#F7F7F7", fg="#333")
        self.task_label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=30, height=8, font=("Helvetica", 12), bg="#FFF", fg="#333", selectbackground="#FFD966", relief="solid", bd=2, highlightthickness=0)
        self.task_listbox.pack(pady=5, padx=15)

        self.task_entry = tk.Entry(root, width=28, font=("Helvetica", 12), bg="#FFF", fg="#333", borderwidth=2, relief="solid")
        self.task_entry.pack(pady=5, padx=15)

        self.add_task_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), width=12, command=self.add_task, bg="#4CAF50", fg="#FFF", relief="solid")
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(root, text="Remove Task", font=("Helvetica", 12), width=12, command=self.remove_task, bg="#F44336", fg="#FFF", relief="solid")
        self.remove_task_button.pack(pady=5)

        # Timer UI
        self.timer_label = tk.Label(root, text="Pomodoro Timer (25:00)", font=("Helvetica", 16, "bold"), bg="#F7F7F7", fg="#333")
        self.timer_label.pack(pady=20)

        self.time_left = 25 * 60  # 25 minutes in seconds
        self.timer_running = False

        button_frame = tk.Frame(root, bg="#F7F7F7")
        button_frame.pack(pady=10)

        self.start_timer_button = tk.Button(button_frame, text="Start Timer", font=("Helvetica", 12), width=10, command=self.start_timer, bg="#2196F3", fg="#FFF", relief="solid")
        self.start_timer_button.grid(row=0, column=0, padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def update_timer_label(self):
        minutes, seconds = divmod(self.time_left, 60)
        self.timer_label.config(text=f"Pomodoro Timer ({minutes:02}:{seconds:02})")

    def countdown(self):
        if self.timer_running:
            if self.time_left > 0:
                self.time_left -= 1
                self.update_timer_label()
                self.root.after(1000, self.countdown)
            else:
                self.timer_running = False
                messagebox.showinfo("Time's up!", "25 minutes are up! Take a short break.")

    def on_closing(self):
        self.timer_running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeManagementApp(root)
    root.mainloop()
