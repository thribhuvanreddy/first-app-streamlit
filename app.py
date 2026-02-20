import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import joblib
import matplotlib.pyplot as plt

st.title("ML Model Demo")
st.header("Prediction System")
st.subheader("Enter Inputs Below")
st.write("This app demonstrates ML model deployment.")
name = st.text_input("Enter Customer Name")
age = st.number_input("Enter Age", min_value=0, max_value=100)
salary = st.slider("Select Salary", 10000, 100000)
gender = st.selectbox("Select Gender", ["Male", "Female"])
education = st.radio("Education Level", ["UG", "PG", "PhD"])
agree = st.checkbox("I agree to terms")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])
if st.button("Predict"):
    st.success("Prediction Successful")
    st.warning("Warning")
    st.error("Error, enter valid input")
df = pd.DataFrame({"A":[1,2], "B":[3,4]})
st.dataframe(df)

appointment = st.date_input("Select the appointment date")
st.write("Appointment Date: ", appointment)
time = st.time_input("Select Appointment time")
st.write("Appointment Time: ", time)
# To display Accuracy, Precision, Recall
st.metric("Accuracy", "92%", "+2%")

# Image Display CNN projects, Computer Vision based apps
st.image("peacock.jpg", caption= "Peacock")
# Audio & Video
# st.audio("<audio file name>")
# st.video("<video file name>")

# Sidebar - for Multi-page apps
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose Page", ["Home", "Prediction"])

# Layout Control
col1, col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")
# Progress & Spinners (ML/DL Models)
with st.spinner("Processing..."):
    # result = model.predict(data)
    st.progress(50)

# Caching Model (Very Important)
# Prevents reloading model everytime
# @st.cache_resource

# def load_model():
    # return joblib.load("model.pkl")

# model = load_model()

# Interactive DataFrame 
data = {
    "Name": ["Ajay", "Shah", "Ram", "Mohit", "John", "Kevin", "Rajesh"],
    "Age" : [12, 43, 54, 65, 43, 76, 43],
    "City": ["Hyd", "Mumbai", "Kolkata", "bhopal", "Chennai", "Delhi", "Jaipur"]
}

data_df = pd.DataFrame(data)
st.dataframe(data_df)

# display some charts
# st.pyplot()
# St.line_chart()