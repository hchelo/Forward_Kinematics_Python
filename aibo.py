import sympy as sp

# Definir variables simbólicas
th1, th2, th3, L1, L2 = sp.symbols('th1 th2 th3 L1 L2')

# Definir las matrices de transformación
Ry1 = sp.Matrix([
    [sp.cos(-th1), 0, sp.sin(-th1), 0],
    [0, 1, 0, 0],
    [-sp.sin(-th1), 0, sp.cos(-th1), 0],
    [0, 0, 0, 1]
])

Rx1 = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.cos(th2), -sp.sin(th2), 0],
    [0, sp.sin(th2), sp.cos(th2), 0],
    [0, 0, 0, 1]
])

Tz1 = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -L1],
    [0, 0, 0, 1]
])

Ry2 = sp.Matrix([
    [sp.cos(-th3), 0, sp.sin(-th3), 0],
    [0, 1, 0, 0],
    [-sp.sin(-th3), 0, sp.cos(-th3), 0],
    [0, 0, 0, 1]
])

Tz2 = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -L2],
    [0, 0, 0, 1]
])

# Calcular la matriz M
M = Ry1 * Rx1 * Tz1 * Ry2 * Tz2

# Simplificar la matriz M multiplicada por el vector [0, 0, 0, 1]
M_simplified = sp.simplify(M * sp.Matrix([0, 0, 0, 1]))

# Mostrar la matriz simplificada
#print("M simplificada:")
#sp.pprint(M_simplified)

# Extraer los valores de x, y, z
x = M_simplified[0]  # Cambiar de notación de paréntesis a corchetes
y = M_simplified[1]
z = M_simplified[2]

# Mostrar valores de x, y, z
print("x:", x)
print("y:", y)
print("z:", z)


# Sustituir valores numéricos
M_numeric = M_simplified.subs({th1: 0, th2: 0, th3: 0, L1: 1, L2: 1})

# Extraer los valores de x, y, z
x = M_numeric[0]
y = M_numeric[1]
z = M_numeric[2]

# Mostrar valores numéricos de x, y, z
print("x:", x)
print("y:", y)
print("z:", z)