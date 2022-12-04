# import <
from dash import html, dcc
from os import listdir, system
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import application, gDirectory

# >


def menuFunction():
    '''  '''

    return dbc.Col(

        width = 3,
        children = [

            # title <
            # open <
            # create <
            # edit or graph <
            html.H2('Project OGIWS'),
            html.Hr(),
            dcc.Dropdown(

                id = 'menuDropdownId',
                placeholder = 'Select a file..',
                style = dict(marginBottom = '2%'),
                options = [

                    {

                        'label' : f.replace('.xls', ''),
                        'value' : f

                    }

                for f in listdir(path = f'{gDirectory}/data')]

            ),
            html.Div(id = 'inputDivId'),
            html.Hr(),
            dbc.Row(

                justify = 'between',
                children = [

                    dbc.Col(width = 'auto', children = dbc.Button(id = 'editButtonId', children = 'Edit')),
                    dbc.Col(width = 'auto', children = dbc.Button(id = 'graphButtonId', children = 'Graph'))

                ]

            )

        ]

    )


@application.callback(

    Output('inputDivId', 'children'),
    Input('menuDropdownId', 'value')

)
def dropdownCallback(pFile: str):
    '''  '''

    if (pFile): return None
    else:

        return [

            dbc.Input(),
            dbc.FormText('Save your file when finished.')

        ]


# @application.callback(
#
#     Output(),
#     Input()
#
# )
