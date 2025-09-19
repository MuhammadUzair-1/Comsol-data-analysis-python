import matplotlib.pyplot as plt
import numpy as np

# Data extracted from the document for FNL modules (positions 1-50)
modules = [
    "COMSOL Multiphysics", "AC/DC Module", "Acoustics Module",
    "Battery Design Module", "CAD Import Module", "CFD Module",
    "Chemical Reaction Engineering Module", "Composite Materials Module",
    "Corrosion Module", "Design Module", "ECAD Import Module",
    "Electric Discharge Module", "Electrochemistry Module",
    "Electrodeposition Module", "Fatigue Module",
    "Fuel Cell & Electrolyzer Module", "Geomechanics Module",
    "Heat Transfer Module", "Liquid & Gas Properties Module",
    "LiveLink for AutoCAD", "LiveLink for Excel", "LiveLink for Inventor",
    "LiveLink for MATLAB", "LiveLink for PTC Creo Parametric",
    "LiveLink for Revit", "LiveLink for Simulink", "LiveLink for Solid Edge",
    "LiveLink for SOLIDWORKS", "Material Library", "MEMS Module",
    "Metal Processing Module", "Microfluidics Module", "Mixer Module",
    "Molecular Flow Module", "Multibody Dynamics Module",
    "Nonlinear Structural Materials Module", "Optimization Module",
    "Particle Tracing Module", "Pipe Flow Module", "Plasma Module",
    "Polymer Flow Module", "Porous Media Flow Module", "Ray Optics Module",
    "RF Module", "Rotordynamics Module", "Semiconductor Module",
    "Structural Mechanics Module", "Subsurface Flow Module",
    "Uncertainty Quantification Module", "Wave Optics Module"
]

quantities = [
    75, 25, 25, 12, 5, 25, 12, 5, 12, 25, 5, 12, 5, 5, 5, 12, 5, 25, 5, 5,
    25, 12, 25, 5, 5, 5, 5, 5, 25, 12, 5, 12, 5, 5, 12, 25, 25, 25, 5, 12,
    5, 5, 12, 25, 5, 5, 25, 12, 5, 25
]

unit_prices = [
    197.00, 88.00, 88.00, 197.00, 41.00, 197.00, 88.00, 88.00, 88.00, 88.00,
    88.00, 197.00, 88.00, 88.00, 88.00, 197.00, 88.00, 88.00, 88.00, 88.00,
    25.00, 88.00, 42.00, 88.00, 88.00, 88.00, 88.00, 88.00, 42.00, 88.00,
    88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 197.00,
    88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00, 88.00
]

# Group modules by unit price
price_groups = {}
for i, (module, quantity, price) in enumerate(zip(modules, quantities, unit_prices)):
    if price not in price_groups:
        price_groups[price] = []
    price_groups[price].append((module, quantity, i))

# Sort by unit price (descending)
sorted_prices = sorted(price_groups.keys(), reverse=True)

# Create lists for plotting, grouped by price
grouped_modules = []
grouped_quantities = []
grouped_colors = []
color_map = {
    197.00: '#1f77b4',  # blue
    88.00: '#ff7f0e',   # orange
    42.00: '#2ca02c',   # green
    41.00: '#d62728',   # red
    25.00: '#9467bd'    # purple
}

x_positions = []
x_tick_labels = []
current_x = 0

for price in sorted_prices:
    group = sorted(price_groups[price], key=lambda x: x[1], reverse=True)  # Sort by quantity
    for module, quantity, orig_idx in group:
        grouped_modules.append(module)
        grouped_quantities.append(quantity)
        grouped_colors.append(color_map[price])
        x_positions.append(current_x)
        x_tick_labels.append(module)
        current_x += 1
    current_x += 1  # Add gap between groups

# Create the plot
plt.figure(figsize=(20, 10))
bars = plt.bar(x_positions, grouped_quantities, color=grouped_colors, edgecolor='black', linewidth=0.5)

# Add value labels on top of bars
for i, (x, q) in enumerate(zip(x_positions, grouped_quantities)):
    plt.text(x, q + 0.5, str(q), ha='center', va='bottom', fontsize=9, rotation=90)

# Customize the plot
plt.title('COMSOL FNL Modules: Number of Purchased Licenses by Unit Price', fontsize=16, pad=20)
plt.xlabel('Modules (Grouped by Unit Price)', fontsize=12)
plt.ylabel('Number of Licenses', fontsize=12)

# Set x-ticks and rotate labels for better readability
plt.xticks(x_positions, x_tick_labels, rotation=90, fontsize=9)
plt.tick_params(axis='x', which='major', labelsize=8)

# Add grid for better readability
plt.grid(axis='y', alpha=0.3)

# Create legend for unit prices
legend_elements = [plt.Rectangle((0,0),1,1, color=color_map[price], label=f'€{price}')
                  for price in sorted_prices]
plt.legend(handles=legend_elements, title='Unit Price', title_fontsize=12, fontsize=11,
           loc='upper right', bbox_to_anchor=(1.15, 1))

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()