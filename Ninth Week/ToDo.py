import tkinter as tk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("toDo list")
        self.tasks = []
        self.taskEntry = tk.Entry(root, width=50)
        self.addButton = tk.Button(root, text="Add Task", command=self.AddTask)#still needs a function
        self.taskList = tk.Listbox(root, selectmode=tk.SINGLE, width=50)#New function!!
        self.deleteButton = tk.Button(root, text="Delete Task", command=self.DeleteTask)#Function needed
        self.taskEntry.pack()
        self.addButton.pack()
        self.taskList.pack()
        self.deleteButton.pack()


    def AddTask(self):
        task = self.taskEntry.get()
        if task:
            self.tasks.append(task)
            self.updateTaskList()
            self.taskEntry.delete(0,tk.END)

    def DeleteTask(self):
        SelectedIndex = self.taskList.curselection()#Current Selection Command
        if SelectedIndex:
            self.tasks.pop(SelectedIndex[0])
            self.updateTaskList()

    def updateTaskList(self):
        self.taskList.delete(0, tk.END)
        for task in self.tasks:
            self.taskList.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = Todo(root)
    root.mainloop()