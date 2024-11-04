import tkinter
import json
from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Main(tkinter.Tk):
    def __init__(self):
        # Creating Windows
        tkinter.Tk.__init__(self)
        self.minsize(400, 600)
        self.maxsize(400, 600)
        self.title("TodoList")
        self.task_vars = []
        self.tasks = []
        self.main_frame = ttk.Frame(self, padding=(10, 8, 10, 8))
        self.main_frame.pack(fill=tkinter.BOTH, expand=True)
        input_frame = ttk.Frame(self.main_frame, padding=2)
        input_frame.pack(fill=tkinter.X)
        self.tasks_frame = ttk.Frame(self.main_frame, padding=(10, 8, 10, 8))
        self.tasks_frame.pack(fill=tkinter.BOTH, expand=True)

        self.task_entry = ttk.Entry(input_frame, width=38)
        self.task_entry.pack(side=tkinter.LEFT, expand=True)

        # Add button
        add_button = ttk.Button(
            input_frame, text="Add", command=self.add_task, bootstyle=(INFO, OUTLINE)
        )
        add_button.pack(side=tkinter.LEFT)
        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.create_task(task_text)
            self.task_entry.delete(0, tkinter.END)
            self.save_tasks()

    def create_task(self, task_text):
        # Create variable for checkbox
        var = tkinter.StringVar()
        self.task_vars.append(var)

        # Create task frame
        task_frame = ttk.Frame(self.tasks_frame, padding=1, border=1)
        task_frame.pack(fill=tkinter.X, pady=5)

        entry = ttk.Entry(task_frame)
        entry.insert(END, task_text)
        entry.pack(side=LEFT, fill=tkinter.X, expand=True)
        ttk.Button(
            task_frame, text="🗹", bootstyle=(INFO,),
            command=lambda: self.update_task(task_text, entry.get().strip())
        ).pack(side=LEFT)
        ttk.Button(
            task_frame, text="𐄂", bootstyle=(DANGER,), command=lambda: self.remove_task(task_frame, task_text)
        ).pack(side=LEFT)
        
        self.tasks.append(task_text)

    def remove_task(self, task_frame, task_text):
        task_frame.destroy()
        if task_text in self.tasks:
            self.tasks.remove(task_text)
        self.save_tasks()

    def update_task(self, old_text, new_text):
        if old_text in self.tasks:
            self.tasks[self.tasks.index(old_text)] = new_text
        self.save_tasks()


    def save_tasks(self):
        # Save tasks to JSON file
        data_file = Path("tasks.json")
        with open(data_file, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        # Load tasks from JSON file
        data_file = Path("tasks.json")
        if data_file.exists():
            with open(data_file, "r") as f:
                tasks = json.load(f)
                for task in tasks:
                    self.create_task(task)


if __name__ == "__main__":
    Main().mainloop()
