#%%
from dash import dcc, Dash, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px



#%%
# load data set
df = pd.read_csv("life_expectancy.csv")

df.head()

#%%

#%%

#%%
'''
selected_countries = ['Suriname', 'Sweden']
filtered_df = pd.DataFrame()
if selected_countries is None:
    print("none selected")
else :
    for i in range(len(selected_countries)):
        selected_country = df[df['country'] == selected_countries[i]]
        filtered_df = pd.concat([filtered_df, selected_country], axis = 0)
avg_life = filtered_df.groupby('country')['life expectancy'].mean().reset_index()
avg_life

px.choropleth(avg_life,
              locations='country',
              locationmode='country names',
              color_continuous_scale='reds',
              scope='world',
              color = 'life expectancy')
'''
selected_countries = ['Suriname', 'Sweden','Afghanistan']
filtered_df = df[df['country'].isin(selected_countries)]
avg_life = filtered_df.groupby('country')['life expectancy'].mean().reset_index()
avg_life
#%%
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
navbar = dbc.NavbarSimple(brand = "LifeExpectancy Dashboard",
                          children = html.A('Data Source', href = 'https://ourworldindata.org/life-expectancy',
                                  target= '_blank', style= {'color': 'black'}),

                          color = 'primary',
                          fluid = True,
                          sticky = 'Top'
                          )
min_year = df['year'].min()
max_year = df['year'].max()

cards = dbc.Card([
            html.H6('Life Expectancy by countries',style={'textAlign':'center'}),

            dcc.RangeSlider(
                id = 'year-slider',
                min = min_year,
                max = max_year,
                value = [min_year,max_year],
                marks = {i:str(i) for i in range(min_year,max_year+1, 10)},
                tooltip = {"placement":"bottom", "always_visible":True}

            )],
            style = {'backgroundColor':'blue'})

df.head()
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
navbar = dbc.NavbarSimple(brand="LifeExpectancy Dashboard",
                          children=html.A('Data Source', href='https://ourworldindata.org/life-expectancy',
                                          target='_blank', style={'color': 'black'}),

                          color='primary',
                          fluid=True,
                          sticky='Top'
                          )
min_year = df['year'].min()
max_year = df['year'].max()
cards = dbc.Card([
            html.H6('Life Expectancy by countries',style={'textAlign':'center'}),

            dcc.RangeSlider(
                id = 'year-slider',
                min = min_year,
                max = max_year,
                value = [min_year,max_year],
                marks = {i:str(i) for i in range(min_year,max_year+1, 10)},
                tooltip = {"placement":"bottom", "always_visible":True}

            )],
            style = {'backgroundColor':'blue'})
@app.callback(
    Output('life-expectancy-graph', 'figure'),
    Input('submit-button', 'n_clicks'),
    State('countries-dropdown', 'value'),
    State('year-slider', 'value')
)
def update_graph(button_clicked, selected_countries, selected_year):
    if selected_countries is None:
        return {}


    filtered_df = df[(df['country'].isin(selected_countries)) &
                     (df['year'] >= selected_year[0]) &
                    (df['year'] <= selected_year[1])
    ]


    avg_life = filtered_df.groupby('country')['life expectancy'].mean().reset_index()
    fig = px.choropleth(
            avg_life,
            locations='country',
            locationmode = 'country names',
            color_continuous_scale='reds',
            scope='world',
            color = 'life expectancy'
    )
    return fig


app.layout = html.Div(
    children= [navbar, cards,html.Br(),
               dcc.Dropdown(
                   id = 'countries-dropdown',
                   options = df['country'].unique(),
                   multi = True,
               ),
               html.Br(),
               dbc.Button(children = 'Submit',
                          id = 'submit-button',
                          n_clicks = 0),
               html.Br(),
               dcc.Graph(id = 'life-expectancy-graph')
    ]
)

#%%






#%%
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
#%%
