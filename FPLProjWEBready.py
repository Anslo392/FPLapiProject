#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests
import pandas as pd
import plotly.express as px
from ipywidgets import interact, widgets
from IPython.display import clear_output

# Grab the data behind the FPL site
data = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').json()
# Convert the data to a table
dataTable = pd.DataFrame(data['elements'])

# Set minimum minutes played requirement
min_minutes = 500
filtered_players = dataTable[dataTable['minutes'] >= min_minutes]

# Create a scatter plot with plotly
fig = px.scatter(filtered_players, x='expected_assists_per_90', y='expected_goals_per_90',
                 color='web_name', labels={'expected_assists_per_90': 'Expected Assists per 90',
                                           'expected_goals_per_90': 'Expected Goals per 90'},
                 hover_data=['web_name'])

# Update layout for better visibility
fig.update_layout(title='Top Players by Expected Goals and Assists per 90 (Min 500 minutes)',
                  xaxis_title='Expected Assists per 90',
                  yaxis_title='Expected Goals per 90',
                  showlegend=False)

# Define columns for dropdowns
columns = filtered_players.columns.tolist()


#Update plot & clear previous
def update_plot(x_label, y_label):
    clear_output(wait=True)  # Clear the previous output
    scatter = px.scatter(filtered_players, x=x_label, y=y_label,
                         color='web_name', hover_data=['web_name'])
    scatter.update_layout(title=f'Top Players by {y_label} and {x_label} (Min 500 minutes)',
                          xaxis_title=x_label,
                          yaxis_title=y_label,
                          showlegend=False)
    scatter.show()

# Interactive dropdowns

interact(update_plot,
         x_label=widgets.Dropdown(options=columns, value='expected_assists_per_90', description='X Label:'),
         y_label=widgets.Dropdown(options=columns, value='expected_goals_per_90', description='Y Label:'))



# In[25]:





# In[ ]:




