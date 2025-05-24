"""
Proyecto Final: Sistema Cardiovascular (Arritmia)
Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Ashley Dayanna Panzzi Hernandez 
Número de control: 22210424
Correo institucional: l22210424@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Definicion de parámetros de los componentes en la primera malla


Amarillo = [1,0.7,0]
Rojo = [1,0,0]
Morado = [0.6,0.3,0.7]
Azul = [0.1,0.5,0.7]




# Definicion de parámetros del generador para la primera malla

def sys_cardio(Z1,C1,R1,L1):
       num = [R1*C1 + 1 ]
       den = [C1*Z1*L1, (R1*C1+1)*Z1, R1*(C1*C1)]
       sys = ctrl.tf(num,den)
       return sys

#  Normotenso (control)
Z1, C1, R1, L1 = 10, 0.03, 1000, 0.05
sysN = sys_cardio(Z1,C1,R1,L1)
print('Individuo: Normotenso')
print(sysN)





frecuencia_gen1 = 1  # Hz
dutycicle_gen1 = 50  # %
amplitud_gen1 = 0.3  # Vp
offset_gen1 =0  # V

# Definicion de parámetros de los componentes en la segunda malla

def sys_cardiot(Z2,C2,R2,L2):
       num2 = [R2*C2 + 1 ]
       den2= [C2*Z2*L1, (R2*C2+1)*Z2, R2*(C2*C2)]
       sys = ctrl.tf(num2,den2)
       return sys



#  tAQUICARDIA (CASO)
Z2, C2, R2, L2 = 0.005,0.05,1000,0.03
sysT = sys_cardio(Z2,C2,R2,L2)
print('Individuo: TAQUICARDIA')
print(sysT)

frecuencia_gen2 = 1 # Hz
dutycicle_gen2 = 50  # %
amplitud_gen2 = 1  # Vp
offset_gen2 = 0  # V

#normal
num = [R1*C1 + 1 ]
den = [C1*Z1*L1, (R1*C1+1)*Z1, R1*(C1*C1)]

#taqui
num2 = [R2*C2 + 1 ]
den2= [C2*Z2*L1, (R2*C2+1)*Z2, R2*(C2*C2)]
#Funciones de transferencia 
num = [R1*C1 + 1 ]
den = [C1*Z1*L1, (R1*C1+1)*Z1, R1*(C1*C1)]
sys = ctrl.tf(num,den)
print("Control:NORMAL")
print(sysN)

#FUNCION DE TRANSFERENCIA TAQUICARDIA
num2 = [R2*C2 + 1 ]
den2= [C2*Z2*L1, (R2*C2+1)*Z2, R2*(C2*C2)]
sys = ctrl.tf(num2,den2)
print("Caso:Taquicardia")
print(sysT)



# Configuracion la simulación
tiempo_simulacion = 5  # segundos
fs = 1000  # frecuencia de muestreo en Hz
tiempo = np.arange(0, tiempo_simulacion, 1/fs)

# Obtenencion de las señales de ambos generadores
senal_malla1 = amplitud_gen1 * np.sin(2 * np.pi * frecuencia_gen1 * tiempo) + offset_gen1
senal_malla2 = amplitud_gen2 * np.sin(2 * np.pi * frecuencia_gen2 * tiempo) + offset_gen2

# Graficacion de las señales de entrada
plt.figure(figsize=(12, 6))


plt.plot(tiempo, senal_malla1, label='Control:Normotenso',color=[0.1,0.5,0.7])
plt.plot(tiempo, senal_malla2, label='Caso:Taquicardia ',color=[1,0.7,0])
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(False)
plt.legend(bbox_to_anchor=(0.5,-0.23),loc='center',ncol=3)

plt.tight_layout()
plt.show()
