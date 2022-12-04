# Project OGIWS by Alex Arbuckle #


# import <
from dash import html
import dash_bootstrap_components as dbc

from frontend.menu import menuFunction
from frontend.graph import graphFunction
from backend.resource import application

# >


application.layout = dbc.Container(

    fluid = True,
    children = dbc.Row(

        children = [

            # menu <
            # graph <
            menuFunction(),
            html.Div(id = 'graphDivId')

            # >

        ]

    )

)


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
