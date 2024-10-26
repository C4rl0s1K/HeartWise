import customtkinter
from PIL import Image
from database import Database
import sqlite3
from tkinter import messagebox



class Login(customtkinter.CTkFrame):
    
    def __init__(self, master, switch_to_register_page, switch_to_main_page):
        super().__init__(master, fg_color="#ffe5ec", corner_radius=0)
        self.switch_to_register_page = switch_to_register_page
        self.switch_to_main_page = switch_to_main_page
        self.db = Database()

        master.bind("<Return>", self.login_into_account)

        self.create_widgets()        

    def create_widgets(self):

        self.label_welcome_text = customtkinter.CTkLabel(self, text="WELCOME\nBACK!", text_color="#FB6F92", font=("Inter", 48, "bold"))
        self.label_welcome_text.place(x=100, y=90)


        self.logo_imgage = customtkinter.CTkImage(light_image=Image.open('images/logo.png'), dark_image=Image.open('images/logo.png'), size=(500, 500))
        self.label_image = customtkinter.CTkLabel(self, text="", image=self.logo_imgage)
        self.label_image.place(x=400, y=110)

        self.label_login = customtkinter.CTkLabel(self, text="Login", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_login.place(x=200, y=250)
        self.entry_login = customtkinter.CTkEntry(self, width=230, height=55, corner_radius=15, fg_color="#FB6F92", border_color="#FB6F92", text_color = "#FFFFFF", font=("Inter", 14, "bold"))
        self.entry_login.place(x=105, y=280)
 
        self.label_password = customtkinter.CTkLabel(self, text="Password", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_password.place(x=185, y=350)
        self.entry_password = customtkinter.CTkEntry(self, width=230, height=55, corner_radius=15, fg_color="#FB6F92", border_color="#FB6F92", text_color = "#FFFFFF", font=("Inter", 14, "bold"), show = "*")
        self.entry_password.place(x=105, y=380)
        
        self.login_imgage = customtkinter.CTkImage(light_image=Image.open('images/door.png'), dark_image=Image.open('images/door.png'), size=(45, 45))
        self.button_login = customtkinter.CTkButton(self, text="Log in", image=self.login_imgage, fg_color="transparent", width=100, height=55, text_color="#FB6F92", font=("Inter", 14, "bold"), hover = False, command=self.login_into_account)
        self.button_login.place(x=335, y=380)

        self.label_create_account = customtkinter.CTkLabel(self, text="Don't have account? Click here", text_color="#FB6F92", font=("Inter", 14, "bold", "underline"))
        self.label_create_account.place(x=110, y=450)
        self.label_create_account.bind("<Enter>", lambda event: self.label_create_account.configure(cursor="hand2"))
        self.label_create_account.bind("<Leave>", lambda event: self.label_create_account.configure(cursor=""))
        self.label_create_account.bind("<Button-1>", self.switch_to_register_page)

    def login_into_account(self, event = None):
        login = self.entry_login.get()
        password = self.entry_password.get()

        if not login or not password:
            messagebox.showerror("Error", "Please enter both login and password.")
            return
        
        print(f"Login: {login}")

        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()

        user_data = self.db.get_user_by_login(login)

        if user_data is None:
            messagebox.showerror("Error", "Login or password is incorrect.")
        else:
            stored_password = user_data[0]
            print(f"Stored password: {stored_password}")

        if password == stored_password:
            messagebox.showinfo("Success", "Login successful!")

            user_info = self.db.get_user_info(login)
            if user_info:
                user_login, user_name, birth_year, user_id = user_info[0], user_info[1], user_info[2], user_info[3]
                self.switch_to_main_page(current_user = user_login, current_user_name=user_name, current_user_birth_year=birth_year, current_user_id = user_id)
                print(f"user_id: {user_id}, user_login: {user_login}, user_name: {user_name}, birth_year: {birth_year}")

            else:
                messagebox.showerror("Error", "User information could not be retrieved.")
        else:
            messagebox.showerror("Error", "Login or password is incorrect.")
        
        self.connection.close()