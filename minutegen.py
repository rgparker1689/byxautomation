import dateutil.utils
import dominate
from dominate.tags import *
import webbrowser
from datetime import date
today = date.today()

doc = dominate.document(title='BYX Chapter Minutes')
doc.head += link(_rel="shortcut icon", _href="#")
with doc.body:
    with div(_class='me_auto'):
        h1('Chapter Minutes ' + today.strftime("%m/%d/%Y"))
        img(src='./BYX_Logo_Red.png')


with open('minutes.html', 'w') as file:
    file.write(doc.render())

webbrowser.open('minutes.html')