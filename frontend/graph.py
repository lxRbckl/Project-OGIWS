# import <
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import application, gDirectory

# >


def graphFunction():
    '''  '''

    return dbc.Col(

        children = html.H1('ok')

    )


# @application.callback(
#
#     Output(),
#     Input()
#
# )
# def buttonCallback():
#     '''  '''
#
#     pass
