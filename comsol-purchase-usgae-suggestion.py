import matplotlib.pyplot as plt
import numpy as np

# Data
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

usage_data = [
    75, 25, 5, 7, 5, 14, 7, 1, 4, 25, 1, 1, 2, 0, 1, 1, 3, 9, 1, 0,
    3, 2, 9, 2, 0, 1, 0, 0, 25, 5, 0, 1, 1, 1, 3, 5, 7, 3, 1, 5,
    2, 1, 2, 7, 0, 4, 25, 5, 1, 7
]

suggested_purchase = [
    100, 15, 12, 12, 15, 15, 12, 5, 12, 15, 5, 12, 5, 5, 5, 12, 5, 12, 5, 5,
    12, 12, 12, 5, 5, 5, 5, 5, 15, 12, 5, 5, 5, 5, 5, 12, 12, 12, 5, 12,
    5, 5, 10, 15, 5, 5, 15, 12, 5, 12
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
for i, (module, quantity, usage, suggested, price) in enumerate(zip(modules, quantities, usage_data, suggested_purchase, unit_prices)):
    if price not in price_groups:
        price_groups[price] = []
    price_groups[price].append((module, quantity, usage, suggested, i))

# Sort by unit price (descending)
sorted_prices = sorted(price_groups.keys(), reverse=True)

# Create lists for plotting, grouped by price
grouped_modules = []
grouped_quantities = []
grouped_usage = []
grouped_suggested = []
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

# Create positions for each module with increased spacing
for price in sorted_prices:
    group = sorted(price_groups[price], key=lambda x: x[1], reverse=True)  # Sort by quantity
    for module, quantity, usage, suggested, orig_idx in group:
        grouped_modules.append(module)
        grouped_quantities.append(quantity)
        grouped_usage.append(usage)
        grouped_suggested.append(suggested)
        grouped_colors.append(color_map[price])
        x_positions.append(current_x)
        x_tick_labels.append(module)
        current_x += 1.2  # Spacing between modules
    current_x += 1.5  # Gap between price groups

# Create the plot with three bars for each module
plt.figure(figsize=(30, 12))
bar_width = 0.35  # Wide bars

# Create bars for available licenses (NO BORDERS)
bars1 = plt.bar([x - bar_width for x in x_positions], grouped_quantities,
                width=bar_width, color=grouped_colors, alpha=0.9,
                label='Available Licenses')

# Create bars for usage data (NO BORDERS)
bars2 = plt.bar(x_positions, grouped_usage,
                width=bar_width, color='#7f7f7f', alpha=0.9,
                label='Maximum Usage')

# Create bars for suggested purchase (NO BORDERS)
bars3 = plt.bar([x + bar_width for x in x_positions], grouped_suggested,
                width=bar_width, color='#e377c2', alpha=0.9,
                label='Suggested Purchase')

# Add value labels on top of bars (only for values > 0)
for i, (x, q, u, s) in enumerate(zip(x_positions, grouped_quantities, grouped_usage, grouped_suggested)):
    if q > 0:
        plt.text(x - bar_width, q + 0.5, str(q), ha='center', va='bottom',
                fontsize=9, fontweight='bold')
    if u > 0:
        plt.text(x, u + 0.5, str(u), ha='center', va='bottom',
                fontsize=9, fontweight='bold')
    if s > 0:
        plt.text(x + bar_width, s + 0.5, str(s), ha='center', va='bottom',
                fontsize=9, fontweight='bold')

# Customize the plot
plt.title('COMSOL FNL Modules: License Analysis by Price Category\n\nAvailable Licenses (Colored by Price) vs Maximum Usage (Gray) vs Suggested Purchase (Pink)',
          fontsize=16, pad=30, fontweight='bold')
plt.xlabel('COMSOL Modules (Grouped by License Price)', fontsize=12, fontweight='bold', labelpad=15)
plt.ylabel('Number of Licenses', fontsize=12, fontweight='bold', labelpad=15)

# Set x-ticks and rotate labels for better readability
plt.xticks(x_positions, x_tick_labels, rotation=90, fontsize=10)
plt.tick_params(axis='x', which='major', labelsize=9, pad=5)

# Add grid for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.8)

# Create legend for unit prices
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color_map[price], label=f'€{price} License Price')
                  for price in sorted_prices]
legend_elements.extend([
    Patch(facecolor='#7f7f7f', label='Maximum Usage (Gray)'),
    Patch(facecolor='#e377c2', label='Suggested Purchase (Pink)')
])

plt.legend(
    handles=legend_elements,
    title='Legend',
    title_fontsize=11,
    fontsize=10,
    loc='upper center',          # Center horizontally
    bbox_to_anchor=(0.5, 1.00),  # Move slightly above the plot
    ncol=5                       # Spread legend items into 3 columns
)

# Adjust y-axis to accommodate all values
max_value = max(max(grouped_quantities), max(grouped_usage), max(grouped_suggested))
plt.ylim(0, max_value * 1.15)

# Add a horizontal line at y=0 for better reference
plt.axhline(y=0, color='black', linewidth=1, alpha=0.5)

# Add vertical lines to separate price groups
separator_positions = []
current_pos = 0
for price in sorted_prices:
    current_pos += len(price_groups[price]) * 1.2  # Account for spacing
    separator_positions.append(current_pos)
    current_pos += 1.5  # Account for gap between groups

for pos in separator_positions[:-1]:  # Skip the last position
    plt.axvline(x=pos - 0.6, color='gray', linestyle='-', alpha=0.4, linewidth=2)

# Add explanatory text
plt.figtext(0.02, 0.02,
           "This graph shows COMSOL FNL module license analysis. Each module has three bars:\n"
           "- Colored bars (by price category): Currently available licenses\n"
           "- Gray bars: Maximum simultaneous usage recorded\n"
           "- Pink bars: Suggested number of licenses to purchase\n\n"
           "Modules are grouped by license price (see legend for price categories).",
           fontsize=10, style='italic', bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.5))

# Adjust layout to prevent clipping
plt.tight_layout(rect=[0, 0.05, 1, 0.95])  # Make room for the explanatory text

# Show the plot
plt.show()