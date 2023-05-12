
import tkinter as tk
import inspect
import importlib.util

# load the module containing your functions
module_name = 'my_functions'  # change this to the name of your file
module_spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

# get a list of all functions defined in the module
function_list = inspect.getmembers(module, inspect.isfunction)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Functions")
        self.pack()

        # create a button for each function
        for function_name, function in function_list:
            button = tk.Button(self, text=function_name, command=lambda f=function: f())
            button.pack()

        # create a console frame
        console_frame = tk.Frame(self)
        console_frame.pack(fill='both', expand=True)

        # create a text widget for the console
        console_text = tk.Text(console_frame, wrap='word', state='disabled')
        console_text.pack(side='left', fill='both', expand=True)

        # create a scrollbar for the console
        console_scrollbar = tk.Scrollbar(console_frame)
        console_scrollbar.pack(side='right', fill='y')

        # connect the scrollbar to the text widget
        console_scrollbar.config(command=console_text.yview)
        console_text.config(yscrollcommand=console_scrollbar.set)

        # define a function to print text to the console
        def print_to_console(text):
            console_text.config(state='normal')
            console_text.insert('end', text + '\n')
            console_text.config(state='disabled')
            console_text.yview('end')

        # redirect stdout to the console
        import sys
        sys.stdout.write = print_to_console

# create the Tkinter window and run the app
root = tk.Tk()
app = App(master=root)
app.mainloop()
