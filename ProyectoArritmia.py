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



# Función para crear sistemas
def sys_cardio(Z,C,R,L):
    num = [R*C + 1 ]
    den = [C*Z*L, (R*C+1)*Z, R*(C*C)]
    return ctrl.tf(num,den)

# Sistema Normotenso (control)
Z1, C1, R1, L1 = 10, 0.03, 1000, 0.05
sysN = sys_cardio(Z1,C1,R1,L1)

# Sistema Taquicardia (caso)
Z2, C2, R2, L2 = 0.005,0.05,1000,0.03
sysT = sys_cardio(Z2,C2,R2,L2)

# Configuración del Controlador PID con tus ganancias
Kp = 1382.64108107363  # Proporcional
Ki = 23976.1659464632  # Integral
Kd = 7.06671657792426  # Derivativo
N = 251170.983745407   # Coeficiente de filtro

# Creación del PID con filtro derivativo
pid_num = [Kd*N + Kp, Kp*N + Ki, Ki*N]
pid_den = [N, N, 0]
pid = ctrl.tf(pid_num, pid_den)

# Configuración de simulación
tiempo_simulacion = 5  # segundos
fs = 1000  # frecuencia de muestreo
tiempo = np.arange(0, tiempo_simulacion, 1/fs)

# Señales de entrada (MANTENIENDO TUS VALORES ORIGINALES)
frecuencia_gen1 = 1  # Hz
amplitud_gen1 = 0.3  # Vp
senal_malla1 = amplitud_gen1 * np.sin(2 * np.pi * frecuencia_gen1 * tiempo)

frecuencia_gen2 = 1  # Hz
amplitud_gen2 = 1    # Vp
senal_malla2 = amplitud_gen2 * np.sin(2 * np.pi * frecuencia_gen2 * tiempo)

# Simulación de la respuesta con control PID
sys_control = ctrl.feedback(ctrl.series(pid, sysT), 1)
_, y_control = ctrl.forced_response(sys_control, tiempo, senal_malla2)

# Gráficas ORIGINALES (como las tenías)
plt.figure(figsize=(12, 6))
plt.plot(tiempo, senal_malla1, label='Control:Normotenso', color=Azul)
plt.plot(tiempo, senal_malla2, label='Caso:Taquicardia', color=Amarillo)
plt.plot(tiempo, y_control, label='Taquicardia con PID', color=Morado, linestyle='--')

plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(False)
plt.legend(bbox_to_anchor=(0.5,-0.23), loc='center', ncol=3)
plt.tight_layout()
plt.show()