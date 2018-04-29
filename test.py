import os
import json
from io import StringIO


import sys
try:
    from io import StringIO  # Python 3
except ImportError:
    from StringIO import StringIO  # Python 2

from coconut.convenience import parse
from coconut.convenience import setup


def lambda_handler(event, context):
    
    code = event['code']
    setup(line_numbers = "TRUE")
    code = parse(code)
    print("compiled")
    print(code)

    return code

  
