# Do not delete this file!


## Work around not getting flask_pymongo to work in app.py
import subprocess
import sys
import os

try:
  import pymongo
except:
  for variable in ["pymongo", "pymongo[srv]"]:
    subprocess.check_call([sys.executable, "-m", "pip", "install", variable])
## End of work around


from replit import web
from app import app

web.run(app)