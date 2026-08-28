import streamlit as st 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from db.models import Message

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



#Questions:
with st.expander("Q / A"):
    query = st.text_input('Search:')

    for message in Message.objects.all().order_by("-date"):

        if not message.text or message.text[-1] not in '؟?':
            continue
        if query and query not in message.text:
            continue
        
        col1, col2 = st.columns([1, 4])
        col1.write(f"**{message.user.username}**")
        col2.write(message.text.replace(query, f"**{query}**"))

    col1, col2 = st.columns(2)
    col1.button('< Previous')
    col2.button('Next >')