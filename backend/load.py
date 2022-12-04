# import <
import xlrd
from lxRbckl import jsonLoad

from backend.resource import gDirectory

# >


def loadFunction(

        pFile: str,
        pSpeed: list = jsonLoad(pFile = f'{gDirectory}/backend/template/wspeed.json')

):
    '''  '''

    # open <
    wb = xlrd.open_workbook(filename = f'{gDirectory}/{pFile}')
    ws =

    # >
