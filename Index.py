import streamlit as st
import pandas as pd
from Regresion_Lineal import * 
from Regresion_Polinomial import *
from Clasificador_Gaussiano import *
from Clasificador_Arboles import *
from Red_Neuronal import *

#st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('PROYECTO 2 - Machine Learning')

st.subheader('Christian Alessander Blanco González - 202000173')
uploaded_file = st.file_uploader(label = "Cargue sus archivos:",type=['csv','xls','xlsx','json'])

df = ""
if uploaded_file is not None:
  print(uploaded_file)
  print(uploaded_file.type)
  print('hello')
  try:
    if uploaded_file.type == 'text/csv':
      print('csv')
      st.text("csv")
      df = pd.read_csv(uploaded_file)
      #settitlepage2(df)
    if uploaded_file.type == 'application/vnd.ms-excel':
      print('xls')
      st.text("xls")
      df = pd.read_excel(uploaded_file)
    if uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
      print("xlsx")
      st.text("xlsx")
      df = pd.read_excel(uploaded_file)
    if uploaded_file.type == 'application/json':
      print("json")
      st.text("json")
      df = pd.read_json(uploaded_file)
    #df = pd.read_json(uploaded_file)
    #st.write(df)
  except Exception as e: 
    print(e)
    st.subheader('Error al cargar archivo: ',e)

#dropbutton
option = st.selectbox(
     'Seleccione el tipo de algoritmo que desea:',
     ('Seleccione una opcion','Regresión lineal', 'Regresión polinomial', 'Clasificador Gaussiano','Clasificador de árboles de decisión','Redes neuronales'))

st.write('Se seleccionó:', option)


if option == 'Regresión lineal':
  RL(df)
elif option == 'Regresión polinomial':
  RPol(df)
elif option == 'Clasificador Gaussiano':
  ClGaussiano(df)
  #param = st.text_input('Ingrese parametro de aproximacion','I')
  #data_top = df.columns.values
  #listaa = data_top.tolist()

  #print("Clasificador Gaussiano")
  #ClGaussiano(df)
elif option == 'Clasificador de árboles de decisión':
  #print("Clasificador de árboles de decisión")
  ArbolD(df)
elif option == 'Redes neuronales':
  RedNeuronal(df)
  
  #print("Redes neuronales")








