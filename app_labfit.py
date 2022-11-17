import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import os
from matplotlib.transforms import IdentityTransform

st.set_page_config(layout="wide")
st.title("App para el ajuste de datos experimentales")
st.markdown(" ### Ajuste lineal $ y = ax + b~~~~~~~~~~~~~~~~~~~~~~~$  Ajuste potencial $ y = a x^b$ ")


with st.sidebar:
    st.markdown(" ## Elige la opción de ajuste ")
    optfit = st.radio("Ajuste tipo:",
    ('Lineal', 'Potencial'))
