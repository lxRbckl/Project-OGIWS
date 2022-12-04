# Project OGIWS by Alex Arbuckle #


# import <
import dash_bootstrap_components as dbc

from frontend.menu import menuFunction
from backend.resource import application

# >


application.layout = dbc.Container(

    fluid = True,
    children = dbc.Row(

        children = menuFunction()

    )

)


# main <
if (__name__ == '__main__'): application.run_server(debug = True)

# >
