# import <
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.load import loadFunction
from backend.resource import application, gDirectory

# >


def graphFunction():
    '''  '''

    return dbc.Col(id = 'graphColId')


@application.callback(

    Output('graphColId', 'children'),
    Input('graphButtonId', 'n_clicks'),
    State('menuDropdownId', 'value'),
    State('createInputId', 'value')

)
def buttonCallback(

        pClick: int,
        pDropdownValue: str,
        pInputValue: str

):
    '''  '''

    if (not pInputValue or not pDropdownValue): return None
    else:

        loadFunction(pFile = pInputValue if (pInputValue) else pDropdownValue)
        return None
