import plotly.graph_objects as go
import pandas as pd

# Load country data (using Plotly's built-in dataset)
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv")

# Create the choropleth map
fig = go.Figure(data=go.Choropleth(
    locations=df['CODE'],  # ISO-3 country codes
    z=df['GDP (BILLIONS)'],  # Values for the color scale (you can change this)
    text=df['COUNTRY'],  # Country names for hover text
    colorscale='Viridis',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix='$',
    colorbar_title='GDP (Billions USD)',
))

fig.update_layout(
    title_text='World GDP by Aman Khan',
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    margin=dict(l=0, r=0, t=50, b=0) #margins to prevent the plot from being too large.
)

fig.show()