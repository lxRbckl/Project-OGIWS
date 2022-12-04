# import <
from lxRbckl import jsonLoad

from backend.resource import gDirectory

# >


def translateFunction(

        pLoad: dict,
        pGraph: list = jsonLoad(pFile = f'{gDirectory}/backend/template/graph.json'),
        pNeighbor: dict = jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json')

):
    '''  '''

    # filter data <
    # get neighbor <
    # rank outcome <
    f1 = lambda l : [int(i) for i in l if (i)]
    f2 = lambda l, r : [(j % 38) for i in l for j in range((int(i) - r[0]), (int(i) + r[1]))]
    f3 = lambda l : {i : l.count(i) for i in pGraph}

    # >

    translate = {}
    for k1, v1 in pLoad.items():

        translate[k1] = []
        for k2, v2 in pNeighbor.items():

            var = f3(l = f2(l = f1(l = v1), r = v2))
            translate[k1].append({

                'name' : k2,
                'x' : list(var.keys()),
                'y' : list(var.values())

            })

    return translate
