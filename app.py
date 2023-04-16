from flask import Flask,request, url_for, redirect, render_template
import numpy as np
import pickle

app = Flask(__name__)

model=pickle.load(open('RandomForestClassifier.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    output=prediction[0]
    forest_type = {0:'Mixed Deciduous Forest',1:'Hinoki Forest',2:'other',3:'Sugi Forest'}
    return render_template('index.html',pred='Your Forest type is "{}"'.format(forest_type[output]))
    

if __name__ == '__main__':
    app.run(debug=True)
