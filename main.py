# Project OGIWS by Alex Arbuckle #


# import <
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from frontend.menu import menuFunction
from frontend.graph import graphFunction
from backend.resource import application

# >


application.layout = dbc.Container(

    fluid = True,
    children = dbc.Row(

        id = 'mainRowId',
        children = [

            # menu <
            # graph <
            menuFunction(),
            graphFunction()

            # >

        ]

    )

)


@application.callback(

    Output('mainRowId', 'children'),
    Input('refreshButtonId', 'n_clicks'),
    State('mainRowId', 'children')


)
def buttonCallback(

        pClick: int,
        pChildren: list

):
    '''  '''

    # if (boot) <
    # else (reset) <
    if (not pClick): return pChildren
    return [

        menuFunction(),
        graphFunction()

    ]

    # >


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
