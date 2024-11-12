import  numpy as np

np.random.seed(102191)

# calcula cuantos encestes logra una jugadora con indice de enceste prob
# que hace qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)



# defino los jugadores
taurasi = 0.7
peloton = np.array(range(501, 600)) / 1000
jugadoras = np.append(taurasi, peloton)

# veo que tiene el vector
jugadoras

# vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)

for i in range(10): # 10 rondas.
  vaciertos = vec_ftirar(jugadoras, 10) # 10 tiros libres cada jugadora
  mejor = np.argmax(vaciertos) # agarro a la mejora jugadora de mi primera ronda.
  aciertos_torneo = vaciertos[mejor] # agarro a la mejora jugadora de mi primera ronda.
  aciertos_segunda = vec_ftirar(jugadoras[mejor], 10) # a mi mejora jugadora, la hago tirar una ronda de 10 tiros.
  print(aciertos_torneo, "\t", aciertos_segunda) # Veo los resultados.


