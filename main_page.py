import customtkinter
from database import Database
from datetime import datetime
from prediction_model import *
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from PIL import Image
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class MainPage(customtkinter.CTkFrame):

    def __init__(self, master, switch_to_login_page, current_user, current_user_birth_year, current_user_name, current_user_id, current_user_sex):
        super().__init__(master, fg_color="#ffe5ec", corner_radius=0)
        self.switch_to_login_page = switch_to_login_page
        self.current_user = current_user
        print(f"current user: {self.current_user}")
        self.current_user_name = current_user_name
        self.current_user_birth_year = current_user_birth_year
        self.current_user_id = current_user_id
        self.current_user_sex = current_user_sex
        self.db = Database()
        self.prediction_model, self.scaler = get_model_and_scaler()

        self.create_top_widgets()
        self.create_input_widgets()
        self.create_analysis_widgets()

    def create_top_widgets(self):
        
        self.top_frame = customtkinter.CTkFrame(self, fg_color="#FB6F92", width=1000, height=200, corner_radius=0)
        self.top_frame.place(x=0,y=0)

        self.label_info = customtkinter.CTkLabel(self.top_frame, text="", fg_color="#FFE5EC", font=("Arial", 20), width=250, height=150, corner_radius=0)
        self.label_info.place(x=700, y=25)

        #Image
        self.logo_imgage = customtkinter.CTkImage(light_image=Image.open('images/logo.png'), dark_image=Image.open('images/logo.png'), size=(250, 250))
        self.label_image = customtkinter.CTkLabel(self.top_frame, text="", image=self.logo_imgage)
        self.label_image.place(x=50, y=-15)
        #Subtitles
        self.title_label = customtkinter.CTkLabel(self.top_frame, text="HeartWise", font=("Inter", 48, "bold"), text_color="#FFE5EC")
        self.title_label.place(x=330,y=25)

        self.slogan_label = customtkinter.CTkLabel(self.top_frame, text="Stay Heart-Smart, Live Longer", font=("Inter", 24, "italic"), text_color="#FFE5EC")
        self.slogan_label.place(x=300,y=85)

        #Label about date
        today = datetime.today().strftime("%d-%m-%Y")
        today_date_label = customtkinter.CTkLabel(self.top_frame, text = f"{today}", width=210, height=32, font=("Inter", 14, "bold"))
        today_date_label.place(x=720, y=37)
        #Label about username
        self.login_label = customtkinter.CTkLabel(self.top_frame, text = f"Login: {self.current_user}", width=210, height=32, font=("Inter", 14, "bold"))
        self.login_label.place(x=720,y=84)
        #Label about user age
        today_year = datetime.today().strftime("%Y")
        age_of_user = int(today_year) - self.current_user_birth_year

        self.age_label = customtkinter.CTkLabel(self.top_frame, text = f"Age: {age_of_user}", width=210, height=32, font=("Inter", 14, "bold"))
        self.age_label.place(x=720,y=131)

    def create_input_widgets(self):

        self.middle_left_frame = customtkinter.CTkFrame(self, fg_color="#FB6F92", width=380, height=450, corner_radius=0)
        self.middle_left_frame.place(x=20, y=220)

        #1 column
        self.welcome_text = customtkinter.CTkLabel(self.middle_left_frame, text=f"Hi, {self.current_user_name.capitalize()}!",  width=170, height=15, font=("Inter", 20, "bold"), text_color="#FFE5EC")
        self.welcome_text.place(x=0, y=25)
        self.instruction_text = customtkinter.CTkLabel(self.middle_left_frame, text="Your details go here",  width=170, height=15, font=("Inter", 14, "bold"),text_color="#FFE5EC")
        self.instruction_text.place(x=0, y=50)

        self.cp_text = customtkinter.CTkLabel(self.middle_left_frame, text="chest\npain",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.cp_text.place(x=3,y=95)
        self.cp_option_menu = customtkinter.CTkOptionMenu(self.middle_left_frame, values=["asymptomatic", "atypical angina", "non-anginal pain", "typical angina"], fg_color="#FFE5EC", button_color="#FFE5EC", text_color="#FB6F92", button_hover_color="#ff8fab", font=("Inter", 12, "bold"), dropdown_font=("Inter", 12, "bold"),dropdown_fg_color="#FFE5EC", dropdown_text_color="#FB6F92", dropdown_hover_color="#ff8fab")
        self.cp_option_menu.place(x=60, y=90)

        self.restecg_text = customtkinter.CTkLabel(self.middle_left_frame, text="restecg",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.restecg_text.place(x=3,y=140)
        self.restecg_option_menu = customtkinter.CTkOptionMenu(self.middle_left_frame, values=["normal", "LV Hypertrophy by Estes", "ST-T Abnormality"], fg_color="#FFE5EC", button_color="#FFE5EC", text_color="#FB6F92", button_hover_color="#ff8fab", font=("Inter", 12, "bold"), dropdown_font=("Inter", 12, "bold"),dropdown_fg_color="#FFE5EC", dropdown_text_color="#FB6F92", dropdown_hover_color="#ff8fab")
        self.restecg_option_menu.place(x=60, y=135)

        self.slope_text = customtkinter.CTkLabel(self.middle_left_frame, text="slope",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.slope_text.place(x=3,y=185)
        self.slope_option_menu = customtkinter.CTkOptionMenu(self.middle_left_frame, values=["downsloping", "flat", "upsloping"], fg_color="#FFE5EC", button_color="#FFE5EC", text_color="#FB6F92", button_hover_color="#ff8fab", font=("Inter", 12, "bold"), dropdown_font=("Inter", 12, "bold"),dropdown_fg_color="#FFE5EC", dropdown_text_color="#FB6F92", dropdown_hover_color="#ff8fab")
        self.slope_option_menu.place(x=60, y=180)

        self.vessels_text = customtkinter.CTkLabel(self.middle_left_frame, text="vessels\nnumber",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.vessels_text.place(x=3,y=225)
        self.vesels_option_menu = customtkinter.CTkOptionMenu(self.middle_left_frame, values=["1","2","3"], fg_color="#FFE5EC", button_color="#FFE5EC", text_color="#FB6F92", button_hover_color="#ff8fab", font=("Inter", 12, "bold"), dropdown_font=("Inter", 12, "bold"),dropdown_fg_color="#FFE5EC", dropdown_text_color="#FB6F92", dropdown_hover_color="#ff8fab")
        self.vesels_option_menu.place(x=60, y=225)

        self.thal_text = customtkinter.CTkLabel(self.middle_left_frame, text="thal",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.thal_text.place(x=3,y=275)
        self.thal_option_menu = customtkinter.CTkOptionMenu(self.middle_left_frame, values=["NULL","fixed defect","normal blood flow", "reversible defect"], fg_color="#FFE5EC", button_color="#FFE5EC", text_color="#FB6F92", button_hover_color="#ff8fab", font=("Inter", 12, "bold"), dropdown_font=("Inter", 12, "bold"),dropdown_fg_color="#FFE5EC", dropdown_text_color="#FB6F92", dropdown_hover_color="#ff8fab")
        self.thal_option_menu.place(x=60, y=270)

        #The person’s fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
        self.fbs_text = customtkinter.CTkLabel(self.middle_left_frame, text="fbs",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.fbs_text.place(x=3,y=320)
        self.fbs_var = customtkinter.IntVar(value=-1)
        self.fbs_true_radio = customtkinter.CTkRadioButton(self.middle_left_frame, text="True", variable=self.fbs_var, text_color="#FFE5EC", font=("Inter", 12, "bold"), border_color="#ff8fab", hover=False, value=1, fg_color="#FFE5EC")
        self.fbs_true_radio.place(x=60, y=315)
        self.fbs_false_radio = customtkinter.CTkRadioButton(self.middle_left_frame, text="False", variable=self.fbs_var, text_color="#FFE5EC", font=("Inter", 12, "bold"), border_color="#ff8fab", hover=False, value=0, fg_color="#FFE5EC")
        self.fbs_false_radio.place(x=130, y=315)

        self.exang_text = customtkinter.CTkLabel(self.middle_left_frame, text="exang",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.exang_text.place(x=3,y=355)
        self.exang_var = customtkinter.IntVar(value=-1)
        self.exang_true_radio = customtkinter.CTkRadioButton(self.middle_left_frame, text="True", variable=self.exang_var, text_color="#FFE5EC", font=("Inter", 12, "bold"), border_color="#ff8fab", hover=False, value=1, fg_color="#FFE5EC")
        self.exang_true_radio.place(x=60, y=350)
        self.exang_false_radio = customtkinter.CTkRadioButton(self.middle_left_frame, text="False", variable=self.exang_var, text_color="#FFE5EC", font=("Inter", 12, "bold"), border_color="#ff8fab", hover=False, value=0, fg_color="#FFE5EC")
        self.exang_false_radio.place(x=130, y=350)

        #2 column
        self.trestbps_text = customtkinter.CTkLabel(self.middle_left_frame, text="trestbps",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.trestbps_text.place(x=220,y=95)
        self.trestbps_entry = customtkinter.CTkEntry(self.middle_left_frame, width=80,height=25, font=("Inter", 12, "bold"),text_color="#FB6F92", fg_color="#FFE5EC", border_color="#FFE5EC")
        self.trestbps_entry.place(x=280, y=90)

        self.chol_text = customtkinter.CTkLabel(self.middle_left_frame, text="chol",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.chol_text.place(x=220,y=140)
        self.chol_entry = customtkinter.CTkEntry(self.middle_left_frame, width=80,height=25, font=("Inter", 12, "bold"),text_color="#FB6F92", fg_color="#FFE5EC", border_color="#FFE5EC")
        self.chol_entry.place(x=280, y=135)

        self.thalach_text = customtkinter.CTkLabel(self.middle_left_frame, text="thalach",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.thalach_text.place(x=220,y=185)
        self.thalach_entry = customtkinter.CTkEntry(self.middle_left_frame, width=80,height=25, font=("Inter", 12, "bold"),text_color="#FB6F92", fg_color="#FFE5EC", border_color="#FFE5EC")
        self.thalach_entry.place(x=280, y=180)

        self.oldpeak_text = customtkinter.CTkLabel(self.middle_left_frame, text="oldpeak",  width=30, height=15, font=("Inter", 12, "bold"),text_color="#FFE5EC")
        self.oldpeak_text.place(x=220,y=230)
        self.oldpeak_entry = customtkinter.CTkEntry(self.middle_left_frame, width=80,height=25, font=("Inter", 12, "bold"),text_color="#FB6F92", fg_color="#FFE5EC", border_color="#FFE5EC")
        self.oldpeak_entry.place(x=280, y=225)

        self.save_button = customtkinter.CTkButton(self.middle_left_frame, text="Save", width=100, height=25, fg_color="#FFE5EC", border_color="#FFE5EC", text_color="#FB6F92", hover_color="#FF8FAB", font=("Inter", 12, "bold"), command=self.save_heart_parameters)
        self.save_button.place(x=135, y=400)

    def chest_pain_map(self):
        return{"asymptomatic":0, "atypical angina":1, "non-anginal pain":2, "typical angina":3}
    
    def restecg_map(self):
        return{"normal":1, "LV Hypertrophy by Estes":0, "ST-T Abnormality":2}
    
    def slope_map(self):
        return{"downsloping":0, "flat":1, "upsloping":2}
    
    def ca_map(self):
        return{"1":1,"2":2,"3":3}
    
    def thal_map(self):
        return{"NULL":0,"fixed defect":1,"normal blood flow":2, "reversible defect":3}
    
    def save_heart_parameters(self):
        chest_pain_type = self.chest_pain_map()[self.cp_option_menu.get()]
        resting_blood_pressure = self.trestbps_entry.get()
        serum_cholestoral = self.chol_entry.get()
        fasting_blood_sugar = self.fbs_var.get()
        resting_electrocardiographic = self.restecg_map()[self.restecg_option_menu.get()]
        max_heart_rate = self.thalach_entry.get()
        exercise_induced_angina = self.exang_var.get()
        oldpeak = self.oldpeak_entry.get()
        vessels = self.ca_map()[self.vesels_option_menu.get()]
        thal = self.thal_map()[self.thal_option_menu.get()]

        if (resting_blood_pressure == "" or serum_cholestoral == "" or max_heart_rate == "" or oldpeak == ""):
            messagebox.showerror("Error", "All fields are required.")
            return
        
        if (chest_pain_type is None or fasting_blood_sugar == -1 or resting_electrocardiographic is None or exercise_induced_angina == -1 or vessels is None or thal is None):
            messagebox.showerror("Error", "All fields are required.")
            return
        
        try:
            resting_blood_pressure = int(resting_blood_pressure)
            serum_cholestoral = int(serum_cholestoral)
            max_heart_rate = int(max_heart_rate)
            oldpeak = float(oldpeak)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")
            return
        
        self.db.add_heart_parameters(user_id = self.current_user_id, chest_pain_type = chest_pain_type, resting_blood_pressure = int(resting_blood_pressure), serum_cholestoral = int(serum_cholestoral), fasting_blood_sugar = fasting_blood_sugar,resting_electrocardiographic = resting_electrocardiographic, max_heart_rate = int(max_heart_rate), exercise_induced_angina = exercise_induced_angina , oldpeak = float(oldpeak), vessels = vessels, thal = thal)
        messagebox.showinfo("Success", "Your heart parameters have been added to the database.")

        self.show_prediction()


    def create_analysis_widgets(self):
            
        self.plot_frame = customtkinter.CTkFrame(self, fg_color="#FB6F92", width=500, height=450, corner_radius=0)
        self.plot_frame.place(x=450, y=220)

        self.switch_button = customtkinter.CTkSegmentedButton(self.plot_frame, values=["Prediction", "Heart Charts"])
        self.switch_button.place(x=5,y=5)
        self.switch_button.set("Prediction")
        self.switch_button.configure(command=self.on_switch_changed)

    def on_switch_changed(self, value):
        if value == "Prediction":
            self.show_prediction()
        else:
            print("under constracting")

    def show_prediction(self):
        try:
            input_data = (
            int(datetime.today().strftime("%Y")) - self.current_user_birth_year,
            int(self.current_user_sex),
            self.chest_pain_map()[self.cp_option_menu.get()],
            int(self.trestbps_entry.get()), 
            int(self.chol_entry.get()),  
            self.fbs_var.get(), 
            self.restecg_map()[self.restecg_option_menu.get()], 
            int(self.thalach_entry.get()),
            self.exang_var.get(),
            float(self.oldpeak_entry.get()), 
            self.slope_map()[self.slope_option_menu.get()], 
            self.ca_map()[self.vesels_option_menu.get()],
            self.thal_map()[self.thal_option_menu.get()]
        )

            input_data_as_numpy_array = np.asarray(input_data)
            input_data_scaled = self.scaler.transform(input_data_as_numpy_array.reshape(1, -1))
            prediction = self.prediction_model.predict(input_data_scaled)

            if prediction[0] == 0:
                # result_text = "Osoba o podanych parametrach nie ma choroby serca."
                print("Osoba o podanych parametrach nie ma choroby serca.")
            else:
                # result_text = "Osoba o podanych parametrach ma chore serce."
                print("Osoba o podanych parametrach ma chore serce.")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")


























    # def plot(self):
    #     user_id = self.current_user_id
    #     user_data = self.db.get_user_heart_parameters_plot(user_id)
    #     print(user_data)

    #     for widget in self.plot_frame.winfo_children():
    #         if isinstance(widget, FigureCanvasTkAgg):
    #             widget.get_tk_widget().destroy()

    #     if user_data:
    #         ids = [row[0] for row in user_data]
    #         blood_pressure =  [row[2] for row in user_data]
    #         cholesterol = [row[3] for row in user_data]
    #         heart_rate = [row[4] for row in user_data]

    #         fig, ax = plt.subplots(figsize=(5, 3), dpi = 100)
    #         ax.plot(ids, blood_pressure, label="Blood Pressure", marker="o")
    #         ax.plot(ids, cholesterol, label="Cholesterol", marker="x")
    #         ax.plot(ids, heart_rate, label="Heart Rate", marker="s")  

    #         ax.set_xlabel("IDs (consecutive measurements)")
    #         ax.set_ylabel("Values")
    #         # ax.set_title("Your Heart Parameters Over Time")
    #         # ax.legend()     

    #         canvas = FigureCanvasTkAgg(fig, self.plot_frame)
    #         canvas.draw()
    #         canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
    #         self.plot_frame.update_idletasks()
    
