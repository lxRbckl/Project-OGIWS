# import <
from lxRbckl import jsonLoad

from backend.resource import gDirectory

# >


def translateFunction(

        pLoad: dict,
        pNeighbor: dict = jsonLoad(pFile = f'{gDirectory}/backend/template/neighbor.json')

):
    '''  '''

    print(pNeighbor)
