from flask import Flask, render_template, request
import pandas as pd
from io import StringIO
import pickle

app = Flask(__name__)

# Load the pre-trained machine learning model
model = pickle.load(open('best_model.pkl','rb'))
encoder = pickle.load(open('encoder.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))
top_50_feature_names = pickle.load(open('top_50_feature_names.pkl','rb'))

@app.route('/')
def index():
    return render_template('application.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the CSV data from the request
    csv_data = request.json['csvData']

    # Convert the CSV data to a Pandas DataFrame
    df = pd.read_csv(StringIO(csv_data))
    
    #data preprocessing
    df = df.fillna(df.mean())
    df['sex']= encoder.transform(df[['sex']])
    df['specific.disorder']= encoder.transform(df[['specific.disorder']])
    df = df.drop(columns =['no.', 'eeg.date', 'Unnamed: 122'], axis =1)
    df1=[]
    for j in list(top_50_feature_names):
        df1.append(df[j])
    df1 = pd.concat(df1, axis = 1)
    df1 = scaler.transform(df1)

    # Make predictions using the pre-trained model
    predictions = model.predict(df1)
    case_mapping = {
    0: "Addictive disorder",
    1: "Trauma and stress related disorder",
    2: "Mood disorder",
    3: "Healthy control",
    4: "Obsessive compulsive disorder",
    5: "Schizophrenia",
    6: "Anxiety disorder"
                 }

    output = case_mapping[predictions] 

    # Return the prediction results as a string
    return 'Prediction result: ' + output

if __name__ == '__main__':
    app.run()
