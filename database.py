import sqlite3

class Database():

    def __init__(self, db_name = "users.db"):
        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()

        self.create_table_user_data()
        self.create_table_heart_data()
    
    def create_table_user_data(self):
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    password TEXT NOT NULL,
                    name TEXT,
                    birth_year INTEGER NOT NULL,
                    sex INTEGER NOT NULL)
                    ''')
        self.connection.commit()

    def create_table_heart_data(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS heart_data
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            chest_pain_type INTEGER NOT NULL,
                            resting_blood_pressure INTEGER NOT NULL,
                            serum_cholestoral INTEGER NOT NULL,
                            fasting_blood_sugar INTEGER NOT NULL,
                            resting_electrocardiographic INTEGER NOT NULL,
                            max_heart_rate INTEGER NOT NULL,
                            exercise_induced_angina INTEGER NOT NULL,
                            oldpeak FLOAT NOT NULL,
                            vessels INTEGER NOT NULL,
                            thal INTEGER NOT NULL
                            )
                            ''')
        self.connection.commit()

    def add_users_to_database(self, login, password, name, birth_year, sex):
        self.cursor.execute(
            '''INSERT INTO USERS (login, password, name, birth_year, sex) VALUES (?,?,?,?,?)''', (login, password, name, birth_year, sex))
        self.connection.commit()

    def add_heart_parameters(self, user_id, chest_pain_type, resting_blood_pressure, serum_cholestoral, fasting_blood_sugar,resting_electrocardiographic, max_heart_rate, exercise_induced_angina, oldpeak, vessels, thal):
        self.cursor.execute('''
                            INSERT INTO heart_data (user_id, chest_pain_type, resting_blood_pressure, serum_cholestoral, fasting_blood_sugar,resting_electrocardiographic, max_heart_rate, exercise_induced_angina, oldpeak, vessels, thal
                            ) VALUES (?,?,?,?,?,?,?,?,?,?,?)
                            ''', (user_id, chest_pain_type, resting_blood_pressure, serum_cholestoral, fasting_blood_sugar,resting_electrocardiographic, max_heart_rate, exercise_induced_angina, oldpeak, vessels, thal)
                            )
        self.connection.commit()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def get_user_by_login(self, login):
        self.cursor.execute("SELECT password from users WHERE login = ?", (login, ))
        return self.cursor.fetchone()
    
    def get_user_info(self, login):
        self.cursor.execute("SELECT login, name, birth_year, id, sex from users WHERE login = ?", (login, ))
        return self.cursor.fetchone()
    
    def get_user_heart_parameters_plot(self, user_id):
        self.cursor.execute("SELECT id, user_id, resting_blood_pressure, serum_cholestoral, max_heart_rate FROM heart_data WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
