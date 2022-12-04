# import <
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.load import loadFunction
from backend.figure import figureFunction
from backend.translate import translateFunction
from backend.resource import application, gDirectory

# >


def graphLayout():
    '''  '''

    return dbc.Row(id = 'graphRowId')


@application.callback(

    Output('graphRowId', 'children'),
    Input('graphButtonId', 'n_clicks'),
    State('menuDropdownId', 'value'),
    State('createInputId', 'value')

)
def graphCallback(

        pClick: int,
        pDropdownValue: str,
        pInputValue: str

):
    '''  '''

    if (not pInputValue and not pDropdownValue): return None
    else:

        # load data <
        # translate data <
        load = loadFunction(pFile = pInputValue if (pInputValue) else pDropdownValue)
        translate = translateFunction(pLoad = load)

        # >

        return [

            dbc.Col(

                width = 12,
                children = figureFunction(

                    k = k,
                    v = v

                )

            )

        for k, v in translate.items()]
