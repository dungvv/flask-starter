import logging

from apiflask import APIFlask
from app.core import config

app = APIFlask(__name__, title='Flask starter', version='0.0.1', spec_path='/openapi.json', docs_path='/docs',
               docs_ui='swagger-ui')

from app.core import app_setup  # no_qa

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
