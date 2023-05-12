import customtkinter as ctk
from settings import *
class InfoFrame(ctk.CTkFrame):
    def __init__(self, parent, label, value):
        super().__init__(parent, fg_color=WHITE, width=200, height=100, corner_radius=12)

        self.label = ctk.CTkLabel(self, text=label, fg_color=WHITE, font=ctk.CTkFont(family='Roboto', size=12),
                                  text_color=BODY_FONT_COLOR)
        self.label.grid(row=0, column=0, padx=10, sticky="w")
        self.value = ctk.CTkLabel(self, text=value, fg_color=WHITE,
                                  text_color=HEAD_FONT_COLOR, font=ctk.CTkFont(family='Arial', size=18))
        self.value.grid(row=1, column=0, padx=10, sticky="w")


if __name__ == '__main__':
    app = InfoFrame()
    app.mainloop()