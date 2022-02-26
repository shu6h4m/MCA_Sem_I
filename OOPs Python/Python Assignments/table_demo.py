"""
==========
Table Demo
==========

Demo of table function to display a table within a plot.
"""
import numpy as np
import matplotlib.pyplot as plt


data = [[ 66, 17, 75, 57, 32],
        [ 58, 38, 78, 99, 16],
        [ 89, 80, 15, 49, 60],
        [ 78, 81, 15, 19, 69],
        [ 13, 33, 34, 78, 52]]

columns = ('MCAC101', 'MCAC102', 'MCAC103', 'MCAC104', 'MCAC105')
rows = ['%d ' % x for x in (Student1, Student1, Student3, Student4, Student5)]

values = np.arange(0, 100, 10)
value_increment = 10

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Marks of Students")
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Student Data Analysis for Ms Goofy')

plt.show()
