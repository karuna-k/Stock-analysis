from flask import Flask, render_template, request
from process import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    import pandas as pd
    import numpy as np

    if request.method == 'POST':
        checkedvalues = request.form.getlist('checkbox')
        # print(request.form.getlist('checkbox'))
        print(checkedvalues)
        dic = processfunction(checkedvalues)
        return dic
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
