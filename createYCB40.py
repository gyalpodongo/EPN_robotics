import os
import numpy as np
from scipy.io import savemat
from scipy.spatial.transform import Rotation
import random

"""
This script processes a dataset of XYZ files and converts them into PLY and MAT files in a specified folder structure.

The input folder should have the following structure:
folder/object/object_number.xyz

The script creates a new folder structure with the following format:
newfolder/object/train (containing .ply and .mat files)
newfolder/object/test (containing .ply and .mat files)
newfolder/object/testR (containing only .mat files with assigned rotation angles)

The script randomly splits the files for each object into train (80%) and test (20%) sets.
The testR folder contains the same files as the test folder but with an assigned rotation matrix in the .mat files.

Note: The script is currently set to process a maximum of 40 objects (MAX_OBJECTS) due to model constraints.
      The point clouds are also reduced by a factor of 4 (vertices[::4]) to accommodate GPU constraints.
      To change the number of points per object, modify the vertices[::4] line.

Input:
    input_folder: The path to the input folder containing the XYZ files.
    output_folder: The path to the output folder where the new folder structure will be created.

Usage:
    Specify the input_folder and output_folder paths in the script and run it.
    The script will process the XYZ files and create the new folder structure with PLY and MAT files.
"""

MAX_OBJECTS = 40
def generate_random_rotation_matrix():
    """
    Generate a random rotation matrix.

    Returns:
        R: A random rotatio    """
    # Generate random rotation angles (in radians)
    angles = np.random.uniform(0, 2*np.pi, size=3)
    
    # Create rotation matrices for each axis
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(angles[0]), -np.sin(angles[0])],
                   [0, np.sin(angles[0]), np.cos(angles[0])]])
    
    Ry = np.array([[np.cos(angles[1]), 0, np.sin(angles[1])],
                   [0, 1, 0],
                   [-np.sin(angles[1]), 0, np.cos(angles[1])]])
    
    Rz = np.array([[np.cos(angles[2]), -np.sin(angles[2]), 0],
                   [np.sin(angles[2]), np.cos(angles[2]), 0],
                   [0, 0, 1]])
    
    # Combine the rotation matrices
    R = Rz @ Ry @ Rx
    
    return R

def convert_xyz_to_ply_and_mat(xyz_file, ply_file, mat_file, object_name, object_id, rotated_mat_file=None):
    """
    Convert an XYZ file to PLY and MAT files.

    Args:
        xyz_file: The path to the input XYZ file.
        ply_file: The path to the output PLY file.
        mat_file: The path to the output MAT file.
        object_name: The name of the object.
        object_id: The ID of the object.
        rotated_mat_file: The path to the output rotated MAT file (optional).
    """
    # Read the .xyz file
    points = np.loadtxt(xyz_file)

    # Extract the coordinates
    x = points[:, 0]
    y = points[:, 1]
    z = points[:, 2]

    # Create the vertex array for PLY
    vertices = np.column_stack((x, y, z))[::4]

    # Assign default colors for PLY (you can modify this if needed)
    colors = np.full((len(vertices), 3), [255, 255, 255])

    # Define the PLY header
    ply_header = [
        "ply",
        "format ascii 1.0",
        f"element vertex {len(vertices)}",
        "property float x",
        "property float y",
        "property float z",
        "property uchar red",
        "property uchar green",
        "property uchar blue",
        "end_header"
    ]

    # Save the PLY file
    with open(ply_file, 'w') as file:
        file.write('\n'.join(ply_header) + '\n')
        for vertex, color in zip(vertices, colors):
            file.write(f"{vertex[0]} {vertex[1]} {vertex[2]} {color[0]} {color[1]} {color[2]}\n")

    # Create a dictionary to store the data for MAT
    file_id = os.path.splitext(os.path.basename(xyz_file))[0]

    # Create a dictionary to store the data for MAT
    data_dict = {
        '__header__': 'MATLAB 5.0 MAT-file Platform: posix, Created on: Wed May 08 03:57:13 2024',
        '__version__': '1.0',
        '__globals__': [],
        'pc': vertices,
        'name': np.array([object_name + "_" + file_id]),
        'label': np.array([[object_id]]),
        'cat': np.array([object_name])
    }

    # Save the data as a .mat file
    savemat(mat_file, data_dict)

    if rotated_mat_file is not None:
        # Generate a random rotation matrix
        R = generate_random_rotation_matrix()
        # Apply the rotation to the reduced coordinates
        # Create a dictionary to store the data for the rotated MAT file
        rotated_data_dict = {
            '__header__': 'MATLAB 5.0 MAT-file Platform: posix, Created on: Wed May 08 03:57:13 2024',
            '__version__': '1.0',
            '__globals__': [],
            'pc': vertices,
            'name': np.array([object_name + "_" + file_id]),
            'label': np.array([[object_id]]),
            'cat': np.array([object_name]),
            'R': R
        }

        # Save the rotated data as a .mat file
        savemat(rotated_mat_file, rotated_data_dict)

