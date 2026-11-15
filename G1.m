
% Population ages 18 to 24

% Education categories
education = {
    'Less than high school graduate'
    'High school graduate (includes equivalency)'
    'Some college or associate''s degree'
    'Bachelor''s degree or higher'
};

% Population percentages
data = [20.4; 51.2; 28.2; 0.2];

% Create bar chart
figure;
b = bar(data);

% Add values on top of each bar
xtips = b.XEndPoints;
ytips = b.YEndPoints;
labels = string(data);

text(xtips, ytips, labels, ...
    'HorizontalAlignment', 'center', ...
    'VerticalAlignment', 'bottom', ...
    'FontSize', 11);

% Add labels and title
xticks(1:4);
xticklabels(education);
xtickangle(20);

xlabel('Education Level');
ylabel('Percentage (%)');
title('Population Ages 18 to 24 by Education Level');

% Graph formatting
ylim([0 60]);
grid on;
set(gca, 'FontSize', 10);
