# import <
from os import listdir
from dash import html, dcc
from lxRbckl import jsonLoad, jsonDump
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.open import openFunction
from backend.create import createFunction
from backend.resource import application, gDirectory

# >


def menuLayout(

        pLimit = jsonLoad(pFile = f'{gDirectory}/backend/template/limit.json'),
        pNeighbor = jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json')

):
    '''  '''

    return dbc.Row(

        justify = 'center',
        children = [

            # left <
            # right <
            dbc.Col(

                width = 3,
                children = [

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
                    html.Hr(id = 'hrId'),

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

                        for f in listdir(path = f'{gDirectory}/backend/data') if ('DS_' not in f)]

                    ),
                    dbc.Input(id = 'createInputId', placeholder = 'Create a file...'),

                    # >

                    # warning <
                    dbc.FormText('Save your file when finished editing.'),
                    html.Hr(),

                    # >

                    # action <
                    dbc.Row(

                        justify = 'between',
                        style = dict(marginBottom = '15%'),
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

            ),
            dbc.Col(

                width = 3,
                children = [

                    # <
                    html.Hr(),
                    *[

                        html.Div(children = dbc.InputGroup(

                            size = 'sm',
                            style = dict(marginTop = '2%'),
                            children = [

                                # name <
                                # range left <
                                # range right <
                                dbc.InputGroupText(k.title()),
                                dbc.Input(type = 'number', value = v['range'][0], min = 0, max = 25),
                                dbc.Input(type = 'number', value = v['range'][1], min = 0, max = 25)

                                # >

                            ]

                        ))

                    for k, v in pNeighbor.items()],

                    # >

                    # limit <
                    html.Hr(),
                    dbc.InputGroup(

                        size = 'sm',
                        children = [

                            # number of col <
                            # ytick <
                            dbc.InputGroupText('Num. Col.'),
                            dbc.Input(value = pLimit['col']),

                            dbc.InputGroupText('ytick'),
                            dbc.Input(value = pLimit['ytick'])

                            # >

                        ]

                    ),

                    # >

                    # update <
                    html.Hr(),
                    dbc.Button(

                        children = 'Update',
                        id = 'updateButtonId',
                        className = 'float-end'

                    )

                    # >

                ]

            )

            # >

        ]

    )


@application.callback(

    Output('hrId', 'children'),
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

    # if (boot) <
    # else (edit) <
    if (not pClick): return None
    else:

        # if (input) <
        # open requested <
        if (pInputValue): createFunction(pFile = pInputValue)
        openFunction(pFile = pInputValue if (pInputValue) else pDropdownValue)

        # >

        return None
