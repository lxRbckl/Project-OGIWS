# import <
from dash import dcc
from lxRbckl import jsonLoad
import plotly.graph_objects as go

from backend.resource import gDirectory

# >


def figureFunction(

        k: str,
        v: list

):
    '''  '''

    # local <
    limit = jsonLoad(pFile = f'{gDirectory}/backend/template/limit.json')
    graph = jsonLoad(pFile = f'{gDirectory}/backend/template/graph.json')

    # >

    figure = go.Figure(

        layout = dict(

            paper_bgcolor = 'rgb(248, 240, 227)',
            margin = {

                'l' : 1,
                'r' : 1

            }

        ),
        data = [

            go.Bar(

                x = n['x'],
                y = n['y'],
                name = n['name']

            )

        for n in v]

    )
    figure.update_layout(

        title = f'Wheel Speed {k}',
        barmode = 'stack',
        yaxis = dict(

            dtick = limit['ytick']

        ),
        xaxis = dict(

            type = 'category',
            tickvals = graph,
            ticktext = graph,
            tickmode = 'array'

        )

    )

    return dcc.Graph(figure = figure)
