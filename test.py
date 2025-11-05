from md2html import *


test, expected = ("***really important***","<em><strong>really important</strong></em>")

print(f'function gives {convert_emphasis(test)} expected is {expected}')
print(f'{convert_emphasis(test)==expected}')