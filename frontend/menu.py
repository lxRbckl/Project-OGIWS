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

            # message <
            dbc.Alert(

                is_open = True,
                dismissable = True,
                id = 'messageAlertId',
                children = 'Action Completed.',
                style = dict(marginTop = '2%')

            ),

            # >

            # header <
            dbc.Row(

                justify = 'between',
                style = dict(

                    marginTop = '2%',
                    marginBottom = '-2%'

                ),
                children = [

                    # title <
                    # refresh <
                    dbc.Col(

                        width = 'auto',
                        children = html.H2('Project OGIWS')

                    ),
                    dbc.Col(

                        width = 'auto',
                        children = dbc.Button(id = 'refreshButtonId', children = '↻')

                    ),

                    # >

                ]

            ),
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

            # warning <
            dbc.FormText('Warning: save your file when finished editing.'),
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

    Output('messageAlertId', 'is_open'),
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

    print(pDropdownValue) # remove
    print(pInputValue) # remove

    # # if (boot) <
    # if (not pClick):

    return True
