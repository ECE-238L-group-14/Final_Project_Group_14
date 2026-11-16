import matplotlib.pyplot as plt
python -m pip install matplotlib
# Education categories
education = [
    'Less than 9th grade',
    '9th to 12th grade, no diploma',
    'High school graduate (includes equivalency)',
    'Some college, no degree',
    "Associate's degree",
    "Bachelor's degree",
    'Graduate or professional degree'
]

# Population percentages
data = [7.5, 18.4, 37.6, 20.6, 5.6, 6.8, 3.5]

# Create bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(range(len(data)), data)

# Display values on top of bars
for bar, value in zip(bars, data):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{value}',
        ha='center',
        va='bottom',
        fontsize=11
    )

# Labels and title
ax.set_xticks(range(len(education)))
ax.set_xticklabels(education, rotation=25)
ax.set_xlabel('Education Level')
ax.set_ylabel('Percentage (%)')
ax.set_title('Population Ages 25 Years and Over')

# Formatting
ax.set_ylim(0, 45)
ax.grid(True, axis='y')
ax.tick_params(labelsize=10)

plt.tight_layout()
plt.show()
