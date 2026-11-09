import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# crearemos nuestra tabla y la guardaremos con pandas 
# tenemos 6 listas de plataformas de streaming con 4 elementos por lista
net = ['Netflix', 8900, True, 2007]
dis = ['Disney+', 7400, False, 2019]
prm = ['Prime Video', 8100, True, 2011]
hbo = ['HBO Max', 6200, False, 2020]
spt = ['Spotify', 9200, True, 2008]
tch = ['Twitch', 4500, False, 2011]

# creamos una lista de listas (conformando tabla)
lista_streaming = [net, dis, prm, hbo, spt, tch]

# utilizar pandas para organizar la tabla (dataframe o marco de datos)
# a cada columna le ponemos nombre
df_streaming = pd.DataFrame(lista_streaming, columns=["Nombre", "Cantidad", "Es_Popular", "Año"])
print(df_streaming)

# creamos el archivo CSV y lo guardamos en CSV 
df_streaming.to_csv("plataformas_streaming.csv", index=False)

# crear grafica de lineas 
# donde X es Nombre en el eje horizontal
# donde Y es Cantidad en el eje vertical
plt.plot(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.title("grafica plataformas streaming 1341")
plt.xlabel("nombre de las plataformas")
plt.ylabel("cantidad de usuarios")
plt.show()

# creamos una grafica de puntos 
plt.scatter(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.show()

# grafica de barras 
plt.bar(df_streaming["Nombre"], df_streaming["Cantidad"])
plt.title("plataformas streaming 1341")
# Etiquetas de los ejes
plt.xlabel("las plataformas")
plt.ylabel("cantidad de usuarios")
# Muestra el gráfico en pantalla
plt.show()

# ordenar la grafica de barras de manera descendente 
# de la mas grande a la pequeña 
df_str_ordenar = df_streaming.sort_values("Cantidad", ascending=False)
plt.bar(df_str_ordenar["Nombre"], df_str_ordenar["Cantidad"])
plt.show()

# coloreamos la grafica 
df_str_ordenar = df_streaming.sort_values("Cantidad", ascending=False)
plt.bar(df_str_ordenar["Nombre"], df_str_ordenar["Cantidad"],
        color=["b", "g", "c", "m", "y", "r"])
plt.show()

# grafica de pastel 
plt.pie(df_streaming["Cantidad"], labels=df_streaming["Nombre"])
plt.show()