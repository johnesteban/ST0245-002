import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
mapa=nx.Graph()

data=pd.read_csv('vertices.csv', sep=",", keep_default_na=True) #C1
data2=pd.read_csv('arcos.csv', sep=",", keep_default_na=True)  #C2

for i in range(len(data)): #C3*n en donde n es la cantidad de vertices
    mapa.add_node(data['ID'].values[i])  #C4*n
    
for i in range(len(data2)):  #C5*m, en donde m es la cantidad de arcos  
    mapa.add_edge(data2['ID_origen'].values[i],data2['ID_destino'].values[i]) #C6*m
    mapa[data2['ID_origen'].values[i]][data2['ID_destino'].values[i]]["weigth"]=data2['distancia'].values[i] #C7*m
    
nx.draw_shell(mapa, node_color='green', edge_color='red', font_size=15, width=4) #C8
plt.show() #C9
    

"""
CALCULO DE COMPLEJIDAD
T(n,m)=C1+C2+C3*n+C4*n+C5*m+C6*m+C7*m+C8+C9
T(n,m) es O(C1+C2+C3*n+C4*n+C5*m+C6*m+C7*m+C8+C9)--->(Notación O)
O(C1+C2+C3*n+C4*n+C5*m+C6*m+C7*m+C8+C9)=O((n*(C3+C4))+(m*(C5+C6+C7))+C')--->(Regla de la suma y factor común)
O((n*(C3+C4))+(m*(C5+C6+C7))+C')=O((n*C)+(m*C))--->(Regla de la suma)
O((n*C)+(m*C))=O(n+m)--->(Regla del producto)
T(n,m) es O(n+m)
en donde n es la cantidad de vertices y m es la cantidad de arcos
"""
