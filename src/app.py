
# your code here
import streamlit as st
from pickle import load

model = load(open('../models/modelado-knearest-proyecto08.pkl', 'rb'))
class_dict = {"0": "Baja Calidad",
              "1": "Media Calidad",
              "2": "Alto Calidad"}

st.title('App vinos')
st.divider()

val1 = st.slider('alcohol', min_value=8.40000, max_value=14.90000, step=0.1)
val2 = st.slider('pH', min_value=2.74000, max_value=4.01000, step=0.1)
val3 = st.slider('residual sugar', min_value=0.90000, max_value=15.50000, step=0.1)

if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3]])[0])
    pred_class = class_dict[prediction]
    st.divider()
    st.write("Prediction:", pred_class)
    st.divider()
