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
    f1 = lambda l, r : [(j % 38) for i in l for j in range((i - r[0]), (i + r[1]))]
    f2 = lambda l : {i : l.count(i) for i in pGraph}

    # m = 37
    # for i in range((m - 4), (m + 5)):
    #
    #   print(i % 38)


    # translate = {}
    # for k, v in pLoad.items():
    #
    #     print(v)
    #     print(len(v)) # remove
    #
    #     # v = [int(i) for i in v if (i != '')]
    #     translate[k] = {
    #
    #         k : {
    #
    #             'x' : ,
    #             'y' :
    #
    #         }
    #
    #     for k, v in pNeighbor.items()}
