import pickle
from flask import Flask, render_template, request

application = Flask(__name__)
app = application

# Load Ridge regression model and StandardScaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('home.html')  # Start at the prediction form

@app.route('/predictdate', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Retrieve and convert form data
            Temperature = float(request.form['Temperature'])
            RH = float(request.form['RH'])
            Ws = float(request.form['Ws'])
            Rain = float(request.form['Rain'])
            FFMC = float(request.form['FFMC'])
            DMC = float(request.form['DMC'])
            ISI = float(request.form['ISI'])
            Classes = float(request.form['Classes'])
            Region = float(request.form['Region'])

            # Scale and predict
            new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
            result = ridge_model.predict(new_data_scaled)

            return render_template('home.html', results=result[0])
        except Exception as e:
            return render_template('home.html', results=f"Error: {str(e)}")
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
