import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv('covid_19_india.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Active'] = df['Confirmed'] - df['Cured'] - df['Deaths']

last      = df[df['Date'] == df['Date'].max()]
total     = int(last['Confirmed'].sum())
recovered = int(last['Cured'].sum())
deaths    = int(last['Deaths'].sum())
active    = total - recovered - deaths

options = [
    {'label': 'Confirmed', 'value': 'Confirmed'},
    {'label': 'Recovered', 'value': 'Cured'},
    {'label': 'Deaths',    'value': 'Deaths'},
]

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Corona Virus Pandemic', style={'color': '#fff', 'text-align': 'center'}),

    # Row 1: KPI Cards
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases', className='text-light'),
                    html.H4(f'{total:,}', className='text-light')
                ], className='card-body')
            ], className='card bg-danger')
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active', className='text-light'),
                    html.H4(f'{active:,}', className='text-light')
                ], className='card-body')
            ], className='card bg-info')
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Recovered', className='text-light'),
                    html.H4(f'{recovered:,}', className='text-light')
                ], className='card-body')
            ], className='card bg-success')
        ], className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Deaths', className='text-light'),
                    html.H4(f'{deaths:,}', className='text-light')
                ], className='card-body')
            ], className='card bg-dark')
        ], className='col-md-3'),
    ], className='row'),

    # Row 2: Line Chart
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='line')
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ], className='row'),

    # Row 3: Bar Chart
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='Confirmed'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className='card')
        ], className='col-md-12')
    ], className='row'),

    # Row 4: Histograms — side by side fix: use style flex on the row
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='hist-confirmed')
                ], className='card-body')
            ], className='card')
        ], className='col-md-6'),

        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='hist-active')
                ], className='card-body')
            ], className='card')
        ], className='col-md-6'),
    ], className='row', style={'display': 'flex'}),

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='hist-recovered')
                ], className='card-body')
            ], className='card')
        ], className='col-md-6'),

        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id='hist-deaths')
                ], className='card-body')
            ], className='card')
        ], className='col-md-6'),
    ], className='row', style={'display': 'flex'}),

], className='container', style={'backgroundColor': '#111', 'maxWidth': '100%', 'padding': '20px'})


# Line chart callback
@app.callback(Output('line', 'figure'), [Input('picker', 'value')])
def update_line(_):
    daily = df.groupby('Date')[['Confirmed', 'Cured', 'Deaths']].sum().reset_index()
    return {
        'data': [
            go.Scatter(x=daily['Date'], y=daily['Confirmed'], mode='lines', name='Confirmed', line=dict(color='red')),
            go.Scatter(x=daily['Date'], y=daily['Cured'],     mode='lines', name='Recovered', line=dict(color='green')),
            go.Scatter(x=daily['Date'], y=daily['Deaths'],    mode='lines', name='Deaths',    line=dict(color='black')),
        ],
        'layout': go.Layout(title='India Covid Trend Over Time', hovermode='x unified')
    }


# Bar chart callback
@app.callback(Output('bar', 'figure'), [Input('picker', 'value')])
def update_bar(col):
    pbar = last.groupby('State/UnionTerritory')[col].sum().reset_index().sort_values(col, ascending=False)
    color_map = {'Confirmed': 'red', 'Cured': 'green', 'Deaths': 'black'}
    return {
        'data': [go.Bar(x=pbar['State/UnionTerritory'], y=pbar[col], marker_color=color_map.get(col, 'blue'))],
        'layout': go.Layout(title='State Wise Count', xaxis_tickangle=-45)
    }


# Shared histogram builder
def make_hist(col, color):
    series = df[col].dropna()
    series = series[series > 0]
    log_vals = np.log10(series)
    counts, bin_edges = np.histogram(log_vals, bins=50)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    return {
        'data': [go.Bar(x=bin_centers, y=counts, marker_color=color, opacity=0.8, name=col)],
        'layout': go.Layout(
            title=f'{col} Distribution',
            xaxis=dict(
                title=col,
                tickvals=[0, 1, 2, 3, 4, 5, 6],
                ticktext=['1', '10', '100', '1K', '10K', '100K', '1M']
            ),
            yaxis=dict(title='Frequency'),
            bargap=0.05
        )
    }


# Histogram callbacks
@app.callback(Output('hist-confirmed', 'figure'), [Input('picker', 'value')])
def hist_confirmed(_): return make_hist('Confirmed', 'red')

@app.callback(Output('hist-active', 'figure'), [Input('picker', 'value')])
def hist_active(_): return make_hist('Active', 'blue')

@app.callback(Output('hist-recovered', 'figure'), [Input('picker', 'value')])
def hist_recovered(_): return make_hist('Cured', 'green')

@app.callback(Output('hist-deaths', 'figure'), [Input('picker', 'value')])
def hist_deaths(_): return make_hist('Deaths', 'black')


if __name__ == '__main__':
    app.run(debug=True, port=5000)