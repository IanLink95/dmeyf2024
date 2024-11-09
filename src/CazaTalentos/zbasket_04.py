import  numpy as np

np.random.seed(102191)

# calcula cuantos encestes logra una jugadora con indice de enceste prob
# que hace qyt tiros libres

def ftirar(prob, qty):
  return sum(np.random.rand(qty) < prob)



# defino los jugadoras
jugadoras = [0.7] * 100


# vectorizo la funcion  ftirar
vec_ftirar = np.vectorize(ftirar)

for i in range(10):
  vaciertos = vec_ftirar(jugadoras, 100) # 10o tiros libres cada jugador.
  mejor = np.argmax(vaciertos)
  aciertos_torneo = vaciertos[mejor]
  aciertos_segunda = vec_ftirar(jugadoras[mejor], 100) # A la ganadora, le hago tirar de nuevo 100 tiros libres.
  print(aciertos_torneo, "\t", aciertos_segunda) # Anoto como le fue en esta segunda ronda.


