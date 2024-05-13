import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from plyfile import PlyData

def load_ply(filepath):
    """
    Load points from a PLY file.

    Parameters:
        filepath (str): The path to the PLY file.

    Returns:
        numpy.ndarray: An array of shape (n, 3) containing the x, y, z coordinates of the points.
    """
    plydata = PlyData.read(filepath)
    data = plydata['vertex']
    points = np.c_[data['x'], data['y'], data['z']]  # Combine x, y, z into a single array
    return points

def load_xyz(filepath):
    """
    Load points from an XYZ file.

    Parameters:
        filepath (str): The path to the XYZ file.

    Returns:
        numpy.ndarray: An array of shape (n, 3) containing the x, y, z coordinates of the points.
    """
    points = []
    with open(filepath, 'r') as file:
        for line in file:
            x, y, z = line.split()
            points.append([float(x), float(y), float(z)])
    return np.array(points)

def plot_point_cloud(points):
    """
    Plot a 3D point cloud.

    Parameters:
        points (numpy.ndarray): An array of shape (n, 3) containing the x, y, z coordinates of the points.

    Returns:
        None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1, c='b')  # Plot each point

    # Hide the axes
    ax.set_axis_off()

    # Optionally, you might want to set the limits to equal to ensure the point cloud isn't distorted
    max_range = np.array([points[:, 0].max()-points[:, 0].min(),
                          points[:, 1].max()-points[:, 1].min(),
                          points[:, 2].max()-points[:, 2].min()]).max() / 2.0
    mid_x = (points[:, 0].max()+points[:, 0].min()) * 0.5
    mid_y = (points[:, 1].max()+points[:, 1].min()) * 0.5
    mid_z = (points[:, 2].max()+points[:, 2].min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    plt.savefig('pointcloud.png')
# Load your PLY file
"""
Pass the name of the file you want to generate a pointcloud of here.
"""
points = load_ply('YCB40/cellphone_poisson_008/test/cellphone_poisson_008__10_4_10_y.ply')

# Plot the loaded point cloud
plot_point_cloud(points)
