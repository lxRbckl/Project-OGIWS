# Project OGIWS by Alex Arbuckle #


# import <
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from frontend.menu import menuLayout
from frontend.graph import graphLayout
from backend.resource import application

# >


application.layout = dbc.Container(

    fluid = True,
    style = dict(backgroundColor = 'rgb(248, 240, 227)'),
    children = dbc.Row(

        id = 'mainRowId',
        children = [

            menuLayout(),
            graphLayout()

        ]

    )

)


@application.callback(

    Output('mainRowId', 'children'),
    Input('refreshButtonId', 'n_clicks')

)
def buttonCallback(pClick: int):
    '''  '''

    return [

        dbc.Row(justify = 'center', children = menuLayout()),
        dbc.Row(justify = 'center', children = graphLayout())

    ]

    # >


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
