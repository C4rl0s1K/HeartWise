import customtkinter
from login import Login
from signup import SignUp
from main_page import MainPage

class App():

    def __init__(self, root):
        self.root = root
        self.root.title("HeartWise")
        self.root.geometry("1000x700")

        self.current_frame = None
        self.show_login_page()

    def show_login_page(self, event=None):
        self.clear_frame()
        self.current_frame = Login(self.root, self.show_register_page, self.show_main_page)
        self.current_frame.pack(fill="both", expand=True)

    def show_register_page(self, event=None):
        self.clear_frame()
        self.current_frame = SignUp(self.root, self.show_login_page, self.show_main_page)
        self.current_frame.pack(fill="both", expand=True)

    def show_main_page(self, current_user, current_user_birth_year, current_user_name, current_user_id, current_user_sex, event=None):
         self.clear_frame()
         self.current_frame = MainPage(self.root, self.show_login_page, current_user=current_user, current_user_birth_year=current_user_birth_year, current_user_name=current_user_name, current_user_id = current_user_id, current_user_sex=current_user_sex)
         self.current_frame.pack(fill="both", expand=True)

    def clear_frame(self):
        if self.current_frame:
             self.current_frame.destroy()

if __name__ == "__main__":

        root = customtkinter.CTk()
        app = App(root)
        root.mainloop()
