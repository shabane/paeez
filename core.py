"""actual functionaliy of the program is write here.
"""
import config


with open(f'theme/{config.theme}/header.html') as header:
    header = header.read()
