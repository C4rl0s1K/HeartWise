import customtkinter
from PIL import Image
import datetime
from database import Database
from tkinter import messagebox


class SignUp(customtkinter.CTkFrame):

    def __init__(self, master, switch_to_login_page, switch_to_main_page):
        super().__init__(master, fg_color="#ffe5ec", corner_radius=0)
        self.switch_to_login_page = switch_to_login_page
        self.switch_to_main_page = switch_to_main_page
        self.db = Database()

        master.bind("<Return>", self.save_user)

        self.create_widgets()

    def create_widgets(self):

        #Subtitles
        self.label_welcome_text = customtkinter.CTkLabel(self, text="WELCOME\nHERE!", text_color="#FB6F92", font=("Inter", 48, "bold"))
        self.label_welcome_text.place(x=100, y=40)

        self.slogan_label = customtkinter.CTkLabel(self, text="Healthy heart, peaceful future!", font=("Inter", 20, "italic", "bold"),text_color="#FB6F92")
        self.slogan_label.place(x=550, y=470)

        #Images
        self.logo_imgage = customtkinter.CTkImage(light_image=Image.open('images/logo.png'), dark_image=Image.open('images/logo.png'), size=(500, 500))
        self.label_image = customtkinter.CTkLabel(self, text="", image=self.logo_imgage)
        self.label_image.place(x=400, y=60)

        self.save_imgage = customtkinter.CTkImage(light_image=Image.open('images/door.png'), dark_image=Image.open('images/door.png'), size=(45, 45))
        self.button_save = customtkinter.CTkButton(self, text="Save", image=self.save_imgage, fg_color="transparent", width=100, height=55, text_color="#FB6F92", font=("Inter", 14, "bold"), hover = False, command=self.save_user)
        self.button_save.place(x=360, y=300)

        #Buttons
        #Button - login
        self.label_login = customtkinter.CTkLabel(self, text="Login", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_login.place(x=200, y= 150)
        self.entry_login = customtkinter.CTkEntry(self, width=230, height=55, corner_radius=15, fg_color="#FB6F92", border_color="#FB6F92", text_color = "#FFFFFF", font=("Inter", 14, "bold"))
        self.entry_login.place(x=105, y=180)
        #Button - password
        self.label_password = customtkinter.CTkLabel(self, text="Password", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_password.place(x=185, y=250)
        self.entry_password = customtkinter.CTkEntry(self, width=230, height=55, corner_radius=15, fg_color="#FB6F92", border_color="#FB6F92", text_color = "#FFFFFF", font=("Inter", 14, "bold"), show = "*")
        self.entry_password.place(x=105, y=280)
        #Button - name
        self.label_name = customtkinter.CTkLabel(self, text="Name", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_name.place(x=200, y= 350)
        self.entry_name = customtkinter.CTkEntry(self, width=230, height=55, corner_radius=15, fg_color="#FB6F92", border_color="#FB6F92", text_color = "#FFFFFF", font=("Inter", 14, "bold"))
        self.entry_name.place(x=105, y=380)       
        #Button - age
        self.label_age = customtkinter.CTkLabel(self, text="Age", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_age.place(x=200, y=450)
        current_year = datetime.datetime.now().year
        years = [str(year) for year in range(current_year, 1900, -1)]
        self.dropdownlist_age = customtkinter.CTkOptionMenu(self, values=years, fg_color="#FB6F92", button_color="#FB6F92", button_hover_color="#ff8fab", text_color="#FFFFFF", font=("Inter", 14, "bold"), dropdown_font=("Inter", 14, "bold"), width=230, height=55, corner_radius=15, dropdown_fg_color="#FB6F92", dropdown_hover_color = "#ff8fab")
        self.dropdownlist_age.set("Select Birth Year")
        self.dropdownlist_age.place(x=105, y=480)
        #Button - sex
        self.label_sex = customtkinter.CTkLabel(self, text="Sex", text_color="#FB6F92", font=("Inter", 14, "bold"))
        self.label_sex.place(x=200, y=550)
        self.sex_var = customtkinter.IntVar(value=-1)
        self.radio_male = customtkinter.CTkRadioButton(self, text="Male", variable=self.sex_var, text_color="#000000", font=("Inter", 14), border_color="#FFFFFF", hover=False, value=1, fg_color="#FB6F92")
        self.radio_female = customtkinter.CTkRadioButton(self, text="Female", variable=self.sex_var, text_color="#000000", font=("Inter", 14), border_color="#FFFFFF", hover=False, value=0, fg_color="#FB6F92")
        self.radio_male.place(x=105, y=580)
        self.radio_female.place(x=205, y=580)
        #Buttonn - account
        self.label_account = customtkinter.CTkLabel(self, text="Do you have account? Click here", text_color="#FB6F92", font=("Inter", 14, "bold", "underline"))
        self.label_account.place(x=105, y=620)
        self.label_account.bind("<Enter>", lambda event: self.label_account.configure(cursor="hand2"))
        self.label_account.bind("<Leave>", lambda event: self.label_account.configure(cursor=""))
        self.label_account.bind("<Button-1>", self.switch_to_login_page)

    def save_user(self, event = None):
        login = self.entry_login.get()
        password = self.entry_password.get()
        name = self.entry_name.get()
        birth_year = self.dropdownlist_age.get()
        sex = self.sex_var.get()

        if login =="" or password == "" or birth_year =="Select Birth Year" or sex ==-1:
            messagebox.showerror("Error", "All Fields are Required")
        else:
            self.db.add_users_to_database(login, password, name, birth_year, sex)
            messagebox.showinfo("Succesfully", f"Congratulations, {login}! Your account has been successfully created.")

            user_info = self.db.get_user_info(login)
            if user_info:
                user_login, user_name, birth_year, user_id, user_sex = user_info[0], user_info[1], user_info[2], user_info[3], user_info[4]
                self.switch_to_main_page(
                    current_user=user_login, 
                    current_user_birth_year=birth_year, 
                    current_user_name=user_name, 
                    current_user_id=user_id,
                    current_user_sex=user_sex
                )
                print(f"user_id: {user_id}, user_login: {user_login}, user_name: {user_name}, birth_year: {birth_year}, sex: {user_sex}")
            else:
                messagebox.showerror("Error", "User information could not be retrieved.")


