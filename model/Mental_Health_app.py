from flask import Flask, request,render_template
import pandas as pd
import pickle
import numpy as np
from form import PredictForm 
from DTmodel import label_encode_dataframe 

app = Flask(__name__)
app.secret_key = 'f50fab6ad19b5c0d342ace8789bcbeba1139873020266ca8'

model = pickle.load(open(r"C:\prakhar major project\Model.pkl", "rb"))

@app.route('/predict', methods=['POST','GET'])
def submit_form():
    form = PredictForm()
    if request.method == 'POST':
        form_data = request.form.to_dict()
        
        features = ['age', 'Gender', 'self_employed', 'family_history', 'work_interfere', 
                    'no_employees', 'remote_work', 'tech_company', 'benefits', 'care_options', 
                    'wellness_program', 'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 
                    'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 
                    'phys_health_interview', 'mental_vs_physical', 'obs_consequence']
        
        # Extract feature values from form_data
        feature_values = [form_data[feature] for feature in features]
        
    	# Create a dictionary with feature names as keys and feature values as values
        features_dict = dict(zip(features, feature_values))
    
        # Create a DataFrame with a single row containing the features
        encoded_feature_df = pd.DataFrame([features_dict])
    
        # Ensure DataFrame has the same column names as your original features
        encoded_feature_df.columns = features
    
        # Encode the features
        encoded_feature_df = label_encode_dataframe(encoded_feature_df)
    
        input_data = np.array(encoded_feature_df ).reshape(1, 22)
        
        # Make predictions
        predict_result = model.predict(input_data)
        
        
        return render_template('result.html', form_data=predict_result)
    return render_template("form.html",form = form)
    

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')    

if __name__ == '__main__':
    app.run(debug=True)
