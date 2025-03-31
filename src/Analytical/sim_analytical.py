import numpy as np
import plotly.graph_objects as go
import sympy
from sympy import symbols, exp, sqrt, pi, erfc
import scipy.special

x, y, z, t, xi, yi, zi, tau = sp.symbols('x y z t xi yi zi tau', real=True)

a = 96

# Define the piecewise temperature function T(x, y, z, t)
T = sp.Piecewise(
    (1200, (z == 0) & (t >= 0)),  # Bottom boundary (z = 0)
    (300, ((x == 0) | (x == L) | (y == 0) | (y == W) | (z == H)) & (t >= 0)),  # Other boundaries
    (300, (t == 0) & (x > 0) & (x < L) & (y > 0) & (y < W) & (z > 0) & (z < H))  # Interior at t = 0
)

H = (
    1200 * (sqrt(t/(pi*a)) * exp(-z**2/(4*a*t)) + (z/(2*a)) * erfc(z/(2*sqrt(a*t)))) 
    + 300 * (sqrt(t/(pi*a)) * exp(-x**2/(4*a*t)) + (x/(2*a)) * erfc(x/(2*sqrt(a*t)))) 
    + 300 * (sqrt(t/(pi*a)) * exp(-y**2/(4*a*t)) + (y/(2*a)) * erfc(y/(2*sqrt(a*t))))
)

H_numpy = sympy.lambdify(
    (x, y, z, t), 
    H, 
    modules=[{"erfc": lambda x: np.sqrt(2) * scipy.special.erfc(x)}, "numpy"]
)


X,Y,Z = np.meshgrid(np.arange(0,20,1),np.arange(0,20,1),np.arange(0,20,1))


fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=H_numpy(X,Y,Z,100).flatten(),
    opacity=0.2,
    surface_count= 25,
))

fig.show()