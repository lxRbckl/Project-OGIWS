# import <
from os import system

from backend.resource import gDirectory

# >


def openFunction(pFile: str):
    '''  '''

    # open for Windows OS <
    # oprn for Mac OS <
    system(command = f'{gDirectory}/{pFile}')
    system(command = f'open {gDirectory}/{pFile}')

    # >
