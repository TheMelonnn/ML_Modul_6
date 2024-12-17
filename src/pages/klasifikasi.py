import streamlit as st
import tensorflow as tf
from pathlib import Path
import numpy as np

st.title("Knows your dog!")
upload = st.file_uploader(
    'Upload your dog image here', 
    type=['png','jpg'])

def predict(image):
    class_names = ['Boxer', 'Daschund', 'Golden Retriever', 'Poodle', 'Rottweiler']

    img = tf.keras.utils.load_img(upload, target_size=(300, 300, 3))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    
    model = tf.keras.models.load_model(Path(__file__).parent / 
    "model/klasifikasi_citra.h5")
    output = model.predict(img_array)
    score = tf.nn.softmax(output[0])
    return class_names[np.argmax(score)]

if st.button('Predict'):
    if upload is not None:
        st.image(upload)
        st.subheader('Predictions:')
        with st.spinner('Predicting...'):
            predictions = predict(upload)
        st.write(predictions)
    else:
        st.write('Please upload an image')