from model import InputForm
from flask import Flask, render_template, request, Response
from compute import comp
import csv, io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = comp(form.index_5p.data, form.motif_size.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
