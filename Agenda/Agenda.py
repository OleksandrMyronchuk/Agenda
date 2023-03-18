import pandas as pd
from jinja2 import Template

# Read the CSV data into a pandas DataFrame
df = pd.read_csv('Data/agenda.csv')

# Read the HTML template from file
with open('Data/template.html', 'r') as f:
    template_html = f.read()

# Render the template with the data
template = Template(template_html)
html = template.render(date=df.columns[1], location=df.iloc[0, 1], data=df.iloc[1:])

# Write the HTML output to a file
with open('Data/meeting_roles.html', 'w') as f:
    f.write(html)
