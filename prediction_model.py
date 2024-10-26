import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore", message="X does not have valid feature names")

def get_model_and_scaler():
    file = "heart.csv"
    data_heart = pd.read_csv(file)

    data_heart.drop_duplicates(inplace=True)
    data_heart.reset_index(drop=True, inplace=True)

    X = data_heart.drop(columns="target", axis=1)
    Y = data_heart["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train_scaled, Y_train)

    X_train_prediction = model.predict(X_train_scaled)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    X_test_scaled = scaler.transform(X_test)
    X_test_prediction = model.predict(X_test_scaled)
    testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)

    print(f"Dokładność danych treningowych: {training_data_accuracy}")
    print(f"Dokładność danych testowych: {testing_data_accuracy}")

    return model, scaler



