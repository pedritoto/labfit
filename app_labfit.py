import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

st.set_page_config(layout="wide")
st.title("App para el ajuste de datos experimentales")
st.markdown(" ### Ajuste lineal $ y = ax + b~~~~~~~~~~~~~~~~~~~~~~~~$  Ajuste potencial $ y = a x^b$ ")


with st.sidebar:
    st.markdown(" ## Elige la opción de ajuste ")
    optfit = st.radio("Ajuste tipo:",('Lineal', 'Potencial'))
    st.markdown(" ## Elige el número de datos (>2)")
    nd = st.number_input('',min_value=0, max_value=20, value=0, step=1)
    st.markdown(" ## Etiquetas de los ejes")
    labelx = st.text_input('Eje x', 'X')
    labely = st.text_input('Eje y', 'Y')
    #datain = st.button('Ingresar datos datos')

    st.image('Dorado.jpg')
    st.markdown(""" 
             ### *Autores:*
             **Dr. Juan Pedro Palomares Báez**


             **Dr. José Manuel Nápoles Duarte**


             **MC. Carlos Armando de la Vega Cobos**
             
             """)


xdata=[]
ydata=[]


if nd != 0:
    df = pd.DataFrame("",index=range(nd),columns=list("XY"))

    #gb = GridOptionsBuilder.from_dataframe(df)
    #gb.configure_default_column(editable=True)

    #gb.configure_grid_options(enableRangeSelection=True)


    #response = AgGrid(
    #    df,
    #    gridOptions=gb.build(),
    #    fit_columns_on_grid_load=True,
    #    allow_unsafe_jscode=True,
    #    enable_enterprise_modules=True
    #)
    with st.form('datos') as f:
        st.header('DATOS:')
        response = AgGrid(df, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button('Realizar ajuste')
    

    #st.write(response['data']) 
    xdata = response['data']['X']
    st.write(xdata)


#    for i in range(1,nd):
#        dd = st.input_number
#        xd.append()
#st.write(df.head())