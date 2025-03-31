import pyvista as pv
from numba import jit
import numpy as np

delta_h = 1

delta_t = 0.1


intended_t = 1

t = 0

mesh = pv.read("./pan.obj")

voxelSpace = pv.voxelize(mesh,density=mesh.length / 200,check_surface=False)

voxelSpace["temperature"] = np.random.randint(10,1000,size=voxelSpace.n_cells)

#voxelSpace["temperature"] = np.full(voxelSpace.n_cells,97)

voxelSpace["conductivity"] = np.full(voxelSpace.n_cells,97)

# Get the center points of each cell
cell_centers = voxelSpace.cell_centers().points

# Extract y-coordinates of the cell centers
y_coords = cell_centers[:, 1]

# Find the minimum y-coordinate
min_y = np.min(y_coords)

# Get indices of cells that are at the minimum y level
lowest_cells = np.where(y_coords == min_y)[0]



p1 = pv.Plotter(off_screen=True)


p1.add_volume(voxelSpace,opacity=0.2,show_scalar_bar="temperature",cmap="viridis")

p1.open_gif("simulation.gif")

print(voxelSpace.n_cells)


# Precompute neighbor indices for all cells (store in a list of lists)
neighbor_indices = [voxelSpace.cell_neighbors(cell_id) for cell_id in range(voxelSpace.n_cells)]

# Vectorized heat equation solver
@jit
def heat_equation_sim(t):
    while t <= intended_t:

        #Boundary Conditions
        voxelSpace.extract_cells(lowest_cells)["temperature"] = 600

        # Get current temperature field
        temperature = voxelSpace.cell_data['temperature']
        
        neighbor_means = np.zeros_like(temperature)  # Initialize output array

        neighbor_means = np.array([
            np.mean(temperature[neighbors]) if len(neighbors) > 0 else temperature[cell_id]
            for cell_id, neighbors in enumerate(neighbor_indices)
        ])


        print (neighbor_indices)
        print (neighbor_means)
        # Compute the temperature update (vectorized operation)

        voxelSpace['temperature'] == temperature + voxelSpace.cell_data["conductivity"] * delta_t * (neighbor_means - temperature)



        t += delta_t
        p1.write_frame()
        print(t)

heat_equation_sim(t)
p1.close()





    # t_f = np.pad(voxelSpace["temprature"],pad_width=1,mode="edge")

    # t_f = cell_scalars.reshape((nx - 1, ny - 1, nz - 1))



    # voxelSpace["temprature"] += (
    #     (
    #         (t_f[2:, 1:-1, 1:-1] - 2 * t_f[1:-1, 1:-1, 1:-1] + t_f[:-2, 1:-1, 1:-1]) +
    #         (t_f[1:-1, 2:, 1:-1] - 2 * t_f[1:-1, 1:-1, 1:-1] + t_f[1:-1, :-2, 1:-1]) +
    #         (t_f[1:-1, 1:-1, 2:] - 2 * t_f[1:-1, 1:-1, 1:-1] + t_f[1:-1, 1:-1, :-2])
    #     ) * voxelSpace["conductivity"]
    # ) * (delta_t)
    