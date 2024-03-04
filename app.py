import re
from datetime import datetime

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"