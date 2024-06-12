import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

def load_csv_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def plot_3d_data(file_path):
    x_data = []
    y_data = []
    z_data = []
    
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        next(csv_reader)  # Skip "X Y Z" row
        for row in csv_reader:
            x_data.append(float(row[0]))  # Extract X value
            y_data.append(float(row[1]))  # Extract Y value
            z_data.append(float(row[2]))  # Extract Z value

    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the data
    ax.scatter(x_data, y_data, z_data, c='r', marker='o')
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Set plot title
    plt.title('3D Data Visualization')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    file_path = load_csv_file()
    if file_path:
        plot_3d_data(file_path)
    else:
        print("No file selected.")
