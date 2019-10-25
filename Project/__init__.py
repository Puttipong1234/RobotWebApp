from flask import Flask , render_template 

app = Flask(__name__,static_folder='static')

from Project import routes