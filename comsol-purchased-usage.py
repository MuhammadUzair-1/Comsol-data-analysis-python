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

# Usage data extracted from the Excel file
usage_data = [
    75, 25, 5, 7, 5, 14, 7, 1, 4, 25, 1, 1, 2, 0, 1, 1, 3, 9, 1, 0,
    3, 2, 9, 2, 0, 1, 0, 0, 25, 5, 0, 1, 1, 1, 3, 5, 7, 3, 1, 5,
    2, 1, 2, 7, 0, 4, 25, 5, 1, 7
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
for i, (module, quantity, usage, price) in enumerate(zip(modules, quantities, usage_data, unit_prices)):
    if price not in price_groups:
        price_groups[price] = []
    price_groups[price].append((module, quantity, usage, i))

# Sort by unit price (descending)
sorted_prices = sorted(price_groups.keys(), reverse=True)

# Create lists for plotting, grouped by price
grouped_modules = []
grouped_quantities = []
grouped_usage = []
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
    for module, quantity, usage, orig_idx in group:
        grouped_modules.append(module)
        grouped_quantities.append(quantity)
        grouped_usage.append(usage)
        grouped_colors.append(color_map[price])
        x_positions.append(current_x)
        x_tick_labels.append(module)
        current_x += 1
    current_x += 1  # Add gap between groups

# Create the plot with two bars for each module
plt.figure(figsize=(24, 10))
bar_width = 0.35

# Create bars for available licenses
bars1 = plt.bar([x - bar_width/2 for x in x_positions], grouped_quantities,
                width=bar_width, color=grouped_colors, edgecolor='black',
                linewidth=0.5, alpha=0.7, label='Available Licenses')

# Create bars for usage data
bars2 = plt.bar([x + bar_width/2 for x in x_positions], grouped_usage,
                width=bar_width, color='lightgray', edgecolor='black',
                linewidth=0.5, alpha=0.9, label='Maximum Usage')

# Add value labels on top of bars
for i, (x, q, u) in enumerate(zip(x_positions, grouped_quantities, grouped_usage)):
    plt.text(x - bar_width/2, q + 0.5, str(q), ha='center', va='bottom', fontsize=8, rotation=90)
    plt.text(x + bar_width/2, u + 0.5, str(u), ha='center', va='bottom', fontsize=8, rotation=90)

# Customize the plot
plt.title('COMSOL FNL Modules: Available Licenses vs Maximum Usage (Grouped by Unit Price)', fontsize=16, pad=20)
plt.xlabel('Modules (Grouped by Unit Price)', fontsize=12)
plt.ylabel('Number of Licenses', fontsize=12)

# Set x-ticks and rotate labels for better readability
plt.xticks(x_positions, x_tick_labels, rotation=90, fontsize=8)
plt.tick_params(axis='x', which='major', labelsize=7)

# Add grid for better readability
plt.grid(axis='y', alpha=0.3)

# Create legend for unit prices
legend_elements = [plt.Rectangle((0,0),1,1, color=color_map[price], label=f'€{price}')
                  for price in sorted_prices]
plt.legend(handles=legend_elements + [bars1[0], bars2[0]],
           title='Unit Price & Data Type', title_fontsize=11, fontsize=10,
           loc='upper right', bbox_to_anchor=(1.15, 1))

# Adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()