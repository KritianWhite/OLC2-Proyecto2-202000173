# import pandas as pd
# import numpy as np
# from sklearn.neural_network import MLPRegressor
# from sklearn.model_selection import train_test_split
# import streamlit as st

# def RedNeuronal(_info):
#     st.title('Redes neuronales')
#     st.subheader('Informacion')
#     st.write(_info)
#     st.subheader('Parametrizacion de redes neuronales')
#     paramx = st.text_input('Ingrese parametro X:', '')
#     paramy = st.text_input('Ingrese parametro Y:', '')
    
#     x = 
    
#     X = paramx[:, np.newaxis]
    
#     X_train, X_test, paramy_train, paramy_test = train_test_split(X, paramy)
    
#     mlr = MLPRegressor(solver='lbgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)
#     mlr.fit(X_train, paramy_train)
#     print(mlr.score(X_train, paramy_train))
    

from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
import pandas as pd
import streamlit as st

def RedNeuronal(_info):
    st.title('Redes neuronales')
    st.subheader('Informacion')
    st.write(_info)
    st.subheader('Parametrizacion de redes neuronales')
    param = st.text_input('Ingrese parametro x:','')
    #unidadPre = st.text_input('Ingrese columna para predicción:','')
    
    valoresX = param.split(sep=',')
    le=preprocessing.LabelEncoder()
    print("Aquiiiiii",valoresX)
    
    array = []
    for valores in valoresX:
        array.append(le.fit_transform(_info[valores].to_numpy()))
    
    Xaux = list (zip(*array))
    # Hasta aqui todo bien
    print("Arrayy aquiii",Xaux)
    
    VarX = np.array(Xaux)
    VarY = np.array(_info[param])
    # Hasta aqui todo bien tambien 
    print("Parametros x aquiii",VarX)
    print("Parametros y aquiii",VarY)
    
    #X = VarX[:, np.newaxis]
    VarX_train, VarX_test, VarY_train, VarY_test = train_test_split(VarX, VarY)
    
    mlr = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3,3), random_state=1)
    mlr.fit(VarX_train, VarY_train)
    predi = mlr.score(VarX_train, VarY_train)
    print(predi)
    
    st.subheader("Predicción de Tendencia")
    st.success(predi)
    
    
    
    



