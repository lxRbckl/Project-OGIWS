# import <
import xlrd
from lxRbckl import jsonLoad

from backend.resource import gDirectory

# >


def loadFunction(

        pFile: str,
        pLimit: dict = jsonLoad(pFile = f'{gDirectory}/backend/template/limit.json'),
        pSpeed: list = jsonLoad(pFile = f'{gDirectory}/backend/template/wspeed.json')

):
    '''  '''

    # open <
    wb = xlrd.open_workbook(filename = f'{gDirectory}/backend/data/{pFile}')
    ws = wb.sheet_by_name('Sheet 1')

    # >

    # load <
    data = {s : [] for s in pSpeed}
    for r, (s, i) in enumerate(data.items(), start = 1):

        for c in range(1, pLimit['row']):

            try:

                data[s].append(ws.cell_value(

                    rowx = r,
                    colx = c

                ))

            except: pass

    # >

    return data
