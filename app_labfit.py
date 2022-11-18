import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode

st.set_page_config(layout="wide")
st.title("App para el ajuste de datos experimentales")
st.markdown(" ### Ajuste lineal $ y = ax + b~~~~~~~~~~~~~~~~~~~~~~~~$  Ajuste potencial $ y = a x^b$ ")

def power_law(x, a, b):
    return a*np.power(x, b)

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
        bu = st.form_submit_button('Realizar ajuste')
    if bu:   
        xdata=np.empty(nd, dtype=float) 
        ydata=np.empty(nd, dtype=float) 

        for i in range (0,nd):
            xdata[i]=float(response['data']['X'][i])
            ydata[i]=float(response['data']['Y'][i])
        xmax = np.max(xdata)
        xmin = np.min(xdata)
        dist=xmax-xmin
        xmax=xmax+dist*0.1
        xmin=xmin-dist*0.1
        xx=np.linspace(xmin, xmax, num=40, endpoint=True, dtype=float)
        fig = plt.figure(figsize=(4, 3), dpi=200)
        ax = fig.add_axes([0.17,0.17,0.8,0.8])
        ax.set_facecolor('azure')
        ax.grid(True,lw=0.8,linestyle='--',zorder=0)
        plt.xlabel(labelx,fontsize='x-large')
        plt.ylabel(labely,fontsize='x-large')

        if optfit == 'Lineal':
            coef = np.polyfit(xdata, ydata, 1)
            poly1d_fn = np.poly1d(coef) 
            st.markdown("### Ajuste:")
            nu1="{:.3f}".format(abs(coef[0]))
            nu2="{:.3f}".format(abs(coef[1]))
            if coef[0]<0.0:
                if coef[1]<0.0:
                    stri = " $ y = -" + nu1+ "~x - "+nu2+"$"
                else:
                    stri = " $ y = -" + nu1+ "~x + "+nu2+"$"
            else:
                if coef[1]<0.0:
                    stri = " $ y = " + nu1+ "~x - "+nu2+"$"
                else:
                    stri = " $ y = " + nu1+ "~x + "+nu2+"$"                
            st.markdown('####'+stri)
            st.markdown("### Gráfica:")
            ax.plot(xdata, ydata, 'ro',label='Experimento')
            ax.plot(xx, coef[0]*xx+coef[1], '-k',label=stri)
            ax.legend(loc='upper left', shadow=True, fontsize='small')
            plt.savefig('plot.png')
            st.pyplot(fig)
        else:
            # Fit the dummy power-law data
            pars, cov = curve_fit(f=power_law, xdata=xdata, ydata=ydata, p0=[0, 0], bounds=(-np.inf, np.inf))
            pot="{:.3f}".format(pars[1])
            stri = " $ y = {:.3f}".format(pars[0]) + "~x^{~"+pot+"}$"
            st.markdown("### Ajuste:")
            st.markdown('#### '+stri)
            st.markdown("### Gráfica:")
            yy=power_law(xx,pars[0],pars[1])
            ax.plot(xdata, ydata, 'ro',label='Experimento')
            ax.plot(xx, yy, '-k',label=stri)
            ax.legend(loc='upper left', shadow=True, fontsize='small')
            plt.savefig('plot.png')
            st.pyplot(fig)            

with open("plot.png", "rb") as file:
    btn = st.download_button(
        label="Descargar imagen",
        data=file,
        file_name=None,
        mime="image/png"
        )
    #if btn:  
    #    os.system("rm *.png") 
