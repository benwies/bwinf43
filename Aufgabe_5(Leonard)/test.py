import math

# Gegebene Werte
m = 0.03  # Masse in kg
g = 9.81  # Erdbeschleunigung in m/s^2
Q = 150e-9  # Ladung in C
theta_deg = 1  # Winkel in Grad

# Gravitationskraft
F_g = m * g

# Winkel in Radiant umrechnen
theta_rad = math.radians(theta_deg)

# Verhältnis der Kräfte
F_E = F_g * math.tan(theta_rad)

# Berechnung der elektrischen Feldstärke
E = F_E / Q

F_g, F_E, E
print(E)