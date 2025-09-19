import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data extracted from your PDF
data = {
    'Module': [
        'COMSOL Multiphysics', 'AC/DC Module', 'Acoustics Module', 'Battery Design Module',
        'CAD Import Module', 'CFD Module', 'Chemical Reaction Engineering Module', 'Composite Materials Module',
        'Corrosion Module', 'Design Module', 'ECAD Import Module', 'Electric Discharge Module',
        'Electrochemistry Module', 'Electrodeposition Module', 'Fatigue Module', 'Fuel Cell & Electrolyzer Module',
        'Geomechanics Module', 'Heat Transfer Module', 'Liquid & Gas Properties Module', 'LiveLink for AutoCAD',
        'LiveLink for Excel', 'LiveLink for Inventor', 'LiveLink for MATLAB', 'LiveLink for PTC Creo Parametric',
        'LiveLink for Revit', 'LiveLink for Simulink', 'LiveLink for Solid Edge', 'LiveLink for SOLIDWORKS',
        'Material Library', 'MEMS Module', 'Metal Processing Module', 'Microfluidics Module', 'Mixer Module',
        'Molecular Flow Module', 'Multibody Dynamics Module', 'Nonlinear Structural Materials Module', 'Optimization Module',
        'Particle Tracing Module', 'Pipe Flow Module', 'Plasma Module', 'Polymer Flow Module', 'Porous Media Flow Module',
        'Ray Optics Module', 'RF Module', 'Rotordynamics Module', 'Semiconductor Module', 'Structural Mechanics Module',
        'Subsurface Flow Module', 'Uncertainty Quantification Module', 'Wave Optics Module'
    ],
    'Unit_Price': [
        197.00, 88.00, 88.00, 197.00, 41.00, 197.00, 88.00, 88.00, 88.00, 88.00, 88.00, 197.00,
        88.00, 88.00, 88.00, 197.00, 88.00, 88.00, 88.00, 88.00, 25.00, 88.00, 42.00, 88.00,
        88.00, 88.00, 88.00, 88.00, 42.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00,
        88.00, 88.00, 88.00, 197.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00,
        88.00, 88.00
    ]
}

df = pd.DataFrame(data)

# Sort by price in descending order (highest first, left side)
df_sorted = df.sort_values(by=['Unit_Price', 'Module'], ascending=[False, True])

# Create a color map with brighter colors
unique_prices = df_sorted['Unit_Price'].unique()
# Using a bright colormap - 'viridis' or 'plasma' would also work well
colors = plt.cm.tab10(np.linspace(0, 1, len(unique_prices)))
price_to_color = dict(zip(unique_prices, colors))

# Assign a color to each bar
bar_colors = [price_to_color[price] for price in df_sorted['Unit_Price']]

# Create the plot with vertical bars
plt.figure(figsize=(20, 10))
bars = plt.bar(range(len(df_sorted)), df_sorted['Unit_Price'], color=bar_colors)
plt.ylabel('Unit Price (€)', fontsize=12)
plt.xlabel('FNL Modules', fontsize=12)
plt.title('FNL Licenses Grouped by Unit Price (Highest to Lowest)', fontsize=14)

# Set x-axis labels as module names, rotated for better readability
plt.xticks(range(len(df_sorted)), df_sorted['Module'], rotation=90, ha='right')
plt.tick_params(axis='x', which='major', labelsize=8)

# Create a legend for the prices
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=price_to_color[price], label=f'€{price:.2f}') for price in sorted(unique_prices, reverse=True)]
plt.legend(handles=legend_elements, title='Unit Prices', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add value labels on top of each bar
for i, (price, module) in enumerate(zip(df_sorted['Unit_Price'], df_sorted['Module'])):
    plt.text(i, price + 1, f'€{price}', ha='center', va='bottom', fontsize=8, rotation=90)

# Adjust layout to prevent cutting off labels
plt.tight_layout()
plt.show()