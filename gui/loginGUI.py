import os
from backend import login

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

path_dir = os.path.dirname(os.path.realpath(__file__))
ASSETS_PATH = os.path.join(path_dir, "assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class LoginWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Login")
        self.geometry("900x600")
        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=900,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            225.0,
            300.0,
            image=image_image_1
        )

        self.canvas.create_text(
            498.0,
            105.0,
            anchor="nw",
            text="Welcome back!",
            fill="#006992",
            font=("Helvetica", 35 * -1, "bold")
        )

        self.canvas.create_text(
            498.0,
            156.0,
            anchor="nw",
            text="Login to your account",
            fill="#878787",
            font=("Helvetica", 15 * -1)
        )

        self.canvas.create_text(
            525.0,
            239.0,
            anchor="nw",
            text="Username:",
            fill="#006992",
            font=("Helvetica", 18 * -1)
        )

        self.canvas.create_text(
            525.0,
            317.0,
            anchor="nw",
            text="Password:",
            fill="#006992",
            font=("Helvetica", 18 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            510.0,
            247.0,
            image=image_image_2
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            668.0,
            289.5,
            image=entry_image_1
        )
        self.username_entry = Entry(
            bd=0,
            bg="#D8F0FE",
            fg="#000716",
            highlightthickness=0,
        )
        self.username_entry.place(
            x=503.0,
            y=274.0,
            width=330.0,
            height=33.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            668.0,
            358.5,
            image=entry_image_2
        )
        self.password_entry = Entry(
            bd=0,
            bg="#D8F0FE",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.password_entry.place(
            x=503.0,
            y=343.0,
            width=330.0,
            height=33.0
        )
        self.error_text = Text(
            self.canvas,
            bd=0,
            bg="#FFFFFF",
            fg="#FF0000",
            highlightthickness=0,
            wrap="word",
            font=("Helvetica", 10)
        )
        self.error_text.place(
            x=503.0,
            y=380.0,
            width=330.0,
            height=33.0
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            510.0,
            327.0,
            image=image_image_3
        )

        button_image_login = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_login = Button(
            image=button_image_login,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_login,
            relief="flat"
        )
        self.button_login.place(
            x=493.0,
            y=444.0,
            width=350.0,
            height=30.0
        )

        button_image_signup = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_signup = Button(
            image=button_image_signup,
            borderwidth=0,
            highlightthickness=0,
            command=self.on_signin,
            relief="flat",
        )
        self.button_signup.place(
            x=493.0,
            y=485.0,
            width=350.0,
            height=30.0
        )
        self.resizable(False, False)
        self.is_logged_in = False
        self.login_mode = None
        self.mainloop()

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username.strip() == "" and password.strip() == "":
            self.error_text.delete("1.0", "end")
            self.error_text.insert("1.0", "Do not leave the box blank")
        else:
            self.is_logged_in, self.login_mode = login.verify_login(username, password)
            if self.is_logged_in:
                self.destroy()
                return
            else:
                self.error_text.delete("1.0", "end")
                self.error_text.insert("1.0", "Username or Password is not correct")

    def on_signin(self):
        username = self.username_entry.get().strip()
        messagebox.showinfo("Sign Up", f"Hey {username if (username != '') else 'There'}!\n"
                                       f"Please contact the Training Department to create a new account.")
