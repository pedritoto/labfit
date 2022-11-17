import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
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
        gb.configure_column('X',type=["numericColumn","numberColumnFilter","customNumericFormat"],valueGetter='(Number(data.X)).toFixed(2)')
        gb.configure_column('Y',type=["numericColumn","numberColumnFilter","customNumericFormat"],valueGetter='(Number(data.Y)).toFixed(2)') 
        st.header('DATOS:')
        response = AgGrid(df, editable=True, fit_columns_on_grid_load=True)
        st.form_submit_button('Realizar ajuste')
    xdata=np.empty(nd, dtype=float) 
    ydata=np.empty(nd, dtype=float) 

    for i in range (0,nd):
        xdata[i]=float(response['data']['X'][i])
        ydata[i]=float(response['data']['Y'][i])
    xmax = np.max(xdata)
    xmin = np.min(xdata)
    dist=xmax-xmin
    xmax=xmax+dist*0.05
    xmin=xmin-dist*0.05
    xx=np.linspace(xmin, xmax, num=40, endpoint=True, dtype=float)
    fig = plt.figure(figsize=(4, 3), dpi=200)
    ax = fig.add_axes([0.03,0.055,0.95,0.95])
    ax.set_facecolor('azure')


    if optfit == 'Lineal':
        coef = np.polyfit(xdata, ydata, 1)
        poly1d_fn = np.poly1d(coef) 
        ax.plot(xdata, ydata, 'yo', xx, coef[0]*xx+coef[1], '--k')
        ax.grid()
        plt.xlabel(labelx)
        plt.ylabel(labely)
        st.pyplot(fig)
    else:
        # Function to calculate the power-law with constants a and b
        def power_law(x, a, b):
            return a*np.power(x, b)
        # Fit the dummy power-law data
        pars, cov = curve_fit(f=power_law, xdata=xdata, ydata=ydata, p0=[0, 0], bounds=(-np.inf, np.inf))
        yy=power_law(xx,pars[0],pars[1])
        ax.plot(xdata, ydata, 'yo', xx, yy, '--k')
        ax.grid()
        plt.xlabel(labelx)
        plt.ylabel(labely)
        st.pyplot(fig)
        #st.write(pars)


