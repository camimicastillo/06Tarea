'''
Este script resuelve numéricamente la ecuación de Fisher-KPP, usando el metodo
de Crank Nicolson y el de Euler explicito. La ecuacion corresponde a
dT/dt = gamma * d2T/dx2 + mu * T - mu * T^2
'''

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def inicializa_T(T, N_steps, h):
    '''
    Rellena T con las condiciones iniciales del problema.
    Se asegura que las condiciones en los bordes sean CB1 y CB2.
    '''
    for i in range(N_steps):
        x = i * h
        T[i] = np.exp(- x ** 2 / 0.1)
    T[0] = CB1
    T[-1] = CB2



#Con solucion Crank Nicolson y Euler explicito
def calcula_b(b, N_steps, r):
    for j in range(1, N_steps - 1):
        b[j] = r * T[j+1] + (1-2*r) * T[j] + r * T[j-1] +
               T[j] * (dt * mu - dt * mu T[j])



def calcula_alpha_y_beta(alhpa, beta, b, r, N_Steps):
    Aplus = -1 * r
    Acero = (1 + 2 * r)
    Aminus = -1 * r
    alpha[0] = 0
    beta[0] = CB1  # viene de la condicion de borde T(t, 0) = 1
    for i in range(1, N_steps):
        alpha[i] = -Aplus / (Acero + Aminus*alpha[i-1])
        beta[i] = (b[i] - Aminus*beta[i-1]) / (Aminus*alpha[i-1] + Acero)


def avanza_paso_temporal(T, T_next, alpha, beta, N_steps):
    T_next[0] = CB1
    T_next[-1] = CB2
    for i in range(N_steps - 2, 0, -1):
        T_next[i] = alpha[i] * T_next[i+1] + beta[i]


# Main

# setup
gamma = 0.001
mu = 1.5

#Condiciones de borde para T(t,0) y T(t,1) respectivamente
CB1 = 1
CB2 = 0

N_steps = 500
N_pasos_temporales =
x_inicial = 0
x_final = 1
t_inicial =
t_final =
#Paso espacial h
h = (x_final - x_inicial) / (N_steps - 1)
#Paso temporal dt
dt = (t_final - t_inicial) / (N_pasos_temporales - 1)

r = (gamma * dt) / (2 * h ** 2)


T = np.zeros(N_steps)
T_next = np.zeros(N_steps)

b = np.zeros(N_steps)
alpha = np.zeros(N_steps)
beta = np.zeros(N_steps)

#Pone las condiciones iniciales
inicializa_T(T, N_steps, h)

# Queremos guardar las soluciones en cada paso
T_solucion = np.zeros((N_pasos_temporales, N_steps))
T_solucion[0, :] = T.copy()

#Crank Nicolson
for i in range(1, N_pasos_temporales):
    calcula_b(b, N_steps, r)
    calcula_alpha_y_beta(alpha, beta, b, r, N_steps)
    avanza_paso_temporal(T, T_next, alpha, beta, N_steps)
    T = T_next.copy()
    T_solucion[i, :] = T.copy()
