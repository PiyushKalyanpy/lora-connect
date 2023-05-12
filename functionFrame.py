import customtkinter as ctk
from settings import *
import inspect
import importlib.util
import datetime

class FunctionsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=WHITE, bg_color=TRANSPARENT, corner_radius=8)

        module_name = 'allFunctions'  # change this to the name of your file
        module_spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)

        self.functionPath = module_spec.origin

        # get a list of all functions defined in the module
        function_list = inspect.getmembers(module, inspect.isfunction)

        # frame for checkbox
        self.checkbox_frame = ctk.CTkFrame(self, fg_color=WHITE, bg_color=WHITE, corner_radius=8)
        self.checkbox_frame.pack(fill=ctk.X, side="top", padx=10, pady=10)

        # for loop for function buttons as CustomCHekButton
        for function_name, function in function_list:
            self.button = CustomCheckButton(self.checkbox_frame, functionName=function_name, function=function)
            self.button.pack(fill=ctk.X, side="left", padx=10, pady=10)

        # run all funciton button
        self.run_all_button = ctk.CTkButton(self.checkbox_frame, text="Run All", command=self.runAllFunctions, fg_color=MAIN_COLOR, text_color=WHITE)
        self.run_all_button.pack(fill=ctk.X, side="left", padx=10, pady=10)

        console_frame = ctk.CTkFrame(self, fg_color=WHITE, bg_color=BG_COLOR, corner_radius=5)
        console_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # show console as label in the frame
        console_label = ctk.CTkLabel(console_frame, text="Console", fg_color=WHITE, text_color=HEAD_FONT_COLOR,
                                        font=ctk.CTkFont(family='Roboto', size=12, weight="bold"), bg_color=WHITE, corner_radius=6)
        console_label.pack(anchor='nw')

        # text widget for the console
        console_text = ctk.CTkTextbox(console_frame, fg_color=BG_COLOR, wrap='word', text_color=HEAD_FONT_COLOR,
                                      bg_color=WHITE, state='disabled', activate_scrollbars=False, spacing1=10)
        console_text.pack(side='left', fill='both', expand=True)

        # scrollbar for the console
        console_scrollbar = ctk.CTkScrollbar(console_frame)
        console_scrollbar.pack( fill='x')

        # scrollbar to the text widget
        console_scrollbar.configure(command=console_text.yview)
        console_text.configure(yscrollcommand=console_scrollbar.set)

        # define a function to print text to the console
        console_text.configure(state='normal')
        console_text.insert('end', f"LoRa Connect \nCopyright (C) Piyush Kalyan. All rights reserved.\n")
        console_text.configure(state='disabled')

        def print_to_console(text):
            self.current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if text.strip():
                console_text.configure(state='normal')
                console_text.insert('end', f"{self.functionPath} : " + text + '\n')
                console_text.configure(state='disabled')
                console_text.yview('end')

        # redirect stdout to the console
        import sys
        sys.stdout.write = print_to_console

    def runAllFunctions(self):
        for widget in self.checkbox_frame.winfo_children():
            if isinstance(widget, CustomCheckButton):
                widget.function()
                widget.checkButton.select()
        print("All functions are successfully runned")




class CustomCheckButton(ctk.CTkFrame):
    def __init__(self, parent, functionName, function):
        super().__init__(parent, bg_color=WHITE)
        self.function = function
        self.functionName = functionName
        self.checkButton = ctk.CTkCheckBox(self, text=functionName, fg_color=WHITE,
                                           text_color=HEAD_FONT_COLOR, font=ctk.CTkFont(family='Roboto', size=12),
                                           border_width=2, corner_radius=6, bg_color=WHITE, checkmark_color=MAIN_COLOR,
                                           hover_color=BG_COLOR, command=self.function)
        self.checkButton.pack()
