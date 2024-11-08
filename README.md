# **HeartWise**: Heart Health Prediction Application

HeartWise is a desktop application designed to predict heart health based on various heart parameters. The application uses machine learning models to predict whether the heart is healthy or at risk, and allows users to track their heart parameters over time.

**Note:** This project is still under development. New features and improvements are being added regularly. 

### **Features:**
- **User Registration and Login:** Users can create accounts, log in, and securely store their data.
- **Heart Health Prediction:** Input key heart parameters to predict heart health using a trained logistic regression model.
- **Data Tracking:** Visualize changes in heart parameters (e.g. blood pressure, cholesterol, heart rate) over time through historical data and interactive charts.
- **SQLite3 Database:** All user data and heart health parameters are stored in an SQLite database.
- **Machine Learning Model:** A logistic regression model is used to predict heart health based on historical data.

### **Technologies Used:**
- **Python:**  Main programming language used to develop the application.
- **CustomTkinter:** A modern, customizable library for creating desktop GUIs in Python
- **SQLite3:** A lightweight database to store user data and heart health parameters.
- **Scikit-Learn:** A library used for machine learning, including logistic regression for heart health prediction.
- **Matplotlib:** For visualizing historical heart data.

### **Installation:**
<p> To run the HeartWise application on your local machine, follow these steps:</P>
1. Clone the repository:
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/HeartWise.git
cd HeartWise
```

2. Create a virtual environment
<p>To avoid conflicts with other projects, it's recommended to create a virtual environment for this project:</p>

```bash
python -m venv venv
```

3. Activate the virtual environment

```bash
.\venv\Scripts\activate

```
4. Install dependencies
<p>Once the virtual environment is activated, install the necessary dependencies using pip:</p>

```bash
pip install -r requirements.txt

```

5.  Running the application
<p>After installing all the dependencies, you can run the application with the following command:</p>

```bash
python HeartWise.py

```

### **Usage:**
- **Login/Registration:**  After launching the application, create a new account or log in if you already have one.
- **Input Parameters:** Enter heart parameters such as blood pressure, cholesterol, and heart rate to see your health prediction.
- **View Predictions:** After entering the data, the model will predict whether you have a healthy heart or if you may be at risk.
- **Track Data:** View graphs of your heart parameters over time to monitor any changes and trends.

### **Future Improvements:**
- **Add more prediction models:** Currently using logistic regression, but adding other models like Random Forests or Neural Networks could improve accuracy.
- **Improve Data Privacy:** Add encryption for user passwords and secure sensitive data.
- **Expand Visualization:** Include additional charts and trends for other health parameters.

### **Screenshots:**
Here are some screenshots of the HeartWise application:

![Login Screen](./images/login_page.png)
<p>*Login screen*</p>

![Registration Page](./images/registration_page.png)
<p>*Registration screen*</p>

<p>Will be more...</p>