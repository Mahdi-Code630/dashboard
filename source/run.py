import streamlit as st 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Login:
login_option = st.sidebar.radio("Login/Signup", ("Login", "Signup"))
if login_option == "Login":
    with st.sidebar.form("Login"):
        st.write("Login Here...")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        #Every Form must have a submit button
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("Signup"):
        st.write("Signup Here...")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Signup")
        if submitted:
            pass

#banner:
banner = Image.open("./data/images.jfif")
st.image(banner)
st.title(":zap: Statistices Dashboard")

#Metrics:
col1, col2 = st.columns(2)
col1.metric(label="Itman Telegram Group Members", value=6, delta="+10")
col2.metric(label="Itman Website Members", value=5, delta="-1")

#Statistices:
with st.expander("Statistices"):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

#User info:    
with st.expander("User Profile"):
    cal1, cal2, col3, col4 = st.columns(4)
    cal1.text_input("Name:")
    cal2.text_input("LastName:")
    col3.text_input("Age:")
    col4.text_input("Location:")
    st.camera_input("Camera Input", key="camera_input")