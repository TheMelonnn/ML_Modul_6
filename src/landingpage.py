import streamlit as st
import numpy as np

st.title("Knows your dog!")

st.subheader("Welcome to Knows your dog!")
st.write("This app will help you to classify the dog breed from the uploaded image.")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image('https://cdn.britannica.com/46/233846-050-8D30A43B/Boxer-dog.jpg')
with col2:
    st.image('https://upload.wikimedia.org/wikipedia/commons/b/be/%EB%8B%A5%EC%8A%A4%ED%9B%88%ED%8A%B8%28%EB%8B%A8%EB%AA%A8%EC%A2%85%29_%28Dachshund_%28Short%29%29.jpg')
with col3:
    st.image('https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRoq_cX-7-8JzWjLm9vQ80PPfAbtFp6ibY-BsYvS087PNjgHhYiNWrO3-t-O7E4CzasfIjpvfKKDsd93_vJv_B_sembF4zGPTK3cXYPFOU')
with col4:
    st.image('https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSoPP6Niq9hSu9nCBgwmpfW8v3txmHrma78vwfl7R4uRYUiyQ-Fxl4Xwf7m-HtOgptf2_XsOKE8H6Poyg9KEE3YlA')
with col5:
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Rottweiler_standing_facing_left.jpg/800px-Rottweiler_standing_facing_left.jpg')


st.write("This app can classify 5 of dog breed: Boxer, Daschund, Golden Retriever, Poodle, and Rottweiler.")
st.write("Want to know your dog breed? Just click the button below!")

if st.button("Click here to classify your dog breed!"):
    st.switch_page("pages/klasifikasi.py")