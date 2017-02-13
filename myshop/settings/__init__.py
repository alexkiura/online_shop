import os
from dotenv import load_dotenv


if os.getenv('TESTING'):
    from .test import *

elif os.getenv('PRODUCTION'):
    from .production import *

else:
    load_dotenv('.env')
    from .developemnt import *

