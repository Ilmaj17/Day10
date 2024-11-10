from flask import Flask, render_template, request
import pickle

with open('salary_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        yoe = int(request.form['yoe'])
        hpw = int(request.form['hpw'])

        pred_result = int(model.predict([[yoe, hpw]]))
        return render_template('index.html', result=pred_result)

if __name__ == "__main__":
    app.run(debug = True)
    