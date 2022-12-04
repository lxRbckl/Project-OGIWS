# import <
from dash import dcc
import plotly.graph_objects as go

# >


def figureFunction(

        k: str,
        v: list

):
    '''  '''

    figure = go.Figure(

        layout = dict(

            paper_bgcolor = 'rgb(248, 240, 227)'

        ),
        data = [

            go.Bar(

                x = n['x'],
                y = n['y'],
                name = n['name']

            )

        for n in v]

    )
    figure.update_layout(barmode = 'stack')
    figure.update_layout(title_text = k)

    return dcc.Graph(figure = figure)
