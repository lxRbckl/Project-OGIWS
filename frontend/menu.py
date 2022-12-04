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
            html.H2('Project OGIWS'),
            html.Hr(),

            # >


            # open <
            # create <
            # notify <
            dcc.Dropdown(

                id = 'menuDropdownId',
                placeholder = 'Open a file...',
                style = dict(marginBottom = '2%'),
                options = [

                    {

                        'label' : f.replace('.xls', ''),
                        'value' : f

                    }

                for f in listdir(path = f'{gDirectory}/data')]

            ),
            dbc.Input(id = 'createInputId', placeholder = 'Create a file...'),

            # >

            # alert <
            dbc.FormText('Save your file when finished editing.'),
            html.Hr(),

            # >

            # action <
            dbc.Row(

                justify = 'between',
                children = [

                    # edit <
                    # graph <
                    dbc.Col(

                        width = 'auto',
                        children = dbc.Button(id = 'editButtonId', children = 'Edit')

                    ),
                    dbc.Col(

                        width = 'auto',
                        children = dbc.Button(id = 'graphButtonId', children = 'Graph')

                    )

                    # >

                ]

            )

            # >

        ]

    )


@application.callback(

    Output('graphDivId', 'children'),
    Input('editButtonId', 'n_clicks'),
    State('menuDropdownId', 'value'),
    State('createInputId', 'value')

)
def buttonCallback(

    pClick: int,
    pDropdownValue: str,
    pInputValue: str

):
    '''  '''

    print(pClick) # remove
    print(pDropdownValue) # remove
    print(pInputValue) # remove

    return None
