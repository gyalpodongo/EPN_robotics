import matplotlib.pyplot as plt
import pickle

"""
This script creates a plot to visualize the accuracies of a model for each category in the YCB40 dataset.

The script reads the accuracies from a pickle file specified by the 'catFile' variable. The pickle file contains
a dictionary where the keys are the category names and the values are lists of accuracies.

The 'name_format' dictionary is used to format the category names from the YCB40 dataset to make them more readable.
If a category name is found in the 'name_format' dictionary, the corresponding formatted name is used; otherwise, the
original category name is used.

The script sorts the data by accuracy in descending order and creates a horizontal bar plot using Matplotlib. Each bar
represents a category, and the length of the bar represents the accuracy percentage. The bars are color-coded based on
the accuracy range: red for accuracy above 90%, yellow for accuracy between 80% and 90%, and blue for accuracy below 80%.

The plot includes labels for the categories and accuracy percentages, as well as an x-axis label, y-axis label, and a
title displaying the average accuracy score. The x-axis limit is set to accommodate 100% bars, and the y-axis limit is
adjusted based on the number of categories.

The plot is customized with adjusted figure size, plot margins, and x-axis grid lines. Finally, the plot is saved as
a PNG file named 'accuracy_plot.png' with a resolution of 300 DPI.
"""

# Data: list of tuples (category, accuracy)

name_format = {
"banana_poisson_002": "Banana",
"binder_poisson_004": "Binder",
"black_and_decker_lithium_drill_driver": "Drill driver",
"boltcutter_poisson_000": "Boltcutter",
"book_poisson_000": "Book",
"box_poisson_019": "Box1",
"box_poisson_020": "Box2",
"box_poisson_021": "Box3",
"box_poisson_022": "Box4",
"box_poisson_023": "Box5",
"box_poisson_026": "Box6",
"brine_mini_soccer_ball": "Soccer ball",
"campbells_condensed_tomato_soup": "Tomato soup",
"can_poisson_002": "Can1",
"can_poisson_009": "Can2",
"cellphone_poisson_008": "Cellphone1",
"cellphone_poisson_013": "Cellphone2",
"clorox_disinfecting_wipes_35": "Disinfecting wipes",
"comet_lemon_fresh_bleach": "Bleach",
"detergent_bottle_poisson_004": "Detergent bottle",
"domino_sugar_1lb": "Sugar",
"donut_poisson_006": "Donut",
"flashlight_poisson_002": "Flashlight",
"frenchs_classic_yellow_mustard_14oz": "Mustard",
"jar_poisson_001": "Jar1",
"jar_poisson_006": "Jar2",
"knife_poisson_004": "Knife1",
"knife_poisson_011": "Knife2",
"knife_poisson_019": "Knife3",
"light_bulb_poisson_001": "Light bulb",
"lime_poisson_001": "Lime",
"melissa_doug_farm_fresh_fruit_lemon": "Lemon",
"morton_salt_shaker": "Salt shaker",
"mushroom_poisson_005": "Mushroom",
"play_go_rainbow_stakin_cups_1_yellow": "Stacking cup",
"pliers_poisson_015": "Pliers",
"pringles_original": "Pringles",
"remote_poisson_006": "Remote1",
"remote_poisson_008": "Remote2",
"remote_poisson_009": "Remote3"
}

catFile = 'cataccs.pkl' #Use this to select pickle file with all the categories with their respective accuracies

with open(catFile, 'rb') as f:
    cataccs = pickle.load(f)
data = [(name_format.get(cat, cat), accs[0]) for cat,accs in cataccs.items()] 
# data = [(cat, accs[0]) for cat,accs in cataccs.items()]


# Sorting data by accuracy
data.sort(key=lambda x: x[1], reverse=True)

# Separating labels and values
categories, accuracies = zip(*data)

# Creating the bar plot
plt.figure(figsize=(12, 10))  # Increased figure size
plt.barh(categories, accuracies, color=['red' if x > 90 else 'yellow' if x > 80 else 'blue' for x in accuracies], height=0.7)
plt.ylabel('Categories', fontweight='bold', fontsize=14)
plt.xlabel('Attention Confidence Predict Accuracy (%)', fontweight='bold', fontsize=14)
plt.title('Average Accuracy Score: 89.74%', fontweight='bold', fontsize=16)
plt.xlim(0, 105)  # Increased x-axis limit to accommodate 100% bars
plt.ylim(-0.5, len(categories) - 0.5)

# Adding data labels
for i, v in enumerate(accuracies):
    plt.text(v + 0.5, i, f'{v:.0f}%', va='center', fontsize=12)

# Adjusting layout and spacing
plt.subplots_adjust(left=0.3, right=0.98, top=0.95, bottom=0.08)  # Adjusted plot margins
plt.grid(axis='x', alpha=0.3)  # Added x-axis grid lines

# Saving the plot
plt.savefig('accuracy_plot.png', format='png', dpi=300, bbox_inches='tight')
plt.show()