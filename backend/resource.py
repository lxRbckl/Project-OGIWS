# import <
from os import path
from dash import Dash
from dash_bootstrap_components import themes

# >


# global <
gDirectory = '/'.join(path.realpath(__file__).split('/')[:-2])
application = Dash(

    name = 'OGIWS',
    title = 'OGIWS',
    # suppress_callback_exceptions = True,
    external_stylesheets = [

        themes.GRID,
        themes.BOOTSTRAP

    ]

)

# >
