import customtkinter as ctk
from settings import *
from information_card import InformationCard
from functionFrame import FunctionsFrame


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG_COLOR)
        self._set_appearance_mode('light')
        self.geometry("900x500")
        self.title("LoRa Connect")

        self.informationFrame = InformationCard(parent=self)
        self.informationFrame.pack(anchor="nw", padx=20, pady=10)

        self.functionFrame = FunctionsFrame(parent=self)
        self.functionFrame.pack(fill=ctk.X, anchor="w", padx=20, pady=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
