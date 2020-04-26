from flask import Flask, render_template, request
from process import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        checkedvalues = request.form.getlist('checkbox')
        #print(request.form.getlist('checkbox'))
        print(checkedvalues)
        processfunction(checkedvalues)
        return 'DONE'
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

