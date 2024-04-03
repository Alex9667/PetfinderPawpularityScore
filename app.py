import pandas as pd

from flask import Flask, render_template, send_from_directory
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, BooleanField, StringField

from flask import Flask

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score

from correlation_matrix import *
from ROC_curve import *

app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

data_path = r'Data\train.csv'
temp_data = pd.read_csv(data_path, index_col=['Id'])

data = pd.DataFrame(temp_data)

X = data.drop(columns=['Pawpularity']).values
y = data['Pawpularity'].values

global reg
def linear_regression():
    global reg
    reg = LinearRegression()
    reg.fit(X,y)
    return reg


def predictScore(Subject_focus, Eyes, Face, Near, Action, Accessory, Group, Collage, Human, Occlusion, Info, Blur):
    return str(linear_regression().predict([[Subject_focus, Eyes, Face, Near, Action, Accessory, Group, Collage, Human, Occlusion, Info, Blur]]))


class PredictForm(FlaskForm):
    subject_focus = BooleanField('Subject_focus')
    eyes = BooleanField('Eyes')
    face = BooleanField('Face')
    near = BooleanField('Near')
    action = BooleanField('Action')
    accessory = BooleanField('Accessory')
    group = BooleanField('Group')
    collage = BooleanField('Collage')
    human = BooleanField('Human')
    occlusion = BooleanField('Occlusion')
    info = BooleanField('Info')
    blur = BooleanField('Blue')

    submit = SubmitField('Submit')

class ImageScoreForm(FlaskForm):
    id = StringField('Id')
    score = 0
        
    submit = SubmitField('Submit')


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('header.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    form = PredictForm()

    if form.validate_on_submit():
        subject_focus = form.subject_focus.data
        eyes = form.eyes.data
        face = form.face.data
        near = form.near.data
        action = form.action.data
        accessory = form.accessory.data
        group = form.group.data
        collage = form.collage.data
        human = form.human.data
        occlusion = form.occlusion.data
        info = form.info.data
        blur = form.blur.data

        return predictScore(int(subject_focus), int(eyes), int(face), int(near), int(action), int(accessory), int(group), int(collage), int(human), int(occlusion), int(info), int(blur))        

    return render_template('predictScore.html', form=form)

def logistic_regression_contains_human():
    X = data[["Occlusion", "Near", "Subject Focus", "Group"]]
    y = data['Human'].values
    global log_reg
    log_reg = LogisticRegression()
    log_reg.fit(X,y)
    test_data = pd.read_csv(r'Data\test.csv')
    x_test= test_data[["Occlusion", "Near", "Subject Focus", "Group"]]
    y_test = test_data["Human"]
    y_pred = log_reg.predict(x_test)
    
    ROCCurve(log_reg,X, y)

    return log_reg
# logistic_regression_contains_human()

@app.route("/imageScore", methods=['GET', 'POST'])
def imageScore():
    form = ImageScoreForm()
    score = None  # Initialize score to None
    
    if form.validate_on_submit():
        id = form.id.data
        score = ImageScoreForm(id)

        return send_from_directory('Data/train', id + '.jpg')
    
    return render_template('imageScore.html', form=form)

class MetricsForm(FlaskForm):
    name = StringField('Id')
    score = 0
        
    submit = SubmitField('Submit')

@app.route("/metrics", methods=['GET', 'POST'])
def metrics():
    form = MetricsForm()
    name = "hi"

    return render_template("metrics.html", form=form, context=name)

# correlationMatrix(data)