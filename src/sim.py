import numpy as np
import plotly.graph_objects as go
import sympy


delta_h = 1


delta_t = 0.0015


intended_t = 100

t = 0


X,Y,Z = np.meshgrid(np.arange(0,50,1),np.arange(0,50,1),np.arange(0,50,1))


t_field = np.full_like(X,600,dtype=np.float32)

alpha_field = np.full_like(X,96,dtype=np.float32) # Thermal diffusivty of Alluminium



while t <= intended_t:

    # Padding = boundary conditions
    t_f = np.pad(
        t_field,
        pad_width=((1, 1), (1, 1), (1, 1)),
        mode='constant',
        constant_values= 0
    )
    t_f[0, :, :] = 300  # Top face Room temp
    t_f[-1, :, :] = 300  # Bottom face Stove
    t_f[:, 0, :] = 1200  # Front face
    t_f[:, -1, :] = 300  # Back face
    t_f[:, :, 0] = 300 # Left face
    t_f[:, :, -1] = 300  # Right face

    t_field += (
        (
            (t_f[2:, 1:-1, 1:-1] - 2 * t_f[1:-1, 1:-1, 1:-1] + t_f[:-2, 1:-1, 1:-1]) +
            (t_f[1:-1, 2:, 1:-1] - 2 * t_f[1:-1, 1:-1, 1:-1] + t_f[1:-1, :-2, 1:-1]) +
            (t_f[1:-1, 1:-1, 2:] - 2 * t_f[1:-1, 1:-1, 1:-1] + t_f[1:-1, 1:-1, :-2])
        ) * alpha_field
    ) * (delta_t / delta_h**2)
    
    t += delta_t
    print(t)
        


fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=t_field.flatten(),
    opacity=0.2,
    surface_count= 25,
))

fig.show()
