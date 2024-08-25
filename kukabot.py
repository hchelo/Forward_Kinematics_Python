import numpy as np

# Convertir ángulos de grados a radianes
th1 = np.radians(-45)
th2 = np.radians(-135)
th3 = np.radians(90)
th4 = np.radians(0)
th5 = np.radians(0)
th6 = np.radians(0)

# Definir una función para generar la matriz de transformación homogénea a partir de los parámetros DH
def dh_transform(theta, d, a, alpha):
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha),  np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta),  np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0,             np.sin(alpha),                 np.cos(alpha),                  d],
        [0,             0,                             0,                              1]
    ])

# Definir los parámetros DH para cada eslabón [θ, d, a, α]
DH_params = [
    [th1, 0, 0, -np.pi/2],   # L0
    [th2, 0, 0.455, 0],      # L1
    [th3, 0, 0.420, 0],      # L2
    [th4, 0, 0, -np.pi/2],     # L3
    [th5, 0, 0, -np.pi/2],     # L4
    [th6, 0, 0.08, 0]          # L5
]

# Inicializar la matriz de transformación total como una matriz identidad 4x4
T = np.eye(4)

# Calcular la matriz de transformación total multiplicando las matrices de cada eslabón
for params in DH_params:
    T = np.dot(T, dh_transform(*params))

# Redondear los elementos de la matriz T a 4 decimales
T_rounded = np.round(T, decimals=4)

# Mostrar la matriz de transformación homogénea resultante con valores redondeados
print("Matriz de transformación homogénea (T) con valores redondeados:")
print(T_rounded)

# Calcular la posición final del efector en el espacio (asumiendo que el punto final es [0, 0, 0, 1] en coordenadas homogéneas)
end_effector_position = np.dot(T, np.array([0, 0, 0, 1]))

# Extraer los valores de x, y, z
x = end_effector_position[0]
y = end_effector_position[1]
z = end_effector_position[2]

# Mostrar valores numéricos de x, y, z
print("x:", x)
print("y:", y)
print("z:", z)
