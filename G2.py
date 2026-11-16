
# Population ages 25 years and over

# Education categories
education = {
    'Less than 9th grade'
    '9th to 12th grade, no diploma'
    'High school graduate (includes equivalency)'
    'Some college, no degree'
    'Associate''s degree'
    'Bachelor''s degree'
    'Graduate or professional degree'
    };

# Population percentages
data = [7.5; 18.4; 37.6; 20.6; 5.6; 6.8; 3.5];

# Create bar chart
figure;
b = bar(data);

# Display values on top of bars
xtips = b.XEndPoints;
ytips = b.YEndPoints;
labels = string(data);

text(xtips, ytips, labels, ...
    'HorizontalAlignment', 'center', ...
    'VerticalAlignment', 'bottom', ...
    'FontSize', 11);

# Labels and title
xticks(1:7);
xticklabels(education);
xtickangle(25);

xlabel('Education Level');
ylabel('Percentage (%)');
title('Population Ages 25 Years and Over');

# Formatting
ylim([0 45]);
grid on;
set(gca, 'FontSize', 10);
