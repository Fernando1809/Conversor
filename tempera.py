
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

temperaturasKaC = pd.read_csv('C:/Users/feran/OneDrive/Escritorio/Conversor/content/Temperaturas.csv', sep=";")
print(temperaturasKaC)

k = temperaturasKaC["k"]
c= temperaturasKaC ["c"]

modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss="mean_squared_error")

epocas = modelo.fit(k,c, epochs=400, verbose=0)

resp = modelo.predict([40])
print(resp)


