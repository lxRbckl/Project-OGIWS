# import <
import xlwt
from lxRbckl import jsonLoad

from backend.resource import gDirectory

# >


def createFunction(

        pFile: str,
        pSpeed: list = jsonLoad(pFile = f'{gDirectory}/backend/template/wspeed.json')

):
    '''  '''

    # create <
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet 1')

    # >

    # add speed <
    for c, i in enumerate(pSpeed, start = 1):

        ws.write(

            r = c,
            c = 0,
            label = i,
            style = xlwt.easyxf('font: bold 1; align: horiz centre;')

        )

    # >

    # save <
    wb.save(f'{gDirectory}/backend/data/{pFile}.xls')

    # >
