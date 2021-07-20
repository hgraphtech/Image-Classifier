from flask import Flask, render_template, request, redirect, url_for
from fastai.learner import *
from fastai.imports import *
from fastai.vision.core import *

def predict(img):
    learn_inf = load_learner('export.pkl')
    pred,pred_idx,probs = learn_inf.predict(img)
    return pred,f'{probs[pred_idx].item()*100:.1f}%'

data = []

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']


@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def upload_file():
    uf = request.files['file']
    filename = uf.filename
    pic = uf.read()
    pred,prob = predict(pic)
    data.append([filename,pred,prob])
    return '', 204


