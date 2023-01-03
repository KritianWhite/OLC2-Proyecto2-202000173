from numpy.core.fromnumeric import size
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd
import streamlit as st
import numpy as np
from sklearn.naive_bayes import GaussianNB

def ClGaussiano(_info):
    st.title('Clasificador Gaussiano')
    st.subheader('Visualización del archivo')
    st.write(_info)
    st.subheader('Ingreso de parametros')
    param = st.text_input('Ingrese parametro de aproximacion: ','')
    
    # Eliminación de columna
    data_top = _info.columns.values
    listaa = data_top.tolist()

    listaaux = ["Seleccionar"]+listaa
    eliminarcolumna =st.selectbox('¿Desea eliminar una columna?',listaaux)

    # Eliminacion en la tabla el parametro predecir
    listaa.remove(param)
    if eliminarcolumna != 'Seleccionar':
        listaa.remove(eliminarcolumna)
    result = _info[param]


    listadedf = []
    for i in listaa:
        aux = _info[i]
        aux = np.asarray(aux)
        listadedf.append(aux)
    listadedf = np.array(listadedf)


    # Creacion del codificador de palabras
    le = preprocessing.LabelEncoder()

    #Se convierte los String a numeros
    listafittransform = []
    for x in listadedf:
        listafittransform.append(le.fit_transform(x))

    #Se convierte los string a numero del parametro
    label = le.fit_transform(result)
    

    # Combinando los atributos en una lista simple de tuplas
    with st.expander("Resultado con etiquetas"):
        featuresencoders = list(zip((listafittransform)))
        featuresencoders = np.array(featuresencoders)
        tamcolumnas = len(listaa)
        tamfilas = featuresencoders.size
        featuresencoders = featuresencoders.reshape(int(tamfilas/tamcolumnas),tamcolumnas)
        #print("\n\nFeatures con coders ",featuresencoders)
        st.dataframe(featuresencoders)

    with st.expander('Resultados sin etiquetas'):
        features = list(zip(np.asarray(listadedf)))
        features = np.asarray(features)
        tamcolumnas = len(features)
        tamfilas=features.size
        features = features.reshape(int(tamfilas/tamcolumnas),tamcolumnas)
        st.dataframe(features)
    #print(features)
    
    # Clasificador Gaussiano
    model = GaussianNB()
    model2 = GaussianNB()
    
    #Se entrena el modelo
    model.fit(np.asarray(features),np.asarray(result))
    model2.fit(featuresencoders,label)

    columna = len(listaa)
    texto = "Ingrese " + str(columna) + " parametros, separados por coma(,)"
    predecirresult = st.text_input(texto,'')

    if predecirresult != '':
        entrada = predecirresult.split(",")
        map_obj = list(map(int,entrada))
        map_obj = np.array(map_obj)
        predicted = model.predict(np.asarray([map_obj]))
        predicted2 = model2.predict(np.asarray([map_obj]))
        print(np.asarray([map_obj]))
        
        st.subheader("Tendencias de predicción")
        co1,co2,co3 = st.columns(3)
        with co2:
            st.write('Prediccion con etiquetas: ')
            st.success(predicted)

        coo1,coo2,coo3 = st.columns(3)
        with coo2:
            st.write('Prediccion sin etiquetas: ')
            st.success(predicted2)