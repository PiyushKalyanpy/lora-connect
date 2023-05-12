import customtkinter as ctk
from settings import *
from info_frame import InfoFrame

class InformationCard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent", corner_radius=12)

        self.rowconfigure((0, 1, 2), weight=1)
        self.columnconfigure((0, 1, 2), weight=1)

        self.deviceAddress = InfoFrame(parent=self, label="Device Address", value="F9JVEK73")
        self.deviceAddress.grid(row=0, column=0, padx=10, pady=10)

        self.noOfDevice = InfoFrame(parent=self, label="No. of Devices", value="2")
        self.noOfDevice.grid(row=0, column=1, padx=10, pady=10)

        self.macAddress = InfoFrame(parent=self, label="MAC Address", value="192.168.84.2")
        self.macAddress.grid(row=0, column=2, padx=10, pady=10)

        self.commandType = InfoFrame(parent=self, label="Command Type", value="-")
        self.commandType.grid(row=0, column=3, padx=10, pady=10)

        self.valueBox = InfoFrame(parent=self, label="Value", value="-")
        self.valueBox.grid(row=0, column=4,  padx=10, pady=10)