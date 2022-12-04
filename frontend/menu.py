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


def menuLayout():
    '''  '''

    # local <
    limit = jsonLoad(pFile = f'{gDirectory}/backend/template/limit.json')
    neighbor = jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json')

    # >

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

                    # limit <
                    # neighbor <
                    html.Hr(),
                    dbc.InputGroup(

                        size = 'sm',
                        children = [

                            # num col <
                            # ytick <
                            dbc.InputGroupText('Num. Col.'),
                            dbc.Input(

                                type = 'number',
                                id = 'numcolInputId',
                                value = limit['col']

                            ),

                            dbc.InputGroupText('ytick'),
                            dbc.Input(

                                type = 'number',
                                id = 'ytickInputId',
                                value = limit['ytick']

                            )

                            # >

                        ]

                    ),
                    *[

                        html.Div(children = dbc.InputGroup(

                            size = 'sm',
                            style = dict(marginTop = '2%'),
                            children = [

                                # name <
                                # range left <
                                # range right <
                                dbc.InputGroupText(k.title()),
                                dbc.Input(

                                    min = 0,
                                    max = 25,
                                    id = f'{k}L',
                                    value = v[0],
                                    type = 'number'

                                ),
                                dbc.Input(

                                    min = 0,
                                    max = 25,
                                    id = f'{k}R',
                                    value = v[1],
                                    type = 'number'

                                )

                                # >

                            ]

                        ))

                    for k, v in neighbor.items()],

                    # >

                    # warning <
                    dbc.FormText('Refresh after updating.'),
                    html.Hr(id = 'hr123Id'),

                    # >

                    # update <
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
def editCallback(

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


@application.callback(

    Output('hr123Id', 'children'),
    Input('updateButtonId', 'n_clicks'),
    State('ytickInputId', 'value'),
    State('numcolInputId', 'value'),
    [State(f'{k}L', 'value') for k in jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json').keys()],
    [State(f'{k}R', 'value') for k in jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json').keys()]

)
def updateCallback(

        pClick: int,
        pTick: str,
        pCol: str,
        *args,
        pLimit: dict = jsonLoad(pFile = f'{gDirectory}/backend/template/limit.json'),
        pNeighbor: dict = jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json')

):
    '''  '''

    if (not pClick): return None
    else:

        # set limit <
        # set neighbor <
        pLimit['col'] = pCol
        pLimit['ytick'] = pTick
        for c, i in enumerate(range(int(len(args) / 2)), start = 1):

            pNeighbor[f'neighbor {c}'] = [

                args[i],
                args[i + int(len(args) / 2)]

            ]

        # >

        # update limit <
        # update neighbor <
        jsonDump(

            pData = pLimit,
            pFile = f'{gDirectory}/backend/template/limit.json'

        ),
        jsonDump(

            pData = pNeighbor,
            pFile = f'{gDirectory}/backend/template/neighbor.json'

        )

        # >

        return None
