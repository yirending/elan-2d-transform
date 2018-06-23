import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.offline as pyo
from dash.dependencies import Input, Output, State

import numpy as np


from generate_plot import eigenplot, eigenplot2


app = dash.Dash(__name__)

server = app.server

#app.scripts.config.serve_locally = True
#app.config['suppress_callback_exceptions'] = True

markdown_text = '''
Visualize linear transformation in the plane.
'''


# --------------------------- App Layout --------------------------------------#

app.layout = html.Div([

    html.H5('Elan\'s Linear Transformation Plot'),
    dcc.Markdown([markdown_text]),
    dcc.Markdown(id='text'),


    #-----------------Enter Parameters---------------#
    html.Br(),
    html.Label('Enter the 2x2 matrix by rows'),
    html.Div([
    dcc.Input(id='numbers-in', value='1, -2, 1, 4',
                style= dict(
                    fontSize = 14,
                    width = '50%',
                    height = 30,
                    marginRight = 10,
                    style={'width': '48%', 'display': 'inline-block'}
                )),

    #---------------------Button1--------------------#
    html.Button(
        id='transform-button',
        n_clicks=0,
        n_clicks_timestamp = '0',
        children='Transform',
        style={'fontSize':10,
                'marginRight':5,
                'marginBottom': 10,
                'marginTop':5,
                'display': 'inline-block'}
    ),
    ]),

    #---------------------Graph 1----------------------------#
    html.Div(id='graph' )

],
)





#------------------------------Callbacks---------------------------------------#


#---------------Update Graph from Input---------------#
@app.callback(Output('text', 'children'),
              [Input('numbers-in', 'value')]
              )
def update_graph(numbers):

    inputs = list(map(float, numbers.split(',')))

    markdown_text = '''
    The matrix you entered is
    {}, {}
    {}, {}

    '''.format(str(inputs[0]), str(inputs[1]), str(inputs[2]), str(inputs[3]))

    return [markdown_text]




#---------------Update Text from Input---------------#
@app.callback(Output('graph', 'children'),
              [Input('transform-button', 'n_clicks')],
              [State('numbers-in', 'value')])
def update_graph(n_clicks, numbers):

    inputs = list(map(float, numbers.split(',')))

    if n_clicks % 2 == 0:
        return html.Div([dcc.Graph(id = 'eigen-plot', animate=True,  figure = eigenplot(inputs),
                                style={'height': 500})])
    else:
        return html.Div([dcc.Graph(id = 'eigen-plot', animate=True,  figure = eigenplot2(inputs),
                                style={'height': 500})])


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
