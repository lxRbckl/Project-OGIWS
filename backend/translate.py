# import <
from lxRbckl import jsonLoad
import plotly.graph_objects as go

from backend.resource import gDirectory

# >


def translateFunction(

        pLoad: dict,
        pGraph: list = jsonLoad(pFile = f'{gDirectory}/backend/template/graph.json'),
        pNeighbor: dict = jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json')

):
    '''  '''

    # <
    # <
    f1 = lambda l : [int(i) for i in l if (i)]
    f2 = lambda l, r : [(j % 38) for i in l for j in range((int(i) - r[0]), (int(i) + r[1]))]
    f3 = lambda l : {i : l.count(i) for i in pGraph}

    # >

    translate = {}
    for k1, v1 in pLoad.items():

        translate[k1] = []
        for k2, v2 in pNeighbor.items():

            a = f1(l = v1)
            b = f2(l = a, r = v2)
            c = f3(l = b)

            var = f3(l = f2(l = f3(l = v1), r = v2))
            translate[k1].append({

                'name' : k2,
                'x' : list(c.keys()),
                'y' : list(c.values())

            })

    return translate
