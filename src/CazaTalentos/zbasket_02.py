import  numpy as np

np.random.seed(102191)

# calcula cuantos encestes logra una jugadora con indice de enceste prob
# haciendo qyt tiros libres.

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob) #Sumo la cantidad de encestadas.



# defino las jugadoras
taurasi = 0.7 # Probabilidad de Taurasi.
peloton = np.array(range(501, 600)) / 1000 # Genero 1000 jugadores de pelotón con probabilidad entre 0.501 y 0.600.
jugadoras = np.append(taurasi, peloton) # Concateno todas las probabilidades en un solo array.

# veo que tiene el vector
jugadoras

# vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)

# hago que los 100 jugadoras tiren 10 veces cada una
vec_ftirar(jugadoras, 10)

primera_ganadora = 0

for i in range(10000):  # Diez mil experimentos.
    vaciertos = vec_ftirar(jugadoras, 10)  # 10 tiros libres cada jugadora.
    mejor = np.argmax(vaciertos)  # Índice de la jugadora con más encestes.
    if mejor == 0:  # Verifica si la mejor jugadora es `taurasi`.
        primera_ganadora += 1 # Si lo es, sumo una victoria para dicha jugadora.




print(primera_ganadora) # Imprimo la cantidad de veces qeu "Taurasi" fue la ganadora sobre las 10.000 pruebas.
