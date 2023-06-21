import os

# raise ValueError("Let's see if this error is shown in the frontend")

import streamlit as st
import requests

response = requests.get('http://backend:8080/ping_redis')
response.raise_for_status()
st.write("Successfully sent request to backend")

uploaded_files = st.file_uploader("Upload a doggos pictures", type=["png", "jpg"], accept_multiple_files=True)

static_folder_path = os.path.dirname(os.path.abspath(__file__)) + "/static"

# check if static folder exists else create it
if not os.path.exists(static_folder_path):
    os.makedirs(static_folder_path)


for file in uploaded_files:
    with open(f"{static_folder_path}/{file.name}", "wb") as f:
        f.write(file.read())


for file in os.listdir(static_folder_path):
    st.image(f"{static_folder_path}/{file}", width=200)




