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

    with st.form('datos') as f:
        gb = GridOptionsBuilder.from_dataframe(df) 
        gb.configure_column('X',type=["numericColumn","numberColumnFilter","customNumericFormat"], valueGetter="data.AMT.toLocaleString('en-US', {style: 'maximumFractionDigits:1})")
        gb.configure_column('Y',type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=4)
        st.header('DATOS:')
        response = AgGrid(df, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button('Realizar ajuste')
     
    xdata = response['data']['X'].to_numpy()
    ydata = response['data']['Y'].to_numpy()
    #xdata = df['X'][1]
    #ydata = df['Y'][1]
    xdata
    ydata
    #st.write(ydata)
    fig = plt.figure(figsize=(4, 4), dpi=200)
    ax = fig.add_axes([0.03,0.055,0.95,0.95])
    ax.set_facecolor('azure')

    if optfit == 'Lineal':

        coef = np.polyfit(xdata, ydata, 1)
        #poly1d_fn = np.poly1d(coef) 
        #fig.plot(xdata, ydata, 'yo', xdata, a*xdata+b, '--k')
        #st.pyplot(fig)

#    for i in range(1,nd):
#        dd = st.input_number
#        xd.append()
#st.write(df.head())