import matplotlib.pyplot as plt
from sklearn import preprocessing
import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import preprocessing

def ArbolD(_info):
    st.title('Clasificador de Arbol de desicion')
    st.subheader('Visualización del archivo')
    st.write(_info)

    st.subheader('Ingreso de parametros')
    param = st.text_input('Ingrese la columna que desea como parametro:','')
    
    # Eliminación columnas
    data_top = _info.columns.values
    listaa = data_top.tolist()

    listaaux = ["Seleccionar"]+listaa
    eliminarcolumna =st.selectbox('¿Desea eliminar una columna?',listaaux)

    listaa.remove(param)
    if eliminarcolumna != 'Seleccionar':
        listaa.remove(eliminarcolumna)
    result = _info[param]


    listadedf = []
    for i in listaa:
        aux = _info[i]
        aux = np.asarray(aux)
        #print('aux=', aux)
        listadedf.append(aux)
    listadedf = np.array(listadedf)

    # Creacion del codificador de palabras
    # NOTE: no salio lo de las palabras :v 
    le = preprocessing.LabelEncoder()

    #Se convierte los String a numeros
    listafittransform = []
    for x in listadedf:
        listafittransform.append(le.fit_transform(x))

    #Se convierte los string a numero del parametro
    label = le.fit_transform(result)

    # Combinando los atributos en una lista simple de tuplas
    with st.expander('Resultados sin etiquetas'):
        features = list(zip(np.asarray(listadedf)))
        features = np.asarray(features)
        tamcolumnas = len(features)
        tamfilas=features.size
        features = features.reshape(int(tamfilas/tamcolumnas),tamcolumnas)
        st.dataframe(features)
    #print(features)
    
    with st.expander("Resultado con etiquetas"):
        featuresencoders = list(zip((listafittransform)))
        featuresencoders = np.array(featuresencoders)
        tamcolumnas = len(listaa)
        tamfilas = featuresencoders.size
        featuresencoders = featuresencoders.reshape(int(tamfilas/tamcolumnas),tamcolumnas)
        #print("\n\nFeatures con coders ",featuresencoders)
        st.dataframe(featuresencoders)

    # Se encaja con el modelo
    clf = DecisionTreeClassifier(max_depth=4).fit(features,result)
    fig,ax = plt.subplots()
    plot_tree(clf,filled = True, fontsize=10)
    st.subheader('Gráficos')
    with st.expander("Mostrar arbol sin etiquetas"):
        plt.figure(figsize=(50,50))
        st.pyplot(fig)

    clf2 = DecisionTreeClassifier(max_depth=5).fit(featuresencoders,label)
    fig2,ax2 = plt.subplots()
    plot_tree(clf2,filled = True)
    with st.expander("Mostrar arbol con etiquetas"):
        plt.figure(figsize=(50,50))
        st.pyplot(fig2)
