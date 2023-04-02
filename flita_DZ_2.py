#USED MODULS
import networkx as nx
import pyvis
import matplotlib.pyplot as plt
import numpy as np

#CONECTING_OF_THE_FILES
file= open(r"C:\Users\Дамириддин\Desktop\ФЛиТА\dz_flita\DZ_2\graphs\outputs\adjacency_matrix_0.txt")
list_str=file.readlines()
matrix=[]
for st_r in list_str:
    list_1=st_r.split()
    matrix.append(list_1)
file.close()


#NETWORKX_PART
G=nx.from_numpy_array(np.array(matrix))
nx.draw_random(G,with_labels=True)
plt.show()













