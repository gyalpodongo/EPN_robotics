import matplotlib.pyplot as plt
import pickle

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