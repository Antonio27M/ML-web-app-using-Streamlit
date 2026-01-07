
# your code here
import streamlit as st
import os
from pickle import load

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "modelado-knearest-proyecto08.pkl")

model = load(open(MODEL_PATH, "rb"))

#model = load(open('../models/modelado-knearest-proyecto08.pkl', 'rb'))
class_dict = {"0": "Baja Calidad",
              "1": "Media Calidad",
              "2": "Alto Calidad"}

st.title('App vinos')
st.divider()

val1 = st.slider('alcohol', min_value=8.40000, max_value=14.90000, step=0.1)
val2 = st.slider('pH', min_value=2.74000, max_value=4.01000, step=0.1)
val3 = st.slider('residual sugar', min_value=0.90000, max_value=15.50000, step=0.00001)
val4 = st.slider('fixed acidity', min_value=4.60000, max_value=15.90000, step=0.1)
val5 = st.slider('volatile acidity', min_value=0.12000, max_value=1.58000, step=0.1)
val6 = st.slider('citric acid', min_value=0.00000, max_value=1.00000, step=0.0001)
val7 = st.slider('chlorides', min_value=0.01200, max_value=0.61100, step=0.0001)
val8 = st.slider('free sulfur dioxide', min_value=1.00000, max_value=72.00000, step=0.1)
val9 = st.slider('total sulfur dioxide', min_value=6.00000, max_value=289.00000, step=0.1)
val10 = st.slider('density', min_value=0.99007, max_value=1.00369, step=0.00001)
val11 = st.slider('sulphates', min_value=0.33000, max_value=2.00000, step=0.00001)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11]])[0])
    pred_class = class_dict[prediction]
    st.divider()
    st.write("Prediction:", pred_class)
    st.divider()