def process_files(input_folder, output_folder):
    """
    Process the XYZ files in the input folder and create the new folder structure with PLY and MAT files.

    Args:
        input_folder: The path to the input folder containing the XYZ files.
        output_folder: The path to the output folder where the new folder structure will be created.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize object ID counter
    object_id = 0

    # Iterate over the object folders
    for object_folder in os.listdir(input_folder):
        if object_id >= MAX_OBJECTS:
            break 
        object_path = os.path.join(input_folder, object_folder)
        if os.path.isdir(object_path):
            # Create the object folder in the output directory
            output_object_folder = os.path.join(output_folder, object_folder)
            os.makedirs(output_object_folder, exist_ok=True)

            # Create the train folder in the output object folder
            output_train_folder = os.path.join(output_object_folder, "train")
            os.makedirs(output_train_folder, exist_ok=True)

            # Create the test folder in the output object folder
            output_test_folder = os.path.join(output_object_folder, "test")
            os.makedirs(output_test_folder, exist_ok=True)

            # Create the testR folder in the output object folder
            output_testR_folder = os.path.join(output_object_folder, "testR")
            os.makedirs(output_testR_folder, exist_ok=True)

            # Iterate over the test folders
            test_folder = os.path.join(object_path, "test")
            if os.path.isdir(test_folder):
                # Get a list of .xyz files in the test folder
                xyz_files = [file for file in os.listdir(test_folder) if file.endswith(".xyz")]
                
                # Shuffle the list of files randomly
                random.shuffle(xyz_files)
                
                # Calculate the split index
                split_index = int(len(xyz_files) * 0.8)
                
                # Split the files into train and test sets
                train_files = xyz_files[:split_index]
                test_files = xyz_files[split_index:]
                
                # Process train files
                for xyz_file in train_files:
                    xyz_path = os.path.join(test_folder, xyz_file)
                    file_id = os.path.splitext(xyz_file)[0]
                    ply_file = os.path.join(output_train_folder, f"{object_folder}_{file_id}.ply")
                    mat_file = os.path.join(output_train_folder, f"{object_folder}_{file_id}.mat")
                    convert_xyz_to_ply_and_mat(xyz_path, ply_file, mat_file, object_folder, object_id)
                
                # Process test files
                for xyz_file in test_files:
                    xyz_path = os.path.join(test_folder, xyz_file)
                    file_id = os.path.splitext(xyz_file)[0]
                    ply_file = os.path.join(output_test_folder, f"{object_folder}_{file_id}.ply")
                    mat_file = os.path.join(output_test_folder, f"{object_folder}_{file_id}.mat")
                    rotated_mat_file = os.path.join(output_testR_folder, f"{object_folder}_{file_id}.mat")
                    convert_xyz_to_ply_and_mat(xyz_path, ply_file, mat_file, object_folder, object_id, rotated_mat_file)

            # Increment object ID for the next object
            object_id += 1


# Specify the input and output folders
input_folder = "3dsgrasp_ycb_train_test_split/gt"
output_folder = "YCB40"

# Process the files
process_files(input_folder, output_folder)