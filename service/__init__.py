from flask import Flask, request, render_template
import os
from da_design_server2.src import mylogger, myconfig
import pdb

app = Flask(__name__)

# create a logger.
project_root_path = os.getenv("DA_DESIGN_SERVER")
cfg = myconfig.get_config('{}/share/project.config'.format(
    project_root_path))
log_directory = cfg['logger'].get('log_directory')
logger = mylogger.get_logger('app', log_directory)

@app.route('/')
def web_main():
    return render_template("index.html")

@app.route('/help')
def web_help():
    return render_template("help.html")
