import customtkinter


class AdminGui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Admin GUI")
        self.geometry("500x500")
        self.mainloop()

