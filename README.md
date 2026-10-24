DELIVERY TIME PREDICTION

Project Overview

  This project uses machine learning to predict food delivery time in minutes based on factors such as delivery distance,traffic,weather,preparation time and rider experience.

Dataset Overview

*Rows: 15000
*Columns: 10
*Target : delivery_time_min

Input Features:

*distance_km 
*order_hour 
*day_of_week
*traffic_level 
*weather
*vehicle_type          
*prep_time_min
*num_items
*rider_experience_yrs

Tools and Technologies:

*Python
*Pandas
*Numpy
*Matplotlib
*Seaborn
*Scikit-learn
*Joblib

Project Workflow

1.Explored the dataset.
2.Checked for missing values and duplicate values.
3.Removed one duplicate.
4.Visualized the distribution of delivery times.
5.Analyzed feature correlations.
6.Split the data into training and testing sets.
7.Trained a Decision Tree Regressor.
8.Evaluated model performance using R2,MAE and RMSE.
9.Analyzed feature importance.
10.Tested predictions using new input values.
11.Saved the trained model using Joblib.

Model Performance:

R2 Score: 0.912
MAE: 3.9 Minutes
RMSE: 4.9 Minutes

Sample Prediction

  For a sample set of delivery conditions,the model predicted a delivery time of 63 minutes.

Saved Model
  The trained model was saved 

Future Improvements:

*Evaluate additional regression algorithms.
*Tune model hyperparameters,
*Improve prediction performance through further experience.






